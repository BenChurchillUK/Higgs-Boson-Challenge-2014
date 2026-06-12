"""
Creates functions for splitting data, standardising where necessary, etc.

"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def splitting_data(x_data, y_data):
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size= 0.25, random_state=42, shuffle = True)
    return x_train, x_test, y_train, y_test

def scaling_data(train_data, test_data):
    scaler = StandardScaler()
    train_scaled = scaler.fit_transform(train_data)
    test_scaled = scaler.transform(test_data)
    return train_scaled, test_scaled, scaler