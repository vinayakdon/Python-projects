def addition():
    sum = 0
    numbers = input("enter the expression: ")
    res = list(map(int, numbers.split("+")))
    for i in res:
        sum+=i
    print(f"{numbers}={sum}")

    return f"{numbers}={sum}"

def substract():
    sub = 0
    numbers = input("enter the expression: ")
    res = list(map(int, numbers.split(' ')))
    print("res:", res)
    for i in res:
        if i > 0:
            i = -i 
        i = -i
        sub-=i
    print(f"{numbers.strip()}={sub}")

    return f"{numbers}={sub}"

def multiplication():
    mul = 1
    numbers = input("enter the expression: ")
    res = list(map(int, numbers.split("*")))
    for i in res:
        mul*=i
    print(f"{numbers}={mul}")

    return f"{numbers}={mul}"

def division():
    div = 0
    numbers = input("enter the expression: ")
    res = list(map(int, numbers.split("/")))
    for i in res:
        div/=i
    print(f"{numbers}={div}")

    return f"{numbers}={div}"

def saveExpression(expression):
    with open("../AdvancedCalculator/History.txt", "a") as files:
        files.write(expression)
        files.write("\n")
        print("Saved as history!!")

def ShowHistory():
    with open("../AdvancedCalculator/History.txt", "r") as file:
        for i in file.read():
            print(i,end="")
        print("\n")

def ClearHistory():
    with open("../AdvancedCalculator/History.txt", '+r') as file:
        print("file is cleared..")
        file.truncate()

def main():
    while True: 
        print("Advanced calculator")
        print("select the following operation to perform calculation: ")
        print("1. Addition\n2. Substract\n3. Multiplication\n4. Division\n5. Show history\n6. Clear history\n 7. Exit")
        user = input("Select from the option: ")
        if user == "1":
            expression = addition() 
            saveExpression(expression)

        elif user=="2":
            expression = substract()
            saveExpression(expression)

        elif user == "3":
            expression = multiplication()
            saveExpression(expression)

        elif user == "4":
            expression = division()
            saveExpression(expression)

        elif user == "5":
            ShowHistory()


        elif user == "6":
            ClearHistory()

        elif user == "7":
            break



if __name__ == "__main__":
    main()


    