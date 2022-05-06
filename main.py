from matplotlib.pyplot import axis
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('Streamlit 超入門')

st.write('Interractive Widgets')

left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字表示')
if button:
    right_column.write('ここは右カラム')


# text = st.text_input('あなたの趣味を教えてください。',)
# conditon = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', conditon
