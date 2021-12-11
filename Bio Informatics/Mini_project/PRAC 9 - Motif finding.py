import random
l=int(input("Enter the length of motif:"))
file=open("Corona.txt","r")
r=file.read()
print("Sequence:",r)
size=len(r)
print("size of sequence",size)
pos=random.randint(0,len(r)-5)
print("Position",pos)
motif=r[pos:pos+1]
print("Motif",motif)
i=pos+1
while(i<=size-1):
    if(motif==r[i:i+1]):
        str1=r[i:i+1]
        print("Match motif",str1)
        file1=open("Motoutput.txt","a")
        file1.write(str1+"")
    i+=1
