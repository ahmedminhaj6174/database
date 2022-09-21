#!/usr/bin/env python
# coding: utf-8

# In[250]:


import mysql.connector
import pandas as pd
import sys


# In[251]:


mydb = mysql.connector.connect(
    
    host="localhost",
#     Enter your Mysql connection username
    user="root",
#     Enter your Mysql connection password
    passwd="",
    database="LAS_PAL"
)

print(mydb)


# In[252]:


def Retrieve():
    
    
    n = input("Enter Table name:")

    cur = mydb.cursor()
            
    cur.execute("select * from `{}`;".format(n))

    myresult = cur.fetchall()

    for row in myresult:
        print(row)


# In[253]:


def Average():
    
    cur = mydb.cursor()
    
    table = input("Please enter the name of the table: ")
    col = input("Please enter the colname: ")
    
    sql = "select avg("+col+") from "+table
    
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        print(row)
    


# In[261]:


def Insert():
    
    user= input("Enter Table name")
    
    if(user == "Room"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        roomID = int(input("Enter roomID:")) 
        roomType = input("Enter roomType:")
        
        cur = mydb.cursor()
        sql = "insert into Room(roomID, roomType) values(%s, %s)"

        val = (roomID, roomType)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
        
    elif (user =="Physician"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        physicianID = int(input("Enter physicianID:")) 
        name = input("Enter name:")
        position = input("Enter position:")
        ssn = int(input("Enter ssn:"))
        
        cur = mydb.cursor()
        sql = "insert into Physician(physicianID, name, position, ssn) values(%s, %s, %s, %s)"

        val = (physicianID, name, position, ssn)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
            
    elif (user =="Department"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        deptID = int(input("Enter deptID:")) 
        name = input("Enter name:")
        headID = int(input("Enter headID:"))
        
        cur = mydb.cursor()
        sql = "insert into Department(deptID, name, headID) values(%s, %s, %s)"

        val = (deptID, name, headID)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
            
    elif (user =="AffiliatedWith"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        physicianID = int(input("Enter physicianID:")) 
        departmentID = int(input("Enter departmentID:"))
        
        cur = mydb.cursor()
        sql = "insert into AffiliatedWith(physicianID, departmentID) values(%s, %s)"

        val = (physicianID, departmentID)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
            
    elif (user =="Procedure"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        procID = int(input("Enter procID:")) 
        name = input("Enter name:")
        cost = float(input("Enter headID:"))
        
        cur = mydb.cursor()
        sql = "insert into `Procedure`(procID, name, cost) values(%s, %s, %s)"

        val = (procID, name, cost)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
    
    elif (user =="Patient"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        patientID = int(input("Enter patientID:"))
        ssn = int(input("Enter ssn:"))
        name = input("Enter name:")
        address = input("Enter address:")
        dob = input("Enter dob yy-mm-dd:")
        phone = input("Enter phone:")
        insuranceNumber = int(input("Enter insuranceNumber:")) 
        primaryPhysID = int(input("Enter primaryPhysID:"))
        
        
        cur = mydb.cursor()
        sql = "insert into Patient(patientID, ssn, name, address, dob, phone, insuranceNumber, primaryPhysID) values(%s, %s, %s, %s, %s, %s, %s, %s)"

        val = (patientID, ssn, name, address, dob, phone, insuranceNumber, primaryPhysID)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
            
    elif (user =="Nurse"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        nurseID = int(input("Enter nurseID:")) 
        name = input("Enter name:")
        position = input("Enter position:")
        ssn = int(input("Enter ssn:"))
        
        cur = mydb.cursor()
        sql = "insert into Nurse(nurseID, name, position, ssn) values(%s, %s, %s, %s)"

        val = (nurseID, name, position, ssn)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
    elif (user =="Medication"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        medID = int(input("Enter medID:")) 
        name = input("Enter name:")
        
        cur = mydb.cursor()
        sql = "insert into Medication(procID, name) values(%s, %s)"

        val = (procID, name)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
            
    elif (user =="Prescribes"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        physicianID = int(input("Enter physicianID:"))
        patientID = int(input("Enter patientID:"))
        medicationID = int(input("Enter medicationID:")) 
        prescribedDate = input("Enter prescribedDate yy-mm-dd:")
        dose = input("Enter dose:")
        
        
        cur = mydb.cursor()
        sql = "insert into Prescribes(physicianID, patientID, medicationID, prescribedDate, dose) values(%s, %s, %s, %s, %s)"

        val = (physicianID, patientID, medicationID, prescribedDate, dose)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
            
    elif (user =="Stay"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        stayID = int(input("Enter stayID:"))
        patientID = int(input("Enter patientID:"))
        roomID = int(input("Enter roomID:")) 
        startDate = input("Enter startDate yy-mm-dd:")
        endDate = input("Enter endDate yy-mm-dd:")
        
        
        cur = mydb.cursor()
        sql = "insert into Stay(stayID, patientID, roomID, startDate, endDate) values(%s, %s, %s, %s, %s)"

        val = (stayID, patientID, roomID, startDate, endDate)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
            
    elif (user =="Undergoes"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        patientID = int(input("Enter patientID:"))
        procedureID = int(input("Enter procedureID:"))
        stayID = int(input("Enter stayID:"))
        procDate = input("Enter procDate yy-mm-dd:")
        physicianID = int(input("Enter physicianID:")) 
        nurseID = int(input("Enter nurseID:"))
        
        
        cur = mydb.cursor()
        sql = "insert into Undergoes(patientID, procedureID, stayID, procDate, physicianID, nurseID) values(%s, %s, %s, %s, %s, %s)"

        val = (patientID, procedureID, stayID, procDate, physicianID, nurseID)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
            
    elif (user =="OnCall"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        nurseID = int(input("Enter nurseID:")) 
        startDate = input("Enter startDate yy-mm-dd:")
        endDate = input("Enter endDate yy-mm-dd:")
        
        cur = mydb.cursor()
        sql = "insert into OnCall(nurseID, startDate, endDate) values(%s, %s, %s)"

        val = (nurseID, startDate, endDate)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
            
    elif (user =="Appointment"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        appID = int(input("Enter appID:"))
        patientID = int(input("Enter patientID:"))
        nurseID = int(input("Enter nurseID:"))
        physicianID = int(input("Enter physicianID:")) 
        startDateTime = input("Enter startDateTime yy-mm-dd:")
        endDateTime = input("Enter endDateTime yy-mm-dd:")
        
        
        cur = mydb.cursor()
        sql = "insert into Appointment(appID, patientID, nurseID, physicianID, startDateTime, endDateTime) values(%s, %s, %s, %s, %s, %s)"

        val = (appID, patientID, nurseID, physicianID, startDateTime, endDateTime)
        try:
            cur.execute(sql, val)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record inserted!")
        mydb.close()
            
    
    else:
        print("Error Incorrect table name")
    


# In[262]:


def Delete():
    user= input("Enter Table name to delete a row")
    
    if(user == "Room"):        

        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        roomID = int(input("Enter roomID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from Room where roomID={}".format(roomID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
        
    elif (user =="Physician"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        physicianID = int(input("Enter physicianID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from Physician where physicianID={}".format(physicianID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
            
    elif (user =="Department"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        deptID = int(input("Enter deptID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from Department where deptID={}".format(deptID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
            
    elif (user =="AffiliatedWith"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        physicianID = int(input("Enter physicianID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from AffiliatedWith where physicianID={}".format(physicianID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
            
    elif (user =="Procedure"):
            cur = mydb.cursor()
            
            cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

            myresult = cur.fetchall()

            for row in myresult:
                print(row)
            
            procID = int(input("Enter procID to delete a row:")) 
        
            cur = mydb.cursor()
            sql = "delete from `Procedure` where procID={}".format(procID)

            try:
                cur.execute(sql)

                mydb.commit()
            except:
                mydb.rollback()
            print(cur.rowcount, "record deleted!")
            mydb.close()
            
    
    elif (user =="Patient"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        patientID = int(input("Enter patientID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from Patient where patientID={}".format(patientID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
            
    elif (user =="Nurse"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        nurseID = int(input("Enter nurseID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from Nurse where nurseID={}".format(nurseID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
    elif (user =="Medication"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        medID = int(input("Enter medID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from Medication where medID={}".format(medID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
            
    elif (user =="Prescribes"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        medID = int(input("Enter medID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from Prescribes where medID={}".format(medID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
            
    elif (user =="Stay"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        stayID = int(input("Enter stayID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from Stay where stayID={}".format(stayID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
            
    elif (user =="Undergoes"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        patientID = int(input("Enter patientID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from Undergoes where patientID={}".format(patientID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
            
    elif (user =="OnCall"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        nurseID = int(input("Enter nurseID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from OnCall where nurseID={}".format(nurseID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
            
    elif (user =="Appointment"):
        cur = mydb.cursor()
            
        cur.execute("SHOW COLUMNS FROM `{}`;".format(user))

        myresult = cur.fetchall()

        for row in myresult:
            print(row)
            
        appID = int(input("Enter appID to delete a row:")) 
        
        cur = mydb.cursor()
        sql = "delete from Appointment where appID={}".format(appID)

        try:
            cur.execute(sql)

            mydb.commit()
        except:
            mydb.rollback()
        print(cur.rowcount, "record deleted!")
        mydb.close()
            
    
    else:
        print("Error Incorrect table name")
    


# In[263]:


if __name__ == '__main__':
    
    print("Functionalities: 'Retrieve','Average','Insert', 'Delete'")
    
    user= input("Enter your desired functionality")
    
    if(user == "Retrieve"):
        Retrieve()
        
    elif (user =="Average"):
            Average()
            
    elif (user =="Insert"):
            Insert()
            
    elif (user =="Delete"):
            Delete()
    
    else:
        print("Error entered wrong functionality ")
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




