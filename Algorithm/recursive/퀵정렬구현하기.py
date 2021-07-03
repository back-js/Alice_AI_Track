def quickSort(array):
    if len(array) <= 1 :
        return array

    return array 

def main():
    line = [int(x) for x in input("정렬할 수를 입력하세요 (예시:10 2 3 4 5 6 9 7 8 1): ").split()]

    print('정렬 결과:', *quickSort(line))

if __name__ == "__main__":
    main()

