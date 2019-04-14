import cx_Oracle
tns=cx_Oracle.makedsn('192.168.0.30',1521,'DB3')
con=cx_Oracle.connect('systemx','oracle123',tns)
