

#1
names = []
print('please enter five names')
for i in range(5):
    name = input(str(i+1) + ':')
    names.append(name)
print('Enter '+str(len(names))+' names:')
print('The names are',end=' ')
for j in range(len(names)):
    print(names[j],end=' ')
    
#2
names = []    
print('please enter five names')
for i in range(5):
    name = input(str(i+1) + ':')
    names.append(name)
print('Enter '+str(len(names))+' names:')
print('The names are',end=' ')
for j in range(len(names)):
    print(names[j],end=' ')
print()
names.sort()
for n in names:
    print(n,end=' ')
    
#3
names = []    
print('please enter five names')
for i in range(5):
    name = input(str(i+1) + ':')
    names.append(name)
print('Enter '+str(len(names))+' names:')
print('The names are',end=' ')
for j in range(len(names)):
    print(names[j],end=' ')
print()
print('The third name you entered is:',names[2])



#4
names = []    
print('please enter five names')
for i in range(5):
    name = input(str(i+1) + ':')
    names.append(name)
print('Enter '+str(len(names))+' names:')
print('The names are',end=' ')
for j in range(len(names)):
    print(names[j],end=' ')
print()
num = int(input('Replace one name. Which one? (1-5): '))
rep = input('name:')
names[num-1] = rep
print('The names are',end=' ')
for n in names:
    print(n,end=' ')
    
    
    
    
    
    
    
def abs(x): 
    if x < 0:
        x = -x
        flag = '-'
    elif x>0:
        flag = '+'
    return x,flag 
Treatment_1 = [2.5,3.5,2.9,2.1,6.9,2.4,4.9,6.6,2.0,2.0,5.8,7.5]
Treatment_2 = [4.0,5.6,3.2,1.9,9.5,2.3,6.7,6.0,3.5,4.0,8.1,19.9]
Different = []
sign = []
for i in range(len(Treatment_1)):
    Different.append(float('%.1f' %(Treatment_1[i] - Treatment_2[i])))    
print(Different)
for i in range(len(Different)):
    Different[i],flag = abs(Different[i])
    sign.append(flag)
R1 = 0
R2 = 0
for i in range(len(Different)):
    if sign[i] == '-':
        R1 = R1 + Different[i]    
    elif sign[i] == '+':
        R2 = R2 + Different[i] 
Different.sort()    
print(Different)    
print(sign)  

print('R-:'+str(R1))
print('R+:'+str(R2))
  
original_list=[[1,5,10,12,17,24,25,29,42,51,70,91,94,105], 
            [2,26,34,38,46,90,104,106,110],
            [3,7,14,16,33,40,48,61,65,101,107],
            [4,6,11,41,53,73,75,82,85,99,103,108],
            [8,9,22,23,52,69,78,79,109,112],
            [13,15,19,27,32,35,37,39,43,44,55,62,72,86,100],
            [18,21,28,57,59,60,63,64,66,71,77,88,96,97,98,114],
            [20,30,31,36,56,80,81,83,95,102],
            [45,49,58,67,76,87,92,93,113],
            [47,50,54,68,74,84,89,111,115]]
new_list = []  
for i in range(len(original_list)):
    new_list.append([])
    for j in range(len(original_list[i])):
        new_list[i].append(original_list[i][j] - 1)
print(new_list)














import copy
or_list = [2,4,5,7,4]
new_list = copy.deepcopy(or_list)
new_list[2] = 4444
#new_list.sort()
print(or_list)
print(new_list)

or_list = [2,4,5,7,4]
new_list = or_list[:]
new_list[2] = 4444
#new_list.sort()
print(or_list)
print(new_list)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
