def operator(x):
    if x%2==0:
        print(f'Число {x} - чётное')
    else: print(f'Число {x} - нечётное')
    if x<0:
        print(f'Число {x} - отрицательное')
    elif x==0:
        print(f'Число {x} - нуль')
    else:
        print(f'Число {x} - положительное')
    if 10<=x<=50:
        print(f'Число {x} принадлежит диапазону [10, 50]')
    else: print(f'Число {x}  не принадлежит диапазону [10, 50]')
operator(int(input()))
