import cx_Oracle
import getpass

username=input("Username: ")
pswd = getpass.getpass('Password: ')
con=cx_Oracle.connect(username,pswd,'DB3')
con.close()
con=cx_Oracle.connect(username,pswd,'192.168.0.30:1521/DB3')
con.close()



