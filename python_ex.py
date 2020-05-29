#=================p1

id_front = 970618
id_back = 1234567

age_condition = str(id_front)[:2]
month = str(id_front)[2:4]
day = str(id_front)[4:]
sex_condtion = str(id_back)[0]

print(id_front)

#conditions1
if 0 <= int(age_condition) <=20:
    print("나이 :",int(age_condition)+21)
else:
    print("나이 :",(100-int(age_condition))+21)
#conditions2
print(f'생일 : {int(month)}월{int(day)}일')
#condition3
if int(sex_condtion) % 2 == 0:
    print('성별 : 여자')
else:
    print('성별 : 남자')

#=================p2

input_num = int(input("몇단?."))

for i in range(1,10):
    print(f'{input_num} X {i} = {input_num*i}')

#=================p3

n = 100
def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

for i in range(n+1):
  if(isPrime(i)):
    print(i)

#====================p4

grade_list = [60,40,30,50,25]
sum = 0
for i in range(len(grade_list)):
    sum += grade_list[i]

avg = sum / len(grade_list)
n = 1
for grade in grade_list:
    if grade > avg:
        print(n,"번째 학생 합격!")
    else:
        print(n,"번째 학생 불합격!")
    n += 1

#=====================p5

a = (1,2,3)
a = list(a)
a.append(5)
a = tuple(a)
print(a)

#=====================p6

my_dict={'최정호':'010-6722-xxxx','송민선':'010-5029-xxxx','이종훈':'010-6335-xxxx','정재환':'010-8589-xxxx'}
input_val = input("찾고자 하는 사람을 입력하시오.")

if input_val in my_dict:
    print(f'{input_val}의 전화번호는 '+my_dict[input_val]+'입니다.')
else:
    print(f'{input_val}의 번호를 찾을 수 없습니다.')
