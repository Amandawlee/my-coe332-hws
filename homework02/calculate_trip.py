import json
import math

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    """
    Calculates distance between initial point to next location using the great-circle distnce algorithm

    Args:
        latitude_1 (float): Initial latitude in decimal notation
        longitude_1 (float): Initial longitude in decimal notation
        latitude_2 (float): Final latitude in decimal notation
        longitude_2 (float): Final longitude in decimal notation

    Returns:
        mars_radius * d_sigma (float): distance traveled from initial to final point
    """
    lat1, long1, lat2, long2 = map(math.radians, [latitude_1, longitude_1, latitude_2, longitude_2])
    d_sigma = math.acos(math.sin(lat1) * math.sin(lat2) +math.cos(lat1) * math.cos(lat2) * math.cos(abs(long1-long2)))
    mars_radius = 3389.5 #km
    return(mars_radius * d_sigma)

def travel_time(distance, speed):
    """
    Calculates travel time by dividing speed from distance traveled

    Args:
        distance (float): Travel distance in decimal notation
        speed (float): Speed traveled in decimal notation

    Returns:
        round(distance/speed,2)) (float): Time taken to travel rounded up to two decimal places
    """
    return(round(distance/speed,2))

def sample_time(composition: str) -> int:
    """
    Associates time taken to take sample with meteorite landing's site composition

    Args:
        composition (string): String from list of meteorite composition (in dictionary)

    Returns:
        time (integer): Integer of hour(s) it takes to get sample
    """
    if composition == 'stony':
        time = 1
    elif composition == 'iron':
        time = 2
    else:
        time = 3
    return(time)

def total_time(travel, sample):
    """
    Calculates total time elapsed for trip(s)

    Args:
        travel (float): time taken to travel to final site
        sample (float): time taken to sample from site

    Returns:
        travel + sample (float): Total time added
    """
    return(travel + sample)
    
def main():
    with open('meteorite_sites.json', 'r') as f:
        generate_sites = json.load(f)

    speed = 10. #km/hr
    start_lat = 16.0
    start_long = 82.0

    totalTime = 0.
    
    for i in range(len(generate_sites['sites'])):
        leg = generate_sites['sites'][i]['site_id']

        distance = calc_gcd(start_lat, start_long, generate_sites['sites'][i]['latitude'], generate_sites['sites'][i]['longitude'])

        timetotravel = travel_time(distance, speed)

        timetosample = sample_time(generate_sites['sites'][i]['composition'])
        print('leg = {}, time to travel = {:.2f} hr, time to sample = {} hr'.format(leg, timetotravel, timetosample))
        
        totalTime += total_time(timetotravel,(timetosample))

    print('===============================')
    print('number of legs = {}, total time elapsed = {:.2f} hr'.format(leg,totalTime))

if __name__ == '__main__':
    main()
