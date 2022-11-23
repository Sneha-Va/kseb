import mysql.connector
from datetime import date
from tabulate import tabulate
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ksebdb')
mycursor = mydb.cursor()
while(True):
    print("select any option")
    print("1.Add consumer")
    print("2.search consumer")
    print("3. delete consumer")
    print("4. update consumer")
    print("5. view all consumer")
    print("6. generate bill")
    print("7. view  bill")
    print("8.Top  2 high bill")
    print("9.exit")
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
        search=input("enter consumer id,phone,name:")
        sql="SELECT  `name`, `address`, `consumerid`, `phone` FROM `consumer` WHERE `consumerid`='"+search+"' OR `name`='"+search+"' OR `phone`='"+search+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        
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
        print('generate bill selected')
        dates = date.today()
        year = dates.year
        month = dates.month
        sql="DELETE FROM `bill` WHERE `month`='"+str(month)+"' AND `year`= '"+str(year)+"'"
        mycursor.execute(sql)
        mydb.commit()
       
        sql="SELECT `id` FROM `consumer`"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            a=i[0]
            print(a)
          
            sql="SELECT SUM(unit) FROM `usage` WHERE `consumerid`='"+str(a)+"' AND MONTH(date)='"+str(month)+"' AND YEAR(date)='"+str(year)+"' "
            mycursor.execute(sql)
            result=mycursor.fetchone()
            unit=(result[0])
            print(result)
            #print(i)
            total_bill=int(str(result[0])) * 5
            print(total_bill)
            #date= datetime.today().strftime('%Y-%m-%d')
            sql="INSERT INTO `bills`(`consumerid`, `month`, `year`, `bill`, `billstatus`, `billdate`, `totalunit`,`duedate`) VALUES (%s,%s,%s,%s,%s,now(),%s,now()+interval 14 day)"
            data = (str(a),str(month),str(year),total_bill,'0',unit)
            mycursor.execute(sql,data)
            mydb.commit()
            print("Bill inserted successfully.")
    elif(choice==7):
        print("view bill")
        print("view the bill which had generated ")
        sql = "SELECT c.name,c.address, b.`month`, b.`year`, b.`billstatus`, b.`billdate`, b.`totalunit`, b.`bill` FROM `bills` b JOIN consumer c ON b.consumerid=c.id"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(tabulate(result,headers=['name','address','month','year', 'billstatus','billdate','totalunit','bill'],tablefmt = "psql"))
    elif(choice==8):
        print('Top 2 high bill')
        sql = "SELECT * FROM `bills` ORDER BY `bills`DESC LIMIT 2"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(tabulate(result,headers=['id', 'User_Id', 'month', 'year', 'bill', 'paid status', 'bill date',  'total_unit','due_date']))   
    elif(choice==9):
        break