from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B
    """
    
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    # Build list of stations
    stations = build_station_list()
    stations_level_over_threshold_list = []
    stations_level_over_threshold_list = stations_level_over_threshold(stations, 0.8)

    print("List of stations with relative water level over the tolerance (0.8) and their relative water levels:")
    for i in range(len(stations_level_over_threshold_list)):
        print("Station name and current relative level: {}, {}".format(stations_level_over_threshold_list[i][0], stations_level_over_threshold_list[i][1]))



if __name__ == "__main__":
    run()