# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

# Test: test_geo
def stations_by_distance(stations, p):
    """This function, when given a list of stations, and a coordinate p, returns a list of tuples (station, distance)
    where distance is the distance of the particular station from p calculated via the haversine formula"""
    # Initilise the empty list
    stations_by_distance_unsorted= []
    for station in stations:
        distance = haversine(station.coord, p)
        stations_by_distance_unsorted.append((station.name, distance))
        # Sort the list by distance
    return sorted_by_key(stations_by_distance_unsorted, 1)

# Test: test_geo_2
def stations_within_radius(stations, centre, r):
    """This function passes a list of stations, a central point, and a radius, and returns the names of stations
    within that radius"""
    # Call the stations by distance function to work out the distance of stations from the centre
    station_distance_tuples = stations_by_distance(stations, centre)
    stations_within_radius = []
    for tuples in station_distance_tuples:
        if tuples[1] < r:
            stations_within_radius.append(tuples[0])
    return sorted(stations_within_radius)

# Test: test_geo_3
def rivers_with_station(stations):
    """This function passes a list of stations, and lists all rivers that have at least one station (without repetition)"""
    # Create empty list
    rivers_with_station = []
    for station in stations: 
        if station.river in rivers_with_station:
            pass
        else:
            rivers_with_station.append(station.river)

    return sorted(rivers_with_station)

# Test: test_geo_4
def stations_by_river(stations):
    """This function returns a dictionary of {river:list of stations on river}"""
    # Create empty dictionary
    stations_by_river = {}
    rivers_with_station = []
    for station in stations: 
        list_of_names = []
    #If exisiting river, add new station to list of stations
        if station.river in rivers_with_station:            
            list_of_names = stations_by_river[station.river]
            list_of_names.append(station.name)
            stations_by_river[station.river] = sorted(list_of_names)
    #If new station, add new entry with station as the whole list
        else:
            rivers_with_station.append(station.river)
            list_of_names.append(station.name)
            stations_by_river[station.river] = list_of_names

    return stations_by_river

# Test: test_geo_5
def rivers_by_station_number(stations, N):        
    """This function returns a list of tuples (river, number of stations on river)"""
    # Copy stations_by_river()
    stations_by_river = {}
    rivers_with_station = []
    for station in stations: 
        list_of_names = []
    
        if station.river in rivers_with_station:            
            list_of_names = stations_by_river[station.river]
            list_of_names.append(station.name)
            stations_by_river[station.river] = sorted(list_of_names)
    
        else:
            rivers_with_station.append(station.river)
            list_of_names.append(station.name)
            stations_by_river[station.river] = list_of_names
    # Create a new list and add the tuples from the dictionary
    rivers_by_station_number_list_reversed =[]
    for river_name, list_of_stations in stations_by_river.items():
        rivers_by_station_number_list_reversed.append((river_name, len(list_of_stations)))
    # Sort the list and take the first N terms
    all_rivers_by_station_number = sorted_by_key(rivers_by_station_number_list_reversed, 1, reverse=True)
    n_rivers_by_station_number = all_rivers_by_station_number[:N]
    # Check to see if N+1th term is equal to Nth, if so add it to the list, increase N by 1 and repeat
    while all_rivers_by_station_number[N][1] == all_rivers_by_station_number[N-1][1]:
        n_rivers_by_station_number.append(all_rivers_by_station_number[N])
        N+=1
        if N == len(all_rivers_by_station_number):
            break
    
    return n_rivers_by_station_number


    

    


