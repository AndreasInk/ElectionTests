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
    if "Main" not in location:
        st.write(location)
        tmpDf = pd.read_csv(location)
        #tmpDf = tmpDf.drop(columns=["Candidate"])
        tmpDf = tmpDf.drop(columns=["Unnamed: 0"])
    
        tmpDf["Candidate"] = [
            1 if item == "Trump" else 0 for item in list(tmpDf["Candidate"])
        ]
        st.table(tmpDf)
    
        title = location.replace("./data/", "").replace(".csv", "")
        for feature in tmpDf.columns:
            if feature != "Candidate":
                cleanBiden = str(tmpDf[feature][0]).replace("%", "")
                cleanTrump = str(tmpDf[feature][1]).replace("%", "")
                
                biden = int(cleanBiden) - int(cleanTrump)
            # trump = int(cleanTrump) - int(cleanBiden)
                amount = []
                if  biden > 0:
                    for i in range(len(tmpDf[feature].index)):
                        amount.append(0)
                        st.write(0)
                else:
                    for i in range(len(tmpDf[feature].index)):
                        amount.append(1)

                tmpDf[feature] = amount
                df[feature] = amount
                st.table(tmpDf)
        
        df2 = np.array(tmpDf)
        labels = np.array(tmpDf.columns)
        # try:
        #     train_features, test_features, train_labels, test_labels = train_test_split(
        #         df2, labels, test_size=0.25, random_state=42
        #     )
        # except:
        #     print(1)
        feature_list = [i for i in list(tmpDf.columns) if i != "Candidate"]
        
    
        
        # st.table(tmpDf)
        # st.write(labels)
   
   # st.table(df)
        #train_model(tmpDf[feature_list], labels, tmpDf[feature_list], df2, title)
    
df.to_csv("./data/Main.csv")
    
    



