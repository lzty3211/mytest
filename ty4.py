import streamlit as st

st.set_page_config(page_title="相册网站", page_icon="📸")

image_ua = [
    {
        'url': 'https://img95.699pic.com/photo/60049/1525.jpg_wh860.jpg',
        'text': '鱼'
    },
    {
        'url': 'https://img95.699pic.com/photo/50506/1953.jpg_wh860.jpg',
        'text': '鸟'
    },
    {
        'url': 'https://pic4.zhimg.com/v2-a2c9c4f88ba1f459c5e6239368cc0337_r.jpg',
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
