def bank(x=int(input("введите сумму: ")),y=int(input("введите количество лет: "))):
    x = [x]
    percent = 10
    for i in range(y):
        for i in x:
            i = int(i * (1 + percent / 100))
            x = [i]
    if 1 < y < 5 :
        print("на вашем счету будет ", x[0], " через ", y, " года")
    elif y == 1: 
        print("на вашем счету будет ", x[0], " через ", y, " год")
    else: 
        print("на вашем счету будет ", x[0], " через ", y, " лет")
    
bank() 