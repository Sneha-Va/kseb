import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ksebdb')
mycursor = mydb.cursor()
while(True):
    print("select any option");
    print("1.Add consumer")
    print("2.search consumer")
    print("3. delete consumer")
    print("4. update consumer")
    print("5. view all consumer")
    print("6. generate bill")
    print("7. view  bill")
    print("8. exit")
    choice=int(input('enter the option'))
    if(choice==1):
        print("add consumer")
        name=input("enter the name")
        address=input("enter address")
        consumerid=input("enter consumer id")
        phone=input("eter phonenumber")
        sql="INSERT INTO `consumer`(`name`, `address`, `consumerid`, `phone`) VALUES (%s,%s,%s,%s)"
        data=(name,address,consumerid,phone)
        mycursor.execute(sql,data)
        mydb.commit()
        print("successfully added")
    elif(choice==2):
        print("search consumer")
        search=input("enter consumer id,phone,name")
        sql="SELECT `id`, `name`, `address`, `consumerid`, `phone` FROM `consumer` WHERE `consumerid`='"+search+"',OR 'name'='"+search+"',OR 'phone'='"+search+"'"
        
    elif(choice==3):
        print("delete consumer")
        consumerid=input("enter consumer id:")
        sql="DELETE FROM `consumer` WHERE `consumerid`="+consumerid
        mycursor.execute(sql)
        mydb.commit()
        print("successfully deleted")
    elif(choice==4):
        print("update consumer")
        consumerid=input("enter consumer id")
        name=input("entre name to be updated:")
        address=input("enter the address to be updated")
        phone=input("enter phone number to be updated")
        sql="UPDATE `consumer` SET `name`='"+name+"',`address`='"+address+"',`phone`='"+phone+"' WHERE `consumerid`="+consumerid
        mycursor.execute(sql)
        mydb.commit()
        print("updated sucessfully")
    elif(choice==5):
        print("view consumer")
        print("view employee")
        sql= 'SELECT * FROM `consumer` WHERE 1'
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==6):
        
        print("generate bill")
    elif(choice==7):
        print("view bill")
    elif(choice==8):
        break