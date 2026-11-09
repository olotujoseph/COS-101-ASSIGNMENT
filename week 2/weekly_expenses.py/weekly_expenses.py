# Student Weekly Expense Calculator

student_name = input("Enter student name: ")

daily_transport_cost = float(input("Enter daily transport cost (NGN): "))
daily_feeding_cost = float(input("Enter daily feeding cost (NGN): "))
days_on_campus = int(input("Enter number of days on campus: "))
other_weekly_expenses = float(input("Enter other weekly expenses (NGN): "))

transport_total = daily_transport_cost * days_on_campus
feeding_total = daily_feeding_cost * days_on_campus

weekly_total = transport_total + feeding_total + other_weekly_expenses

print("\nWEEKLY EXPENSE SUMMARY")
print("Student:", student_name)
print(f"Transport total: NGN {transport_total:,.2f}")
print(f"Feeding total: NGN {feeding_total:,.2f}")
print(f"Other expenses: NGN {other_weekly_expenses:,.2f}")
print(f"Weekly total: NGN {weekly_total:,.2f}")

#input
#it collects the following info
#1.student name
#2.daily transport cost
#3.daily feeding costs
#4.number of days on campus
#5.other weekly expenses

#process
#transport total= daily transport total * days on campus
#feeding total=daily feeding total * days on campus
#weekly total=weekly transport total + weekly feeding total + other weekly expenses total

#output
#it shows the following
#1.students name
#2.total transport expense
#3.total feeding expense
#4.other weekly expense
#5.tootal weekly expense


#psuedecode
#BEGIN

#    INPUT student_name
#   INPUT daily_transport_cost
#    INPUT daily_feeding_cost
#    INPUT days_on_campus
#    INPUT other_weekly_expenses

#   transport_total = daily_transport_cost * days_on_campus

 #   feeding_total = daily_feeding_cost * days_on_campus

  #  weekly_total = transport_total + feeding_total + other_weekly_expenses

#    DISPLAY "WEEKLY EXPENSE SUMMARY"
#    DISPLAY student_name
#    DISPLAY transport_total
#    DISPLAY feeding_total
#    DISPLAY other_weekly_expenses
#    DISPLAY weekly_total

#END
#1.string
#it was used cause there were texts
#2.floats
#this was used due to the possibility that the monetary value might include decimal
#3.integer
#it is used because a day is a whole number


