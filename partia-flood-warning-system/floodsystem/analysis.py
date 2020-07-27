from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from .station import MonitoringStation
from .stationdata import update_water_levels
import numpy as np
import matplotlib
from matplotlib import dates


def polyfit(dates, levels, p):
    """Returns a polyfit for water levels"""
    x = matplotlib.dates.date2num(dates)
    poly_coeff = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(poly_coeff)
    return poly