        #ordered immutable allow duplicate
        tuple_1=(34,67,89,23)
        print(tuple_1)
        print(tuple(tuple_1))

        tuple_2=(5,)
        print(type(tuple_2))

        tuple_3=(12,45,67,89,23)
        for data in tuple_3:
            print(data,end=" ")
        print()
        i=0
        while i<len(tuple_3):
            print(tuple_3[i],end="")
            i+=1
        print()
        
t = (10, 20, 10, 30, 20, 40)

for i in set(t):
    if t.count(i) > 1:
        print(i, end=" ")