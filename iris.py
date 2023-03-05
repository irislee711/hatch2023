import streamlit as st
from PIL import Image

#title
st.title("Welcome to lightbulb! :bulb: :four_leaf_clover:")
menu = []

#header
st.subheader("Shedding Light on Plants")

#subheader
st.text("Emilia Accardi, Jenna Kim, Iris Lee, Aidan Mann")


imageCaptured = st.camera_input("Capture Image", help="Take a picture of the plant!")
if imageCaptured:
    st.image(imageCaptured)

st.caption('Plant: Clover Scientific Name: _Trifolium Repens_ family: Fabaceae Origin: Europe Additional Sequencing Info: https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/3899/.')