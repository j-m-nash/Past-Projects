from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level



def test_flood():
    disagree = 0
    stations = build_station_list()
    stations_level_over_threshold_list = []
    stations_level_over_threshold_list = stations_level_over_threshold(stations, 0.6)
    for i in range(len(stations_level_over_threshold_list)):
        if stations_level_over_threshold_list[i][1] < 0.6:
            disagree += 1
        else:
            pass
    assert disagree == 0

def test_flood_2():
    stations = build_station_list()
    stations_highest_rel_level_list = []
    stations_highest_rel_level_list = stations_highest_rel_level(stations, 10)   
    if len(stations_highest_rel_level_list) > 10:
        assert stations_highest_rel_level_list[9][1] == stations_highest_rel_level_list[len(stations_highest_rel_level_list)-1][1]
    else:
        assert len(stations_highest_rel_level_list) == 10