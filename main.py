from matplotlib.pyplot import axis
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('Streamlit 超入門')

st.write('Interractive Widgets')

text = st.text_input('あなたの趣味を教えてください。',)
'あなたの趣味：', text

conditon = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', conditon
