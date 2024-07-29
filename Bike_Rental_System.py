class bikeshop:


    def __init__(self,stock):
     self.stock=stock

    def displayBike(self):
     print("Total Bikes ",self.stock)

    def rentforbike(self,q,s):

     if q<=0:
      print("please enter the valid value")
     elif q>self.stock:
      print("your given bike Demand is more Then Stock ")
     else:
      print("Total Rent is = ",q*50*s)
      print("total available bike = ",self.stock-n)


while True:
 obj=bikeshop(100)
 print("Enter Your Choice : ")
 uc=int (input('''
  1. Display Available Bikes
  2. Request For a Bike Rent (50 Rs ->1qty)
  3. Exit
'''))
 
 if uc==1:
  obj.displayBike()
 elif uc==2:
  n=int(input("Enter The Quantity :-"))
  s=int(input("Enter the Hour for rent :-"))
  obj.rentforbike(n,s)
 elif uc==3:
  break
 else:
  print("Enter valid choice ")













