"""
Purpose of this script is to organise functions for cleaning and organising data to 
ensure consistent results through testing.

Assumptions:
- The official dataset from 2014 will be used (atlas-higgs-challenge-2014-v2.csv)
- The official dataset is unchanged
- Any different datasets follow the same format as the official 2014 dataset
        (i.e. signals will be under "Label", identified as "s", and all columns will have headings)
- Following the exploratory data analysis, there are no null values.

"""

import pandas as pd
from pathlib import Path

def pull_data(file):
    root = Path().resolve()
    while not (root/"src").exists():
        root = root.parent
    df = pd.read_csv(root/file)
    return df

def create_target(df):
    df["Target"] = (df["Label"] == "s").astype(int)
    return df



def select_features(df, features, target):
    x_data, y_data = df[features], df[target]
    return x_data, y_data