# 소득(income)과 세금(tax) 변수 선언
income = 4500   # 소득 (단위: 만원)
tax = 0         # 세금 초기값

# if-else 문으로 소득 수준 분류
if income >= 10000:
    tax = income * 0.3
    level = "고소득자"
elif income >= 5000:
    tax = income * 0.2
    level = "중간소득자"
elif income >= 3000:
    tax = income * 0.1
    level = "저소득자"
else:
    tax = income * 0.05
    level = "최저소득자"

# 결과 출력
print("소득:", income, "만원")
print("소득 수준:", level)
print("부과 세금:", tax, "만원")
