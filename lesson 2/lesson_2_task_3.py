def square (arg_square = float(input("введите сторону квадрата "))):
      square_area = arg_square * arg_square  
      if square_area % 1 == 0: 
        print("площадь квадрата ", int(square_area))
      else:
        print("площадь квадрата ", int(-1 * square_area // 1 * -1))

square()