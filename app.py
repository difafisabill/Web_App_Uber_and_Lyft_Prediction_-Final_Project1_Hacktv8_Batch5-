import streamlit as st
from predict import display_predict
from explore import display_explore
from PIL import Image
import requests
from io import BytesIO
st.set_page_config(page_title="Uber-Lyft Price Predict", page_icon=":taxi:", layout="wide")

# Download the image from the URL
url = 'https://th.bing.com/th/id/R.9b0869ade2a3e80616a79a23eae7de02?rik=aFzksQrr0xJkKw&riu=http%3a%2f%2fmedia.foxbusiness.com%2fBrightCove%2f854081161001%2f202008%2f3226%2f854081161001_6183052056001_6183055367001-vs.jpg&ehk=nMvNFfPmtpHPomKPuoqe3x5yPc7fkKdTcZtixefreXA%3d&risl=&pid=ImgRaw&r=0'
response = requests.get(url)

if response.status_code == 200:
    # Open the image using PIL
    image = Image.open(BytesIO(response.content))

    # Display the image
    st.image(image, use_column_width=True)
else:
    st.error(f"Failed to download image. Status code: {response.status_code}")

page = st.sidebar.selectbox("Explore Or Predict", ("Explore","Predict"))

if page == "Explore":
    
    display_explore()
    
else:
    display_predict()