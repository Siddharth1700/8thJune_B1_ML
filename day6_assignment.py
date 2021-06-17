## SIDDHARTH KAVADIA

## Q1
## Installed Python

## Q2
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a = 20
a += 30
a %= 3
print(a)
print(True*False)
print(True&False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
print('False' in 'False')
print(((True == False) or (False > True)) and (False <= True))

## Q3
s1 = "Nice to have it"
s2 = "here"
print(s1+" "+s2)

## Q4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

print(a[3][1][2][0])

## Q5
a = [s1]+a[:]+[s2]
print(a)

## Q6
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(set.difference(color_list_1,color_list_2))

## Q7
string = input("Enter the string : ")
if len(set('abcdefghijklmnopqrstuvwxyz') - set(string.lower())) == 0 :
    print("It is a pangram String")
else:
    print("It is not a pangram string")

## Q8
n = int(eval(input('Enter the value:')))
e = str(n)
n1 = int(e)
n2 = int(e+e)
n3 = int(e+e+e)
print(n1+n2+n3)

## Q9
values = list(input("Enter the strings by comma seperated : ").split(','))
values.sort()
values = ','.join(values)
print(values)

## Q10
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])
