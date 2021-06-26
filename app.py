import streamlit as st 
from functions import *
st.write('Driver detection with image')


image = st.file_uploader(label='upload image on which you want to detect',type = ['png','jpg'])


if image is not None:
    st.image(image= image,caption = 'uploaded image')
    x = predict_with_image(image)
    st.write(x)
else:
    st.write('upload the image first')
