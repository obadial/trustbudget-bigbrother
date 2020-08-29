import json
import requests


class OpenFactFood:

    def getProductByBarrecode(self, barcode):
        product = requests.get('https://world.openfoodfacts.org/api/v0/product/' + str(barcode) + '.json')
        return (product)
