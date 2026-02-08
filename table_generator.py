while True:
    num = int(input("Enter a number (0 to exit): "))

    if num == 0:
        print("Goodbye!")
        break

    print("\nMultiplication Table of" , num)
    print("-------------------------")

    for i in range(1,11):
        print(num , "x" , i, "=", num * i)