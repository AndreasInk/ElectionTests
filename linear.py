# import sklearn as sk
import pickle
import streamlit as st
import glob
import pandas as pd

def showData(path):

    candidate = 0



    locations = glob.glob(path + "/*.csv")

    count = 1
    for location in locations:
        if "Main" not in location:
            tmpDf = pd.read_csv(location)
            tmpDf = tmpDf.drop(columns=["Unnamed: 0"])
        
            tmpDf["Candidate"] = [
                1 if item == "Trump" else 0 for item in list(tmpDf["Candidate"])
            ]
            title = location.replace(path + "/", "").replace(".csv", "")

        
            
            
            
            withoutCandidate = [] 
            for feature in tmpDf.columns:
                if feature != "Candidate":
                    cleanBiden = str(tmpDf[feature][0]).replace("%", "")
                    cleanTrump = str(tmpDf[feature][1]).replace("%", "")
                    withoutCandidate.append(feature)
                    difference = int(cleanTrump) - int(cleanBiden)
            
                    tmpDf[feature] = difference/100
            
                else:
                    tmpDf[feature] = 0
            st.header(str(count) + ") " + title)
            # st.expander("Show Table").table(tmpDf)
            op1 = st.selectbox("", options=tmpDf.columns, key=title)

            st.session_state["score"] += tmpDf[op1][0]
            count += 1
        
    st.sidebar.header("Output")
    st.sidebar.subheader(round(st.session_state["score"], 2))
    if st.session_state["score"] > 0:
        st.sidebar.image("Trump.jpg")
    else:
         st.sidebar.image("Biden.webp")