from flask import Flask, request
import json
import xmltodict
import requests
import math

app = Flask(__name__)

response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
data = xmltodict.parse(response.text)

@app.route('/', methods = ['GET'])
def entire_data_set() -> dict:
    """
    Accesses data set from the URL
    
    Args:
        No arguments
    Returns:
        data: A dictionary of data set
    """
    return(data)

@app.route('/epochs', methods = ['GET'])
def epochs() -> list:
    """
    Generates all epochs as a list from the dictionary of the data set
    Args:
        No arguments
    Returns:
        allEpochs: A list of all epoch time stamps (with corresponding information from the data set
    """

    if (data == []):
        return([])
        exit()

    offset = request.args.get('offset',0)
    limit = request.args.get('limit',len(data['ndm']['oem']['body']['segment']['data']['stateVector']))

    if offset:
        try:
            offset = int(offset)
        except ValueError:
            return("Error: Offset parameter must be greater than 0.")

    if limit:
        try:
            limit = int(limit)
        except ValueError:
            return("Error: Limit parameter must be greater than 0.")

    epochsList = []
    count = 0
    offset_count = 0

    for d in data['ndm']['oem']['body']['segment']['data']['stateVector']:
        if (count == limit):
            break

        if offset_count >= offset:
            epochsList.append(d['EPOCH'])
            count += 1

        offset_count += 1

    return(epochsList)

@app.route('/epochs/<epoch>', methods = ['GET'])
def state_vector(epoch) -> list:
    """
    Displays the state vector for a specific epoch from query parameter
    Args:
        epoch: Specific epoch time stamp from data set (referenced in query line

    Returns:
        stateVector: The state vector of the specific epoch time stamp referenced by user
    """

    if (data == []):
        return([])
        exit()

    allEpochs = []
    for d in data['ndm']['oem']['body']['segment']['data']['stateVector']:
        allEpochs.append(d['EPOCH'])

    if epoch in allEpochs:
        specific = allEpochs.index(epoch)
        stateVector = data['ndm']['oem']['body']['segment']['data']['stateVector'][specific]
        return(stateVector)
    else:
        return('Please enter a valid Epoch time stamp.')

@app.route('/epochs/<epoch>/speed', methods = ['GET'])
def speed(epoch) -> float:
    """
    Reads the list of epochs and calculates the instantaneous speed from a specific epoch time stamp from the state vector
    Args:
        epoch: Specific epoch time stamp from data set (referenced in query line
    Returns: 
        speed: The instantaneous speed calculated from the state vector
    """

    if (data == []):
        return([])
        exit()

    allEpochs = epochs()
    if epoch in allEpochs:
        epochData = state_vector(epoch)
        x_dot = float(epochData['X_DOT']['#text'])
        y_dot = float(epochData['Y_DOT']['#text'])
        z_dot = float(epochData['Z_DOT']['#text'])
        speed = math.sqrt(x_dot**2 + y_dot**2 + z_dot**2)
        return(str(speed) + '\n')
    else:
        return('Please enter a valid Epoch time stamp.\n')

@app.route('/help', methods = ['GET'])
def help() -> str:
    """
    Produces a help text that briefly describes each route
    
    Args:
        No arguments
    Returns:
        helpText: Returns help text as a guide for all routes
    """

    helpText = "Access elements from the NASA ISS Trajectory data set with the following routes:\n\
$ curl http://127.0.0.1:5000... \n\
\t/                                  Returns entire data set\n\
\t/epochs                            Returns list of all Epochs in the data set\n\
\t/epochs?limit=int&offset=int       Returns modified list of Epochs given query parameters\n\
\t/epochs/<epoch>                    Returns state vectors for a specific Epoch from the data set\n\
\t/epochs/<epoch>/speed              Returns instantaneous speed for a specific Epoch in the data set\n\
\t/help                              Returns help text that briefly describes each route\n\
\t/delete-data                       Deletes all data from the dictionary object\n\
\t/post-data                         Reloads the dictionary object with data from the web\n"

    return(helpText)

@app.route('/delete-data', methods = ['DELETE'])
def delete_data() -> str:
    """
    Deletes the data set from the .json file that was being used
    Args:
        No arguments
    Returns:
        deleted_data_statement: A statement (str) indicating that the  data set has been deleted
    """

    global data
    data = []
    deleted_data_statement = "NASA ISS trajectory data set has been deleted.\n"
    return(deleted_data_statement)

@app.route('/post-data', methods = ['POST'])
def post_data() -> str:
    """
    Reloads the data set from ISS Trajectory website and adds it to a .json file
    Args:
        No arguments
    Returns:
        reloaded_data_statement: A statement (str) indicating that the data set has been reloaded
    """

    global data
    response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.text)
    reloaded_data_statement = "NASA ISS Trajectory data set has been reloaded.\n"
    return(reloaded_data_statement)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
