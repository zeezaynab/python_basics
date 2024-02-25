filling_status = int(input("Enter your filing status (0, 1, 2, or 3): "))

if filling_status == 0 or filling_status == 1 or filling_status == 2 or filling_status == 3:
    income = float(input("Enter your income: "))  # Convert input to float

    if filling_status == 0:
        if 0 <= income <= 8350:
            PI_tax = income * 0.10
        elif 8351 <= income <= 33950:
            PI_tax = income * 0.15
        elif 33951 <= income <= 82250:
            PI_tax = income * 0.25
        elif 82251 <= income <= 171550:
            PI_tax = income * 0.28
        elif 171551 <= income <= 372950:
            PI_tax = income * 0.33
        elif income > 372950:
            PI_tax = income * 0.35
        else:
            print("Invalid income")

    elif filling_status == 1:
        if 0 <= income <= 16700:
            PI_tax = income * 0.10
        elif 16701 <= income <= 67900:
            PI_tax = income * 0.15
        elif 67901 <= income <= 137050:
            PI_tax = income * 0.25
        elif 137051 <= income <= 208850:
            PI_tax = income * 0.28
        elif 208851 <= income <= 372950:
            PI_tax = income * 0.33
        elif income > 372950:
            PI_tax = income * 0.35
        else:
            print("Invalid income")

    elif filling_status == 2:
        if 0 <= income <= 8350:
            PI_tax = income * 0.10
        elif 8351 <= income <= 33950:
            PI_tax = income * 0.15
        elif 33951 <= income <= 68525:
            PI_tax = income * 0.25
        elif 68526 <= income <= 104425:
            PI_tax = income * 0.28
        elif 104426 <= income <= 186475:
            PI_tax = income * 0.33
        elif income > 186475:
            PI_tax = income * 0.35
        else:
            print("Invalid income")

    elif filling_status == 3:
        if 0 <= income <= 11950:
            PI_tax = income * 0.10
        elif 11951 <= income <= 45500:
            PI_tax = income * 0.15
        elif 45501 <= income <= 117450:
            PI_tax = income * 0.25
        elif 117451 <= income <= 190200:
            PI_tax = income * 0.28
        elif 190201 <= income <= 372950:
            PI_tax = income * 0.33
        elif income > 372950:
            PI_tax = income * 0.35
        else:
            print("Invalid income")

    print(f"Your income tax is: {PI_tax}")

else:
    print("Invalid entry.")


        







