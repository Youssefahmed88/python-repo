file1=open(r"C:\Users\Youssif\OneDrive\Desktop\text.txt",'r')

##for reading   
line1=file1.readline()
line2=file1.readline()
print(line1,line2)

sum=0
count=0
for i in file1:
    sum +=int(i)
    count+=1
try:                      ##try&&catch 
    print(sum/count)
except:
    print('empty file')
file1.close()
##for appending
file1=open(r"C:\Users\Youssif\OneDrive\Desktop\text.txt",'a')
file1.write(1,2,3,4)
for i in file1:
    print(i)
##for writing
file1=open(r"C:\Users\Youssif\OneDrive\Desktop\text.txt",'w')
file1.write(1,2)
for i in file1:
    print(i)

file1.close()
