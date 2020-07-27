# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        
        self.risk = 0

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """This method prevents erroneous data whereby high flow < low flow,
        being passed into the flood monitoring system
        """
        if isinstance(self.typical_range, tuple):
            if self.typical_range[1] - self.typical_range[0] < 0:
                return False
            else:
                True        
        else:
            return False

    def relative_water_level(self):
        """This method returns the latest water level as a fraction of its typical highest and lowest values,
        whereby 1.0 is equal to typical highest value, and 0.0 is equal to typical lowest"""
        if isinstance(self.typical_range, tuple):
            if self.typical_range[1] - self.typical_range[0] < 0:
                return None
            else:
                if self.latest_level == None:
                    return None #This is being triggered by all of them
                else:
                    return (self.latest_level-self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])
        else:
            return None        
            


# Test: test_station_2
def inconsistent_typical_range_stations(stations):
    """This function, when a list stations is passed, returns a list of inconsistent stations
    """
    # Initialise empty list for results
    inconsistent_stations = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent_stations.append(station.name)      
    return sorted(inconsistent_stations)           




