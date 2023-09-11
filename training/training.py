import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sb
import matplotlib.pyplot as plt
from warnings import filterwarnings
filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

train = pd.read_csv("./Training.csv")
test = pd.read_csv('./Testing.csv')
A = train
B = test

A = A.drop(["Unnamed: 133"],axis=1)

Y = A[["prognosis"]]
X = A.drop(["prognosis"],axis=1)
P = B.drop(["prognosis"],axis=1)

xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size = 0.2, random_state = 42)

dtc= DecisionTreeClassifier(random_state = 42)
model_dtc = dtc.fit(xtrain, ytrain)
tr_pred_dtc = model_dtc.predict(xtrain)
ts_pred_dtc = model_dtc.predict(xtest)

print(tr_pred_dtc)

model = joblib.load('./decision_tree_model.pkl')
