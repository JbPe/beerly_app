import os
from numpy.lib.function_base import place
import streamlit as st
import base64
import requests
import numpy as np
from PIL import Image
import pickle
import pandas as pd
import json

if __name__ == '__main__':
    main_bg = "beerly_wp.png"
    main_bg_ext = "png"

    # Nom de la page + icone
    st.set_page_config(page_title='Beerly', page_icon='🍻')

    # Cacher le menu
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """,
                unsafe_allow_html=True)

    # Set Background
    st.markdown(f"""
        <style>
            .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
            }}
        </style>
        """,
                unsafe_allow_html=True)

    # identification de l'user
    placeholder = st.form('test', clear_on_submit=True)
    with placeholder:
        username = st.text_input('Username','99996')
        password = st.text_input('Password')
        login = st.form_submit_button('Login')

    # Si l'identification est successful
    if password == 'test' and username != None:
        # Select a file
        st.write(f'# Hello {username}!')
        img = st.file_uploader("Please upload a menu", type=['jpg', 'png', 'jpeg'])

        if img != None:

            # Besoin de vérifier directement si l'image ressemble à un menu ou non

            # convert image to np array
            img = Image.open(img)
            rgb_im = img.convert('RGB')
            imgArray = np.array(rgb_im)

            # encode into 1 dim uint8 string
            img = imgArray.astype('uint8')
            height, width, channel = img.shape
            img_reshape = img.reshape(height*width*channel)
            img_enc = base64.b64encode(img_reshape)

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

            #Call API
            call_api = st.button('Go get me the best beer my little man !')

            #appeler l'API avec image_file + aroma + appearance + palate + taste + username
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
                    'content': 1
                }

                # requête et décodage
                #req = requests.post('http://127.0.0.1:8000/predict',json.dumps(request_dict), headers = headers)

                #st.write(req)


                url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"

                # return un DataFramede X bières
                reponse = requests.get(url, params="userId=3")
                contenu = reponse.json()
                dataframe = st.dataframe(contenu)

                # Contenu de la réponse JSON
                # st.write(type(contenu))
                # st.write(contenu)

                # 1ère ligne de la réponse JSON
                # st.write(contenu[0]["title"])
                # st.write(contenu[0]["id"])

                # sélectionner la meilleure bière


                # best_beer_name
                # best_beer_rating

                col1, col2 = st.columns(2)
                col1.metric("Beer", contenu[0]["title"])
                col2.metric("Estimated Rating", contenu[0]["id"])
