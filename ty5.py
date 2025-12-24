import streamlit as st

st.set_page_config(page_title="音乐播放器", page_icon="🎵")

image_ua = [
    {
        'url': 'http://p1.music.126.net/dLCEfgsi35KVrmZBggKS8Q==/109951162850228147.jpg?param=130y130',
        'gem': '鱼玄机',
        'geshou': ' 迁梦 / 洛天依',
        'shichang': '3:30',
        'text': '专辑封面',
        'audio_file':'https://music.163.com/song/media/outer/url?id=441617355.mp3'
    },
    {
        'url': 'http://p1.music.126.net/QYOtbVhmJ-jpPzCPWqjZUw==/109951165965398413.jpg?param=130y130',
        'gem': '星河万里',
        'geshou': ' Rom邢锐',
        'shichang': '3:32',
        'text': '专辑封面',
        'audio_file':'https://music.163.com/song/media/outer/url?id=1843704418.mp3'
    },
    {
        'url': 'http://p2.music.126.net/kVwk6b8Qdya8oDyGDcyAVA==/1364493930777368.jpg?param=130y130',
        'gem': '盲点',
        'geshou': 'G.E.M.邓紫棋',
        'shichang': '3:46',
        'text': '专辑封面',
        'audio_file':'https://music.163.com/song/media/outer/url?id=36199531.mp3'
    }
]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

st.header("🎵简易音乐播放器")
st.text("使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

col1, col2 = st.columns([1,2])

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)

def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_ua)

with col1:
    st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])

with col2:
    st.header(image_ua[st.session_state['ind']]['gem'])
    st.text("歌手:"+image_ua[st.session_state['ind']]['geshou'])
    st.text("时长:"+image_ua[st.session_state['ind']]['shichang'])
    col2_1, col2_2 = st.columns(2)
    with col2_1:
        st.button('⏮上一首', use_container_width=True, on_click=prevImg)
    with col2_2:
        st.button('下一首⏭', use_container_width=True, on_click=nextImg)

st.audio(image_ua[st.session_state['ind']]['audio_file'])
