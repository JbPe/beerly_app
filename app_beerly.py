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
    st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)


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
        """, unsafe_allow_html=True)

    # CSS Parameters

    # H1
    st.markdown(
        '<style>h1{ font-family: "Luminari, fantasy"; font-size: 40px; line-height: 60px; margin: 10px 0 20px; text-align: center;text-transform: uppercase; }</style>',
        unsafe_allow_html=True)
    # H2
    st.markdown(
        '<style>h2{font-family: "Luminari, fantasy" ;font-size: 30px; letter-spacing: -1px; text-shadow: 1px 1px 0 #000, margin: 10px 0 24px; line-height: 50px;}</style>',
        unsafe_allow_html=True)
    # P
    st.markdown(
        '<style>p{text-align: justify;font-family: "Luminari, fantasy", sans-serif; font-size: 15px; line-height: 24px; margin: 0 0 24px;}</style>',
        unsafe_allow_html=True)
    # H3
    st.markdown(
        '<style>h3{font-family: "Luminari, fantasy" ;font-size: 25px; letter-spacing: -1px; text-shadow: 1px 1px 0 #000, margin: 10px 0 24px; text-align: center; line-height: 50px;}</style>',
        unsafe_allow_html=True)
    # H4
    st.markdown(
        '<style>h4{font-family: "Luminari, fantasy" ;font-size: 20px; letter-spacing: -1px; text-shadow: 1px 1px 0 #000, margin: 10px 0 24px; text-align: center; line-height: 50px;}</style>',
        unsafe_allow_html=True)

    #Test Javascript

    html_string = '''
    <div class="container">
    <div class="text"></div>
    </div>

    <script language="css">
    @import 'https://fonts.googleapis.com/css?family=Roboto+Mono:100'
    html, body
    font-family 'Roboto Mono', monospace
    background #212121
    height 100%
    .container
    height 100%
    width 100%
    justify-content center
    align-items center
    display flex
    .text
    font-weight 100
    font-size 28px
    color #FAFAFA
    .dud
    color #757575
    </script>

    <script language="javascript">
    // ——————————————————————————————————————————————————
    // TextScramble
    // ——————————————————————————————————————————————————

    class TextScramble {
    constructor(el) {
        this.el = el
        this.chars = '!<>-_\\/[]{}—=+*^?#________'
        this.update = this.update.bind(this)
    }
    setText(newText) {
        const oldText = this.el.innerText
        const length = Math.max(oldText.length, newText.length)
        const promise = new Promise((resolve) => this.resolve = resolve)
        this.queue = []
        for (let i = 0; i < length; i++) {
        const from = oldText[i] || ''
        const to = newText[i] || ''
        const start = Math.floor(Math.random() * 40)
        const end = start + Math.floor(Math.random() * 40)
        this.queue.push({ from, to, start, end })
        }
        cancelAnimationFrame(this.frameRequest)
        this.frame = 0
        this.update()
        return promise
    }
    update() {
        let output = ''
        let complete = 0
        for (let i = 0, n = this.queue.length; i < n; i++) {
        let { from, to, start, end, char } = this.queue[i]
        if (this.frame >= end) {
            complete++
            output += to
        } else if (this.frame >= start) {
            if (!char || Math.random() < 0.28) {
            char = this.randomChar()
            this.queue[i].char = char
            }
            output += `<span class="dud">${char}</span>`
        } else {
            output += from
        }
        }
        this.el.innerHTML = output
        if (complete === this.queue.length) {
        this.resolve()
        } else {
        this.frameRequest = requestAnimationFrame(this.update)
        this.frame++
        }
    }
    randomChar() {
        return this.chars[Math.floor(Math.random() * this.chars.length)]
    }
    }

    // ——————————————————————————————————————————————————
    // Example
    // ——————————————————————————————————————————————————

    const phrases = [
    'There is nothing',
    'which has yet been contrived by man',
    'by which so much happiness is produced',
    'as by a good tavern or inn.',
    '–Samuel Johnson'
    ]

    const el = document.querySelector('.text')
    const fx = new TextScramble(el)

    let counter = 0
    const next = () => {
    fx.setText(phrases[counter]).then(() => {
        setTimeout(next, 800)
    })
    counter = (counter + 1) % phrases.length
    }

    next()
    </script>
    '''

    components.html(html_string)  # JavaScript works



    # user authentification
    placeholder = st.empty()
    with placeholder.form('test', clear_on_submit=True):
        username = st.text_input('Username','89000')
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
    if password == 'test' and username != None:

        #removing the authentification
        placeholder.empty()

        # Select a file
        st.write('## Please upload a menu')
        img = st.file_uploader("", type=['jpg', 'png', 'jpeg'])

        if img != None:

            # Need to check if the image looks like a menu before calling the api

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

            # encode into 1 dim uint8 string
            img = imgArray.astype('uint8')
            height, width, channel = img.shape
            img_reshape = img.reshape(height * width * channel)
            img_enc = base64.b64encode(img_reshape)

            #Call API
            col1, col2, col3 = st.columns(3)
            with col1:
                pass
            with col3:
                pass
            with col2 :
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
                    'taste': taste/50,
                    'appearance': appearance/50,
                    'palate': palate/50,
                    'aroma': aroma/50,
                    'overall': 1,
                    'content': 5
                }

                # request & decoding
                req = requests.post(
                    'https://beerly0-kui5hxyjoa-ew.a.run.app/predict',
                    json.dumps(request_dict),
                    headers=headers)

                content_response = req.json()

                content_response = eval(content_response)

                beer_list = []

                for i in content_response['beer_name'].values():
                    if i not in beer_list:
                        beer_list.append(i)


                st.write(f'### You should try {beer_list[0]} !')

                if len(beer_list) > 5:
                    st.write(
                        "Don't want this beer ? Look at the other beers in the top 5"
                    )
                    for i in range(1,5):
                        st.write(f'{i+1} - {beer_list[i]}')
                else:
                    st.write(
                        "Don't want this beer ? Look at the other beers in the menu"
                    )
                    for i in range(1,len(beer_list)):
                        st.write(f'{i+1} - {beer_list[i]}')


                #don't want this beer ? here is the top 5 of the menu for you

                # content = pd.DataFrame(content_response)

                # st.write(f'## You should try {content_response[0]["title"]}')

                # st.write(
                #     '#### Here are the other beers of your menu ranked according to your taste :'
                # )
                # st.table(content)
                #content.style.highlight_max(props='font-weight:bold;color:#FFFF00'))

                # JSON Content
                # st.write(type(contenu))
                # st.write(contenu)

                # 1st row of the JSON content
                # st.write(contenu[0]["title"])
                # st.write(contenu[0]["id"])
