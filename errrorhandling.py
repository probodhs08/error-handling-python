try:
    a=int(input())
    b=int(input())
    print(a/b)
    file1=open("file.txt",'r')
except Exception as Argument:
    print("Exception",Argument)
finally:
    print("try except finally")