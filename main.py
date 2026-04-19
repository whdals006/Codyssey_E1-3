from core.mac import mac_operation
from core.judge import judge
from input_output.input_handler import get_matrix

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
    print(f"판정: {result}")


def main():
    print("=== Mini NPU Simulator ===")
    print("1. 사용자 입력 (3x3)")
    print("2. 종료")

    choice = input("선택: ")

    if choice == "1":
        run_manual_mode()
    else:
        print("종료")


if __name__ == "__main__":
    main()