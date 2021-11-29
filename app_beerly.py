import os
from numpy.lib.function_base import place
import streamlit as st
import base64
import requests
import numpy as np
from PIL import Image
import pickle

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
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')

    # Si l'identification est successful
    if password == 'test' and username != None:
        # Select a file
        st.write(f'# Hello {username}!')
        st.write('## Please upload a menu')
        img = st.file_uploader("Your menu", type=['jpg', 'png', 'jpeg'])

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

            # request to be sent to the api. Need a user_id
            headers = {}
            headers['Content-Type'] = 'application/json'
            request_dict = {'image' : img_enc.decode('utf8').replace("'", '"'),
                            'user' : username,
                            'height' : height,
                            'width' : width,
                            'channel' : channel}

            #post request
            #requests.post('http://127.0.0.1:8000/predict',json.dumps(request_dict), headers = headers)


            # Sliders
            st.write('## Choose your parameters')
            st.write("### Or let them as is if you don't have any preferences")
            aroma = st.slider("Aroma",value=1.0, min_value=0.0, max_value=1.0, step=0.1)
            st.write("The aroma of a beer originates from a number of sources, which essentially comes down to the malt, hops, yeast and any additional ingredients added during the brewing process.")
            appearance = st.slider("Appearance", value=1.0, min_value=0.0, max_value=1.0, step=0.1)
            st.write("##### ")
            palate = st.slider("Palate", value=1.0, min_value=0.0, max_value=1.0, step=0.1)
            st.write("##### ")
            taste = st.slider("Taste", value=1.0, min_value=0.0, max_value=1.0, step=0.1)
            st.write("##### ")

            #Call API
            call_api = st.button('Go get me the best beer !')

            #appeler l'API avec image_file + aroma + appearance + palate + taste + username
            if call_api:
                url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"

                # return un DataFramede X bières
                reponse = requests.get(url, params="userId=3")
                contenu = reponse.json()
                dataframe = st.dataframe(contenu)

                # 1 trier le dictionnaire

                # 2 sélectionner la meilleure bière
