# if statement

# i=10
# if(i<15):
#     print("10 is lessthan 15")
#     print("i am not in it")

# if else statement

# i=20
# if(i>15):
#     print("i is smaller than 15")
#     print('i am in if block')
# else:
#     print("i is grater than 15 ")
#     print("i am in else block")
#     print("i am not in if block and i am not in else block")
    
#if elif statement

# a=30
# b=20
# if(a>b):
#     print("a is bigger than b")
# elif(a==b):
#     print("a & b are euals")

# if elif else statement

# i=int(input("enter any number"))
# if(i==10):
#     print("i is 10")
# elif(i==15):
#     print("i is 15")
# elif(i==20):
#     print('i is 20')
# elif(i==30):
#     print("i is 30")
# elif(i==40):
#     print("i is 40")
# else:
#     print("i is not present") 

# nested if statement  

# i=10
# if(i==10):
#  if(i<15):
#      print("i is smaller than 15")
# if(i<12):
#     print("i is smaller than 12")

#"""" ifelse if statements"""a

# a=input("enter any number")
# b=input("enter another number")
# if(a<=b):
#     print(b,"is begger than a=",a)
# else:
#     print(a,"is begger than b=",b)
# if(a==b):
#     print(a,b,"are equal numbers")


# nested if else

# name=input("enter your name")
# day=input("enter what day is today:")
# if(day=="sunday"):
#     print(name,"you can go out ,but you must return compus at 5:30")
#     where=input("where are going ?.....")
#     if(where=="katraj"):
#         print(name,"can you bring biscuits for me")
#     else:
#         print(where,".......")    
# else: 
#         print(name,"on this",day,"you must to take permission from Disco didi")
#         permission=input("do you taken permission from Disco didi?.....")
#         if(permission=="yes"):
#             print(name,"ok you can go out of the compus.")
#         else:
#             print(name,"first you must to take permission from Disco didi.then only you allowed to out")

        
#  reverse print
# a=input("enter any number")
# # a="123"
# print(a[::-1])



# email creation
# a=input("do you have email id or not?...")
# if(a=="yes"):
#     print("don't need to create email id")
# elif(a=="no"):
#     print("pleace create email id")
#     print("go to the create email id - Google Search.html")
#     email=input("link open then go and create emailid ")
#     if(email=="ok"):
#         print("then give ur details like name ,surname,phone number,password")
#         name=input("enter your name:")
#         surname=input("enter your surname:")
#         phone=input("enter your phone number:  ")
#         # if phone == len("10"):
#             # phone=input("re enter your phone number must be 10 digits:")
#         id=input("create your email id :   ")
#         password=input("put strong password:  ")
#         repass=input("re enter your password:  ")
#         print("u have successfully created your emilid:",id,repass)
#         if(password!=repass):
#             print("your password not match with firstone ,so enter corretly.")
#             password=input("set strong password:  ")
#             repass=input("match your password what you enter firstly")
#             print("your email id successfully completed")
#         else:
#             print("your emailid successfully completed")




    # finding lenth of number.

# a="1234567890"
# print(len(a))
# if(len(a)==10):
#      print(len('0'))


#   notes
# a=input("enter amount")
# print(a[1:-1])

  # identity,membership,bitwise
  
# name=["anu","suni","shivi","haseena"]
# print("anu"  not in name)
# print("shivi" in name)
# print(name in "suni")


# a=20
# b=39
# print(a is not b)
# print(a is b)

# a=12
# b=10
# print(a&b)


  # finding digit r character r special character

# # character=(input("enter an character"))
# # # specailcharecter=("@","#","%","$")
# # if character.isdigit():
# #     print("The given character is digit.")
# # elif character.isalpha():
# #     print("The given character is alphabet.")
# # else:
# #     print("The given character is special character")

# #     #prime number 



# # a=int(input("enter any number"))
# # if a==2 or a==3  or a==5 or a==7:
# #     print("prime")
# # elif a%2==0 or a%3==0 or a%5==0 or a%7==0:
# #   print("not prime")
# # else:
# #   print("prime")  


#   # percentage.....
# # name=input("enter student name")
# # math=float(input("enter maths marks"))
# # com=float(input("enter computer marks"))
# # phy=float(input("enter physics marks"))
# # chem=float(input("enter chemstry marks"))
# # bio=float(input("enter biology marks"))
# # tot=math+com+phy+chem+bio
# # per=tot/500*100
# # print(per)
# # if(per>=90/100*100):
# #       print(name, "got A grade")
# # elif(per<=80/100*100):
# #       print(name,"got a rank B")
# # elif(per<=70/100*100):
# #       print(name,"got C grade")
# # elif(per<=50/100*100):
# #       print(name,"got D grade")
# # else:
# #       print(name,"failled ")


#     #  table

# # n=int(input('enter any number :'))
# # print(n,"* 1 =",n*1)
# # print(n,'* 2 =',n*2)
# # print(n,"* 3 =",n*3)
# # print(n,"* 4 =",n*4)
# # print(n,"* 5 = ",n*5)

# #   #  next date

# # d=int(input("enter date:"))
# # m=int(input("enter month"))
# # y=int(input("enter year"))
# # if 28>d>=1 and m==2:
# #   if d==28 and m==2:
# #     print("1 /",m+1,y)
# #   else:
# #     print(d+1,"/",m,"/",y) 
# # elif 30>d>=1 and m==4 or m==9 or m==11 or m==6:
# #       print(d+1,"/",m,"/",y)
# # elif d==30 and m==4 or m==9 or m==11 or m==6 :
# #       print("1 /",m+1,"/",y)
# #     # else:
# #     #   print(d+1,"/",m,"/",y)
# # elif(31>d>=1 and m==1 or m==3 or m==5 or m==7 or m==8 or m==10  or m==12):
# #   print(d+1,"/",m,"/",y)  
# # elif d==31 and m==1 or m==3 or m==5 or m==7 or m==10 or m==8 or  m==12:
# #   print("1 / 1",y+1)
# # else:
# #   print(d+1,"/",m,"/",y)

#     #  weekday number

# # n=input("enter number")
# # if n=='1':
# #   print("sunday")
# # elif n=="2":
# #   print("monday")
# # elif n=="3":
# #   print("thuesday")
# # elif n=="4":
# #   print("wednesday")
# # elif n=="5":
# #   print("thursday")
# # elif n=="6":
# #   print("friday")
# # elif n=="7":
# #   print("saterday")
# # else:
#   # print("not a week number ..")

     
#       #  2nd largest number

# # a=int(input("enter number"))
# # b=int(input("enter number"))
# # c=int(input("enter number"))
# # if c>a>b or b>a>c:
# #   print(a)
# # elif c>b>a or a>b>c:
# #   print(b) 
# # else:
# #   print(c)            
  

# #  hello & 5 multiple
# # n=int(input('enter any number'))
# # if n%5==0:
# #   print("hello")
# # else:
# #   print('bye')


# # bike price and taxes

# # b=int(input('enter bike price.....'))
# # if b>100000:
# #   print(b+15/100,"total price","tax=15%")
# # elif (b>50000 and b<=100000):
# #   print("total price=",b+10/100)
# # elif (b<=50000):
#   # print("total price="/,b+5/100)\



# # a='5' 
# # b=18.5
# # print=(a+b)
# # a=int=a

#          # atm notes............      
# a=int(input("enter amount:"))
# u=int(input("enter which notes u want:"))
# if u==10 and (a//10)!=0:
#   print("10 notes-",a//10)
# if u==20 and (a//20)!=0:
#   print("20 notes-",a//20)
#   t=a-(a//20)*20
#   if t!=0:
#     t=t//10
#     print("10 notes--",t)    
# if u==50 and a//50!=0:
#   print("50 notes--",a//50)
#   c=a-(a//50)*50
#   t=c//20
#   m=c-t*20
#   print("20notes--",t)
#   if m!=0:
#       l=m-(t)*20
#       d=l//10
#       print("10 notes--",d)
# if u==100 and a//100!=0:
#   print("100 notes--",a//100)
#   h=a-(a//100)*100
#   if h!=0:
#     f=h//50
#     print("50 notes--",h//50)
#     c=h-(f)*50
#     # print(c)
#     t=c//20
#     d=c-(t)*20
#     # print(d)
#     print("20notes--",t)
#     if d!=0:
#        k=d//10
#        print("10 notes",k)  
# if u==200 and a//200!=0:
#    print("200 notes--",a//200)
#    b=a-(a//200)*200
#    h=b//100
#    print("100 notes--",h)
#    c=b-(h)*100
#    d=c//50
#    print("50 notes",d)
#    e=c-(d)*50
#   #  print(e)
#    t=e//20
#    d=e-(t)*20
#   #  print(d)
#    print("20 notes--",t)
#    if d!=0:
#       k=d//10
#       print("10 notes--",k)
# if u==500 and (a//500)!=0:
#   print("500 notes are--",a//500)
#   s=a-(a//500)*500
#   # s!=0
#   print("200 notes--",s//200)
#   b=s-(s//200)*200
#   h=b//100
#   print("100 notes--",h)
#   c=b-(h)*100
#   d=c//50
#   print("50 notes--",d)
#   e=c-(d)*50
#   #  print(e)
#   t=e//20
#   d=e-(t)*20
#   #  print(d)
#   print("20notes--",t)
#   if d!=0:
#     k=d//10
#     print("10 notes--",k)  
# if u==1000 and a//1000!=0:
#   print("1000 notes are--",a//1000)
#   z=a-(a//1000)*1000
#   print("500 notes are--",z//500)
#   s=z-(z//500)*500
#   print("200 notes--",s//200)
#   b=s-(s//200)*200
#   h=b//100
#   print("100 notes--",h)
#   c=b-(h)*100
#   d=c//50
#   print("50 notes--",d)
#   e=c-(d)*50
#   #  print(e)
#   t=e//20
#   d=e-(t)*20
#   #  print(d)
#   print("20notes--",t)
#   if d!=0:
#     k=d//10
#     print("10 notes--",k)
# if u==2000 and a//2000!=0:
#   print("2000 notes--",a//2000)
#   w=a-(a//2000)*2000   
#   print("1000 notes are--",w//1000)
#   z=w-(w//1000)*1000
#   print("500 notes are--",z//500)
#   s=z-(z//500)*500
#   print("200 notes--",s//200)
#   b=s-(s//200)*200
#   h=b//100
#   print("100 notes--",h)
#   c=b-(h)*100
#   d=c//50
#   print("50 notes--",d)
#   e=c-(d)*50
#   t=e//20
#   d=e-(t)*20
#   print("20notes--",t)
#   if d!=0:
#     k=d//10
#     print("10 notes--",k)
      


#       #digit and alphabets 

# # s=input("enter any number or alphabet:")
# # if (s>="a" and s<="z") or (s>="A" and s<="Z"):
# #    print("alphabet",s)
# # elif s>"0":
# #    print("digit",s)

# positive and negative ......

# a=int(input("enter any number :"))
# if a<0:
#   print(-(a))
# else:
#   print(-(a))


# shop=input("enter the shop:")
# items=input("enter the items :")
# if shop=="first":
#   print("open")
#   if items=="biscut":
#     print(items,"is present")
#   elif items=="chocoidte":
#     print(items,"is present")
#   else:
#     print(items,"is not present")
# elif shop=="second":
#   if items=="kurkur":
#     print(items,"is present")
#   elif items=="berad":
#     print(items,"is present")
#   else:
#     print(items,"is not present")
# else:
#   print("come beck hoe")                
    