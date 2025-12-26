import streamlit as st
import pandas as pd
import plotly.express as px


def get_dataframe_from_excel():
    
    df = pd.read_excel('supermarket_sales.xlsx',
                       sheet_name='销售数据',
                       skiprows=1,
                       index_col='订单号')
    
    df['小时数'] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
    return df


def add_sidebar_func(df):
    """创建侧边栏筛选功能"""
    with st.sidebar:
        st.header("请筛选数据：")
        
        # 获取唯一值并处理空值
        city_unique = df["城市"].unique() if "城市" in df.columns else []
        customer_type_unique = df["顾客类型"].unique() if "顾客类型" in df.columns else []
        gender_unique = df["性别"].unique() if "性别" in df.columns else []
        
        # 设置默认选中所有选项
        city = st.multiselect(
            "请选择城市：",
            options=city_unique,
            default=city_unique if city_unique.size > 0 else []
        )
        
        customer_type = st.multiselect(
            "请选择顾客类型：",
            options=customer_type_unique,
            default=customer_type_unique if customer_type_unique.size > 0 else []
        )
        
        gender = st.multiselect(
            "请选择性别",
            options=gender_unique,
            default=gender_unique if gender_unique.size > 0 else []
        )
        
        # 处理空筛选条件
        if not city:
            city = city_unique.tolist() if city_unique.size > 0 else []
        if not customer_type:
            customer_type = customer_type_unique.tolist() if customer_type_unique.size > 0 else []
        if not gender:
            gender = gender_unique.tolist() if gender_unique.size > 0 else []
        
        # 执行筛选
        try:
            df_selection = df.query(
                "城市 == @city & 顾客类型 == @customer_type & 性别 == @gender"
            )
        except Exception as e:
            st.sidebar.error(f"筛选数据时出错: {e}")
            df_selection = pd.DataFrame()
            
        return df_selection


def product_line_chart(df):
    # 将df按"产品类型"列分组，并计算"总价"列的和，然后按总价排序（移除by参数）
    sales_by_product_line = (
        df.groupby(by=["产品类型"])["总价"].sum().sort_values()  # 关键修正：删除by="总价"
    )
    
    fig_product_sales = px.bar(
        sales_by_product_line,
        x="总价",
        y=sales_by_product_line.index,
        orientation="h",
        title="<b>按产品类型划分的销售额</b>",
    )
    # 将生成的条形图返回
    return fig_product_sales


def hour_chart(df):
    #将df按"小时数"列分组，并计算"总价"列的和
    sales_by_hour = (
        df.groupby(by=["小时数"])["总价"].sum()
    )
    
    fig_hour_sales = px.bar(
        sales_by_hour,
        x=sales_by_hour.index,
        y="总价",
        title="<b>按小时数划分的销售额</b>",
    )
    #将生成的条形图返回
    return fig_hour_sales


def main_page_demo(df):
    """主界面函数"""
    #设置标题
    st.title('📉销售仪表板')
    
    #创建关键指标信息区，生成3个列容器
    left_key_col, middle_key_col, right_key_col = st.columns(3)
    
    #选中数据框中的"总价"列，使用sum()计算"总价"列的和，使用int()求整
    total_sales = int(df["总价"].sum())
    #选中数据框中的"评分"列，使用mean()计算"评分"列的平均值，使用round()四舍五入
    #保留一位小数
    average_rating = round(df["评分"].mean(), 1)
    #对刚刚的结果再次四舍五入，只保留整数，并使用int()函数，表示就要整数，增加代码的
    #可读性
    star_rating_string = ":star:" * int(round(average_rating, 0))
    #选中的数据框中的"总价"列，使用mean()计算"总价"列的平均值，使用round()四舍五入
    #保留两位小数
    average_sale_by_transaction = round(df["总价"].mean(), 2)
    
    with left_key_col:
        st.subheader("总销售额：")
        st.subheader(f"RMB ¥ {total_sales:,}")
    
    with middle_key_col:
        st.subheader("顾客评分的平均值：")
        st.subheader(f"{average_rating} {star_rating_string}")
    
    with right_key_col:
        st.subheader("每单的平均销售额：")
        st.subheader(f"RMB ¥ {average_sale_by_transaction}")
    
    st.divider()  #生成一个水平分割线
    
    #创建图表信息区，生成两个列容器
    left_chart_col, right_chart_col = st.columns(2)
    with left_chart_col:
        #生成纵向条形图
        hour_fig = hour_chart(df)
        #展示生成的Plotly图形，并设置使用父容器的宽度
        st.plotly_chart(hour_fig, use_container_width=True)
    
    with right_chart_col:
        #生成横向条形图
        product_fig = product_line_chart(df)
        #展示生成的Plotly图形，并设置使用父容器的宽度
        st.plotly_chart(product_fig, use_container_width=True)


def run_app():
    """启动应用"""
    #设置页面
    st.set_page_config(
        page_title="销售仪表板", #标题
        page_icon="📉", #图标
        layout="wide" #宽布局
    )
    
    #将Excel中的销售数据读取到数据框中
    sale_df = get_dataframe_from_excel()
    #添加不同的多选下拉按钮，并形成筛选后的数据框，构建筛选区
    df_selection = add_sidebar_func(sale_df)
    #构建主界面
    main_page_demo(df_selection)

if __name__ == "__main__":
    run_app()
