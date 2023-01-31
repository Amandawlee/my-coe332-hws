import json

from random import uniform
from random import choice

def randomLatitude():
    latitude = uniform(16.0,18.0)
    return(latitude)

def randomLongitude():
    longitude = uniform(82.0,84.0)
    return longitude

def randomComposition():
    composition = ['stony', 'iron', 'stony-iron']
    return(choice(composition))

def generate_sites():
    sites = []
    for i in range(1,6):
        site = {'site_id': i, 'latitude': randomLatitude(),\
                'longitude': randomLongitude(), 'composition': randomComposition(),}
        sites.append(site)

    generate_sites = {'sites': sites}
    
    with open('meteorite_sites.json', 'w') as out:
        json.dump(generate_sites, out, indent=2)
