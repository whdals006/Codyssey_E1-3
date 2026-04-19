from core.mac import mac_operation
from core.judge import judge
from core.normalize import normalize_label
from input_output.input_handler import get_matrix
from input_output.json_loader import load_json
from analysis.performance import run_performance_test


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

    result = judge(score_a, score_b)

    print(f"A 점수: {score_a}")
    print(f"B 점수: {score_b}")

    if result == "UNDECIDED":
        print("판정: UNDECIDED (|A-B| < epsilon)")
    else:
        print(f"판정: {result}")


# -------------------------
# [2] JSON 분석 모드
# -------------------------
def run_json_mode():
    data = load_json()

    filters = data["filters"]
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

    for key, value in patterns.items():
        total += 1

        # size 추출 (size_13_1 → 13)
        try:
            size = int(key.split("_")[1])
        except:
            print(f"{key}: size 파싱 실패 → FAIL")
            failed_cases.append(key)
            continue

        pattern = value.get("input")
        expected_raw = value.get("expected")

        if pattern is None or expected_raw is None:
            print(f"{key}: 데이터 누락 → FAIL")
            failed_cases.append(key)
            continue

        expected = normalize_label(expected_raw)

        # 필터 가져오기
        filter_data = filters.get(f"size_{size}")
        if filter_data is None:
            print(f"{key}: 필터 없음(size_{size}) → FAIL")
            failed_cases.append(key)
            continue

        filter_cross = filter_data.get("cross")
        filter_x = filter_data.get("x")

        # 크기 검증
        if len(pattern) != size or len(pattern[0]) != size:
            print(f"{key}: 패턴 크기 불일치 → FAIL")
            failed_cases.append(key)
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
            failed_cases.append(key)

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
    print("=== Mini NPU Simulator ===")
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")

    choice = input("선택: ")

    if choice == "1":
        run_manual_mode()
    elif choice == "2":
        run_json_mode()
    else:
        print("잘못된 입력")


if __name__ == "__main__":
    main()