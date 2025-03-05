def sum_even(num):
    if num % 2 == 1:
        num -= 1
    sum = 0
    for i in range (num, 0, -2):
        sum += i
    return sum
print(sum_even(7))


def calculate_bmi(w, h):
    return w/(h*h)

print(calculate_bmi(84, 1.3))

def count_down_up(n):
    for i in range(n, 0, -1):
        print(i, end = " ")
    for i in range(2, 4, +1):
        print(i, end = " ")
        
count_down_up(3)