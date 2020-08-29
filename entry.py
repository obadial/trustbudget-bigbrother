from BigBrother.BigBrother import BigBrother
import basket_validation.core as pred_core

bigbrother = BigBrother()

data = {
    "amount": 12,
    "item": [{
        "nom": "Vinaigrette balsamique Tomates séchées",
        "prix": "2.52",
        "quantity": 1,
        "barre_code": "3265478858004",
        "image": "https://static.openfoodfacts.org/images/products/326/547/885/8004/fron..."
    },
        {
        "nom": "Vinaigrette Vinaigre de Xérès - Ail - Basilic",
        "prix": "2.56",
        "quantity": 1,
        "barre_code": "3265472088001",
        "image": "https://static.openfoodfacts.org/images/products/326/547/885/8004/fron..."
    },
        {
        "nom": "Riz basmati du Penjab",
        "prix": "1.54",
        "quantity": 1,
        "barre_code": "3560071052621",
        "image": "https://static.openfoodfacts.org/images/products/326/547/885/8004/fron..."
    },
        {
        "nom": "Thon blanc élaboré en Bretagne",
        "prix": "2.99",
        "quantity": 1,
        "barre_code": "3245390140388",
        "image": "https://static.openfoodfacts.org/images/products/326/547/885/8004/fron..."
    },
        {
        "nom": "Soupe de potiron pointe de muscade",
        "prix": "2.31",
        "quantity": 1,
        "barre_code": "8711200350339",
        "image": "https://static.openfoodfacts.org/images/products/326/547/885/8004/fron..."
    },
        {
        "nom": "Soupe de potiron pointe de muscade",
        "prix": "2.31",
        "quantity": 1,
        "barre_code": "8711200350339",
        "image": "https://static.openfoodfacts.org/images/products/326/547/885/8004/fron..."
    }],
    "id_obp_sender": "5d826eedc1b0d300118bdcca"
}

prediction = pred_core.prediction_action(data, bigbrother)
print("prediction => {} ".format(prediction))