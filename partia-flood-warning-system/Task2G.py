from floodsystem.flood_warning import watch_out
from floodsystem.stationdata import build_station_list, update_water_levels

def run():

    """Requirements for Task 2G"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
 #   for station in stations:
  #      print(station.relative_water_level())

    print(watch_out(stations))

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

