#Libraries
import pandas as pd
import streamlit as st
import numpy as np
import pickle
import streamlit as st
import streamlit.components.v1 as components
from babel.numbers import format_currency
import gunicorn
from sklearn.model_selection import train_test_split



def main():
    st.set_page_config(page_title='House-Price-Finder', page_icon='resources/favicon.png', layout="centered", initial_sidebar_state="auto", menu_items=None)

    html_string = '''
    <script language="javascript">
    alert("நன்றி! / Thank You  / धन्यवाद - Project by Immanuel");
    </script>
    '''

    components.html(html_string)
    rating_string = '''
    <script type="text/javascript">function zforms_open_window(url, height, width){var leftPos = 0;var topPos = 0;if(screen){leftPos = (screen.width - width) / 2;topPos = (screen.height - height) / 2;window.open(url, null, 'width='+width+',height='+height+',left='+leftPos+',top='+topPos+', toolbar=0, location=0, status=1, scrollbars=1, resizable=1');}}</script><a href='https://forms.zohopublic.com/arulshirts/form/ProductReview/formperma/cPBQI8W_IAzwgeHo2oSeohvGYuSnYX2v1253WjxRX6o' title="Review" target='_blank' onclick="zforms_open_window(this.href, 648, 700); return false"> 👋Ratings Here </a>>
    '''

    

    
    



    #Dataset
    data = pd.read_csv("cleaned.csv")
    model = pickle.load(open('model_pkl','rb'))


    st.markdown("<h1 style='text-align: center; color: grey;'>Chennai House Price</h1>", unsafe_allow_html=True)





    #st.title("Finding House Price")


    AREA = st.selectbox("Select your city ",data.AREA.unique())
    if AREA == 'Chrompet':
        filtered=data[data['AREA']=='Chrompet']
        AREA = 2
    elif AREA == 'Karapakkam':
        filtered=data[data['AREA']=='Karapakkam']
        AREA  = 4
    elif AREA == 'KK Nagar':
        filtered=data[data['AREA']=='KK Nagar']
        AREA = 3
    elif AREA == 'Anna Nagar':
        filtered=data[data['AREA']=='Anna Nagar']
        AREA = 1
    elif AREA == 'Adyar':
        filtered=data[data['AREA']=='Adyar']
        AREA = 0
    elif AREA == 'T Nagar':
        filtered=data[data['AREA']=='T Nagar']
        AREA = 5
    elif AREA == 'Velachery':
        filtered=data[data['AREA']=='Velachery']
        AREA = 6





    INT_SQFT = st.slider("How many SQFT you want",int(data.INT_SQFT.min()),int(data.INT_SQFT.max()))

    N_BEDROOM = st.slider("How many Bedrooms you want",int(data.N_BEDROOM.min()),int(data.N_BEDROOM.max()))

    PARK_FACIL = st.radio("Do you want parking Facilty ?",data.PARK_FACIL.unique())
    if PARK_FACIL == 'Yes':
        PARK_FACIL = 1
    else:
        PARK_FACIL = 0


    #Coverting MZZONe categorical to numerical
    MZZONE = st.selectbox("Which Zone you prefer ?",filtered.MZZONE.unique())
    if MZZONE == 'A':
        MZZONE = 0
    elif MZZONE == 'RH':
        MZZONE = 3
    elif MZZONE == 'RL':
        MZZONE = 4
    elif MZZONE == 'I':
        MZZONE = 2
    elif MZZONE == 'C':
        MZZONE = 1
    else:
        MZZONE = 5

    BUILDTYPE = st.radio("What kind of purpose you need  ?",data.BUILDTYPE.unique())

    if BUILDTYPE == 'House':
        BUILDTYPE = 1
    elif BUILDTYPE == 'Others':
        BUILDTYPE = 2
    else:
        BUILDTYPE = 0





    input = pd.DataFrame([[INT_SQFT,BUILDTYPE,MZZONE,AREA,N_BEDROOM,PARK_FACIL]],columns=['INT_SQFT','BUILDTYPE','MZZONE','AREA','N_BEDROOM','PARK_FACIL'],index=['index'])
                        
                        
    #st.dataframe(input)

    valu = model.predict(input)
    low=int(valu-(valu*0.02))
    low = format_currency(low, 'INR', locale='en_IN')


    high=int(valu+(valu*0.02))
    high = format_currency(high, 'INR', locale='en_IN')

    #print('Estimated value is:',low , 'to', high)


    if st.button("Find Price",help="Click here to predict the price"):
        st.markdown("<h1 style='text-align: center; color: grey;'>Estimated House Price</h1>", unsafe_allow_html=True)
        st.write("*******************************",  low , 'to', high   ,"*******************************")
        st.balloons()

    components.html(rating_string)


if __name__=='__main__':
    main()



    


#By Immanuel

