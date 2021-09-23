# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:27:20 2021

@author: ASUS
"""

import pandas as pd
import numpy as np
import streamlit as st
import re
import pickle
import projectfinal

st.sidebar.image("Team_Logo1.JPG" , width=300)

menu = ["Home" , "About Us"]

choice = st.sidebar.selectbox("Menu" , menu)

if choice == "Home": #Home
    
    st.markdown("<h1 style='text-align: center; color:#1DA1F2'><b>Twitter Sentiment Analysis Tool For <br> Racism And Sexism</b></h1>", unsafe_allow_html=True)
    
    st.text("")
    
    st.image("Body_image3.jpg" , width = 700)
    
    st.text("")
    
    user_review = st.text_input('Enter The Comment You Want To Test')

    if st.button("Analyze"):
        prediction = projectfinal.testing(user_review)
        if prediction == 0:
            st.success('Your comment is a positive comment. Racism and Sexism should not be in the world.You are great!')
        elif prediction == 1:
            st.error('Your comment is a negative comment. The day you stop blaming others is the day you begin to discover who you truely are.')

   
else: #About Us
    
    st.markdown("<p style='text-align: left; color: #1DA1F2; font-size: 150%'><b>We are Team Trio. We made the app together by doing our part task. Here, we         want to tell about ourself.</b></p>", unsafe_allow_html=True)
    
    st.text("")
    
    col1 , col2 , col3 = st.columns(3)
    col1.image('https://th.bing.com/th/id/OIP.W-P6hA0MFd0MfJUWtC025gAAAA?pid=ImgDet&rs=1', width = 200)
    col1.write("<p style = 'text-align: left; font-size:110%; color:#1DA1F2'></p>", unsafe_allow_html = True)
    
    col2.image('nmk.png', width = 200)
    col2.write("<p style = 'text-align: left; font-size:110%; color:#1DA1F2'>I am Nyi Min Khant. I am a student from UTYCC. I made the User Interface of this               software.</p>", unsafe_allow_html = True)
    
    col3.image('https://th.bing.com/th/id/OIP.W-P6hA0MFd0MfJUWtC025gAAAA?pid=ImgDet&rs=1', width = 200)  
    col3.write("<p style = 'text-align: left; font-size:110%; color:#1DA1F2'></p>", unsafe_allow_html = True)
