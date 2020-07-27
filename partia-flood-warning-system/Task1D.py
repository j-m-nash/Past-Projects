from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""

    print("*** Task 1D: CUED Part IA Flood Warning System ***")

    #Build list of stations
    stations = build_station_list()
    rivers_with_station_list = rivers_with_station(stations)

    # Count number of unique rivers
    print("Number of unique rivers:")
    print(len(rivers_with_station_list))

    #List the first ten alphabetically
    print("First ten rivers alphabetically:")
    print(rivers_with_station_list[:10])

    #List the stations on the specified rivers
    stations_by_river_dict = stations_by_river(stations)
    print("Stations on the River Aire:")
    print(stations_by_river_dict['River Aire'])
    print("Stations on the River Cam:")
    print(stations_by_river_dict['River Cam'])
    print("Stations on the River Thames:")
    print(stations_by_river_dict['River Thames'])

if __name__ == "__main__":
    run()