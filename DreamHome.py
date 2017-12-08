#Dream Home Project
def savings_calculation(savings,salary):
    monthly=int(salary*savings)
    return monthly

def duration_calculation(price,salary,savings):
    psavings = savings_calculation(savings,salary)
    total=int(price/psavings)
    return total


try:
    salary = int(input("Enter your salary: "))

    savings = float(input("Enter the Percentage of salary you want to save(In Decimal):"))

    price = int(input("Enter Enter the cost of your dream home: "))

except ValueError:
    print("Kindly enter the input in the correct format")

print("This will take ",duration_calculation(price,salary,savings), "months")

