import unittest
from BigBrother.Distance.distance import Distance
import json

class Test_Date(unittest.TestCase) :

    def test_getDistance(self):
        # Endroit identique : distance minimum
        self.lat1 = 45.692319
        self.lon1 = -0.309957
        self.dist = 1
        self.assertEqual(Distance.getDistance(self, 45.692319, -0.309957), bool(True))

    def test_getDistance2(self):
        # Endroit identique : distance nulle
        self.lat1 = 45.692319
        self.lon1 = -0.309957
        self.dist = 0
        self.assertEqual(Distance.getDistance(self, 45.692319, -0.309957), bool(True))

    def test_getDistance3(self):
        # Endroit différent distance insuffisante
        self.lat1 = 45.692319
        self.lon1 = -0.309957
        self.dist = 100
        self.assertEqual(Distance.getDistance(self, 46.69266673147251, -0.3042235162961333), bool(False))

    def test_getDistance4(self):
        # Vérification 1° lattitude ~= 120km
        self.lat1 = 45.692319
        self.lon1 = -0.309957
        self.dist = 120
        self.assertEqual(Distance.getDistance(self, 46.69266673147251, -0.3042235162961333), bool(True))

    def test_getDistance5(self):
        # Vérification 1° longitude ~= 120km
        self.lat1 = 45.692319
        self.lon1 = -0.309957
        self.dist = 240
        self.assertEqual(Distance.getDistance(self, 46.69266673147251, -1.3042235162961333), bool(True))

    def test_getListDistance(self):
        # Liste vide
        self.lat1 = 45.692319
        self.lon1 = -0.309957
        self.dist = 10
        self.list = []
        self.assertEqual(Distance.getListDistance(self), '[]')

    def test_getListDistance2(self):
        # Magasins iddentiques
        tab = [{"stores": [{"store_lat": 45.692319, "store_lon": -0.309957}]}]
        tab2 = [{"store_lat": 45.692319, "store_lon": -0.309957}]
        distance = Distance(45.692319, -0.309957, tab, 10)
        self.assertEqual(distance.getListDistance(), json.dumps(tab2, sort_keys=True, ensure_ascii=False))

    def test_getListDistance3(self):
        # Magasin iddentique + distance insuffisante
        tab = [{"stores": [{"store_lat": 45.692319, "store_lon": -0.309957}, {"store_lat": 46.692319, "store_lon": -0.309957}]}]
        tab2 = [{"store_lat": 45.692319, "store_lon": -0.309957}]
        distance = Distance(45.692319, -0.309957, tab, 10)
        self.assertEqual(distance.getListDistance(), json.dumps(tab2, sort_keys=True, ensure_ascii=False))

    def test_getListDistance4(self):
        # Magasin iddentique + distance suffisante
        tab = [{"stores": [{"store_lat": 45.692319, "store_lon": -0.309957}, {"store_lat": 46.692319, "store_lon": -0.309957}]}]
        tab2 = [{"store_lat": 45.692319, "store_lon": -0.309957}, {"store_lat": 46.692319, "store_lon": -0.309957}]
        distance = Distance(45.692319, -0.309957, tab, 120)
        self.assertEqual(distance.getListDistance(), json.dumps(tab2, sort_keys=True, ensure_ascii=False))

if __name__ == '__main__':
    unittest.main()
