def mac_operation(pattern, filt):   # 실제 계산을 담당하는 로직
    total = 0.0     # 이 변수는 실수(Float, 소수점이 있는 수) 타입으로 시작한다는 뜻

    for i in range(len(pattern)):          # len(pattern)은 행(row)의 개수를 뜻한다.
        for j in range(len(pattern[0])):   # len(pattern[0])은 열(column)의 개수를 뜻한다. 선택된 행 안에서 열(column)을 하나씩 넘긴다. [0]을 쓴 이유는 0번째,1번째,2번째 행의 길이가 다 똑같기 때문. [i]를 써도 결과는 똑같다.
            total += pattern[i][j] * filt[i][j]     # 같은 위치끼리 곱해서 모두 더하기

    return total