from flask import Flask
import requests
import xmltodict
import math

app = Flask(__name__)

response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
data = xmltodict.parse(response.text)

@app.route('/', methods = ['GET'])
def entire_data_set() -> dict:
    """
    Returns data from URL as a dictionary
    """
    return(data)

@app.route('/epochs', methods = ['GET'])
def epochs() -> list:
    """
    Returns epochs as a list from the dictionary
    """
    allEpochs = []
    for d in data['ndm']['oem']['body']['segment']['data']['stateVector']:
        allEpochs.append(d['EPOCH'])
    return(allEpochs)

@app.route('/epochs/<epoch>', methods = ['GET'])
def state_vector(epoch) -> list:
    """
    Returns the state vector for a specific epoch

    Input: epoch (Epoch time stamp)

    Returns: stateVector
    """
    allEpochs = epochs()
    if epoch in allEpochs:
        specific = allEpochs.index(epoch)
        stateVector = data['ndm']['oem']['body']['segment']['data']['stateVector'][specific]
        return(stateVector)
    else:
        return('Please enter a valid Epoch time stamp.')

@app.route('/epochs/<epoch>/speed', methods = ['GET'])
def speed(epoch) -> float:
    """
    Reads the list of epochs and calculates the instantaneous speed from a \
            specific epoch time stamp from the state vector

    Input: epoch (Epoch time stamp)

    Returns: speed
    """
    allEpochs = epochs()
    if epoch in allEpochs:
        epochData = state_vector(epoch)
        x_dot = float(epochData['X_DOT']['#text'])
        y_dot = float(epochData['Y_DOT']['#text'])
        z_dot = float(epochData['Z_DOT']['#text'])
        speed = math.sqrt(x_dot**2 + y_dot**2 + z_dot**2)
        return(str(speed) + '\n')
    else:
        return('Please enter a valid Epoch time stamp.')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
