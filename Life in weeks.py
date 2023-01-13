# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this
new_age = int(age)
final_year = 90
meses = (final_year - new_age) * 12
semanas = (final_year - new_age) * 52
dias = (final_year - new_age) * 365
print(f"You have {dias} days, {semanas} weeks, and {meses} months left")


