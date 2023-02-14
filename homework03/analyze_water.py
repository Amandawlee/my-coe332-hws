import math
import requests

def turbidity(a0,I90):
    """
    T = Turbidity in NTU Units (0 - 40)
    a0 = Calibration constant
    I90 = Ninety degree detector current
    """

    T = a0 * I90
    return(T)

def minimum_time(Ts,T0,d):
    """
    Ts = Turbidity threshold for safe water
    T0 = Current turbidity
    d = Decay factor per hour, expressed as a decimal
    b = Hours elapsed
    """

    b = math.log(Ts/T0)/math.log(1-d)
    return(b)

def main():
    # From requests library
    response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')

    data = response.json()

    # Initial information
    T = 0.
    Ts = 1.0 #NTU
    d = 0.02 #2%

    # Calculates and adds the turbidity of most recent five data points
    for i in range(-5,0): 
        T += turbidity(data['turbidity_data'][i]['calibration_constant'], data['turbidity_data'][i]['detector_current'])
      
    # Calculates average turbidity of most recent five data points   
    T = T/5.0
        
    print('\nAverage turbidity based on most recent five measurements = {:.4f} NTU'.format(T))
    
    # Calculates minimum time required to return below Ts
    b = minimum_time(Ts,T,d)

    if (Ts >= T):
        print('Info: Turbidity is below threshold for safe use')
        print('Minimum time required to return below a safe threshold = 0 hours\n')
    else:
        print('Warning: Turbidity is above threshold for safe use')
        print ('Minimum time required to return below a safe threshold = {:.2f} hours\n'.format(b))

if __name__ == '__main__':
    main()



