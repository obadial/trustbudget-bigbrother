import json
import requests


class OpenPetFoodFacts:

    def getProductByBarrecode(self, barcode):
        product = requests.get('https://world.openpetfoodfacts.org/api/v0/product/' + str(barcode) + '.json')
        return (product)
