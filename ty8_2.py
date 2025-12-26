# 导入streamlit库，用于快速构建交互式Web应用，别名st是行业通用写法
import streamlit as st
# 导入pandas库，用于数据处理和分析，别名pd是行业通用写法
import pandas as pd

st.set_page_config(layout="wide")

st.title("杂七杂八")
tab1, tab2, tab3,tab4,tab5 = st.tabs(["数字档案", "简历生成", "美食地图", "播放音乐", "图片展示"])

with tab1:
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

with tab2:
	st.header('个人简历生成器')
	st.markdown(':gray[使用Streamlit创建您的个性化简历]')

# 分栏：左侧表单、右侧预览
	col1, col2 = st.columns([1, 2])

	with col1:
		st.header('个人信息表单')
    
    # 基础信息
		xm = st.text_input('姓名', '')
		zw = st.text_input('职位', '')
		dh = st.text_input('电话', '')
		yx = st.text_input('邮箱', '')
		rq = st.date_input("出生日期", )  # 预设示例日期
    
    # 性别单选
		xb = st.radio(
			'性别',
			['男', '女', '其他'],
			horizontal=True,
			index=0  # 默认选“男”
		)
    
    # 学历下拉
		xl = st.selectbox(
			'学历',
			['高中', '专科', '本科', '硕士', '博士'],
			index=2  # 默认选“本科”
		)
    
    # 语言能力多选
		yy = st.multiselect(
			'语言能力',
			['中文', '英语', '日语', '法语', '德语', '西班牙语'],
			default=['中文', '英语']  # 预设示例
		)
		st.write('语言能力:', ', '.join(yy))
    
    # 技能多选
		skills = st.multiselect(
			'技能（可多选）',
			['Java', 'HTML/CSS', '机器学习', 'Python', '其他'],
			default=['Java', 'HTML/CSS', '机器学习', 'Python']  # 预设示例
		)
		st.write('技能:', ', '.join(skills))
    
    # 工作经验滑块
		work_exp = st.slider(
			'工作经验（年）',
			min_value=0, max_value=10,
			value=6  # 预设示例（6年）
		)
    
    # 期望薪资范围滑块
		salary_min, salary_max = st.slider(
			'期望薪资范围（元）',
			min_value=0, max_value=50000,
			value=(19123, 23950)  # 匹配截图数值
		)
    
    # 个人简介文本框
		intro = st.text_area(
			'个人简介',
			height=150,
			value=""  # 预设示例
		)
    
    # 最佳联系时段
		contact_time = st.selectbox(
			'每日最佳联系时段',
			['9:00-12:00', '14:00-18:00', '20:41', '其他'],
			index=2  # 匹配截图“20:41”
		)
    
    # 上传照片
		uploaded_file = st.file_uploader(
			"上传个人照片",
			type=["jpg", "png", "jpeg"],
			help="Drag and drop file here (支持JPG/PNG)"
		)
    # 显示默认头像提示
		if not uploaded_file:
			st.write("当前使用默认头像")


	with col2:
		st.header('简历实时预览')
		st.header(xm)  # 姓名大标题
    
    # 预览分栏：左（头像+基础信息）、右（补充信息）
		col2_1, col2_2 = st.columns([1, 3])
		with col2_1:
        # 头像显示（默认占位图）
			if uploaded_file:
				st.image(uploaded_file, width=120)
			else:
            # 用在线占位图模拟默认头像
				st.image("https://via.placeholder.com/120x160?text=头像", width=120)
        
        # 基础信息
			st.markdown(f'职位: {zw}')
			st.markdown(f'电话: {dh}')
			st.markdown(f'邮箱: {yx}')
			st.write(f"出生日期: {rq}")
    
		with col2_2:
        # 补充信息
			st.write(f'性别: {xb}')
			st.write(f'学历: {xl}')
			st.write(f'工作经验: {work_exp}年')
			st.write(f'期望薪资: {salary_min}-{salary_max}元')
			st.write(f'最佳联系时间: {contact_time}')
			st.write(f'语言能力: {", ".join(yy)}')
    
    # 个人简介模块
		st.subheader('个人简介')
		st.write(intro)
    
    # 专业技能模块
		st.subheader('专业技能')
		for skill in skills:
			st.write(f'• {skill}')
    
    # 底部标语（匹配截图）
		st.markdown('<br><p style="color:gray;">"在算法的世界里，你是最优解"</p>', unsafe_allow_html=True)

with tab3:
	restaurants_data = {
		"餐厅": ["尝不忘(体育路店)", "KFC(盛天地店)", "三品王(朝阳百盛店)", "麦当劳(爱琴海店)", "蜜雪冰城(桃花源店)"],
		"类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
		"评分": [4.2, 4.5, 4.0, 4.7, 4.3],
		"人均消费(元)": [15, 20, 25, 35, 50],
		'latitude':[22.800752,22.810761,22.814813,22.813654,22.877677],
		'longitude':[108.313224,108.401252,108.322737,108.423010,108.308964]
	}
	df = pd.DataFrame(restaurants_data)

	st.map(df)

	st.header("🔑餐厅评分")
	st.bar_chart(df, x='餐厅',y='评分')

	st.header("🔑不同类型餐厅价格")
	st.line_chart(df, x='类型',y='人均消费(元)')

	yye_data = {
		"月份": ['01月','02月','03月','04月','05月','06月'],
		"尝不忘": [33000, 27000, 35000, 35000,42000,45000],
		"肯德基": [42000, 22000, 37000, 38000,45000,39000],
		"三品王": [33000, 25000, 38000, 35000,39000,47000],
		"麦当劳": [33000, 27000, 35000, 37000,42000,44000],
		"蜜雪冰城": [55000, 42000, 50000, 48000,49000,45000],
	}
	df1 = pd.DataFrame(yye_data)

	st.header("🔑上半年各餐厅营业额")
	st.area_chart(df1, x='月份',y=['尝不忘','肯德基','三品王','麦当劳','蜜雪冰城'])

with tab4:
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

with tab5:
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