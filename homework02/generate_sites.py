import json

from random import uniform
from random import choice


def randomLatitude():
    """
    Randomly chooses a latitude between 16.0 and 18.0 degrees North

    Returns:
        latitude (float): Latitude in decimal notation
    """
    latitude = uniform(16.0,18.0)
    return(latitude)

def randomLongitude():
    """
    Randomly chooses a longitude between 82.0 and 84.0 degrees East

    Returns:
        longitude (float): Longitude in decimal notation
    """
    longitude = uniform(82.0,84.0)
    return(longitude)

def randomComposition():
    """
    Randomly chooses a meteorite composition from a list
    
    Returns:
        composition (string): String to indicate randomly chosen meteorite composition
    """
    composition = ['stony', 'iron', 'stony-iron']
    return(choice(composition))

def generate_sites():
    """
    Generates five sites into a dictionary with one key, "sites" and saves data in a .json file
    """
    sites = []
    for i in range(1,6):
        site = {'site_id': i, 'latitude': randomLatitude(),\
                'longitude': randomLongitude(), 'composition': randomComposition(),}
        sites.append(site)

    generate_sites = {'sites': sites}
    
    with open('meteorite_sites.json', 'w') as out:
        json.dump(generate_sites, out, indent=2)

generate_sites()
