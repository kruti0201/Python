not_working = False
for i in range(4, 10000):
    has_factors = False
    for j in range(2, i):
        if (i % j) == 0:
            has_factors = True
            break
    # if((i*i - 1)%24 == 0):
    #     print('24 method',i, not has_factors)
    if(not has_factors):
        if((i*i - 1)%24 != 0):
            not_working = True
        # print('conventional method', i, (i*i - 1)%24 == 0, '\n')
print('NOT WORKING' if not_working else 'ARE YOU KIDDING ME!')