name = input(" Enter your name: ")
age = input(" Enter your age: ")
monthly_salary = input(" Enter your monthly salary: ")
print("Testing:", name, age, monthly_salary)
yearly_salary = int(monthly_salary) * 12
user_info = {
    "name": name,
    "age": age,
    "monthly_salary": monthly_salary,
    "yearly_salary": yearly_salary
}
print("User Information:", user_info)
