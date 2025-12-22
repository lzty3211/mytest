import streamlit as st

st.set_page_config(page_title="相册网站", page_icon="📸")

image_ua = [
    {
        'url': 'https://cdn.britannica.com/73/9173-050-9D9EA4BA.jpg',
        'text': '鱼'
    },
    {
        'url': 'https://tse3-mm.cn.bing.net/th/id/OIP-C.f219Grmy5nMdkLKGqX_MKgHaE7?w=266&h=180&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1',
        'text': '鸟'
    },
    {
        'url': 'https://www.baltana.com/files/wallpapers-2/Cute-Cat-Images-07756.jpg',
        'text': '猫'
    }
]

# 初始化session_state中的索引
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 显示当前图片
st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])

# 分两列放按钮
col1, col2 = st.columns(2)

# 下一张函数
def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)

# 上一张函数（新增）
def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_ua)

# 上一张按钮（绑定prevImg函数）
with col1:
    st.button('上一张', use_container_width=True, on_click=prevImg)

# 下一张按钮
with col2:
    st.button('下一张', use_container_width=True, on_click=nextImg)
