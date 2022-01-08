from bs4 import BeautifulSoup
from urllib.request import urlopen
import streamlit as st
import pandas as pd
import re

# url = "https://outlook.office.com/mail/inbox/id/AAQkADBkNjEyZTIzLWFjYzYtNDI4NS1iYTFjLTAzZjk1MDMxOTY0MAAQAKi4CQlarU5HneqQvTFe908%3D"

# content = urlopen(url).read()
f = open("./websiteHTML.html", "r")

soup = BeautifulSoup(f.read()) 

# print(soup.prettify())
df = pd.DataFrame()
texts = []
for text in soup.find_all("div", {"class": "exit-polls-generalsstyles__ExitPollCardBackground-sc-1takans-29 bxkxsr"}):

    texts.append(text.get_text())
df["raw"] = texts


# st.table(df)
df2 = pd.DataFrame()
questions = []
precentages = []
categories = []
for div in soup.find_all("div", {"class": "exit-polls-generalsstyles__ExitPollCardBackground-sc-1takans-29 bxkxsr"}):

    for text in div.find_all("td", {"class": "hWSzXd"}):
        st.write(text)
for raw in df["raw"]:
    try:
        question = raw.split("?")[0]
        questions.append(question)
        text = raw.split("?")[1]
        res = [re.findall(r'\b\S+\b', text) ]
       
       
        # st.write(question)
        newTxt = ""
        for char in text:
            if char in "0123456789%":
                
                newTxt += " "
            else:
                newTxt += char
        for cat in newTxt.split(" "):
            categories.append(cat)
        # st.text(newTxt)
        
        precent = re.findall('\d*%', text)
        precentages.append(precent)
       # st.write(precent) 
       
        
    except:
        print(1)

# df2["Precentages"] = precentages
# df2["Questions"] = questions
# df2["Category"] = categories
st.table(precentages)
st.table(categories)