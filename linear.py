import sklearn as sk
import pickle
import streamlit as st
import glob
import pandas as pd
def load_classifier_model():
    # import_dir = "./models/View of Mike Pence:.sav"
    import_dir = "./models/Age.sav"
    model = pickle.load(open(import_dir, "rb"))
    return model

class_model = load_classifier_model()
tmpDf = pd.read_csv("./data/Age.csv")
tmpDf = tmpDf.drop(columns=["Unnamed: 0"])
tmpDf["Candidate"] = [
    1 if item == "Trump" else 0 for item in list(tmpDf["Candidate"])
]
st.table(tmpDf)
age = st.slider("Age", key="Age")
candidate = 0
if age > 40 and age < 50:
    distanceToCenter = age - 45
    if distanceToCenter != 0:
        candidate += 0.5/distanceToCenter
if age < 40:
    candidate -= 0.5

if age > 50:
    candidate += 0.3

tmpDf = pd.read_csv("./data/Religion.csv")
tmpDf = tmpDf.drop(columns=["Unnamed: 0"])
tmpDf["Candidate"] = [
    1 if item == "Trump" else 0 for item in list(tmpDf["Candidate"])
]
st.table(tmpDf)

col1, col2, col3, col4 = st.columns(4)
christan = col1.button("Christan")
catholic = col2.button("Catholic")
jewish = col3.button("Jewish")
none = col4.button("None")


if christan:
    candidate += 0.5
if catholic:
    candidate -= 0.2

# age2 = st.slider("Older than 45")
# fav = st.slider("Pence is Favorable")
# notFav = st.slider("Pence is Not Favorable")
# model_input = [[age, age2]]
# class_pred = class_model.predict(model_input)

path = "./data"
locations = glob.glob(path + "/*.csv")


for location in locations:
    if "Main" not in location:
        tmpDf = pd.read_csv(location)
        #tmpDf = tmpDf.drop(columns=["Candidate"])
        tmpDf = tmpDf.drop(columns=["Unnamed: 0"])
    
        tmpDf["Candidate"] = [
            1 if item == "Trump" else 0 for item in list(tmpDf["Candidate"])
        ]
        title = location.replace("./data/", "").replace(".csv", "")
        #st.header(title)
        st.table(tmpDf)
        
        
        withoutCandidate = [] 
        for feature in tmpDf.columns:
            if feature != "Candidate":
                cleanBiden = str(tmpDf[feature][0]).replace("%", "")
                cleanTrump = str(tmpDf[feature][1]).replace("%", "")
                withoutCandidate.append(feature)
                difference = int(cleanTrump) - int(cleanBiden)
            # trump = int(cleanTrump) - int(cleanBiden)
                # amount = []
                # amount.append()
                # if  difference > 0:
                #     for i in range(len(tmpDf[feature].index)):
                #         amount.append(difference/10)
                #         #st.write(0)
                # else:
                #     for i in range(len(tmpDf[feature].index)):
                #         amount.append(difference/10)

                tmpDf[feature] = difference/100
        
            else:
                tmpDf[feature] = 0
        op1 = st.selectbox(title, options=tmpDf.columns)
        st.write(tmpDf[op1])
        candidate += tmpDf[op1][0]
                #df[feature] = amount
        #st.table(tmpDf)
        
        # df2 = np.array(tmpDf)
        # labels = np.array(tmpDf.columns)
        # try:
        #     train_features, test_features, train_labels, test_labels = train_test_split(
        #         df2, labels, test_size=0.25, random_state=42
        #     )
        # except:
        #     print(1)
        # feature_list = [i for i in list(tmpDf.columns) if i != "Candidate"]

# st.write("Trump" if candidate > 0 else "Biden")
st.header(candidate)