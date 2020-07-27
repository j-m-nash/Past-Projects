from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1E"""

    print("*** Task 1E: CUED Part IA Flood Warning System ***")

    #Build list of stations
    stations = build_station_list()
    print("Top 12 rivers by number of stations, and all other rivers with equal number of stations:")
    print(rivers_by_station_number(stations, 12))


if __name__ == "__main__":
    run()