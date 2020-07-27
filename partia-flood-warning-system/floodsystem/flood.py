from . import datafetcher
from .station import MonitoringStation
from .stationdata import update_water_levels
from .utils import sorted_by_key  # noqa

def stations_level_over_threshold(stations, tol):
    """ returns a list of tuples, where each tuple holds (i) a station 
    (object) at which the latest relative water level is over tol and 
    (ii) the relative water level at the station. 
    """

    stations_over_threshold = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            if station.relative_water_level() > tol:
                stations_over_threshold.append((station.name, station.relative_water_level()))
            else: 
                pass

    return stations_over_threshold

def stations_highest_rel_level(stations, N):
    """Return the list of N stations with highest relative water level in descending order"""

    stations_with_threshold = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            
            stations_with_threshold.append((station.name, station.relative_water_level()))
            

        # Sort the list and take the first N terms
    all_stations_by_relative_water_level = sorted_by_key(stations_with_threshold, 1, reverse=True)
    n_stations_by_relative_water_level = all_stations_by_relative_water_level[:N]
    # Check to see if N+1th term is equal to Nth, if so add it to the list, increase N by 1 and repeat
    while all_stations_by_relative_water_level[N][1] == all_stations_by_relative_water_level[N-1][1]:
        n_stations_by_relative_water_level.append(all_stations_by_relative_water_level[N])
        N+=1
        if N == len(all_stations_by_relative_water_level):
            break
    
    return n_stations_by_relative_water_level