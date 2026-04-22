def get_matrix(size):         # 만들고 싶은 행렬의 크기(가로, 세로 길이)를 인자로 받는다. (예: 3을 넣으면 3x3 행렬)
    matrix = []                 # 사용자가 입력한 행들을 하나씩 담을 비어있는 리스트

    for i in range(size):
        while True:
            row = input(f"{i+1}번째 줄 입력: ").split()         # 사용자가 1 0 1이라고 입력하면 공백을 기준으로 잘라 ['1', '0', '1']이라는 리스트로 만든다.

            # 1️⃣ 개수 체크
            if len(row) != size:
                print(f"입력 형식 오류: {size}개의 숫자를 입력하세요.")
                continue

            try:
                row = list(map(int, row))
            except:
                print("입력 오류: 숫자만 입력하세요.")
                continue

            # 2️⃣ 0, 1만 허용
            if any(x not in (0, 1) for x in row):
                print("입력 오류: 0과 1만 입력할 수 있습니다.")
                continue

            matrix.append(row)
            break

    return matrix

# 이 코드는 사용자로부터 **정사각형 형태의 이차원 리스트(행렬)**를 안전하게 입력받기 위한 함수.
# 사용자가 실수로 숫자를 적게 입력하거나 문자를 입력했을 때 발생하는 에러를 방지하는 '예외 처리' 로직이 포함.