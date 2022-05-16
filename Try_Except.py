try:
    age=int(input("Age: "))
    income=45000
    div=income/age 
    print(div)
except ZeroDivisionError:
    print("Age cannot be Zero.")
except ValueError:
    print("Enter a valid number.")