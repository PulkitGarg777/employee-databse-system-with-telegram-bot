check = 0
import getpass
import requests
from tabulate import tabulate
tga_bot = "https://api.telegram.org/bot1356192558:AAGpzOSJm_-f6ukQUsSu2CJkpOadvDi5fPE/sendMessage?chat_id=826723031&text="

p = getpass.getpass(prompt= "PLEASE ENTER THE PASSWORD")
prompt1 = ("""LOGGED IN SUCCESSFULLY :)

----------------------------------------WELCOME TO SBSS----------------------------------------
            PLEASE SELECT ONE OF THE OPTIONS TO MANAGE EMPLOYEES:
            1) ADD AN EMPLOYEE
            2) CLEAR A OFFICE(ID REQUIRED)
            3) PROMOTE/DEMOTE AN EMPLOYEE
            4) SEARCH FOR AN EMPLOYEE
            5) VIEW ALL RECORDS
            6) TERMINATE PROGRAMME.""")

prompt2 = ("""---------------------------------------------------------------------------

            RUNNING AGAIN!

------------PLEASE SELECT ONE OF THE OPTIONS TO MANAGE EMPLOYEES: ----------
            1) ADD AN EMPLOYEE
            2) CLEAR A OFFICE(ID REQUIRED)
            3) PROMOTE/DEMOTE AN EMPLOYEE
            4) SEARCH FOR AN EMPLOYEE
            5) VIEW ALL RECORDS
            6) TERMINATE PROGRAMME. """)




def rec_add():
    print("EXECUTING PROGRAMME.")
    a=int(input("ENTER ID :"))
    import mysql.connector
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
    mycursor = mydb.cursor( buffered=True)
    bro = (a)
    add_comrade = """INSERT INTO EMPLOYEES(ID, NAME, DOB, EMAIL_ADD, DESIGNATION, DEPT, SALARY , GENDER)
        VALUES ('%d', '%s' , '%s' , '%s' , '%s' , '%d' , '%d' , '%s')"""
    REC = "SELECT* FROM EMPLOYEES WHERE ID = '%d'"
    mycursor.execute(REC % bro)
    z = mycursor.rowcount
    if z ==0:
        b=str(input("ENTER NAME :"))
        c=str(input("ENTER DOB (YYYY-MM-DD) :"))
        d=str(input("ENTER EMAIL : "))
        e=str(input("ENTER DESIGNATION :"))
        f=int(input("ENTER DEPARTMENT NO. :"))
        g=int(input("ENTER SALARY :"))
        h=str(input("ENTER GENDER : "))
        data = (a,b,c,d,e,f,g,h)
        mycursor.execute(add_comrade % data)
        mydb.commit()
        mycursor.execute(REC % bro)
        W =  mycursor.fetchall()
        wow = (tabulate(W, headers=['EMP ID','EMP NAME','DOB','EMAIL','DESIGNATION','DEPT. NO','SALARY','GENDER'], tablefmt='github'))
        print("DONE :)")
        print("THE UPDATED RECORDS :")
        mycursor.execute("SELECT* FROM EMPLOYEES")
        myrecords = mycursor.fetchall()
        result = str(wow)
        r =requests.get(tga_bot+'\n''\n'+"DATA ADDED IN RECORDS.THE ADDED RECORD IS : "+'\n''\n'+result+'\n''\n'+"WELCOME TO LA FAMILIA   ლ(▀̿̿Ĺ̯̿̿▀̿ლ)")
        print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
    else:
        print("EMPLOYEE ALREADY EXISTS. PLEASE TRY AGAIN.")
    



def rec_del():
    print("EXECUTING PROGRAMME.")
    a = int(input("ENTER THE EMPLOYEES ID : "))
    import mysql.connector
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
    mycursor = mydb.cursor( buffered=True)
    data = (a)
    REC = "SELECT* FROM EMPLOYEES WHERE ID = '%d'"
    mycursor.execute(REC % data)
    z = mycursor.rowcount
    print(z)
    if z == 1:
        mycursor.execute(REC % data)
        W = mycursor.fetchall()
        wow = (tabulate(W, headers=['ID','NAME','DOB','EMAIL','DESIG.','DEPT. NO','SALARY','GENDER'], tablefmt='github'))
        bye_comrade = "DELETE FROM EMPLOYEES WHERE ID = '%d' "
        mycursor.execute(bye_comrade % data)
        mydb.commit()
        print("DONE :)")
        print("THE UPDATED RECORDS :")
        mycursor.execute("SELECT* FROM EMPLOYEES")
        myrecords = mycursor.fetchall()
        result = str(wow)
        r =requests.get(tga_bot+'\n''\n'+"DATA DELETED FROM RECORDS.THE DELETED RECORD IS :"+'\n''\n'+result+'\n''\n'+"SORRY TO SEE YOU GO   (°∀°)ゝ” ")
        print(tabulate(myrecords, headers=['EMP ID' , 'EMP NAME' , 'DOB' , 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
    else:
        print("EMPLOYEE DOES NOT EXIST")


def rec_view():
    import mysql.connector
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT* FROM EMPLOYEES")
    myrecords = mycursor.fetchall()
    print("HERE YOU GO :)")
    print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
    view_data = "DATA VIEWED"
    r =requests.get(tga_bot + view_data)
    


def rec_dem():
    print("EXECUTING PROGRAMME.")
    a=int(input("ENTER ID :"))
    import mysql.connector
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
    mycursor = mydb.cursor(buffered=True)
    bwahaa = (a)
    LEL = "SELECT* FROM EMPLOYEES WHERE ID = '%d'"
    mycursor.execute(LEL %  bwahaa)
    z = mycursor.rowcount
    if z == 1:
        mycursor.execute(LEL %  bwahaa)
        W = mycursor.fetchall()
        wow = (tabulate(W, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='github'))
        e=str(input("ENTER DESIGNATION :"))
        f=int(input("ENTER DEPARTMENT NO. :"))
        g=int(input("ENTER SALARY :"))
        data = (e,f,g,a)
        dem_pro = " UPDATE EMPLOYEES SET DESIGNATION = '%s' , DEPT = '%d' , SALARY = '%d' WHERE ID = '%d' "
        mycursor.execute(dem_pro % data)
        mydb.commit()
        print("DONE :)")
        print("THE UPDATED RECORDS :")
        mycursor.execute("SELECT* FROM EMPLOYEES")
        myrecords = mycursor.fetchall()
        change_data = "DATA CHANGED. THE RECORD THAT WAS UPDATED IS: "
        result = str(wow)
        r =requests.get(tga_bot+change_data+'\n''\n'+result+'\n''\n'+"(TO CHECK THE NEW RECORDS , PLEASE LOG INTO THE SYSTEM)")
        print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
    else:
        print("EMPLOYEE DOES NOT EXIST")

def rec_search():
    print("<<<<<<<<<<<<<<<<<<<<<<<<<MENU FOR SEARCHING>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("enter 1 for searching through ID")
    print("enter 2 for searching through NAME")
    print("enter 3 for searching through DOB")
    print("enter 4 for searching through EMAIL")
    print("enter 5 for searching through DESIGNATION")
    print("enter 6 for searching through DEPT")
    print("enter 7 for searching through SALARY")
    serr=int(input("enter a number from the menu : "))
    if serr == 1:
        print("EXECUTING PROGRAMME")
        a=int(input("ENTER ID : "))
        import mysql.connector
        mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
        mycursor = mydb.cursor( buffered=True)
        rec_ser = "SELECT * FROM EMPLOYEES WHERE ID = '%d' " 
        data = (a)
        mycursor.execute(rec_ser % data)
        z = mycursor.rowcount
        if z == 1:
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            id_search = "DATA SEARCHED BY ID"
            r =requests.get(tga_bot+id_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
        else:
            print("EMPLOYEE DOES NOT EXIST")

    elif serr == 2:
        b=str(input("ENTER NAME (BLOCK LETTERS) : "))
        import mysql.connector
        mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
        mycursor = mydb.cursor( buffered=True)
        rec_ser = " SELECT * FROM EMPLOYEES WHERE NAME = '%s' " 
        data = (b)
        mycursor.execute(rec_ser % data)
        z = mycursor.rowcount
        if z == 1:
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            name_search = "DATA SEARCHED BY NAME"
            r =requests.get(tga_bot+name_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
        else:
            print("EMPLOYEE DOES NOT EXIST")
    
       
    elif serr == 3:
        c=str(input("ENTER DOB (YYYY-MM-DD) :"))
        import mysql.connector
        mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
        mycursor = mydb.cursor( buffered=True)
        rec_ser = " SELECT * FROM EMPLOYEES WHERE DOB = '%s' " 
        data = (c)
        mycursor.execute(rec_ser % data)
        z = mycursor.rowcount
        if z ==1:
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            dob_search = "DATA SEARCHED BY DOB"
            r =requests.get(tga_bot+dob_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
        else:
            print("EMPLOYEE DOES NOT EXIST")
            

       
            

    elif serr == 4:
        d=str(input("ENTER EMAIL : "))
        import mysql.connector
        mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
        mycursor = mydb.cursor( buffered=True)
        rec_ser = " SELECT * FROM EMPLOYEES WHERE EMAIL_ADD = '%s' " 
        data = (d)
        mycursor.execute(rec_ser % data)
        z = mycursor.rowcount
        if z ==1:
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            email_search = "DATA SEARCHED BY EMAIL"
            r =requests.get(tga_bot+email_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
        else:
            print("EMPLOYEE DOES NOT EXIST")


    elif serr == 5:
        e=str(input("ENTER DESIGNATION :"))
        import mysql.connector
        mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
        mycursor = mydb.cursor( buffered=True)
        rec_ser = " SELECT * FROM EMPLOYEES WHERE DESIGNATION = '%s' " 
        data = (e)
        mycursor.execute(rec_ser % data)
        z = mycursor.rowcount
        if z ==1:
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            desig_search = "DATA SEARCHED BY DESIGNATION"
            r =requests.get(tga_bot+desig_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
        else:
            print("EMPLOYEE DOES NOT EXIST")


    elif serr == 6:
        f=int(input("ENTER DEPARTMENT NO. :"))
        import mysql.connector
        mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
        mycursor = mydb.cursor( buffered=True)
        rec_ser = " SELECT * FROM EMPLOYEES WHERE DEPT = '%d' " 
        data = (f)
        mycursor.execute(rec_ser % data)
        z = mycursor.rowcount
        if z ==1:
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            dept_search = "DATA SEARCHED BY DEPT.NO"
            r =requests.get(tga_bot+dept_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
        else:
            print("EMPLOYEE DOES NOT EXIST")


    elif serr == 7:
        g=int(input("ENTER SALARY : "))
        print("<<<<<<<<<<RANGE SELECTION>>>>>>>>>>")
        print("ifyou want details for salary #LESS# than the inputted value, enter L or 1")
        print("if you want details for salary #GREATER# than the inputted value, enter G or 2")
        print("if you want details for salary #EQUAL# to the inputted value, enter E or 3")
        print("if you want details for salary #LESS THAN OR EQUAL TO# the inputted value, enter LE or 4")
        print("if you want details for salary #GREATER THAN OR EQUAL TO# than the inputted value, enter GE or 5")

        ter=str(input("enter an option from the menu : "))

        if ter == 'L' or ter =='1':
            import mysql.connector
            mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
            mycursor = mydb.cursor()
            rec_ser = " SELECT * FROM EMPLOYEES WHERE SALARY < '%d' " 
            data = (g)
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            sal1_search = "DATA SEARCHED BY SALARY [LESS THAN] "
            r =requests.get(tga_bot+ sal1_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))
            
            
        elif ter == 'G' or ter =='2':
            import mysql.connector
            mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
            mycursor = mydb.cursor()
            rec_ser = " SELECT * FROM EMPLOYEES WHERE SALARY > '%d' " 
            data = (g)
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            sal1_search = "DATA SEARCHED BY SALARY [GREATER THAN]"
            r =requests.get(tga_bot+ sal1_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))


        elif ter == 'E' or ter =='3':
            import mysql.connector
            mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
            mycursor = mydb.cursor()
            rec_ser = " SELECT * FROM EMPLOYEES WHERE SALARY = '%d' " 
            data = (g)
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            sal1_search = "DATA SEARCHED BY SALARY [EQUAL TO]"
            r =requests.get(tga_bot+ sal1_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))


        elif ter == 'LE' or ter =='4':
            import mysql.connector
            mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
            mycursor = mydb.cursor()
            rec_ser = " SELECT * FROM EMPLOYEES WHERE SALARY <= '%d' " 
            data = (g)
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            sal1_search = "DATA SEARCHED BY SALARY [LESS THAN OR EQUAL TO]"
            r =requests.get(tga_bot+ sal1_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))

        
        elif ter == 'GE' or ter =='5':
            import mysql.connector
            mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "root"  , db = "CS_PROJEKT")
            mycursor = mydb.cursor()
            rec_ser = " SELECT * FROM EMPLOYEES WHERE SALARY >= '%d' " 
            data = (g)
            mycursor.execute(rec_ser % data)
            myrecords = mycursor.fetchall()
            sal1_search = "DATA SEARCHED BY SALARY [GREATER THAN OR EQUAL TO]"
            r =requests.get(tga_bot+ sal1_search)
            print(tabulate(myrecords, headers=['EMP ID', 'EMP NAME', 'DOB', 'EMAIL' , 'DESIGNATION' , 'DEPT. NO' , 'SALARY' , 'GENDER'], tablefmt='fancy_grid'))

    else:
        print("\\\\\\\\PLEASE  READ THE MENU , AND TRY AGAIN////")

if p.lower() == "kkewl":
    
    while True:
        if check ==0:
            r =requests.get(tga_bot+ "LOGGED IN SUCCESSFULLY   (*^▽^*)")
            print(prompt1)
            check = check+1

        

        elif check ==1: 
            print(prompt2)
            

        ch=str(input("enter a number>> "))
        if ch == '1':
            rec_add()
        
               

        elif ch == '2':
            rec_del()


        elif ch == '3':
            rec_dem()

        
        elif ch =='4':
            rec_search()

               
        
        elif ch == '5':
            rec_view()
           
                
        
        elif ch == '6':
            print("HOPE YOU HAVE A GOOD DAY :)")
            r =requests.get(tga_bot+"LOGGED OUT SUCCESSFULLY . HAVE A GOOD DAY   〜(^∇^〜)")
            exit()
            
            
    
    
        else:
            print("WRONG CHOICE , PLEASE TRY AGAIN")
            exit()
    

else:
    print("WRONG PASSWORD. PLEASE TRY AGAIN.")
    r =requests.get(tga_bot+"WRONG PASSWORD ENTERED   (ง •̀_•́)ง ")
