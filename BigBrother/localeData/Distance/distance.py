from math import sin, cos, sqrt, atan2, radians
import geopy.distance
import json

class Distance:

    def __init__(self, lat1, lon1, list, dist):
        # approximate radius of earth in km
        self.R = 6373.0
        # Position de la personne
        self.lat1 = lat1
        self.lon1 = lon1
        self.list = list
        self.dist = dist

    def getDistance(self, lat2, lon2):

        coords_1 = (self.lat1, self.lon1)
        coords_2 = (lat2, lon2)
        distance = geopy.distance.distance(coords_1, coords_2).km
        d = 0
        if distance <= self.dist:
            d = 1
        return d

    def getListDistance(self):
        mag = []
        for elem in self.list:
            if "stores" in elem:
                for store in elem['stores']:
                    if self.getDistance(store["store_lat"], store["store_lon"]) == 1:
                        store["mag_name"] = elem["name"]
                        mag.append(store)
        mag = json.dumps(mag, sort_keys=True, ensure_ascii=False)
        return mag

