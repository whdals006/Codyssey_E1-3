def judge(score_a, score_b, epsilon=1e-9):      # 두 점수를 비교하여 승자를 결정하는 판정(Judge) 로직
    # 거의 같으면
    if abs(score_a - score_b) < epsilon:
        return "UNDECIDED"

    # A가 더 크면
    if score_a > score_b:
        return "A"

    # B가 더 크면
    return "B"

# score_a 와 score_b 는 비교할 두 대상의 점수
# epsilon=1e-9 에서 1e-9는 10^{-9} (0.000000001)을 의미하는 아주 작은 소수
# epsilon 을 사용하는 이유: 컴퓨터는 소수점 계산(float)을 할 때, 0.000000001 의 미세한 오차가 발생할 수 있는데 이러한 오차로 인해 승패가 갈리는 걸 막기 위한 "여유 오차"
# abs()는 절대값을 구하는 내장 함수