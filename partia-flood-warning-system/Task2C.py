from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C
    """
    
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    # Build list of stations
    stations = build_station_list()
    stations_highest_rel_level_list = []
    stations_highest_rel_level_list = stations_highest_rel_level(stations, 10)

    print("List of 10 stations with highest relative water levels (And any with equal relative water levels), and their water levels:")
    for i in range(len(stations_highest_rel_level_list)):
        print("Station name and current relative level: {}, {}".format(stations_highest_rel_level_list[i][0], stations_highest_rel_level_list[i][1]))



if __name__ == "__main__":
    run()