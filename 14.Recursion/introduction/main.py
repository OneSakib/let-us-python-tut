# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         p = n*fact(n-1)
#     return p
# num=int(input("Enter Number:"))
# res=fact(num)
# print("Factorial of {} is {}".format(num,res))

# def generate(n):
#     lol = [[] for i in range(n**n)]
#     pos = 0    
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             for k in range(1, n+1):
#                 t = [i, j, k]
#                 lol[pos] = t                
#                 pos += 1
#     return lol


# data = generate(3)
# print(">>>>>>>>data", data)

def generate(n):
    t=[]
    lol=[[] for i in range(n**n)]
    helper(n,t,lol)
    return lol
def helper(n,t,lol):
    global j
    if len(t)==n:
        lol[j]=lol[j]+t
        j+=1
        return 
    for i in range(1,n+1):
        t.append(i)
        helper(n,t,lol)
        t.pop()



j=0 
l=generate(3)
print(l)