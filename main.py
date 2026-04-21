from core.mac import mac_operation
from core.judge import judge
from core.normalize import normalize_label
from input_output.input_handler import get_matrix
from input_output.json_loader import load_json
from analysis.performance import run_performance_test
from analysis.performance import measure_mac_time


# -------------------------
# [1] 사용자 입력 모드
# -------------------------
def run_manual_mode():
    print("\n#----------------------------------------")
    print("# [1] 필터 입력")
    print("#----------------------------------------")

    print("필터 A (3줄 입력, 공백 구분)")
    filter_a = get_matrix(3)

    print("\n필터 B (3줄 입력, 공백 구분)")
    filter_b = get_matrix(3)

    print("\n#----------------------------------------")
    print("# [2] 패턴 입력")
    print("#----------------------------------------")

    pattern = get_matrix(3)

    print("\n#----------------------------------------")
    print("# [3] MAC 결과")
    print("#----------------------------------------")

    score_a = mac_operation(pattern, filter_a)
    score_b = mac_operation(pattern, filter_b)

    avg_time = measure_mac_time(pattern, filter_a)

    result = judge(score_a, score_b)

    print(f"A 점수: {score_a}")
    print(f"B 점수: {score_b}")
    print(f"연산 시간(평균/10회): {avg_time:.6f} ms")

    if result == "UNDECIDED":
        print("판정: UNDECIDED (|A-B| < epsilon)")
    else:
        print(f"판정: {result}")


# -------------------------
# [2] JSON 분석 모드
# -------------------------
def run_json_mode():
    data = load_json()

    filters = data["filters"]       # data.json 파일의 "filters"의 value 값을 변수 filters 에 담는다.
    patterns = data["patterns"]

    print("\n#---------------------------------------")
    print("# [1] 필터 로드")
    print("#---------------------------------------")

    for key in filters:
        print(f"✓ {key} 필터 로드 완료 (Cross, X)")

    total = 0
    passed = 0
    failed_cases = []

    print("\n#---------------------------------------")
    print("# [2] 패턴 분석 (라벨 정규화 적용)")
    print("#---------------------------------------")

    for key, value in patterns.items():     # patterns에 있는 key값과 value값을 꺼내서 각각 key, value 변수에 넣는다.
        total += 1

        # size 추출 (size_13_1 → 13)
        try:
            size = int(key.split("_")[1])       # "_"를 기준으로 잘라서, 인덱스1번자리, 즉 2번째 자리 값을 정수로 만들어서 size에 저장.
        except:
            print(f"{key}: size 파싱 실패 → FAIL")
            failed_cases.append(key)            # 데이터/스키마 문제 (key의 형식 문제로 발생)
            continue

        pattern = value.get("input")            # 변수 value에 있는 "input"의 value값을 변수 pattern에 저장. (찾는 key값이 없으면 none을 출력)
        expected_raw = value.get("expected")

        if pattern is None or expected_raw is None:
            print(f"{key}: 데이터 누락 → FAIL")
            failed_cases.append(key)            # 데이터/스키마 문제 (key값이 없거나 value값이 없을 때 발생)
            continue

        expected = normalize_label(expected_raw)

        # 필터 가져오기
        filter_data = filters.get(f"size_{size}")
        if filter_data is None:
            print(f"{key}: 필터 없음(size_{size}) → FAIL")
            failed_cases.append(key)            # 데이터/스키마 문제 (size에 맞는 필터가 없을 때 발생)
            continue

        filter_cross = filter_data.get("cross")
        filter_x = filter_data.get("x")

        # 크기 검증
        if len(pattern) != size or len(pattern[0]) != size:
            print(f"{key}: 패턴 크기 불일치 → FAIL")
            failed_cases.append(key)            # 데이터/스키마 문제 (pattern의 행열 크기가 불일치 할 때 발생)
            continue

        # MAC 계산
        score_cross = mac_operation(pattern, filter_cross)
        score_x = mac_operation(pattern, filter_x)

        # 판정
        result = judge(score_cross, score_x)

        if result == "A":
            predicted = "Cross"
        elif result == "B":
            predicted = "X"
        else:
            predicted = "UNDECIDED"

        # PASS / FAIL
        if predicted == expected:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed_cases.append(key)            # data.json의 expected를 잘못 적었을 때 발생

        print(f"\n--- {key} ---")
        print(f"Cross 점수: {score_cross}")
        print(f"X 점수: {score_x}")
        print(f"판정: {predicted} | expected: {expected} | {status}")

    # 결과 요약
    print("\n#---------------------------------------")
    print("# [3] 결과 요약")
    print("#---------------------------------------")

    print(f"총 테스트: {total}")
    print(f"통과: {passed}")
    print(f"실패: {total - passed}")

    if failed_cases:
        print("실패 케이스:")
        for case in failed_cases:
            print("-", case)

    # 성능 분석 실행
    run_performance_test()


# -------------------------
# [3] 메인 실행
# -------------------------
def main():
    while True:
        print("\n=== Mini NPU Simulator ===")
        print("1. 사용자 입력 (3x3)")
        print("2. data.json 분석")
        print("3. 종료")

        choice = input("선택: ")

        if choice == "1":
            run_manual_mode()
        elif choice == "2":
            run_json_mode()
        elif choice == "3":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()