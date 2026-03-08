import json
import random
import string
from pathlib import Path 
#(import this because to find the path of the data.json)

class Bank:

    # store the path of data.json in the database
    database= 'data.json' 

    # we will create the dummy data because the dummy data will exist in file so accessing will become easy and after that will update the main data file    
    data= []
    
    # we will open the data.json file read the content and load into the dummy data that is data by json.loads
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print("File does not exist")
    except Exception as err:
        print("The file does not exist")

    # we are making it static method so that it cant be accessed
    @classmethod
    def __update(cls):
        # now open the file of the json and put the dummy data in the main data
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
            

    @classmethod
    # for creating the account number randomly
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        # thesse value will be in aline so therefore to shuufle this
        id= alpha + num + spchar
        random.shuffle(id)
        # this will genrate the list therefore to convert this into string
        return "".join(id)
    
          


    def Createaccount(self):
        # we will input the data of the user in the key value pair because because in the json the data are stored in the key value pair

        info={
            "name": input("Enter your name "),
            "age" : int(input("Enter you age ")),
            "email" : input("Enter your email "),
            "pin": int(input("enter your pin ")),
            "account_no": Bank.__accountgenerate(),
            "balance":0
        }

        if info["age"]<18 or len(str(info["pin"]))!=4:
            print("Sorry your account cannot be created")
        else:
            print("Account created successfully")  

            for i in info :
                print(f"{i} : {info[i]}")
                
            print("Please note down your account number") 

            # now this information will be create in the dummy data
            Bank.data.append(info)
            
            # now this update become private therefore only acceded in class only
            Bank.__update()        


    def depositmoney(self):
        account_num=input("Please tell your account number")
        pin=int(input("Please tell your pin"))

        userdata=[i for i in Bank.data if i["account_no"]==account_num and i["pin"]==pin]

        if userdata==False:
            print("Sorry account not found")

        else:
            amount=int(input("enter the amount you want to deposit"))

            if amount>10000 or amount<0:
                print("Sorry the amount is to much")

            else:
                userdata[0]["balance"]+=amount
                Bank.__update()

                print("Amount deposit succesfully")


    def withdrawmoney(self):
        account_num=input("Please tell your account number")
        pin=int(input("Please tell your pin"))

        userdata=[i for i in Bank.data if i["account_no"]==account_num and i["pin"]==pin]

        if userdata==False:
            print("Sorry account not found")

        else:
            amount=int(input("enter the amount you want to withdraw"))

            if userdata[0]["balance"]< amount :
                print("Sorry the amount is not present in the account")

            else:
                userdata[0]["balance"]-=amount
                Bank.__update()

                print("Amount withdraw succesfully")


    def details(self):
         
        account_num=input("Please tell your account number")
        pin=int(input("Please tell your pin")) 

        userdata=[i for i in Bank.data if i["account_no"]==account_num and i["pin"]==pin]        

        if len(userdata)==0:
            print("Sorry account not found")

        else:
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
            print("Account details print succesfully")


    def updatedetails(self):
        account_num=input("Please tell your account number")
        pin=int(input("Please tell your pin")) 

        userdata=[i for i in Bank.data if i["account_no"]==account_num and i["pin"]==pin]        

        if userdata == False:
            print("Sorry account not found")

        else:
            print("press 1 for updating the name")
            print("press 2 for updating the email")
            print("press 3 for updating the pin")

            n=int(input("enter your response "))

            if n==1:
                name=input("enter the updated name")
                userdata[0]["name"]=name


            elif n==2:
                email=input("enter your updated email")
                userdata[0]['email']=email

            elif n==3:
                pin=int(input("enter your updated pin"))
                userdata[0]["pin"]=pin   
            print("updation is done successfully") 
            Bank.__update()        

    def delete(self):
        account_num=input("Please tell your account number")
        pin=int(input("Please tell your pin")) 

        userdata=[i for i in Bank.data if i["account_no"]==account_num and i["pin"]==pin]        

        if userdata == False:
            print("Sorry account not found")
        else:
            check=input("press y for deleteing the account else n")
            if check=='n' or check=='N':
                print("bypass")
            else:
                index=Bank.data.index(userdata[[0]])
                Bank.data.pop(index)
                print("Account delete successfully")

                Bank.__update()


user=Bank()



print("Press 1 for crearing an account")
print("Press 2 for deposit the money")
print("Press 3 for withdraw the money")
print("Press 4 for details ")
print("Press 5 for updating the details")
print("press 6 for deleting an account")

check=int(input("Enter your response "))

if check==1:
    user.Createaccount()

if check==2:
    user.depositmoney()

if check==3:
    user.withdrawmoney()      

if check==4:
    user.details()      

if check==5:
    user.updatedetails()  

if check==6:
    user.delete()      