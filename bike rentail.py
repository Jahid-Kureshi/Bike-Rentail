class bikeshop:

    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Total Bikes",self.stock)  
    def rentForBike(self,q):

        if q<=0:
            print("Enter the Postive Value or greater then zero")
        elif q>self.stock:
            print("Enter the value (less then stock)") 
        else:
            self.stock=self.stock-q
            print("Total Prices",q*100)
            print("Total Bikes",self.stock)       
while True:
    obj=bikeshop(100)
    uc=int(input('''
    1 Display Stocks
    2 Rent a Bike
    3 Exit

    '''))
    if uc==1:
        obj.displaybike()
    elif uc==2:    
        n=int(input("Enter the Qty"))
        obj.rentForBike(n)
    else:
        break    