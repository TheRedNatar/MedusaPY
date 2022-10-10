import pickle


import numpy as np
import pandas as pd


import medusapy.medusa_model_1 as medusa_model_1
import medusapy.medusa_model_n as medusa_model_n


def load(path_to_model_1, path_to_model_n):
    models = {
        "model_1": _load_model(path_to_model_1),
        "model_n": _load_model(path_to_model_n)
    }
    return models


def predict(models, X):
    if X == []:
        return []

    X_1, X_n = _split(X)
    predictions_1, predictions_n = [], []

    if X_1 != []:
        predictions_1 = _predict(models["model_1"], "model_1", medusa_model_1.prepare_row, X_1)
    if X_n != []:
        predictions_n = _predict(models["model_n"], "model_n", medusa_model_n.prepare_row, X_n)

    return predictions_1 + predictions_n


def _load_model(path_to_model):
    with open(path_to_model, 'rb') as f:
        model = pickle.load(f)
        return model

def _split(X):
    X_1, X_n = [], []

    for x in X:
        if x["fe_type"] == "ndays_1":
            X_1.append(x["fe_struct"])
        else:
            X_n.append(x["fe_struct"])

    return (X_1, X_n)

def _predict(model, model_name, prepare_row, raw_X):
    df = pd.DataFrame([prepare_row(x) for x in raw_X])
    pids = list(df["player_id"].values)
    X = df.drop(columns=["player_id"]).values
    preds, preds_proba = _pred(model, X)
    inactive_index = _get_inactive_index(model)
    probs = list(zip(*preds_proba))
    pack = zip([model_name]*len(preds.tolist()), pids, preds.tolist(), probs[inactive_index])
    return list(pack)


def _get_inactive_index(model):
    one, two = model.classes_
    if one is True:
        return 0
    else:
        return 1


def _pred(model, X):
    preds_proba = model.predict_proba(X)
    preds = _predict_normal(model, preds_proba)
    return (preds, preds_proba)


def _predict_normal(model, proba):

    if model.n_outputs_ == 1:
        return model.classes_.take(np.argmax(proba, axis=1), axis=0)

    else:
        n_samples = proba[0].shape[0]
        # all dtypes should be the same, so just take the first
        class_type = model.classes_[0].dtype
        predictions = np.empty((n_samples, model.n_outputs_), dtype=class_type)

        for k in range(model.n_outputs_):
            predictions[:, k] = model.classes_[k].take(
                np.argmax(proba[k], axis=1), axis=0
            )

        return predictions
