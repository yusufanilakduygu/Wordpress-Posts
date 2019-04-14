import cx_Oracle
import getpass

while(1==1):
    username=input("Username: ")
    pswd = getpass.getpass('Password: ')
    try:
        tns=cx_Oracle.makedsn('192.168.0.30',1521,'DB3')
        con=cx_Oracle.connect(username,pswd,tns)
    except cx_Oracle.DatabaseError as e:
        print("""
        Database Connection Error ; 
        Please Enter credentials one more time """ + str(e.args[0]))
        continue
    break
print("Connected to the Database successfully")