import streamlit as st
import random

# 页面配置
st.set_page_config(
    page_title="🧮 AI数学小老师",
    page_icon="🎮",
    layout="centered"
)

# 标题
st.title("🧮 AI数学小老师")
st.subheader("8岁程序员作品")

# 选择题型
topic = st.selectbox(
    "选择你想挑战的题型：",
    ["面积练习", "鸡兔同笼", "分数问题"]
)

# 得分初始化
if 'score' not in st.session_state:
    st.session_state.score = 0

st.sidebar.write(f"⭐ 当前得分：{st.session_state.score}")

# 面积练习
if topic == "面积练习":
    st.header("📐 面积练习")
    
    # 生成题目
    if 'area_answer' not in st.session_state:
        shape = random.choice(["长方形", "正方形"])
        if shape == "正方形":
            side = random.randint(3, 10)
            st.session_state.area_question = f"一个正方形，边长是{side}厘米"
            st.session_state.area_answer = side * side
        else:
            length = random.randint(4, 12)
            width = random.randint(3, 8)
            st.session_state.area_question = f"一个长方形，长是{length}厘米，宽是{width}厘米"
            st.session_state.area_answer = length * width
        st.session_state.area_shape = shape
    
    # 显示题目
    st.info(st.session_state.area_question)
    st.write("面积是多少平方厘米？")
    
    # 输入答案
    user_answer = st.number_input("你的答案：", min_value=0, step=1)
    
    # 提交按钮
    if st.button("提交答案"):
        if user_answer == st.session_state.area_answer:
            st.success("🎉 答对了！")
            st.balloons()
            st.session_state.score += 10
        else:
            st.error(f"😅 答案是{st.session_state.area_answer}")
        
        # 清除当前题目，生成新题
        if 'area_answer' in st.session_state:
            del st.session_state.area_answer
        if 'area_question' in st.session_state:
            del st.session_state.area_question
        if 'area_shape' in st.session_state:
            del st.session_state.area_shape
        st.button("下一题")

# 鸡兔同笼
elif topic == "鸡兔同笼":
    st.header("🐔🐰 鸡兔同笼")
    st.info("功能开发中，敬请期待...")

# 分数问题
elif topic == "分数问题":
    st.header("🍕 分数问题")
    st.info("功能开发中，敬请期待...")

# 页脚
st.sidebar.markdown("---")
st.sidebar.write("👨‍👩‍👧 父子联合开发")
st.sidebar.write("🚀 用AI学习，而不是被学习")
