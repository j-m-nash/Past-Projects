"""Unit test for plot module"""

from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def test_plot():
    # Build list of stations
    stations = build_station_list()
    # Find 5 stations at which the current level is the highest
    stations_highest_rel_level_list = []
    stations_highest_rel_level_list_b = []
    N=5
    for i in range(len(stations_highest_rel_level(stations, N))):
        stations_highest_rel_level_list.append(stations_highest_rel_level(stations, N)[i][0])
    # Do the same again for 6 stations
    for i in range(len(stations_highest_rel_level(stations, N+1))):
        stations_highest_rel_level_list_b.append(stations_highest_rel_level(stations, N+1)[i][0])
    # Check these stations have the highest water level
    relative_level_one = None
    relative_level_two = None
    for station in stations:
        if station.name == stations_highest_rel_level_list[4]:
            relative_level_one = station.relative_water_level()
        if station.name == stations_highest_rel_level_list_b[5]:
            relative_level_two = station.relative_water_level()
        else:
            pass
    assert relative_level_one > relative_level_two
        

        
