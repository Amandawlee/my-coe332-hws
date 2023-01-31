import json
import math

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, long1, lat2, long2 = map(math.radians, [latitude_1, longitude_1, latitude_2, longitude_2])
    d_sigma = math.acos(math.sin(lat1) * math.sin(lat2) +math.cos(lat1) * math.cos(lat2) * math.cos(abs(long1-long2)))
    mars_radius = 3389.5 #km
    return(mars_radius * d_sigma)

def travel_time(distance, speed):
    return(round(distance/speed,2))

def sample_time(composition: str) -> int:
    if composition == 'stony':
        time = 1
    elif composition == 'iron':
        time = 2
    else:
        time = 3
    return(time)

def total_time(travel, sample):
    return(travel + sample)
    
def main():
    with open('meteorite_sites.json', 'r') as f:
        generate_sites = json.load(f)

    speed = 10 #km/hr
    start_lat = 16.0
    start_long = 82.0

    totalTime = 0.
    
    for i in range(len(generate_sites['sites'])):
        leg = generate_sites['sites'][i]['site_id']

        distance = calc_gcd(start_lat, start_long, generate_sites['sites'][i]['latitude'], generate_sites['sites'][i]['longitude'])

        timetotravel = travel_time(distance, speed)

        timetosample = sample_time(generate_sites['sites'][i]['composition'])
        print('leg = {}, time to travel = {} hr, time to sample = {} hr'.format(leg, timetotravel, timetosample))
        
        totalTime += total_time(timetotravel,(timetosample))

    print('===============================')
    print('number of legs = {}, total time elapsed = {} hr'.format(leg,totalTime))

if __name__ == '__main__':
    main()
