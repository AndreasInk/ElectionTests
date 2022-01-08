import streamlit as st
import pandas as pd
import glob
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import numpy as np
import pickle
def train_model(train_features, train_labels, test_features, test_lables, title):
    # Instantiate model
    n_estimators = 1000
    random_state = 42
    # reg_model = RandomForestRegressor(
    #     n_estimators=n_estimators, random_state=random_state
    # )
    class_model = RandomForestClassifier(
        n_estimators=n_estimators, random_state=random_state
    )

    # Train the models on training data
    #reg_model.fit(train_features, train_labels)
    class_model.fit(train_features, train_labels)

    # Use the forest's predict method on the test data
    #reg_pred = reg_model.predict(test_features)
    class_pred = class_model.predict(test_features)
    st.write(class_pred)
    pickle.dump(class_model, open("./models/" + title + ".sav", "wb"))
    return class_model, class_pred




path = "./data"
locations = glob.glob(path + "/*.csv")
st.write(locations)

df = pd.DataFrame()
for location in locations:
    st.write(location)
    tmpDf = pd.read_csv(location)
    tmpDf = tmpDf.drop(columns=["Unnamed: 0"])
    tmpDf["Candidate"] = [
        1 if item == "Trump" else 0 for item in list(tmpDf["Candidate"])
    ]
    st.table(tmpDf)
    labels = np.array(tmpDf["Candidate"])
    
    for feature in tmpDf.columns:
        cleanBiden = str(tmpDf[feature][0]).replace("%", "")
        cleanTrump = str(tmpDf[feature][1]).replace("%", "")
        
        biden = int(cleanBiden) - int(cleanTrump)
        trump = int(cleanTrump) - int(cleanBiden)
        tmpDf[feature] = [biden, trump]
        st.table(tmpDf)
    
    df = np.array(tmpDf)
    train_features, test_features, train_labels, test_labels = train_test_split(
        df, labels, test_size=0.25, random_state=42
    )
    feature_list = [i for i in list(tmpDf.columns) if i != "Candidate"]
    tmpDf = tmpDf.drop(columns=["Candidate"])
    title = location.replace("./data/", "").replace(".csv", "")
    train_model(tmpDf[feature_list], labels, tmpDf[feature_list], df, title)
    
    



