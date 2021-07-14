def main():
    num1 = int(input())
    num2 = int(input())
    sum = 0
    for i in range(0,3):
        result = num1 * (num2 // (10**i) % 10)
        sum += result*(10**i)
        print(result)
    print(sum)


main()
