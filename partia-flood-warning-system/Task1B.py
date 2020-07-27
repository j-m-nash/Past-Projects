from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():

    """Requirements for Task 1B"""
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    # Build list of stations
    stations = build_station_list()
    
    # Create list of tuples of station name and distance from Cambridge
    stations_from_cambridge = []
    stations_from_cambridge = stations_by_distance(stations, (52.2053, 0.1218))
    
    # Prints the 10 closest stations to Cambridge
    print("Closest 10 Stations to Cambridge:")
    print(stations_from_cambridge[:10])
    
    # Prints the 10 furthers stations from Cambridge
    print("Furthest 10 Stations from Cambridge:")
    print(stations_from_cambridge[-10:])
    
if __name__ == "__main__":
    run()