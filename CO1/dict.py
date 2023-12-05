dic={}
n1=int(input("Total number of elements in dict 1 : "))
for i in range(n1):
    dic[i]=input("Enter element : ")
print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0])))
print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))