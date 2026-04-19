import time
from core.mac import mac_operation

# 1️⃣ MAC 시간 측정
def measure_mac_time(pattern, filt, repeat=10):         # repeat=10 → 10번 반복해서 시간 측정
    start = time.perf_counter()     # 반복 시작하기 전 시점의 시간을 기록

    for _ in range(repeat):
        mac_operation(pattern, filt)

    end = time.perf_counter()       # 모든 반복이 끝난 시점의 시각을 기록

    avg_time = (end - start) / repeat * 1000
    return avg_time

# 이 코드는 mac_operation 함수가 얼마나 빠르게 작동하는지 측정하는 '성능 테스트(Benchmarking)' 코드이다.
# time.per_counter() : 파이썬에서 코드의 실행 시간이나 벤치마킹을 측정할 때 사용하는 가장 정밀한 고해상도 타이머. 스톱워치처럼 작동.
# for _ in range(repeat) 에서 언더바(_)는 반복문 내에서 변수의 값을 사용하지 않을 것임을 명시적으로 나타내는 관례적인 변수명. 단순히 횟수 반복이 목적일 때 주로 사용.
# *1000 하는 이유 : perf_counter는 초(second) 단위로 측정되는데, 보통 연산 속도는 매우 빠르기 때문에 사람이 읽기 편하도록 밀리초(ms, 1000분의 1초) 단위로 변환

# 2️⃣ 더미 데이터 생성
def generate_dummy_matrix(size):
    return [[1 for _ in range(size)] for _ in range(size)]

# "테스트용 가짜 데이터 만들기"
# 성능 측정을 할 때마다 일일이 숫자를 입력할 수 없으니, 컴퓨터가 자동으로 데이터를 채우게 만든다.

# 3️⃣ 성능 테스트 실행
def run_performance_test():
    sizes = [3, 5, 13, 25]                                       # ① 실험 조건을 설정 (3x3 부터 25x25 까지)

    print("\n#---------------------------------------")
    print("# [4] 성능 분석")
    print("#---------------------------------------")

    print(f"{'크기':<10}{'평균 시간(ms)':<20}{'연산 횟수'}")        # ② 표 헤더(Header) 출력.
    print("-" * 40)

    for size in sizes:                                          # ③ 반복 실험 및 결과 출력
        pattern = generate_dummy_matrix(size)
        filt = generate_dummy_matrix(size)

        avg_time = measure_mac_time(pattern, filt)

        print(f"{size}x{size:<7}{avg_time:<20.6f}{size*size}")

# "실험 설계 및 실행"
# 이 함수는 여러 가지 크기의 환경에서 실험을 진행합니다.
# print(f"{'크기':<10}{'평균 시간(ms)':<20}{'연산 횟수'}") 해석 : '크기'를 왼쪽정렬하고 10칸 확보
#                                                             '평균시간'을 왼쪽정렬하고 20칸 확보
# print(f"{size}x{size:<7}{avg_time:<20.6f}{size*size}") 해석 : {size}x{size}를 왼쪽정렬하고 7칸 확보
#                                                              {avg_time}을 소수점 6자리 까지 나타내고, 왼쪽정렬하고 20칸 확보