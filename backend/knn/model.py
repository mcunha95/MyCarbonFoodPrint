import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

data_csv = pd.read_csv("data/formated_normalized_food_per_country_ageGroup.csv")

X = np.asarray(data_csv.iloc[:,2:])
y_country = np.asarray(data_csv.iloc[:,0])
y_age = np.asarray(data_csv.iloc[:,1])

neigh_country = KNeighborsClassifier(n_neighbors = 1, weights='uniform', algorithm='auto')
neigh_country.fit(X, y_country)

neigh_age = KNeighborsClassifier(n_neighbors = 1, weights='uniform', algorithm='auto')
neigh_age.fit(X, y_age)

def predict(in_data, info='country'):
    if info == 'country':
        return neigh_country.predict(in_data)[0]
    elif info == 'age':
        return neigh_country.predict(in_data)[0]
    else:
        raise ValueError('Expected "info" to be "country" or "age, got ', info)