from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation

def run():
    """Requirements for Task 1F
    """
    
    print("*** Task 1F: CUED Part IA Flood Warning System ***")

    # Build list of stations
    stations = build_station_list()

    # Build list of stations with inconsistent data
    print("The following are inconsistent stations, whereby the data received from DEFRA is erroneous such that the typical high flow is less than the low flow, or the data provided was not in the form a tuple:")
    print((inconsistent_typical_range_stations(stations)))
   
if __name__ == "__main__":
    run()
