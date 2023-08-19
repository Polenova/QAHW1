def bank(x=int(input()),y=int(input())):
    x = [x]
    percent = 10
    for i in range(y):
        for i in x:
            i = int(i * (1 + percent / 100))
            x = [i]
    print(x[0])
    
bank() 