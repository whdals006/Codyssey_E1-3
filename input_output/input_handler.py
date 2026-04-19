def get_matrix(size):       # 만들고 싶은 행렬의 크기(가로, 세로 길이)를 인자로 받는다. (예: 3을 넣으면 3x3 행렬)
    matrix = []             # 사용자가 입력한 행들을 하나씩 담을 비어있는 리스트

    for i in range(size):
        while True:
            row = input(f"{i+1}번째 줄 입력: ").split()     # 사용자가 1 0 1이라고 입력하면 공백을 기준으로 잘라 ['1', '0', '1']이라는 리스트로 만든다.

            # 길이 체크
            if len(row) != size:
                print(f"입력 형식 오류: {size}개의 숫자를 입력하세요.")
                continue

            try:
                row = list(map(float, row))     # row 에 있는 데이터를 모두 실수로 바꾸고 리스트에 담는다.
                matrix.append(row)              # 비어있는 matrix 리스트에 row 넣기.
                break
            except:
                print("숫자만 입력하세요.")

    return matrix