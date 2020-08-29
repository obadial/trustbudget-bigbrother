from catboost import CatBoostClassifier
from .parser import BasketParser


MODEL = None


def load_perf_model(path='./basket_validation/catboost_iteration/model_with_ratio_evaluation.cbm'):
    global MODEL
    common_conf = {
        'iterations': 500,
        'learning_rate': 0.01,
        'depth': 4,
        'use_best_model': True,
        'random_seed': 42,
        'loss_function': 'MultiClass',
        'eval_metric': 'WKappa'
    }
    try:
        MODEL = CatBoostClassifier(**common_conf).load_model(fname=path)
        return True
    except Exception:
        print("Could not perf model")
        return False


def load_legacy_model(path='./basket_validation/catboost_iteration/model_with_ration_evaluation.cbm'):
    global MODEL
    common_conf = {
        'iterations': 1500,
        'learning_rate': 0.01,
        'depth': 9,
        'use_best_model': True,
        'random_seed': 42,
        'loss_function': 'MultiClass',
        'eval_metric': 'WKappa'
    }
    try:
        MODEL = CatBoostClassifier(**common_conf).load_model(fname=path)
        return True
    except Exception:
        print("Could not load legacy model")
        return False


def prediction_action(data, big_brother):
    global MODEL
    if not MODEL:
        if not load_perf_model():
            return False
    #try:
    parsed_data = BasketParser(data)
    pre_result = parsed_data.build(big_brother)
    if not pre_result:
        return "KO"
    else:
        return "OK"
    prediction = MODEL.predict(parsed_data.DATA_FRAME)
    return prediction[0, 0]
    # except Exception:
    #     print("Fail to predict for user => {} ".format(data["id_obp_sender"]))
    #     return False


load_perf_model()
