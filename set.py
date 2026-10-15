#set
#set unique unordered mutable
numbers={1,2,3,4,3,2}
print(numbers)
names={"abilash","basha","david","elango"}
print(names)
empty_set=set() #create empty set
empty_set={45,67,}
print(empty_set)

nums1={10,20,30,40}
print(nums1)
nums1.add(50)
print(nums1)
nums1.update([60,70,80])
print(nums1)

nums2=[1,2,3,1,2,3,3,4,67,567]
unique_set=set(num2)
print(unique_set)

nums3={56,78,90,34,12}
nums.remove(56)
print(nums3)
nums.discard(12)
print(nums3)
nums.remove(100)
print(nums3)
nums3.discard(100)
print(nums3)
nums3.clear()
print(nums3)

nums4={1,2,3,4,5,6,7,8,9}
for value in nums4:
    print(value,ends="")
    print()
    a={1,2,3,4}
    b={3,4,5}
    print(a.union(b))
    print(a.intersection(b))
    print(a.difference(b))
    mutable,colection of key value pairs key unique vakyes repeat
student1={
    "name":"naveen",
    "age": "20",
    "mark": "459",
    "dept": "ece"
}
print(student1)
print(student1["name"])
print(student1["age"])
print(student1.get("city","not applicable"))
student1["mark"]=499
print(student1)
student1["city"]="pondy"
print(student1)
student1.pop("age")
print(student1)

for a,b in student1.items():
    print(a,":",b)