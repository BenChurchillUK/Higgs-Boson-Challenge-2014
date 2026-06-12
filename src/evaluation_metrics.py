import pandas as pd
import math
from sklearn.metrics import accuracy_score, roc_auc_score, log_loss

def approximate_median_significance(posr, negr, regt):
    ams = math.sqrt(2((posr+negr+regt) (math.log(1 + (posr/(negr+regt)))) - posr))
    return ams

def evaluate_model(test, prediction, probability):
    # ams = approximate_median_significance(posr, negr, regt)
    accuracy = accuracy_score(test, prediction)
    roc_auc = roc_auc_score(test, probability)
    log_loss_value = log_loss(test, probability)
    df = pd.DataFrame([["Accuracy", accuracy], ["roc-auc", roc_auc], ["Log Loss", log_loss_value]])
    return df