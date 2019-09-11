n = int(input("please input the numbers of students:"))
data ={}
subjects=("物理","数学","历史")
for i in range(0,n):
    name=input("input name of student:{}".format(i+1))
    marks=[]
    for x in subjects:
        marks.append(int(input("enter the mark of {}".format(x))))
    data[name]=marks
for x,y in data.items():
    total=sum(y)
    print("{}'s total marks {}".format(x,total))
    if total<120:
        print(x,"failed")
    else:
        print(x,"passed")
    
    

