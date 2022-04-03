# Import Libraries
import pandas as pd
import numpy as np
import pickle
import streamlit as st
import streamlit.components.v1 as components
from babel.numbers import format_currency
import gunicorn
from sklearn.model_selection import train_test_split
from zipfile import ZipFile
zip = ZipFile('model.zip')
zip.extractall()

def main():
  st.set_page_config(page_title="House-Price-Predictor",page_icon="house.jpg",layout="centered",initial_sidebar_state="auto",menu_items=None)
  st.image("house.jpg")
  st.title("House Sales Price and Overall Price Predictor")
  
  html_string='''
  <script language="javascript">
  alert("Thank You for visiting my project-Vignesh S")
  </script>
  '''
  components.html(html_string)

  # Data
  Data = pd.read_csv("train-chennai-sale.csv")
  Data_1 = pd.read_csv("Final_Data.csv")
  Data_2 = pd.read_csv("Final_Data_2.csv")
  model_1=pickle.load(open("model_pkl_1","rb"))
  model_2=pickle.load(open("model_pkl_2","rb"))

  st.markdown("<ht styl='text-align:center; color: Black;'>Chennai House SalesPrice and Overall Price</hr>",unsafe_allow_html=True)

  #Finding House sales price and overall price
  AREA=st.selectbox("Select your city",Data.AREA.unique())
  if AREA == "Karapakkam":
    filtered=Data_1[Data_1["AREA"]=="Karapakkam"]
    AREA = 4
  elif AREA == "Anna Nagar":
    filtered=Data_1[Data_1["AREA"]=="Anna Nagar"]
    AREA = 1
  elif AREA == "Adyar":
    filtered=Data_1[Data_1["AREA"]=="Adyar"]
    AREA = 0
  elif AREA == "Velachery":
    filtered=Data_1[Data_1["AREA"]=="Velachery"]
    AREA = 6
  elif AREA == "Chrompet":
    filtered=Data_1[Data_1["AREA"]=="Chrompet"]
    AREA = 2
  elif AREA == "KK Nagar":
    filtered=Data_1[Data_1["AREA"]=="KK Nagar"]
    AREA = 3
  elif AREA == "T Nagar":
    filtered=Data_1[Data_1["AREA"]=="T Nagar"]
    AREA = 5

  INT_SQFT = st.slider("How many Square Feet do you want",int(Data_1.INT_SQFT.min()),int(Data_1.INT_SQFT.max()))

  N_BEDROOM = st.slider("How many Bedrooms you want",int(Data_1.N_BEDROOM.min()),int(Data_1.N_BEDROOM.max()))

  N_BATHROOM = st.slider("How many Bathrooms you want",int(Data_1.N_BATHROOM.min()),int(Data_1.N_BATHROOM.max()))

  N_ROOM = st.slider("How many Rooms you want",int(Data_1.N_ROOM.min()),int(Data_1.N_ROOM.max()))

  PARK_FACIL = st.radio("Do you want parking Facilty ?",Data.PARK_FACIL.unique())
  if PARK_FACIL == 'Yes':
      PARK_FACIL = 1
  else:
      PARK_FACIL = 0

  BUILDTYPE = st.radio("What Should be the Buildtype of your house  ?",Data.BUILDTYPE.unique())

  if BUILDTYPE == 'House':
      BUILDTYPE = 2
  elif BUILDTYPE == 'Others':
      BUILDTYPE = 1
  elif BUILDTYPE == 'Commerical':
      BUILDTYPE = 0

  STREET = st.radio("Which Street do you need  ?",Data.STREET.unique())

  if STREET == 'Paved':
      STREET = 0
  elif STREET == 'Gravel':
      STREET = 1
  elif STREET == 'Others':
      STREET = 2

  MZZONE = st.selectbox("Which Zone do you prefer ?",Data.MZZONE.unique())
  if MZZONE == 'A':
      MZZONE = 0
  elif MZZONE == 'RH':
      MZZONE = 1
  elif MZZONE == 'RL':
      MZZONE = 2
  elif MZZONE == 'I':
      MZZONE = 3
  elif MZZONE == 'C':
      MZZONE = 4
  elif MZZONE == 'RM':
      MZZONE = 5

  AGE_OF_HOUSE = st.slider("What should be the age of your house ,int(Data_1.AGE_OF_HOUSE.min()),int(Data_1.AGE_OF_HOUSE.max()))


  input = pd.DataFrame([[AREA,INT_SQFT,N_BEDROOM,N_BATHROOM,N_ROOM,PARK_FACIL,BUILDTYPE,STREET,MZZONE,AGE_OF_HOUSE]],columns=['AREA','INT_SQFT','N_BEDROOM','N_BATHROOM','N_ROOM','PARK_FACIL','BUILDTYPE','STREET','MZZONE','AGE_OF_HOUSE'],index=['index'])

  i=model_1.predict(input)
  low_1=int(i-(0.0159*i))
  low_1 = format_currency(low_1, 'INR', locale='en_IN')
  high_1=int(i+(0.0159*i))
  high_1 = format_currency(high_1, 'INR', locale='en_IN')

  j=model_1.predict(input)
  low_2=int(i-(0.0166*i))
  low_2 = format_currency(low_2, 'INR', locale='en_IN')
  high_2=int(i+(0.0166*i))
  high_2 = format_currency(high_2, 'INR', locale='en_IN')

  if st.button("Find Sales Price",help="Click for Sales price"):
        st.markdown("<h1 style='text-align: center; color: grey;'>Estimated House Sales Price</h1>", unsafe_allow_html=True)
        st.write(low_1 , 'to', high_1)
        st.balloons()

  if st.button("Find Overall Price",help="Click for Overall price"):
        st.markdown("<h1 style='text-align: center; color: grey;'>Estimated House Overall Price</h1>", unsafe_allow_html=True)
        st.write("Overall price is the combination of Sales Price, Registration Fee and Commision")
        st.write(low_2 , 'to', high_2)
        st.balloons()

  


  if st.button("Like",help="Click to Like the Prediction"):
      st.write("Thanks for Liking the project")

if __name__=='__main__':
    main()


    




