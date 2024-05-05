import random
class Bank:
    def __init__(self,name):
        self.name = name
        self.user_account_list = []
        self.initial_balance = 0
        self.total_loan_amount = 0
        self.loan_status = False
            
    def transfer_money(self,amount,account_number,bank):
        use = bank.find_user_account(account_number)
        if use:
            if amount <= self.initial_balance:
                self.initial_balance -= amount
                user.initial_balance +=  amount
                print("\n\tAmount Transfer successfully!!")
            else:
                print("\n\tTransfer Amount Exceeded!!")
        else:
            print("\n\tAccount does not exist!!")
            
    def create_user_account(self,user):
        self.user_account_list.append(user)
        print(f"User Account successfully created!!!\n")
    
    def user_list(self):
        for account in self.user_account_list:
            print(f"Name of the User: {account.name}\t and Email of the user: {account.email}")
    
    def bank_balance(self):
        print(f"{self.name} your current balance is {self.initial_balance} taka!")
    
    def loan_balance(self):
        print(self.total_loan_amount)
    
    def remove_user_account(self,email):
        for acc in self.user_account_list:
            if email == acc.email:
                self.user_account_list.remove(acc)
                print("\n\tAccount Removed Successfully!")
            else:
                print("\n\tAccount does not exist!")
     
    def find_user_account(self,name,email):
        for account in self.user_account_list:
            if name == account.name and email == account.email:
                return account
            else:
                return None
            
    def find_admin_account(self,name,email):
        for account in self.user_account_list:
            if name == account.name and email == account.email:
                return account
            else:
                return None
    
    
    def loan_er_obostha(self,opt):
        if opt == 'on':
            self.loan_status=True
            print(f"Loan status is ON!!\n")
        else:
            self.loan_status=False
            print(f"Loan status is OFF!!\n")
            
            
class basic_account:
    def __init__(self,name,email,password,address):
        self.name=name
        self.email=email
        self.password=password
        
class Customer(basic_account):
    def __init__(self,name,email,password,address,account_type):
        super(Customer,self).__init__(name,email,password,address)
        self.account_type = account_type
        self.initial_balance = 0
        self.loan=2
        self.__transactionHistory = []
        self.account_number = (name+address)+str(random.randint(0,100))
        
    def transaction_history(self):
        for info in self.__transactionHistory:
            for key,value in info.items():
                print(f"{key} : {value}")
                
                
    def deposit_balance(self,amount,bank):
        if amount > 0:
            self.initial_balance += amount
            bank.initial_balance += amount
            print(f"{amount} taka Deposited Successfully!\n")
            self.__transactionHistory.append({'Amount':amount, 'Operation Name':"Deposit" , "Current Balance": self.initial_balance})
        else:
            print(f"{amount} taka is invalid amount!\n")
    

    def withdraw_balance(self,amount,bank):
        if self.initial_balance>=amount:
            self.initial_balance -= amount
            bank.initial_balance -= amount
            print(f"{amount} taka Withdrawn Successfully!\n")
            self.__transactionHistory.append({'Amount':amount, 'Operation Name':"Withdraw" , "Current Balance": self.initial_balance})
        elif self.initial_balance == 0:
            print("\n\tBank is Bankrupt!!")
        else:
            print("Withdrawal amount exceeded!!\n")
            
    def check_balance(self):
        print(f"Your current amount is {self.initial_balance} taka!")
        
    
    def take_loan(self,amount,bank):
        if self.loan>0:
            self.initial_balance += amount
            bank.total_loan_amount += amount
            self.loan -= 1
            print("\nLoan taken successfully!!!")
        else:
            print("\nLoan unavailable!!!")



class Admin(basic_account):
    # def __init__(self,name,email,password):
    #     super().__init__(name,email,password)
    def __init__(self,name,email,password,address):
        super().__init__(name,email,password,address)
        
    def create_account(self,name,email,password,address,account_type):
        user=Customer(name,email,password,address,account_type)
        bank.create_user_account(user)

    def remove_account(self, email, bank):
        bank.remove_user_account(email)

    def view_user_account(self, bank):
        bank.user_list()

    def checkBalance(self, bank):
        bank.bank_balance()

    def checkLoan(self, bank):
        bank.loan_balance()
        print(f"Total Loan Balance: {bank.loan_balance()}")

    def set_Loan_Status(self, status, bank):
        loan_er_obostha(status, bank)
        
        
        
bank = Bank("Amar Sonar Bank!")
admin = Admin("Rahim",'rahim@gmail.com','123456','Kaunia')


def Admin_World():
    while True:
        print("!!!Admin World!!!")
        print(f" 1 : Create new account\n 2 : Delete User\n 3 : View User List\n 4 : Total Bank Balance\n 5 : Total Loan Amount\n 6 : Loan Status\n 7 : Exit\n")
        
        Option = int(input("Choose one option : "))
        
        if Option == 1:
            name = input(f"\tEnter User Name : ")
            email = input(f"\tEnter User Email : ")
            password = input(f"\tEnter User Password : ")
            address = input(f"\tEnter User Address : ")
            account_type = input(f"\tEnter User Account Type : ")
            
            admin.create_account(name,email,password,address,account_type)
            
            
        elif Option == 2:
            email = input(f"\tEnter User Email, which you want to delete : ")
            admin.remove_account(email,bank)
            
        elif Option == 3:
            admin.view_user_account(bank)
            
        elif Option == 4:
            admin.checkBalance(bank)
        
        elif Option == 5:
            admin.checkLoan(bank)
            
        elif Option == 6:
            status = input("Choose - (on/off): ")
            admin.set_Loan_Status(status.lower(),bank)
        
        elif Option == 7:
            break
        else:
            print("\tINVALID INPUT!")
            
            
def user_section(user):
    while True:
        print("\tWelcome To User Paradise!\n")
        print(f" 1 : Deposit Balance into Account\n 2 : Withdraw Balance\n 3 : View Available Banlance\n 4 : Take Loan from Bank\n 5 : Trasfer Money \n 6 : View Transaction History\n 7 : Exit\n")
        option = int(input("Enter an option you want to choose..."))
        
        if option == 1:
            amount = int(input("Enter amount for deposit balance: \t"))
            user.deposit_balance(amount,bank)
            
        elif option == 2:
            amount = int(input("\nEnter withdraw amount: \t"))
            user.withdraw_balance(amount,bank)
            
        elif option == 3:
            user.check_balance()
        
        elif option == 4:
            amount = int(input("\tEnter amount for loan: "))
            user.take_loan(amount,bank)
            
        elif option == 5:
            amount = int(input("\tEnter amount for tranfer money: "))
            user.transfer_money(amount)
            
        elif option == 6:
            user.transaction_history()
            
        elif option == 7:
            break
        
        else:
            print("Invalid option given\n")


def userLogin():
    while True:
        print(f"Choose an Option\nOption - 1 : Login\nOption - 2 : Sign Up\nOption - 3 : Exit\n")
        opt = int(input())
        if opt == 1:
            print(f"Please Login First!!!")
            email = input("Please Enter Your Email ")
            if bank.find_user_account(name,email):
                print("\n\tLOGIN SUCCESSFUL\n")
                user_section(user)
            else:
                print("Email does not exist\n")
            
        elif opt == 2:
            print("Create a new account!!!\n")
            user_name = input("Enter your username : ").lower()
            user_email = input("Enter your email : ").lower()
            user_address = input("Enter your address : ").lower()
            password = input("Enter your password : ").lower()
            print("Account Type : 'Savings'/'Current'")
            account_type = input("Account type : ").lower()
            if bank.find_user_account(user_name,user_email) is not None:
                print(f"Sorry {user_email} Already Exist")
            else:
                client = Customer(user_name,user_email,password,user_address,account_type)
                bank.create_user_account(client)
                user_section(client)
                
        elif opt == 3:
            break
                  
    
while True:
    print(f"Welcome to Banking System!\n")
    print(f"Which option you want to choose?\n")
    print(f"1. Administrators\n2. Customer/Users\n3. Exit System\n")
    
    opt = int(input("Enter your choice: "))
    
    if opt == 1:
        Admin_World()
        
    if opt == 2:
        userLogin()

    elif opt == 3:
        break
    else:
        print("Invalid Choice!")