amount=float(input("enter purchase amount:"))
if amount<0:
 print("invalid amount")
else:
 discount=0.0
if amount>=5000:
 discount=amount*20/100
elif amount>=2000 and amount < 5000:
 discount=amount*10/100
print("discount amount:",discount)
print("final payable amount:",amount-discount)
num1=int(input("enter first number"))
num2=int(input("enter second number"))
operator=input("enter operator:"