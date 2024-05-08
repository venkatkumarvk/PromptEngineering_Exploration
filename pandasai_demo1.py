import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.middlewares.streamlit import StreamlitMiddleware
from pandasai.llm import GooglePalm
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="EXL ConversionalBI", page_icon="📈")
st.title("EXL ConversionalBI-MultipleCSV")

if "openai_key" not in st.session_state:
    with st.sidebar.form("API key"):
        key = st.text_input("Google Palm Key", value="pls put your Googlepalmapi", type="password")
        if st.form_submit_button("Submit"):
            st.session_state.openai_key = key
            st.session_state.prompt_history = []
            st.session_state.df_list = []
            st.success('Saved API key for this session.')

if "openai_key" in st.session_state:
    with st.sidebar:
        uploaded_files = st.file_uploader(
            "Choose CSV files. These should be in long format (one datapoint per row).",
            accept_multiple_files=True,
            type="csv",
        )
        
        if uploaded_files:
            selected_file_name = st.selectbox("Select a file", [file.name for file in uploaded_files])
            selected_file = next(file for file in uploaded_files if file.name == selected_file_name)
            df = pd.read_csv(selected_file)
            st.session_state.df_list = [df]

    if st.session_state.df_list:
        df = st.session_state.df_list[0]  # Assuming only one DataFrame is uploaded at a time
        st.subheader("Current Data:")
        st.write(df)

        with st.form("Question"):
            question = st.text_input("Question", value="", type="default")
            submitted = st.form_submit_button("Submit")
            if submitted:
                with st.spinner():
                    llm = GooglePalm(api_key=st.session_state.openai_key)
                    pandas_ai = PandasAI(llm, middlewares=[StreamlitMiddleware()])
                    x = pandas_ai.run(df, prompt=question)

                    if os.path.exists('temp_chart.png'):
                        im = plt.imread('temp_chart.png')
                        st.image(im)
                        import PIL.Image
                        import google.generativeai as genai
                        img = PIL.Image.open('temp_chart.png')

                        model = genai.GenerativeModel('gemini-pro-vision')
                        response = model.generate_content(img)
                        print(response)
                        st.write(response)

                        os.remove('temp_chart.png')

                    if x is not None:
                        st.write(x)
                    st.session_state.prompt_history.append(question)
        with st.sidebar:
            st.subheader("Prompt history:")
            st.write(st.session_state.prompt_history)

        with st.sidebar:
            if st.button("Clear"):
                st.session_state.prompt_history = []
                st.session_state.df_list = []
