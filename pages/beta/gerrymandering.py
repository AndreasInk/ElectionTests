import streamlit as st
from sim import Community
from sim import Voter
import random as rnd
   
def gerry():
    Blue_Limit = st.slider('Blue_Limit', 0, 100)/100
    Red_Limit =  st.slider('Red_Limit', 0, 100)/100
    Grey_Limit = st.slider('Grey_Limit', 0, 100)/100
    if st.button("RUN"):
        Person = 0
        
        Total_Blues = 0
        Total_Reds = 0
        Total_Greys = 0
        Total_Lean = ""
        community = Community()

        while Person < 1000:
            number = rnd.random()
            if number < Blue_Limit:
                lean = "+"
                Blue_Limit_New = .7
                Red_Limit_New = .97
                Grey_Limit_New = 1
                Total_Blues = Total_Blues + 1
            elif number < Red_Limit:
                lean = "-"
                Blue_Limit_New = .32
                Red_Limit_New = .97
                Grey_Limit_New = 1
                Total_Reds = Total_Reds + 1
            else:
                lean = "?"
                Blue_Limit_New = .45
                Red_Limit_New = .9
                Grey_Limit_New = 1
                Total_Greys = Total_Greys + 1
            v = Voter(lean)
            community.Add_Voter(v)
            Blue_Limit = Blue_Limit_New
            Red_Limit = Red_Limit_New
            Grey_Limit = Grey_Limit_New
            Total_Lean = Total_Lean + lean
            Person = Person + 1

        print ()
        print (community.Get_Voter_String())
        print (community.Get_Community_Lean(), community.voter_lean_blue, community.voter_lean_red, community.voter_lean_grey)
        print ()

        #let's split up our community in smaller communities (i.e. districts)
        for i in range(0, 10):
            #define a district
            D = Community()
            #assign the proper voters to the proper district (voters 0 through 9 to District 1, voters 10 through 19 to District 2, etc...)
            D.voter_list = community.voter_list[i*10 : i*10 + 10]
            community.Add_District(D)
            print()
            print (D.Get_Voter_String())
            print (D.Get_Community_Lean())

        districts_leaning_blue = 0
        districts_leaning_red = 0
        districts_leaning_grey = 0

        for d in community.voter_districts: # voter_districts after split
            if d.Get_Community_Lean() == "Blue":
                districts_leaning_blue = districts_leaning_blue + 1
            elif d.Get_Community_Lean() == "Red":
                districts_leaning_red = districts_leaning_red + 1
            elif d.Get_Community_Lean() == "Grey":
                districts_leaning_grey = districts_leaning_grey + 1

        districts_lean = ""
        if districts_leaning_blue >= districts_leaning_red and districts_leaning_blue >= districts_leaning_grey:
            districts_lean = "Blue"
        elif districts_leaning_red >= districts_leaning_blue and districts_leaning_red >= districts_leaning_grey:
            districts_lean = "Red"
        elif districts_leaning_grey >= districts_leaning_blue and districts_leaning_grey >= districts_leaning_red:
            districts_lean = "Grey"
        print()
        print("\tPlus leaning voter\tMinus leaning voters\tNumber of independent voters")
        print (community.Get_Community_Lean(), community.voter_lean_blue, community.voter_lean_red, community.voter_lean_grey)
        print (districts_lean, districts_leaning_blue, districts_leaning_red, districts_leaning_grey)
        st.write(community.Get_Community_Lean())

gerry()