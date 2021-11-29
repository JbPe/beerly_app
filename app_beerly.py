import os
import streamlit as st
#from ocr import ocr_image
import cv2 as cv2
import base64

if __name__ == '__main__':
    #main_bg = "../raw_data/img/beerly_wp.png"
    main_bg = "beerly_wp.png"
    main_bg_ext = "png"


    st.set_page_config(page_title='Beerly', page_icon='🍻')

    st.markdown(""" <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)

    st.markdown("""
        <style>
                .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
            }}
        </style>
        """,
                unsafe_allow_html=True)

    # identification de l'user



    with st.form('test', clear_on_submit=True):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')

    if password != 'test' or username == None:
        pass

    else:
        # Select a file
        st.write('# Upload a menu')
        image_file = st.file_uploader("Your menu", type=['jpg', 'png', 'jpeg'])


        if image_file != None:
            #st.write(ocr_image(image_file.name))
            aroma = st.slider('Aroma', min_value=0, max_value=1, value=1, step=0.1)
