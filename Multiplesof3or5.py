def solution(number):
    sum = 0
    num = number - 1
    while num >= 3:
        if num % 3 == 0 and num % 5 == 0:
            sum += num
        elif num % 3 == 0:
            sum += num
        elif num % 5 == 0:
            sum += num
        num -= 1
    return sum


number = int(input())
print(solution(number))

# def solution(number):
#    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
