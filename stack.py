li=[]
top=-1
max=10
while(1):
    c=int(input("1.Push \n2.Pop \n3.Show \n4.Exit \nEnter your choice: "))
    if(c==1):
        if(top<max):
            top=top+1
            n=input("Enter the element to insert: ")
            li.append(n)
        elif(top==max):
            print("Stack is full")
    elif(c==2):
        if(top==-1):
            print("stack is empty")
        else:
            print("popped: ",li[top])
            li.pop()
            top=top-1
    elif(c==3):
        if(top==-1):
            print("stack is empty")
        for i in li:
            print(i,end=" ")
        print()
    else:
        break      
