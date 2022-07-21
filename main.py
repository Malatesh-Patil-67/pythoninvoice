import pymongo
from datetime import datetime,date

client=pymongo.MongoClient()

##### adding customers to database##########
mydb=client["CUSTOMERS"]
mycol=mydb["User_info"]

datalist=[{  "ssn": "988-696-678",
             "blood_group": "0+",
             "username": "mgp67",
             "name":"malatesh girish",
             "sex": "M",
             "address": "0032 Walker Fords Apt 358Heidiview UT 88398",
             "mail": "malteshpatil40629@mail.com",
             "birthdate": "02-0-1997",
             "age": "25"},
          {"ssn": "988-987-876",
           "blood_group": "0-",
           "username": "mgp66",
           "name": "varun",
           "sex": "M",
           "address":"0032 Walker Fords Apt 358Heidiview UT 78986",
           "mail": "varun@@mail.com",
           "birthdate": "02-0-1998",
           "age": "24"}
          ]

#mycol.insert_many(datalist)

mydb=client["admin"]
mycol=mydb["ADMIN_INFO"]
data={ "user_name": "John",
         "password": "Mongodb123"}

#mycol.insert_one(data)



####### Customer search function

def search(input_name):
    mydb = client["CUSTOMERS"]
    col2 = mydb["User_info"]
    att2 = col2.find()
    for data in att2:
        #print(data)
        cus_username = data['username']
        cus_dateofbirth = data['birthdate']
        #print(cus_username)
        #print(input_name)
        if(input_name==cus_username):
            #print(1)
            #value="true"
            break
        else:
           cus_dateofbirth="zero"

    return cus_dateofbirthc


def newinvoice(input_customer_username,t):
    mydb = client["invoice1"]
    col3 = mydb["medicine"]
    att3 = col3.find()
    bill = 0
    while(True):
        print("\nChoose an option: \n")
        print("\n1.Enter product details\n2.Display Invoice\n")
        y = input("\nEnter your choice --> ")
        if (y == "1"):
            value2 = "false"
            product = input("\nEnter product --> ")
            for data in att3:
                product_name = data['Name']
                product_quantity = data['Quantity']
                product_mrp = data['mrp']
                #print(product_name)
                #print(product)
                if (product_name == product):
                    print("1")
                    value2="true"
                    r = input("\nEnter the quantity --> ")
                    if (int(r) <= int(product_quantity)):
                        update_medicine_quantity(r,product_name,product_quantity)
                        bill = float(bill) + float(r) * float(product_mrp)
                        break
                    else:
                        print("\nThere are only  " + product_quantity + "  products in the store")
                        break

            if(value2=="false"):
                print("\nProduct not available")


        if (y == "2"):
            date_values = t.split('-')
            born = date_values[2] + "-" + date_values[1] + "-" + date_values[0]
            born = datetime.strptime(born, "%d-%m-%Y").date()
            today = date.today()
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

            if (age >= 0 and age <= 15):
                bill = float(bill) - (25 * float(bill) / 100)
            if (age >= 16 and age <= 30):
                bill = float(bill) - (10 * float(bill) / 100)
            if (age >= 31 and age <= 55):
                bill = float(bill) - (15 * float(bill) / 100)
            else:
                bill = float(bill) - (25 * float(bill) / 100)
            addproduct()
            update_bill(bill,input_customer_username)
            print("\n Your Total Bill is:"+str(bill)+"\n")
            break



def update_medicine_quantity(r,product_name,product_quantity):
    product_quantity2=int(product_quantity)-int(r)
    #myquery = {"Name": product_name}

    ## Ask About updating database after purchasing
    #mydb = client["CUSTOMERS"]
    #$col2 = mydb["User_info"]
    #col2.update_many({'username': 'james22'}, {'$set': {'Bill': 0}}, upsert=True)
   # col2.update_one(
     #   {},
     #   {"$set": {"Bill": 0}},
     #   {"upsert": True,
      #   "multi": True})

    mydb = client["invoice1"]
    col3 = mydb["medicine"]
    #col3.update_one({'Name': product_name}}{, {'$set': {"Quantity": str(product_quantity2)}}, upsert=True)

    col3.update_many({'Name': product_name}, {'$set': {"Quantity": str(product_quantity2)}}, upsert=True)
    #col2.update_many({}, {'$set': {"Bill": float(0)}}, upsert=True)

    #newvalues = {"$set": {"quantity": product_quantity2}}



def update_bill(bill, input_customer_username):
    mydb = client["CUSTOMERS"]
    col2 = mydb["User_info"]
    col2.update_one({'username': input_customer_username}, {'$set': {"Bill": float(bill)}}, upsert=True)
    # addproduct(mydb,)


def createpatient(input_customer_username):
    a = input("\nEnter Customer SSN --> ")
    b = input("\nEnter Customer Blood group --> ")
    c = input_customer_username
    d = input("\nEnter Customer Name --> ")
    e = input("\nEnter Customer Sex --> ")
    f = input("\nEnter Customer Address --> ")
    g = input("\nEnter Customer Email id --> ")
    h = input("\nEnter Customer Birth date --> ")

    customer_record = {
        "ssn": a,
        "blood_group": b,
        "username": c,
        "name": d,
        "sex": e,
        "address": f,
        "mail": g,
        "birthdate": h,
    }

    mydb = client["CUSTOMERS"]
    col2 = mydb["User_info"]
    col2.insert_one(customer_record)

    return h



###########deleting user from database#######
########### updating user from database######




####### Admin function

def Admin():
 # check if admin is present (Admin authentication , username and password check)
 # if admin authentication is succesful


 input_admin_username = input("\nEnter your username --> ")
 input_admin_password = input("\nEnter your password --> ")

 col = mydb["ADMIN_INFO"]

 att = col.find_one()

 admin_username=att['user_name']
 admin_password=att['password']

 if ((admin_username ==  input_admin_username) and (admin_password ==  input_admin_password)):
     print("\n Login successful \n")
     print("\n Choose an option -->  ")
     print("\n1. Create and Display Invoice After Discount \n2. Exit")
     x = input("\nEnter your choice --> ")
     if (x == "1"):
         input_customer_username = input("\nEnter Customer's username --> ")
         t=search(input_customer_username)
         #print(t)
         if (t!="zero"):
             newinvoice(input_customer_username,t)
         else:
             datebirth=createpatient(input_customer_username)
             newinvoice(input_customer_username,datebirth)

     elif(x == "2"):
          exit()

     else:
         print("\nWrong Choice")

 else:
     print("\nLogin unsuccessful")




def start():
 x = 0
 while (1):
  print("1. Admin\n")
  print("2. Patient\n")
  x = input("\nChoose an Option --> ")
  if (x == "1"):
   Admin()
   break
  elif (x == "2"):
   Patient()
   break
  else:
   print("\nWrong Choice\n")

start()