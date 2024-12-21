import streamlit as st
import random
import time

# 指定的列表
my_list = [
     "A7",	"B7",	"C7",	"D7",	"E7",	"F7",	"G7",	"bB7",	"bD7",	"bE7",	"#F7",	"bA7",	"Am7",	"Bm7",	"Cm7",	"Dm7",	"Em7",	"Fm7",	"Gm7",	"bBm7",	"bDm7",	"bEm7",	"#Fm7",	"bAm7",	"＃A7",	"＃C7",	"＃D7",	"bG7",	"＃G7",	"＃Am7",	"＃Cm7",	"＃Dm7",	"bGm7",	"＃Gm7",	"Amaj7",	"Bmaj7",	"Cmaj7",	"Dmaj7",	"Emaj7",	"Fmaj7",	"Gmaj7",	"bBmaj7",	"bDmaj7",	"bEmaj7",	"#Fmaj7",	"bAmaj7",	"＃Amaj7",	"＃Cmaj7",	"＃Dmaj7",	"bGmaj7",	"＃Gmaj7",

]

# 设置网页标题（小一点的字体）
st.markdown("<h1 style='font-size: 24px;'>七和弦中随机生成10个</h1>", unsafe_allow_html=True)

# 用于保存上一次点击按钮的时间
if 'last_click_time' not in st.session_state:
    st.session_state.last_click_time = None

# 记录当前时间
current_time = time.time()

# 显示时间间隔
if st.session_state.last_click_time is not None:
    time_interval = current_time - st.session_state.last_click_time
    st.write(f"上一次点击到现在的时间间隔：{time_interval:.2f} 秒")
else:
    st.write("这是第一次点击按钮。")

# 添加按钮，点击后生成10个随机元素
if st.button('和弦生成', key="generate_button"):
    # 确保列表中至少有10个元素
    if len(my_list) >= 10:
        random_items = random.sample(my_list, 10)  # 随机选择10个元素

        # 用HTML和CSS来显示两个横向行
        row_html = '<div style="display: flex; justify-content: space-between; font-size: 28px;">'

        # 第一行显示前5个元素
        row_html += ''.join([f'<div style="margin-right: 20px;">{item}</div>' for item in random_items[:5]])

        row_html += '</div><br>'

        # 第二行显示后5个元素
        row_html += '<div style="display: flex; justify-content: space-between; font-size: 28px;">'
        row_html += ''.join([f'<div style="margin-right: 20px;">{item}</div>' for item in random_items[5:]])
        row_html += '</div>'

        # 使用st.markdown()渲染HTML
        st.markdown(row_html, unsafe_allow_html=True)

        # 更新上一次点击时间
        st.session_state.last_click_time = current_time
    else:
        st.write('列表中的元素不足10个，请添加更多元素。')

# 设置按钮样式和位置（底部中央）
st.markdown("""
    <style>
        .stButton > button {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 30px;
            padding: 20px 50px;
        }
    </style>
""", unsafe_allow_html=True)