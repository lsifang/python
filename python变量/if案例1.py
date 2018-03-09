print('******************')
print('体脂率采样器')
print('******************')
name = input('请输入您的名字:')
sex = input('请输入您的性别:')
if sex != '男' and sex != '女':
    sex = input('请输入正常的性别哦:')
year = int(input('请输入您的年龄:'))
hei = float(input('请输入您的身高:'))
if hei > 2:
    hei = hei / 100

wid = float(input('请输入您的体重:'))
bmi = wid / (hei ** 2)
if sex == '男':
    ti = ((1.2) * bmi) + (0.23 * year) - 5.4 - 10.8
    if ti < 15:
        print('******************')
        print('姓名：', name)
        print('性别：', sex)
        print('年龄：', year)
        print('先生你好，请注意，你的身体偏瘦')
    if ti > 15 and ti < 18:
        print('******************')
        print('姓名：', name)
        print('性别：', sex)
        print('年龄：', year)
        print('恭喜你，身体非常健康，请继续保持')
    if ti > 18:
        print('******************')
        print('姓名：', name)
        print('性别：', sex)
        print('年龄：', year)
        print('先生你好，请注意，你的身体偏胖')
elif sex == '女':
    ti = (1.2) * bmi + 0.23 * year - 5.4
    if ti < 25:
        print('******************')
        print('姓名：', name)
        print('性别：', sex)
        print('年龄：', year)
        print('美女你好，请注意，你的身体偏瘦')
    if ti > 25 and ti < 28:
        print('******************')
        print('姓名：', name)
        print('性别：', sex)
        print('年龄：', year)
        print('恭喜你，身体非常健康，请继续保持')
    if ti > 28:
        print('******************')
        print('姓名：', name)
        print('性别：', sex)
        print('年龄：', year)
        print('美女你好，请注意，你的身体偏胖')
print('end 谢谢使用')