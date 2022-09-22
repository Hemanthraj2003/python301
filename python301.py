class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class bank:
    
    
    def __init__(self,initial_amt=0):
        self.balance = initial_amt
        print ("\tYour Current Balance is:\t",self.balance)
        f = open("passbook.txt", "a")
        f.write("\n\nTRANCTION_ID   TYPE              AMOUNT        STATUS      BALANCE\n")
        
    def deposit(self,amt=0.0,id=0):
        self.balance = self.balance + amt
        print (bcolors.WARNING + bcolors.UNDERLINE + "\n\tCurrent Balance :\t",self.balance )
        bcolors.ENDC
        print(bcolors.OKBLUE + bcolors.BOLD  + "\n\t\t\t\tTransaction Successfull.!!!" + bcolors.ENDC)
        f = open("passbook.txt", "a")
        f.write(f"{id}           deposit           +{amt}        success     {self.balance}\n")
        f.close()
        
        
    def widthdraw(self,amt=0.0,id=0):
        if amt > self.balance:
            print(bcolors.FAIL + "\t\t\t\tTransaction Failed.!!!" )
            print ("\t\t\t\tInsufficient Blance." + bcolors.ENDC)
        else:    
            self.balance = self.balance - amt
            print (bcolors.WARNING + bcolors.UNDERLINE + "\n\tCurrent Balance :\t",self.balance )
            bcolors.ENDC
            print(bcolors.OKBLUE + bcolors.BOLD  + "\n\t\t\t\tTransaction Successfull.!!!" + bcolors.ENDC)
            f = open("passbook.txt", "a")
            f.write(f"{id}           deposit           -{amt}        success     {self.balance}\n")
            f.close()
    
    def bal(self):
        print ("\tCurrent Balance :\t",self.balance)


start = input("\n\n\tDo your want to start Banking Y/N :\n\t")
start = start.lower()   
if start == "y":
    initial = input("\tEnter the initial amount \n\t:")    
    initial = float(initial)     
    transc = bank(initial)   
    
    
i = 1000  
while start == "y":
  try:
    i = i + 1
    print ("\n\n\tDo you want to Deposit or Widthdraw") 

    trans = input("\tEnter 1 for deposit\n\tEnter 2 for widthdraw \n\tEnter 3 for Balance Enquery\n\t: ")
    trans = float(trans)

    if trans == 1:
        amt = input("\tEnter the amt to be deposited : ")
        amt = float(amt)
        transc.deposit(amt,i) 
    elif trans == 2:
        amt = input("\tEnter the amt to be widthdrawn : ")
        amt = float(amt)
        transc.widthdraw(amt,i) 
    elif trans == 3:
        transc.bal()
    else:
        print (bcolors.FAIL + "You Can Only Perfrom Thr Above Transcations Only" + bcolors.ENDC)
    start = input("\n\n\tDo your want to continue Banking Y/N :\n\t")   
    start = start.lower() 
  except Exception:
        print(bcolors.FAIL + "\t\t\t\tTransaction Failed.!!!" )
transc.bal()   




    
    

   
    