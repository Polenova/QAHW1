def fizz_buzz(n = int(input("введите число "))):
    for i in range (1, n+1):
        if (i % 3 == 0) and (i % 5 > 0):
            print("Fizz")
        elif (i % 5 == 0) and (i % 3 > 0):
            print("Buzz")
        elif (i % 5 == 0) and (i % 3 == 0):
            print("FizzBuzz")
    return(n)

fizz_buzz()


