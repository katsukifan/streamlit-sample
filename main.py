import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入门篇')


st.write('Display Image')
if st.checkbox('Show Image'):
    img = Image.open('1.jpg')
    st.image(img, caption='kohaku', use_column_width=True)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)

option = st.selectbox(
    '请选择你喜欢的数字。',
    list(range(1,11))
)
'你喜欢的数字是:', option

text = st.text_input('请填写你的兴趣爱好。')
'你的兴趣爱好是', text

condition = st.slider('你现在的状态是？', 0, 100, 50)
'状态是',condition

st.write('Intercative Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右侧显示文字')
if button:
    right_column.write('这里是右侧')

expander = st.expander('客服')
expander.text_input('请写下想要询问的内容')


st.title('显示进度条')
'Start!!!'

lastest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    lastest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done !!!'

