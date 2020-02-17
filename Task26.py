nums = int(input('Введите числа: '))
even = odd = 0
while nums > 0:
    if nums % 2 == 0:
        even += 1
    else:
        odd +=1
    nums = nums // 10
print ('Чётных - %d, Нечётных - %d' % (even, odd))