def normalize_label(label):
    label = label.lower()       # 입력받은 문자열을 모두 소문자로 변환

    if label in ["+", "cross"]:
        return "Cross"
    elif label in ["x"]:
        return "X"

    return "UNKNOWN"

# 이 코드는 사용자가 입력한 다양한 형태의 문자열을 시스템이 정해둔 **표준 이름(Standard Name)**으로 통일시켜 주는 '데이터 정규화(Normalization)' 함수
# 사용자가 +라고 치든, cross라고 치든 똑같이 "Cross"라고 인식하게 만드는 아주 유용한 전처리 단계.
# 이 코드가 필요한 이유: "데이터의 일관성"
# 이 함수는 보통 아까 만든 judge 함수와 함께 사용되어, "A가 이겼는데, 그 A가 사실은 어떤 모양인가?"를 사용자에게 친절하게 보여줄 때 사용