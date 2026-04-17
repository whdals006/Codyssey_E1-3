from core.mac import mac_operation

def main():
    pattern = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    filt = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    result = mac_operation(pattern, filt)
    print("MAC 결과:", result)


if __name__ == "__main__":
    main()