import streamlit as st
import pandas as pd

st.title("🥽学生 小陆-数字档案")
st.header("🔑基础信息")
st.text("学生ID：0816!")
st.markdown(f"**{'注册时间：'}** {':green[2023-10-01 08:30:17  ]'} **{'| 精神状态：'}** {'不❎'}")
st.markdown(f"**{'当前教室：'}** {':green[实训楼301  ]'} **{'| 安全等级：'}** {':green[绝密]'}")
st.header("📊技能矩阵")
skill_col1, skill_col2, skill_col3 = st.columns(3)
with skill_col1:
    st.text('C语言',help='这是提示')
    st.markdown('### 95%')
    st.markdown(':green[↑ 2%]')
with skill_col2:
    st.text('Python')
    st.markdown('### 87%')
    st.markdown(':red[↓ 1%]')
with skill_col3:
    st.text('Java',help='这是提示')
    st.markdown('### 68%')
    st.markdown(':red[↓ 10%]')
st.subheader('Streamlit课程进度')
st.text("Streamlit课程进度")
st.progress(0.1)
st.header("😪任务日志")
data = {
    '日期':['2023-10-01','2023-10-05','2023-10-12'],
    '任务':['学生数字档案','课程管理系统','数据图表展示'],
    '状态':['✅完成','🔘进行中','❌未完成'],
    '难度':['★☆☆☆☆','★★☆☆☆','★★★☆☆'],
}
df = pd.DataFrame(data)
st.dataframe(df)
st.header("#️⃣最新代码成果")
python_code = '''def hello():
    print("你好，Streamlit！")
'''
st.code(python_code)


st.markdown(f"{':green[>> SYSTEM MESSAGE:]'} **{'下一个任务目标已解锁...'}**")
st.markdown(f"{':green[>> TARGET:]'} **{'课程管理系统'}**")
st.markdown(f"{':green[>> COUNTDOWN:]'} **{'2025-06-03 15:24:58'}**")
st.markdown('**系统状态:在线 连接状态:已加密**')
