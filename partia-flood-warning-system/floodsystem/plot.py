"""
This module contains a function that uses MatPlotLib to build a plot of water
level over time for a station
"""

import matplotlib.pyplot as plt
from .station import MonitoringStation
import numpy as np
from .analysis import polyfit
import matplotlib
from matplotlib import dates

# Test: test_plot
def plot_water_level(station, dates, levels):
    """Plots the water level over time for a station"""
    
    # Plot
    plt.plot(dates, levels)
    # Plot the high and low flows
    # Create list of high and low flow data to pass into plot
    high_flow = []
    low_flow = []
    for i in range(len(dates)):
        low_flow.append(station.typical_range[0])
        high_flow.append(station.typical_range[1])
    # Then add to plot
    plt.plot(dates, high_flow)
    plt.plot(dates, low_flow)
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    x_computable = x - x[0]
    y = levels
    poly = polyfit(dates, levels, p)
    x1 = np.linspace(x_computable[0], x_computable[-1], len(x))
    plt.plot(dates, poly(x1))
    plt.plot(dates, y)
    high_flow = []
    low_flow = []
    for i in range(len(dates)):
        low_flow.append(station.typical_range[0])
        high_flow.append(station.typical_range[1])
    plt.plot(dates, high_flow)
    plt.plot(dates, low_flow)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.show()
