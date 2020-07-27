from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():

    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()

    # Find 5 stations at which the current level is the highest
    stations_highest_rel_level_list = []
    N = 5
    for i in range(len(stations_highest_rel_level(stations, N))):
        stations_highest_rel_level_list.append(stations_highest_rel_level(stations, N)[i][0])
    

    # Plot the water level for each of these stations over the past 10 days
    
    # First fetch the time history for a station
    for station in stations:
        if station.name in stations_highest_rel_level_list:
            
            dt = 2
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
              # This gives list of dates and levels to be passed into a plot
            plot_water_level_with_fit(station, dates, levels, 4)
        else:
            pass
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()

