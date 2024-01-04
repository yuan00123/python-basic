age = int(input('請輸入年齡：'))
# age = eval(input('請輸入年齡：'))
student = input('你是不是學生(Y/N)：')
print(age, student)

#法三
money = 0

if student == "Y" and age >= 5:
    money = 100
elif student == "N" and age >= 5:
    if age <= 18:
        money = 120
    else:
        money = 150

print(str(money)+'元')     #str()將其他資料型態轉換成字串型態，例如數字、布林值、列表、字典等


#法二
# if age < 5 or student == "Y":
#     if age < 5:
#         print('免費')
#     else:
#         print('100元')
# else:
#     if 5<= age <= 18:
#         print('120元')
#     else:
#         print('150元')


#法一
# if age < 5:
#     print('免費')
# elif student == Y:
#     print('100元')
# elif age >= 5 and age <= 18:
#     print('120元')
# else:
#     print('150元')