from Data.Point import Point
from Data.Edges import Edges
import random

def Readfile(str, encod):
    f = ''
    if encod == 'utf8':
        f = open(str, "r", encoding='utf8')
    else:
        f = open(str, "r")

    return f


def Read_PointData():
    obj = []
    points = Readfile("Data\PointsData.txt", ' ')
    for item in points:
        item = item.split("**")
        id = item[0]
        if len(id) > 2:
            id = id[-2:]
        name = item[1]
        longitude = int(item[2])
        latitude = int(item[3])
        address = item[4]
        if address[-2:] == "\n":
            address = address[:-2]

        obj.append(Point(id, name, longitude, latitude, address))

    return obj


def Read_EdgeData():
    obj = []
    _maxflow = []

    edges = Readfile("Data\EdgesData.txt", 'utf8')
    for item in edges:
        item = item.split("**")
        id = item[0]
        if len(id) > 2:
            id = id[-2:]
        street_name = item[1]
        _from = item[2]
        _to = item[3]
        weight = int(item[4])

        max_flow = item[6]
        if max_flow[-2:] == "\n":
            max_flow = int(max_flow[:-2])

        # traffic_flow = int(item[5])
        traffic_flow = random.randint(0, int(max_flow) + 1)

        if ((float(traffic_flow)/float(max_flow))*100) > 80:
            _maxflow.append((_from, _to))

        obj.append(Edges(id, street_name, _from, _to, weight, traffic_flow, max_flow))

    return obj, _maxflow


def main():
    # edge_file = Readfile('', )
    # point_file =
    x = Read_PointData()
    #y = Read_EdgeData()
   # print(x[0].getId(), x[0].getName(), x[0].getAddress(), x[0].getLatitude(), x[0].getLongitude())


main()