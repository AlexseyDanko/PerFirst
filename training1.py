import datetime
td=datetime.datetime.now().date()
bdAnna=datetime.date(1989,3,20)
BDAlex=datetime.date(1990,11,20)
age_years=int((td-bdAnna).days/365.22)
Age_years=int((td-BDAlex).days/365.22)
print(age_years)
print(Age_years)
if age_years>Age_years:
    print("старше Anna")
else:
    print("старше Alex")