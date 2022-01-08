from typing import List
from bs4 import BeautifulSoup
from urllib.request import urlopen
import streamlit as st
import pandas as pd
import re

def showData(text, question):
        
        #text = [re.findall(r'\b\S+\b', text) ]
        df2 = pd.DataFrame()
       
        #st.write(question)
        featuresArr = []
        newTxt = ""
        for char in text:
            if char in "-,0123456789%":
                if newTxt:
                    featuresArr.append(newTxt.replace("total respondents", ""))
                newTxt = ""
            else:
                newTxt += char
        #st.text(newTxt)
        precent = re.findall('\d*%', text)
        st.write(precent) 
        
        for index in range(len(featuresArr)):
            
            df2[featuresArr[index]] = [precent[index]]
        st.header(question)
        st.table(df2)
# url = "https://outlook.office.com/mail/inbox/id/AAQkADBkNjEyZTIzLWFjYzYtNDI4NS1iYTFjLTAzZjk1MDMxOTY0MAAQAKi4CQlarU5HneqQvTFe908%3D"

# content = urlopen(url).read()
f = open("./websiteHTML.html", "r")

soup = BeautifulSoup(f.read()) 

# print(soup.prettify())


for div in soup.find_all("div", {"class": "exit-polls-generalsstyles__ExitPollCardBackground-sc-1takans-29 bxkxsr"}):
    featuresArr = []
    texts = []
    questions = []
    biden = []
    trump = []
    none = []
    
    # df["Candidate"] = ["Biden", "Trump"]
    for text in div.find_all("div", {"class": "bNbmto"}):
       
            featuresArr.append(text.text)
        
      
    index = 0
    
    
    st.write(div.text)
    try:
        precents =  div.text.split("Biden")[1]
        st.write(precents)
    
        st.write(div.text.split("Biden")[0])
        if "Joe" in  div.text.split("Biden")[0]:
            precents =  div.text.split("Biden")[1].split("Biden")[0]
            st.write(precents)
            bidenPrecent =  precents.split("Trump")[0]
            #trumpPrecent =  precents.split("Trump")[1]
        else:
            bidenPrecent =  precents.split("Trump")[0]
            trumpPrecent =  precents.split("Trump")[1]
    except:
        print()
    precentsB = re.findall('\d*%', bidenPrecent)
    precentsT = re.findall('\d*%', trumpPrecent)
    if "n/a" in bidenPrecent:
        precentsB.append("0%")

    if "n/a" in trumpPrecent:
        precentsT.append("0%")

    #     none.append(text.text)
    # for text in div.find_all("td", {"class": "bDkkGs"}):
    #     trump.append(text.text)
    # for text in div.find_all("td", {"class": "hWSzXd"}):
    #     biden.append(text.text)
            # if index % 2 == 0:
                
            #     precentages.append(text.text)
            #     # st.write(precentages)
            # else:
            #      precentages.append(text.text)
            #     # st.write(precentages)
            
        
            
            # index += 1
    for text in div.find_all("div", {"class": "sPzuG"}):
        questions.append(text.text)
    

        
            
        # for index in range(len(featuresArr)):
        #     columns = []
        #     try:
        #         columns = [precentages[index]]
        #         # st.write(df[featuresArr[index]])
                
        #     except:
        #         print(1)
        #     = columns
    st.header(text.text) 
    st.write(precentsB)
    st.write(precentsT)
    st.write(none)
    st.write(featuresArr)
    df = pd.DataFrame()
    df["Candidate"] = ["Biden", "Trump"]
    for index in range(len(featuresArr)):
        try:
            df[featuresArr[index]] = [precentsB[index], precentsT[index]]
        except:
            print()
    st.table(df)
    df.to_csv("./data/" + text.text + ".csv")
        
        
    

    # df["Precentages"] = p
        
   




questions = []
tableIndex = 0


# for raw in df["raw"]:
#     df2 = pd.DataFrame()
    
#     tableIndex += 1

