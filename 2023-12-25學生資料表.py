list1 = ['陳育法', '趙善傑', '陳國宏', '吳宗花', '陳文成', '韓天勇', '陳昭正',
         '潘懿辛', '林善昀', '袁怡如', '陳幸啟', '劉怡貞', '侯山吉', '趙惠婷']

學號 = []
for n in range(1,15):
    # 學號.append(str(n).format())
    學號.append('{:03}'.format(n))

print(學號)



# 學號 = ['001','002','003']

# 學號.append('004')      #增加東西在後面
# 學號.append('005')
# 學號.append('006')
# 學號.append('007')
# print(學號)


# for n in range(1,15):
#     print(n)

# print(dir([]))