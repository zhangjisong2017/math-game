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
    ["面积练习", "鸡兔同笼", "分数加减", "单位换算", "植树问题"]
)

# 得分初始化
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_count' not in st.session_state:
    st.session_state.question_count = 0

st.sidebar.write(f"⭐ 当前得分：{st.session_state.score}")
st.sidebar.write(f"📊 答题数：{st.session_state.question_count}")

# ==================== 面积练习 ====================
if topic == "面积练习":
    st.header("📐 面积练习")
    
    if 'area_answer' not in st.session_state:
        shape = random.choice(["正方形", "长方形"])
        if shape == "正方形":
            side = random.randint(3, 10)
            st.session_state.area_question = f"一个正方形，边长是{side}厘米"
            st.session_state.area_answer = side * side
            st.session_state.area_hint = f"面积 = 边长 × 边长 = {side} × {side}"
        else:
            length = random.randint(4, 12)
            width = random.randint(3, 8)
            st.session_state.area_question = f"一个长方形，长是{length}厘米，宽是{width}厘米"
            st.session_state.area_answer = length * width
            st.session_state.area_hint = f"面积 = 长 × 宽 = {length} × {width}"
        st.session_state.area_shape = shape
    
    # 确保 area_hint 存在
    if 'area_hint' not in st.session_state:
        st.session_state.area_hint = "面积 = 长 × 宽"
    
    st.info(st.session_state.area_question)
    st.caption(f"💡 提示：{st.session_state.area_hint}")
    st.write("面积是多少平方厘米？")
    
    user_answer = st.number_input("你的答案：", min_value=0, step=1, key="area_input")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("提交答案", key="area_submit"):
            st.session_state.question_count += 1
            if user_answer == st.session_state.area_answer:
                st.success("🎉 答对了！")
                st.balloons()
                st.session_state.score += 10
            else:
                st.error(f"😅 答案是{st.session_state.area_answer}")
    
    with col2:
        if st.button("下一题", key="area_next"):
            for key in ['area_answer', 'area_question', 'area_hint', 'area_shape']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

# ==================== 鸡兔同笼 ====================
elif topic == "鸡兔同笼":
    st.header("🐔🐰 鸡兔同笼")
    
    if 'cr_chicken' not in st.session_state:
        chicken = random.randint(3, 8)
        rabbit = random.randint(2, 6)
        total_heads = chicken + rabbit
        total_feet = chicken * 2 + rabbit * 4
        
        st.session_state.cr_question = f"笼子里有鸡和兔共{total_heads}只，脚共{total_feet}只"
        st.session_state.cr_chicken = chicken
        st.session_state.cr_rabbit = rabbit
        st.session_state.cr_hint = f"假设全是鸡，应该有{total_heads*2}只脚，多了{total_feet-total_heads*2}只，每只兔多2只脚"
    
    # 确保 hint 存在
    if 'cr_hint' not in st.session_state:
        st.session_state.cr_hint = "假设全是鸡，算多出来的脚"
    
    st.info(st.session_state.cr_question)
    st.caption(f"💡 提示：{st.session_state.cr_hint}")
    
    col1, col2 = st.columns(2)
    with col1:
        chicken_answer = st.number_input("鸡有几只：", min_value=0, step=1, key="chicken_input")
    with col2:
        rabbit_answer = st.number_input("兔有几只：", min_value=0, step=1, key="rabbit_input")
    
    col3, col4 = st.columns(2)
    with col3:
        if st.button("提交答案", key="cr_submit"):
            st.session_state.question_count += 1
            if chicken_answer == st.session_state.cr_chicken and rabbit_answer == st.session_state.cr_rabbit:
                st.success("🎉 完全正确！")
                st.balloons()
                st.session_state.score += 15
            else:
                st.error(f"😅 答案是：鸡{st.session_state.cr_chicken}只，兔{st.session_state.cr_rabbit}只")
    
    with col4:
        if st.button("下一题", key="cr_next"):
            for key in ['cr_question', 'cr_chicken', 'cr_rabbit', 'cr_hint']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

# ==================== 分数加减 ====================
elif topic == "分数加减":
    st.header("🍕 分数加减")
    
    if 'fraction_answer_num' not in st.session_state:
        denominator = random.choice([4, 5, 6, 8, 10])
        a = random.randint(1, denominator - 1)
        b = random.randint(1, denominator - 1)
        operation = random.choice(["加", "减"])
        
        if operation == "加":
            while a + b > denominator:
                a = random.randint(1, denominator - 1)
                b = random.randint(1, denominator - 1)
            st.session_state.fraction_question = f"{a}/{denominator} + {b}/{denominator} = ?"
            st.session_state.fraction_answer_num = a + b
            st.session_state.fraction_hint = f"同分母相加，分母不变，分子相加：{a} + {b}"
        else:
            while a <= b:
                a = random.randint(2, denominator - 1)
                b = random.randint(1, a - 1)
            st.session_state.fraction_question = f"{a}/{denominator} - {b}/{denominator} = ?"
            st.session_state.fraction_answer_num = a - b
            st.session_state.fraction_hint = f"同分母相减，分母不变，分子相减：{a} - {b}"
        
        st.session_state.fraction_denominator = denominator
    
    # 确保 hint 存在
    if 'fraction_hint' not in st.session_state:
        st.session_state.fraction_hint = "同分母分数相加减，分母不变"
    
    st.info(st.session_state.fraction_question)
    st.caption(f"💡 提示：{st.session_state.fraction_hint}")
    st.write(f"答案分母是{st.session_state.fraction_denominator}，分子是多少？")
    
    user_num = st.number_input("分子：", min_value=0, step=1, key="fraction_input")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("提交答案", key="fraction_submit"):
            st.session_state.question_count += 1
            if user_num == st.session_state.fraction_answer_num:
                st.success(f"🎉 答对了！答案是 {st.session_state.fraction_answer_num}/{st.session_state.fraction_denominator}")
                st.balloons()
                st.session_state.score += 10
            else:
                st.error(f"😅 分子是{st.session_state.fraction_answer_num}")
    
    with col2:
        if st.button("下一题", key="fraction_next"):
            for key in ['fraction_question', 'fraction_answer_num', 'fraction_denominator', 'fraction_hint']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

# ==================== 单位换算 ====================
elif topic == "单位换算":
    st.header("📏 单位换算")
    
    if 'unit_answer' not in st.session_state:
        units = [
            ("米", "厘米", 100),
            ("千克", "克", 1000),
            ("小时", "分钟", 60),
            ("元", "角", 10)
        ]
        unit1, unit2, rate = random.choice(units)
        direction = random.choice([True, False])
        
        if direction:
            a = random.randint(1, 10)
            st.session_state.unit_question = f"{a}{unit1} = ? {unit2}"
            st.session_state.unit_answer = a * rate
            st.session_state.unit_hint = f"1{unit1} = {rate}{unit2}，所以{a}{unit1} = {a}×{rate}"
        else:
            a = random.randint(1, 10) * rate
            st.session_state.unit_question = f"{a}{unit2} = ? {unit1}"
            st.session_state.unit_answer = a // rate
            st.session_state.unit_hint = f"{rate}{unit2} = 1{unit1}，所以{a}{unit2} = {a}÷{rate}"
    
    # 确保 hint 存在
    if 'unit_hint' not in st.session_state:
        st.session_state.unit_hint = "注意单位之间的进率"
    
    st.info(st.session_state.unit_question)
    st.caption(f"💡 提示：{st.session_state.unit_hint}")
    
    user_answer = st.number_input("你的答案：", min_value=0, step=1, key="unit_input")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("提交答案", key="unit_submit"):
            st.session_state.question_count += 1
            if user_answer == st.session_state.unit_answer:
                st.success("🎉 答对了！")
                st.balloons()
                st.session_state.score += 10
            else:
                st.error(f"😅 答案是{st.session_state.unit_answer}")
    
    with col2:
        if st.button("下一题", key="unit_next"):
            for key in ['unit_answer', 'unit_question', 'unit_hint']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

# ==================== 植树问题 ====================
elif topic == "植树问题":
    st.header("🌳 植树问题")
    
    if 'tree_answer' not in st.session_state:
        length = random.randint(20, 100)
        interval = random.choice([5, 10])
        scenario = random.choice(["两端都种", "一端种", "两端不种"])
        
        if scenario == "两端都种":
            answer = length // interval + 1
            hint = f"间隔数 = {length}÷{interval} = {length//interval}，两端都种，树 = 间隔数 + 1"
        elif scenario == "一端种":
            answer = length // interval
            hint = f"间隔数 = {length}÷{interval} = {length//interval}，一端种，树 = 间隔数"
        else:
            answer = length // interval - 1
            hint = f"间隔数 = {length}÷{interval} = {length//interval}，两端不种，树 = 间隔数 - 1"
        
        st.session_state.tree_question = f"一条{length}米的路，每隔{interval}米种一棵树，{scenario}，一共种多少棵？"
        st.session_state.tree_answer = answer
        st.session_state.tree_hint = hint
    
    # 确保 hint 存在
    if 'tree_hint' not in st.session_state:
        st.session_state.tree_hint = "先算间隔数，再看两端"
    
    st.info(st.session_state.tree_question)
    st.caption(f"💡 提示：{st.session_state.tree_hint}")
    
    user_answer = st.number_input("你的答案：", min_value=0, step=1, key="tree_input")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("提交答案", key="tree_submit"):
            st.session_state.question_count += 1
            if user_answer == st.session_state.tree_answer:
                st.success("🎉 答对了！")
                st.balloons()
                st.session_state.score += 15
            else:
                st.error(f"😅 答案是{st.session_state.tree_answer}棵")
    
    with col2:
        if st.button("下一题", key="tree_next"):
            for key in ['tree_answer', 'tree_question', 'tree_hint']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

# 页脚
st.sidebar.markdown("---")
st.sidebar.write("👨‍👩‍👧 父子联合开发")
st.sidebar.write("🚀 用AI学习，而不是被学习")
st.sidebar.write("📧 欢迎提建议！")
