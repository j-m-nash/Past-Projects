"""Unit test for geo module"""
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

def test_geo():
    
    # Build list of stations
    stations = build_station_list()
    
    # Create list of tuples of station name and distance from Cambridge
    stations_from_cambridge = []
    for i in range(len(stations_by_distance(stations, (52.2053, 0.1218)))):
        stations_from_cambridge.append(stations_by_distance(stations, (52.2053, 0.1218))[i])
    closest = stations_from_cambridge[0]
    assert closest[0] == "Cambridge Jesus Lock"

def test_geo_2():
    
    # Build list of stations
    stations = build_station_list()

    # Print stations within 10km of Cambridge
    stations_near_cambridge = []
    stations_near_cambridge = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert stations_near_cambridge[0] == "Bin Brook"

def test_geo_3():

    stations = build_station_list()
    rivers_with_station_list = sorted(rivers_with_station(stations))
    assert rivers_with_station_list[0] == 'Addlestone Bourne'    
    for i in range(100,200):
        assert rivers_with_station_list[i] != rivers_with_station_list[i+1]

def test_geo_4():

    stations = build_station_list()
    stations_by_river_dict = stations_by_river(stations)
    assert stations_by_river_dict['River Wallington'] == ['Denmead', 'North Fareham weir']

def test_geo_5():

    stations = build_station_list()
    assert rivers_by_station_number(stations, 12)[0] == ('River Thames', 55)
    assert len(rivers_by_station_number(stations, 800)) != 800