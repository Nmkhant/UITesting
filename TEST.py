import pandas as pd
import numpy as np
import streamlit as st
import re
import pickle
import Model

from sklearn.feature_extraction.text import TfidfVectorizer
Tfidf_vexct = TfidfVectorizer()
 
def apply_cleaning_function_to_list(X):
    cleaned_X = []
    for element in X:
        cleaned_X.append(clean_text(element))
    return cleaned_X

st.sidebar.image("Team_Logo1.JPG" , width=300)

menu = ["Home" , "About Us"]

choice = st.sidebar.selectbox("Menu" , menu)

if choice == "Home": #Home
    
    st.markdown("<h1 style='text-align: center; color: #1DA1F2'><b>Twitter Sentiment Analysis Tool For <br> Racism And Sexism</b></h2>", unsafe_allow_html=True)
    
    st.text("")
    
    st.image("https://i.morioh.com/2020/02/04/beef36fd707d.jpg" , width = 700)
    
    st.text("")
    
    user_review = st.text_input('Enter The Review You Want To Test')
    
    if st.button("Analyze"):
        st.success('Well Done')

    else:
        st.markdown("<p style= 'color:red'>Please Enter A Review</p>", unsafe_allow_html=True)

   
else: #About Us
    
    st.markdown("<p style='text-align: left; color: #1DA1F2; font-size: 150%'><b>We are Team Trio. We made the app together by doing our part task. Here, we         want to tell about ourself.</b></p>", unsafe_allow_html=True)
    
    st.text("")
    
    col1 , col2 , col3 = st.columns(3)
    col1.image('https://th.bing.com/th/id/OIP.W-P6hA0MFd0MfJUWtC025gAAAA?pid=ImgDet&rs=1', width = 200)
    col1.write("<p style = 'text-align: left; font-size:120%; color:#1DA1F2'>I am Ma Htet Htet Mon.</p>", unsafe_allow_html = True)
    
    col2.image('https://th.bing.com/th/id/OIP.W-P6hA0MFd0MfJUWtC025gAAAA?pid=ImgDet&rs=1', width = 200)
    col2.write("<p style = 'text-align: left; font-size:120%; color:#1DA1F2'>I am Mg Nyi Min Khant. I am a student from UTYCC. I made the User Interface of this               software</p>", unsafe_allow_html = True)
    
    col3.image('https://th.bing.com/th/id/OIP.W-P6hA0MFd0MfJUWtC025gAAAA?pid=ImgDet&rs=1', width = 200)  
    col3.write("<p style = 'text-align: left; font-size:120%; color:#1DA1F2'>I am Ma Thwet Yin Nyein.</p>", unsafe_allow_html = True)
