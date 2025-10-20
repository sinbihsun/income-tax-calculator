import streamlit as st

st.set_page_config(page_title="소득세 계산기", page_icon="💰", layout="centered")

st.title("💰 소득세 계산기 (파이썬 if-elif-else)")
st.caption("고소득층 50%, 중간소득층 25%, 저소득층 10%, 최저소득층 5%")

with st.form("tax_form"):
    income = st.number_input("소득을 입력하세요 (단위: 만원)", min_value=0, step=100, value=4500)
    submitted = st.form_submit_button("계산하기")

def classify_and_tax(income: int):
    if income >= 10000:
        tax = income * 0.5
        level = "고소득층"
    elif income >= 5000:
        tax = income * 0.25
        level = "중간소득층"
    elif income >= 3000:
        tax = income * 0.1
        level = "저소득층"
    else:
        tax = income * 0.05
        level = "최저소득층"
    return level, tax

if submitted:
    level, tax = classify_and_tax(int(income))
    st.success(f"소득: {int(income)}만원  •  소득 수준: {level}  •  세금: {tax:.1f}만원")
    st.write("---")
    st.subheader("로직 (Python)")
    st.code(
        """if income >= 10000:
    tax = income * 0.5        # 고소득층 50%
    level = "고소득층"
elif income >= 5000:
    tax = income * 0.25       # 중간소득층 25%
    level = "중간소득층"
elif income >= 3000:
    tax = income * 0.1        # 저소득층 10%
    level = "저소득층"
else:
    tax = income * 0.05       # 최저소득층 5%
    level = "최저소득층" """,
        language="python",
    )

st.info("팁: 이 파일 이름을 'streamlit_app.py' 또는 'app.py'로 저장하면 Streamlit Cloud가 기본 진입점으로 인식해요.")
