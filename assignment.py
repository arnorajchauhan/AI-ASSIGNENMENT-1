print("Is every human good grader?")
x=[1,1,0,0]     #every human does not study well
y=[0,1,0,1]     #good graders study well
z=[]            #is every human good grader
j=0             #indexing variable
for i in x:
    if i==0:
        i=1
        z.append(i and y[j])
    else:
        i=0
        z.append(i and y[j])
    j+=1
if z.count(1)==4:   #checking whether result is tautology or not
    print("Yes")
else:
    print("No")
