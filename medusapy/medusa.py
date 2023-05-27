import pickle

import numpy as np
import pandas as pd

from medusapy.medusa_model import prepare_row


def load(path_to_model):
    return _load_model(path_to_model)


def predict(model, data):
    if data == []:
        return []

    df = pd.DataFrame([prepare_row(x) for x in data])
    pids = list(df["player_id"].values)
    X = df.drop(columns=["player_id"]).values
    preds, preds_proba = _pred(model, X)
    inactive_index = _get_inactive_index(model)
    probs = list(zip(*preds_proba))
    pack = zip(pids, [x == inactive_index for x in preds.tolist()], probs[inactive_index])
    return list(pack)


def _load_model(path_to_model):
    with open(path_to_model, 'rb') as f:
        model = pickle.load(f)
        return model


def _get_inactive_index(model):
    class_0, class_1 = model.classes_
    if class_0 is True:
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
