from numpy.lib.function_base import place
import streamlit as st
import base64
import requests
import numpy as np
from PIL import Image
import pandas as pd
import json

if __name__ == '__main__':
    main_bg = "beerly_wp.png"
    main_bg_ext = "png"

    #test


    # Name of the page + icon
    st.set_page_config(page_title='Beerly', page_icon='🍻')

    # Hide left menu
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # Set Background
    st.markdown(f"""
        <style>
            .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});background-repeat: no-repeat
            }}
        </style>
        """,
                unsafe_allow_html=True)

    # CSS Parameters
    st.markdown(
        '<style>h1{ font-family: "American Typewriter", cursive; font-size: 50px; line-height: 60px; margin: 10px 0 20px; text-transform: uppercase; text-shadow: 2px 2px 0 #000, margin: 10px 0 24px; text-align: center; }</style>',
        unsafe_allow_html=True)
    st.markdown(
        '<style>h2{font-family: "Palatino" ;font-size: 30px; letter-spacing: -1px; text-transform: uppercase; text-shadow: 1px 1px 0 #000, margin: 10px 0 24px; text-align: center; line-height: 50px;}</style>',
        unsafe_allow_html=True)
    st.markdown(
        '<style>p{text-align: justify;font-family: "Palatino", sans-serif; font-size: 16px; line-height: 24px; margin: 0 0 24px;}</style>',
        unsafe_allow_html=True)
    st.markdown(
        '<style>h3{font-family: "Impact" ;font-size: 30px; letter-spacing: -1px; text-transform: uppercase; text-shadow: 1px 1px 0 #000, margin: 10px 0 24px; text-align: center; line-height: 50px;}</style>',
        unsafe_allow_html=True)

    # user authentification
    placeholder = st.empty()
    with placeholder.form('test', clear_on_submit=True):
        username = st.text_input('Username','Cadiz')
        password = st.text_input('Password', type = 'password')
        col1, col2, col3 , col4, col5 = st.columns(5)
        with col1:
            pass
        with col2:
            pass
        with col4:
            pass
        with col5:
            pass
        with col3 :
            login = st.form_submit_button('Login')

    # If authentification is successful
    if password == 'test' and username != None:
        placeholder.empty()
        # Select a file
        greetings = st.write(f'# Hello {username} !')
        st.write('## Please upload a menu')
        img = st.file_uploader("\n", type=['jpg', 'png', 'jpeg'])

        if img != None:
            # Need to check if the image looks like a menu before calling the api

            # Sliders
            st.write('## Choose your parameters')
            st.write("Or let them as is if you don't have any preferences")
            with st.expander("Aroma"):
                aroma = st.slider(
                    "The aroma of a beer originates from a number of sources, which essentially comes down to the malt, hops, yeast and any additional ingredients added during the brewing process.",
                    value=1.0,
                    min_value=0.0,
                    max_value=1.0,
                    step=0.1)
            with st.expander("Appearance"):
                appearance = st.slider(
                    "The visual characteristics that may be observed in a beer are colour, clarity, and nature of the head. Colour is usually imparted by the malts used, notably the adjunct malts added to darker beers, though other ingredients may contribute to the colour of some styles such as fruit beers.",
                    value=1.0,
                    min_value=0.0,
                    max_value=1.0,
                    step=0.1)
            with st.expander("Palate"):
                palate = st.slider(
                    "Palate is typically defined as the sense of taste. In Ratebeer's system, it refers to mouthfeel and not taste or aroma.",
                    value=1.0,
                    min_value=0.0,
                    max_value=1.0,
                    step=0.1)
            with st.expander("Taste"):
                taste = st.slider(
                    "The taste of beer primarily depends on its ingredients. ... Hops adds a trace of bitterness to beer that goes well with citrus and floral additives. Yeast gives a neutral, sugary taste to beer and emphasizes fruit and spicy notes in its aroma.",
                    value=1.0,
                    min_value=0.0,
                    max_value=1.0,
                    step=0.1)

            # convert image to np array
            img = Image.open(img)
            rgb_im = img.convert('RGB')
            imgArray = np.array(rgb_im)

            # encode into 1 dim uint8 string
            img = imgArray.astype('uint8')
            height, width, channel = img.shape
            img_reshape = img.reshape(height * width * channel)
            img_enc = base64.b64encode(img_reshape)

            #Call API
            col1, col2, col3 , col4, col5 = st.columns(5)
            with col1:
                pass
            with col2:
                pass
            with col4:
                pass
            with col5:
                pass
            with col3 :
                call_api = st.button('Get me my beer !')


            #call the API with image_file + aroma + appearance + palate + taste + username
            if call_api:

                # request to be sent to the api
                headers = {}
                headers['Content-Type'] = 'application/json'
                request_dict = {
                    'image': img_enc.decode('utf8').replace("'", '"'),
                    'user': username,
                    'height': height,
                    'width': width,
                    'channel': channel,
                    'taste': taste,
                    'appearance': appearance,
                    'palate': palate,
                    'aroma': aroma,
                    'overall': 1,
                    'content': 5
                }

                # request & decoding
                #req = requests.post('http://127.0.0.1:8000/predict',json.dumps(request_dict), headers = headers)

                #st.write(req)


                url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"

                # return a dataframe of X beers

                #
                response = requests.get(url, params="userId=3")
                content_response = response.json()

                content = pd.DataFrame(content_response)

                st.table(
                    content.style.highlight_max(
                        props='font-weight:bold;color:#FFFF00'))

                # JSON Content
                # st.write(type(contenu))
                # st.write(contenu)

                # 1st row of the JSON content
                # st.write(contenu[0]["title"])
                # st.write(contenu[0]["id"])

                # Selecting the best beer

                st.write("## The beer we've chosen for you is :")
                st.write(f'### {content_response[0]["title"]}')
                #contenu[0]["id"]
