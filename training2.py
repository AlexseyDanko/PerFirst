import datetime
year = int(input("Введите год рождения Anna в формате четырёхзначного числа:"))
month = int(input("Введите месяц рождения Anna в формате однозначного или двухзначного числа:"))
day = int(input("Введите день рождения Anna в формате однозначного или двухзначного числа:"))
Year = int(input("Введите год рождения Alex в формате четырёхзначного числа:"))
Month = int(input("Введите месяц рождения Alex в формате однозначного или двухзначного числа:"))
Day = int(input("Введите день рождения Alex в формате однозначного или двухзначного числа:"))
td = datetime.datetime.now().date()
bdAnna = datetime.date(year,month,day)
bdAlex = datetime.date(Year,Month,Day)
age_years_Alex = int((td-bdAlex).days / 365.10)
age_years_Anna = int((td-bdAnna).days / 365.25)
print(age_years_Anna)
print(age_years_Alex)
if age_years_Anna>age_years_Alex:
    print("Anna старше")
elif age_years_Anna == age_years_Alex:
    print("Они одного возраста")
elif age_years_Alex>age_years_Anna:
    print("Alex старше")




