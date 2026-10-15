


























# #exception handling
# try:
#     a=int(input())
#     b=int(input())
#     c=a//b
#     print(c)
# except zerodivisionerror:
#     print("please enter postive number")
# except valueError:
#     print("enter integer only")
# finally:
#     print("java programming")

# #oops - object oriented programming language or system
# #class object inheritance polymorphism encapsulation abstraction interface

# class studenttwo:
#     name="unknown"
#     mark=0
#     def display(self):
#         print(self.name,"",self.mark)

# class studentone:
#     name="naveen"
#     age=20
#     dept="cse"
#     def marks(self):
#         print("maths: 90, english: 78")

#  class studentthree:
#      name="unknown"
#      mark=0
#      def_init_(self,name,mark):
#          self.name=name
#          self.mark=mark


#      #def setdetails(self,name,mark)
#      # self.name=name
#      # self.mark=mark
#      def printdetails(self)
#          print(self.name," ",self.mark)


# s1=studentone()
# print(s1.name)
# print(s1.age)
# s1.marks()

# s2=studenttwo()
# s2.name="aravindh"
# s2.mark=345
# s2.display()
# s3=studenttwo()
# s3.name="dharshan"
# s3.mark=456
# s3.display()

# s4=studentthree("kumar",34)
# #s4.setdetails("jagan",500)
# s4.printdetails()

# #oops - object oriented programming language or system
# #class object inheritance polumorphism encapsulation abstraction interface
# #single inheritance-> one parent class one child class

# class device:
#     def power_on(self):
#         print("device switched on")
# class phone(device):
#     def call(self):
#         print("making a phone call")
# samsung=phone()
# samsung.power_on()
# samsung.call()
# print()
# #multilevel inheritance-. grandparent->parent->son 
# class device:
#     def power_on(self):
#          print("device switched on")
# class computer(device):
#     def run_program(self):
#         print("running a puthon program")
# class laptop(computer):
#     def charge(self):
#         print("laptop battery charging")
# asus=(laptop)
# asus.poer_on()
# asus.run_program()
# asus.charge()
# print()
# #multiple inheritance one child class multiple parent class
# class camera:
#     def take_photo(self):
#         print("taking a photo")
# class musicplayer:
#     def play_music(self):
#         print("playing music")
# class smartphone(camera,musicplayer):
#     def call (self):
#         print("making a phone call")
# mi=smartphone()
# mi.call()
# mi.take_photo()
# mi.play_music() 