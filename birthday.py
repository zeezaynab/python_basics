#inputs:
birth_month=int(input("Enter birth month in numbers: "))
current_month=int(input("Enter current month: "))
birth_year=int(input("Enter year of birth: "))
current_year=int(input("Enter current year: "))
birth_date=int(input("Enter your birth date: "))
current_date=int(input("Enter current date: "))

#year and month:
if current_month>=birth_month:
 age_months=current_month-birth_month
 age_years=current_year-birth_year
elif birth_month>current_month:
 age_months=12+current_month-birth_month
 age_years=current_year-birth_year-1
else:
 print("Invalid entry")
 exit()
#day:
if age_months==1 or age_months==3 or age_months==5 or age_months==7 or age_months==8 or age_months==10 or age_months==12:
 s=31
elif age_months==2:
 s=29
else:
 s=30
if current_date>=birth_date:
 age_days=current_date-birth_date
else:
 age_days=s+current_date-birth_date
 age_months-=1

#result:
print(f"You are {age_years} years, {age_months} months, {age_days} days old.")




