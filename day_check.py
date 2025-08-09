'''
Write a program to ask user to enter today's day of the week 
(Ex: Monday, Tuesday etc).

The program should then print "Yey!, it's party time!!" if 
the day entered by user is Saturday or Sunday.

If not, print "Woo, time to focus! its work/school day".

'''
day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
user_day=input("Enter today's day of the week: ")
user_day= user_day.lower()
print("\n")
print("+++++++++++")
if user_day not in day_list:
    print("Invalid day entered. Please enter a valid day of the week.")
elif user_day == "saturday" or user_day == "sunday":
    print("Yey!, it's party time!!")
else:
    print("Woo, time to focus! its work/school day")