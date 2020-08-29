import json
import requests


class OpenBeautyFacts:

    def getProductByBarrecode(self, barcode):
        product = requests.get('https://world.openbeautyfacts.org/api/v0/product/' + str(barcode) + '.json')
        return (product)
