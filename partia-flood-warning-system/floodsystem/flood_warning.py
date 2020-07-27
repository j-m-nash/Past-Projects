"""This module contains functionality to warn of a flood"""

from .station import MonitoringStation
from .analysis import polyfit
import datetime
from .datafetcher import fetch_measure_levels
import matplotlib
import numpy as np

def watch_out(stations):
    """This function asseses the risk of a flood when passed a list of stations and returns stations
    in lists of similar risks. The risk is calculated from the relative water level, and then a multiplier
    based on trajectory"""
    severe = []
    high = []
    moderate = []
    low = []
    dt = 2
    for station in stations:
        if station.relative_water_level() == None:
            pass
        #INCREASE THIS 0.7 IF YOU WANT MORE STATIONS INCLUDED
        elif station.relative_water_level() < 0.7: 
            pass
        else:
        #DECREASE THIS 0.6 OR INCREASE THIS 10 TO INCREASE THE STARTING RISK VALUES 
        #(THE LOWER THE 0.6 VALUE GOES, THE GREATER EFFECT THE MULTIPLIER WILL HAVE ON THE LOWER WATER LEVEL STATIONS) 
            station.risk = 10*(station.relative_water_level()-0.6)
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            x = matplotlib.dates.date2num(dates)
            if len(x) == 0:            
                pass
            else:
                x_computable = x - x[0]
                poly = polyfit(dates, levels, 4)
                polyder = np.polyder(poly)
        #INCREASE THESE 0, 12, 24 IF YOU WANT TO TAKE THE GRADIENTS FROM FURTHER BACK IN TIME
                gradient1 = polyder(x_computable[0])
                gradient2 = polyder(x_computable[12])
                gradient3 = polyder(x_computable[24])
        #THESE ARE THE MULTIPLIERS FOR THE MOST RECENT GRADIENT
                if gradient1 > 0.5:
                    station.risk = station.risk * 2
                elif gradient1 > 0.2:
                    station.risk = station.risk * 1.6
                elif gradient1 > 0:
                    station.risk = station.risk * 1.2
                else:
                    station.risk = station.risk * 0.8
        #THESE ARE FOR THE SECOND GRADIENT
                if gradient2 > 0.5:
                    station.risk = station.risk * 1.5
                elif gradient2 > 0.2:
                    station.risk = station.risk * 1.3
                elif gradient2 > 0:
                    station.risk = station.risk * 1.1
                else:
                    station.risk = station.risk * 0.9
        #AND FOR THE THIRD:
                if gradient3 > 0.5:
                    station.risk = station.risk * 1.5
                elif gradient3 > 0.2:
                    station.risk = station.risk * 1.3
                elif gradient3 > 0:
                    station.risk = station.risk * 1.1
                else:
                    station.risk = station.risk * 0.9 


    #LASTLY SCALE THESE ACCORDINGLY
    for station in stations:
        if station.risk > 10:
            if station.town in severe:
                pass
            else:
                severe.append(station.town)
        else: 
            pass

    for station in stations:
        if station.risk > 6:
            if station.town in high:
                pass
            elif station.town in severe:
                pass
            else:
                high.append(station.town)
        else: 
            pass

    for station in stations:
        if station.risk > 4:
            if station.town in severe:
                pass
            elif station.town in high:
                pass
            elif station.town in moderate:
                pass
            else:
                moderate.append(station.town)
        else: 
            pass

    for station in stations:
        if station.risk > 2:
            if station.town in severe:
                pass
            elif station.town in high:
                pass
            elif station.town in moderate:
                pass
            elif station.town in low:
                pass
            else:
                low.append(station.town)
        else: 
            pass
            


    print("This floodsystem assigns a risk value to each station.")
    print("This value is calculated by combination of the relative water level and its trajectory.")
    print("The risk value designates the level of risk.")
    print("Towns with a station above a certain risk level will be added to the corresponding list")
    print("This designation can be altered depending on operator requirements.")
    print("See flood_warning module.")
    print("Severe risk towns:")
    print(sorted(severe))
    print("High risk towns:")
    print(sorted(high))
    print("Moderate risk towns")
    print(sorted(moderate))
    print("Low risk towns")
    print(sorted(low))

    

    

    





