height = float(input('请输入身高(米):'))
weight = float(input('请输入体重:'))
BMI = weight / (height ** 2)

print(round(BMI,2))
if BMI < 18.5:
    print("体重过轻")

elif BMI < 24:
    print("正常范围")

else:
    print("体重过重")