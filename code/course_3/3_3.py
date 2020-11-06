# 根据某学生的百分制成绩，判断其对应的等级：
# 若score<60，“不及格”；
# 若60<score<=70，“及格”；
# 若70<score<=80，“中等”；
# 若80<score<=90，“良好”；
# 若90<score<=100，“优秀”；
# 试试看怎么样IF条件判断实现？
score = int(float(input('请输入你的成绩：')))
if 0 <= score < 60:
    print('不及格')
elif score <= 70:
    print('及格')
elif score <= 80:
    print('中等')
elif score <= 90:
    print('良好')
elif score <= 100:
    print('优秀')
else:
    print('请输入正确的成绩！')
