def findKth(myInput, k) :
    
    result = []
    data = []
    for v in myInput :
        data.append(v)
        data.sort()
        if len(data) < k :
            result.append(-1)
        else :
            result.append(data[k-1])
    return result

def main():

    firstLine = [int(x) for x in input("n과 k를 입력하세요 (예시:10 3): ").split()]
    myInput = [int(x) for x in input("n개의 숫자를 차례대로 입력하세요 (예시:1 9 8 5 2 3 5 6 2 10): ").split()]

    print('정렬 결과: ', *findKth(myInput, firstLine[1]))

if __name__ == "__main__":
    main()
