def prime_multiplier(num):
    count = 0
    multiplier = 2
    print(f'{num}->', end=" ")
    while num>1:
        if num%multiplier == 0:
            num /= multiplier
            print(multiplier, end=' ')
            count+=1
        else: multiplier+=1
    return print(f'Колличество делителей: {count}')
number = int(input("Введите число: "))
prime_multiplier(number)
