"""

"""

import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score

#  Cross Validation

def cross_validation(model, x_data, y_data, heading, folds = 10):
    k_folds = StratifiedKFold(n_splits = folds, shuffle = True, random_state = 42)
    cv_accuracy_scores = cross_val_score(model, x_data, y_data, cv = k_folds, scoring = 'accuracy')
    cv_roc_auc_scores = cross_val_score(model, x_data, y_data, cv = k_folds, scoring = 'roc_auc')
    cv_log_loss_scores = cross_val_score(model, x_data, y_data, cv = k_folds, scoring = 'neg_log_loss')

    metrics = {
        "": heading,
        # "Accuracy Scores": cv_accuracy_scores,
        "Average Accuracy": np.average(cv_accuracy_scores),
        "Accuracy STD": np.std(cv_accuracy_scores),
        "Maximum Accuracy": cv_accuracy_scores.max(),
        "Minimum Accuracy": cv_accuracy_scores.min(),
        # "ROC AUC Scores": cv_roc_auc_scores,
        "Average ROC AUC": np.average(cv_roc_auc_scores),
        "ROC AUC STD": np.std(cv_roc_auc_scores),
        "Maximum ROC AUC": cv_roc_auc_scores.max(),
        "Minimum ROC AUC": cv_roc_auc_scores.min(),
        # "Log Loss Scores": cv_log_loss_scores,
        "Average Log Loss": np.average(cv_log_loss_scores),
        "Log Loss STD": np.std(cv_log_loss_scores),
        "Maximum Log Loss": cv_log_loss_scores.max(),
        "Minimum Log Loss": cv_log_loss_scores.min()
    }
    return metrics

#  Repeated Splits

#  Stability Checks