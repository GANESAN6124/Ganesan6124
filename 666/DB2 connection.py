from enum import Flag
import ibm_db
conn =ibm_db.connect("DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hgt43191;PWD=pG1XZqjaI1xcDGA8",'','')
sql='SELECT * FROM products'
stmt = ibm_db.exec_immediate(conn, sql)
# dictionary=ibm_db.fetch_row(stmt)
# while dictionary!=False:
#     # print("the id is :",dictionary[0])
#     print("the name is :",dictionary[0])
#     dictionary=ibm_db.fetch_row(stmt) 
#immediately connect to server with out security

#num_rows() retrun number of rows changed or affected
#bind_param -> is take the stmt and pick position(?) and place the value like input(name =1)
#print("Number of affected rows:", ibm_db.num_rows(stmt))
name=2
address="elampillai"
city='salem'#
pin=61241910


sql="SELECT * FROM products WHERE name=?"  
stmt=ibm_db.prepare(conn, sql)
ibm_db.bind_param(stmt,1,name)
ibm_db.execute(stmt)
account=ibm_db.fetch_assoc(stmt)
print(account)

if account:
    print("yes it is")
else:
    insert_sql='INSERT INTO products VALUES (?,?,?,?)'
    prep_stmt=ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, name)
    ibm_db.bind_param(prep_stmt, 2, address)
    ibm_db.bind_param(prep_stmt, 3, city)
    ibm_db.bind_param(prep_stmt, 4, pin)
    ibm_db.execute(prep_stmt)
    

print(conn)
print("successfully connected")
