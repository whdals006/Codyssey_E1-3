from core.mac import mac_operation
from core.judge import judge

def main():
    pattern = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    filter_a = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    filter_b = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    score_a = mac_operation(pattern, filter_a)
    score_b = mac_operation(pattern, filter_b)

    result = judge(score_a, score_b)

    print("A 점수:", score_a)
    print("B 점수:", score_b)
    print("판정:", result)


if __name__ == "__main__":
    main()