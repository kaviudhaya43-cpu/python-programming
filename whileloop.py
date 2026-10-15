      if i%2==0:
        totals+=i 
 print(totals) 

num = 5
for i in range(1,11):
    num1=num*i
    print(num,"*",i,"=",num1) 

number=int(input())
fact=1
for i in range(1,number+1):
    fact=fact*i
    print(i,end="")
    if i<number:
        print("*",end="")
print("=",fact) 

n=int(input()) #123
digits=0
total=0
while n!=0:
   rem=n%10
   digits+=1
   total=total+rem
   n=n//10
print("no of digits:",digits)
print("sum of digits:",total)
 
num=int(input()) #38
while not (num>=0 and num<=9):
    sums=0
    while num!=0:
        rem=num%10
        sums=sums+rem
        num=num//10
    num=sums
else:
    print(num) 

num=int(input())
digits=0
temp=num
temp1=num
while num!=0:
    digits+=1
    num//=10
sums=0
while temp!=0:
    rem=temp%10
    sums=sums+rem**digits
    temp=temp//10
if temp1==sums:
    print("amstrong number")
else:
    print("not amstrong number") 