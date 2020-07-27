from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C
    """
    
    print("*** Task 1C: CUED Part IA Flood Warning System ***")

    # Build list of stations
    stations = build_station_list()

    # Print stations within 10km of Cambridge
    stations_near_cambridge = []
    stations_near_cambridge = stations_within_radius(stations, (52.2053, 0.1218), 10)
    print("The 10 stations closest to Cambridge:")
    print(stations_near_cambridge)

if __name__ == "__main__":
    run()