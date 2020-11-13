f = open('G:\program\python\python_cource\code\data\input.txt',encoding='utf-8')
total_pages = int(f.readline())
c = [0,0,0,0,0,0,0,0,0,0]
for i in range(1,total_pages+1):
    tmp = i
    while tmp>0:
        c[tmp%10] += 1
        tmp = tmp//10
for i in range(len(c)):
    f = open("G:\program\python\python_cource\code\data\out.txt", "a")
    f.write(str(c[i])+'\n')
f.close()
# f = open("out.txt", "w")            　 # 打开文件以便写入
# while year <= numyears:
#     principal = principal * (1 + rate)
#     print >> f, "%3d %0.2f" % (year, principal)
#     year += 1
# f.close()





#创建文件
#file_path：文件路径
#msg：即要写入的内容
# def create__file(file_path,msg):
#     f=open(file_path,"a")
#     f.write(msg)
#     f.close
#
#
# for i in range(1,341):
#     create__file('G:\program\python\python_cource\code\data/'+ str(i)+'.txt',str(i))