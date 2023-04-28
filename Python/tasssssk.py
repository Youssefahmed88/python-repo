from collections import Counter
task3=open(r'C:\Users\Youssif\OneDrive\Desktop\text.txt.txt','r')
list1=[]
frq=[]
for line in task3:
    word=line.split()
    list1 +=word
list1=sorted(list1)
print(Counter(list1))