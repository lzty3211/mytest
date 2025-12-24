import streamlit as st

st.set_page_config(page_title="视频中心", page_icon="🎵")

video_arr=[
    {'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/34/17/34942421734/34942421734-1-192.mp4?e=ig8euxZM2rNcNbR1hWdVhwdlhWR1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=cosovbv&og=ali&nbs=1&trid=1c839e0f54fd438cb582daefc13c419h&gen=playurlv3&oi=771356656&platform=html5&deadline=1766565403&uipk=5&mid=0&upsig=d117c9ca23983301d0d8a7fbf7b5b5fb&uparams=e,os,og,nbs,trid,gen,oi,platform,deadline,uipk,mid&bvc=vod&nettype=0&bw=896298&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
     'title':'灵感菇'
     },
    {'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/88/45/34875834588/34875834588-1-192.mp4?e=ig8euxZM2rNcNbRV7zdVhwdlhWdahwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=cosovbv&oi=771356656&platform=html5&trid=9ec0ee1ec79e433ab0e024f460ff48dh&og=ali&deadline=1766566741&nbs=1&uipk=5&mid=0&gen=playurlv3&upsig=30b3a2989ca30486d470ebd43457fa6c&uparams=e,os,oi,platform,trid,og,deadline,nbs,uipk,mid,gen&bvc=vod&nettype=0&bw=882067&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
     'title':'纸巾萝卜'
     },
    {'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/48/36/34896153648/34896153648-1-192.mp4?e=ig8euxZM2rNcNbR1nWdVhwdlhWRHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&gen=playurlv3&os=cosovbv&nbs=1&og=hw&deadline=1766566827&oi=771356656&trid=385ec87fef2f4c578c2974570813cf4h&mid=0&uipk=5&platform=html5&upsig=f0d920a22935aefdf9b815620199e27d&uparams=e,gen,os,nbs,og,deadline,oi,trid,mid,uipk,platform&bvc=vod&nettype=0&bw=963968&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
     'title':'吃吧'
     }
    ]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

st.header(video_arr[st.session_state['ind']]['title'])

st.video(video_arr[st.session_state['ind']]['url'])

def playVideo(e):
    st.session_state['ind']=int(e)

cols = st.columns(len(video_arr))

for i in range(len(video_arr)):
    with cols[i]:
        st.button('第'+str(i+1)+'集',on_click=playVideo,args=([i]))

