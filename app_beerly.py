import streamlit as st
import streamlit.components.v1 as components
import base64
import requests
import numpy as np
from PIL import Image
import pandas as pd
import json

if __name__ == '__main__':
    main_bg = "beerly_wp.png"
    main_bg_ext = "png"

    # Name of the page + icon
    st.set_page_config(page_title='Beerly', page_icon='🍻')


    #padding
    padding = 0
    max_width = 600
    st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        max-width: {max_width}px;
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """,
                unsafe_allow_html=True)


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
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});background-repeat: no-repeat; background-size:cover
            }}
        </style>
        """, unsafe_allow_html=True)

    # CSS Parameters

    # H1
    st.markdown(
        '<style>h1 { color: #333333; font-family: "Tahoma", serif; font-size: 50px; font-weight: normal; line-height: 54px; margin: 0 0 54px; }</style>',
        unsafe_allow_html=True)
    # H2
    st.markdown(
        '<style>h2 {color: #333333; font-family: "Tahoma", serif;font-size: 26px; line-height: 36px; margin: 0 0 28px; }</style>',
        unsafe_allow_html=True)
    # P
    st.markdown(
        '<style>p { color: #333333; font-family: "Tahoma", serif; font-size: 18px; line-height: 28px; margin: 0 0 28px; }</style>',
        unsafe_allow_html=True)
    # H3
    st.markdown(
        '<style>h3{font-family: "Tahoma" ;font-size: 25px; letter-spacing: -1px; text-shadow: 1px 1px 0 #000, margin: 10px 0 24px; text-align: center; line-height: 50px;}</style>',
        unsafe_allow_html=True)
    # H4
    st.markdown(
        '<style>h4{font-family: "Tahoma" ;font-size: 20px; letter-spacing: -1px; text-shadow: 1px 1px 0 #000, margin: 10px 0 24px; text-align: center; line-height: 50px;}</style>',
        unsafe_allow_html=True)


    # user authentification
    placeholder = st.empty()
    with placeholder.form('test', clear_on_submit=True):
        username = st.text_input('Username','Thomas')
        password = st.text_input('Password', type = 'password')
        # centered button
        col1, col2, col3 , col4, col5 = st.columns(5)
        with col1:
            pass
        with col2:
            pass
        with col3 :
            login = st.form_submit_button('Login')
        with col4:
            pass
        with col5:
            pass

    # If authentification is successful
    if password == 'beerly' and username != None:

        #removing the authentification
        placeholder.empty()


        placeholder = st.empty()
        # Select a file
        img = placeholder.file_uploader("Please upload a menu", type=['jpg', 'png', 'jpeg'])

        if img != None:

            placeholder.empty()

            # Sliders
            with st.expander("Advanced parameters"):
                aroma = st.slider(
                    "Aroma",
                    value=50,
                    min_value=0,
                    max_value=100,
                    step=10, help="The aroma of a beer originates from a number of sources, which essentially comes down to the malt, hops, yeast and any additional ingredients added during the brewing process.")
                appearance = st.slider(
                    "Appearance",
                    value=50,
                    min_value=0,
                    max_value=100,
                    step=10,
                    help="The visual characteristics that may be observed in a beer are colour, clarity, and nature of the head. Colour is usually imparted by the malts used, notably the adjunct malts added to darker beers, though other ingredients may contribute to the colour of some styles such as fruit beers."
                )
                palate = st.slider(
                    "Palate",
                    value=50,
                    min_value=0,
                    max_value=100,
                    step=10,
                    help="Palate is typically defined as the sense of taste. In Ratebeer's system, it refers to mouthfeel and not taste or aroma."
                )
                taste = st.slider(
                    "Taste",
                    value=50,
                    min_value=0,
                    max_value=100,
                    step=10,
                    help="The taste of beer primarily depends on its ingredients. ... Hops adds a trace of bitterness to beer that goes well with citrus and floral additives. Yeast gives a neutral, sugary taste to beer and emphasizes fruit and spicy notes in its aroma."
                )

            # convert image to np array
            img = Image.open(img)
            rgb_im = img.convert('RGB')
            imgArray = np.array(rgb_im)

            #Call API
            col1, col2, col3 = st.columns(5)
            with col1:
                pass
            with col2:
                pass
            with col3 :
                call_api = st.button('I want my beer !')
            with col4:
                pass
            with col5:
                pass
            img_placeholder = st.image(img)

            # encode into 1 dim uint8 string
            img = imgArray.astype('uint8')
            height, width, channel = img.shape
            img_reshape = img.reshape(height * width * channel)
            img_enc = base64.b64encode(img_reshape)

            # imgArray = np.array(rgb_im)
            # height, width, channel = imgArray.shape
            # ratio = width / height
            # new_height = 600
            # new_width = int(new_height * ratio)
            # img_resize = cv2.resize(imgArray, (new_width,new_height),interpolation=cv2.INTER_AREA)
            # imgArray = np.array(img_resize)
            # img_reshape = imgArray.reshape(new_height * new_width * channel)
            # # encode into 1 dim uint8 string
            # img_reshape = img_reshape.astype('uint8')

            # img_enc = base64.b64encode(img_reshape)

            # st.image(Image.fromarray(img_resize))
            #call the API with image_file + aroma + appearance + palate + taste + username
            if call_api:

                # request to be sent to the api
                headers = {}
                headers['Content-Type'] = 'application/json'
                request_dict = {
                    'image': img_enc.decode('utf8').replace("'", '"'),
                    'user': '89000',
                    'height': height,
                    'width': width,
                    'channel': channel,
                    'taste': taste / 50,
                    'appearance': appearance / 50,
                    'palate': palate / 50,
                    'aroma': aroma / 10,
                    'overall': 1,
                    'content': 5
                }

                # request & decoding
                req = requests.post(
                    'https://beerlyv0-yc55p5eduq-ew.a.run.app/predict',
                    json.dumps(request_dict),
                    headers=headers)
                print(req)
                content_response = req.json()

                content_response = eval(content_response)

                beer_list = []

                for i in content_response['beer_name'].values():
                    if i not in beer_list:
                        beer_list.append(i)


                st.write(f'### You should try the {beer_list[0]} !')
                cx='58d6365333e732894'
                endpoint = 'https://www.googleapis.com/customsearch/v1'
                key = st.secrets["GOOGLE_API_KEY"]

                # text to search :
                q = beer_list[0] + ' bière'

                req = requests.get(f'{endpoint}?key={key}&cx={cx}&q={q}&searchType=image&imgSize=large&alt=json&num=1&start=1')

                d = json.loads(req.content)
                link = d['items'][0]['link']
                col1, col2, col3 = st.columns(3)
                with col1:
                    pass
                with col3:
                    pass
                with col2 :
                    st.image(link)

                if len(beer_list) > 5:
                    st.write(
                        "### Don't want this beer ? Look at the other beers in the top 5 !"
                    )
                    for i in range(1,5):
                        st.write(f'### {i+1} - {beer_list[i]}')
                else:
                    st.write(
                        "### Don't want this beer ? Look at the other beers in the menu !"
                    )
                    for i in range(1,len(beer_list)):
                        st.write(f'### {i+1} - {beer_list[i]}')

                img_placeholder.empty()
