import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name,user_name,user_password):
	connection=None
	try:
		connection=mysql.connector.connect(host=host_name,user=user_name,password=user_password)
		print("Mysql connection was successfull")
	except Error as err:
		print(f"Error:'{err}'")
	return connection
pw="root"
db="intern" #write your database name
connection=create_server_connection("localhost","root","root")

def create_database(connection,query):
 	cursor=connection.cursor()
 	try:
 		cursor.execute(query)
 		print("Database Create successfully")
 	except Error as err:
 		print(f"Error: '{err}'")
create_database_query="create database intern"
create_database(connection,create_database_query)

def create_db_connection(host_name,user_name,user_password,db_name):
	connection=None
	try:
		connection=mysql.connector.connect(host=host_name,user=user_name,password=user_password,database=db_name)
		
	except Error as err:
		print(f"Error: '{err}'")
	return connection

def execute_query(connection,query):
	cursor=connection.cursor()
	try:
		cursor.execute(query)
		connection.commit()
		print("query was successfull")
	except Error as err:
		print(f"Error: '{err}'")
 
def read_query(connection,query):
	cursor=connection.cursor()
	result=None
	try:
		cursor.execute(query)
		result=cursor.fetchall()
		return result
	except Error as err:
		print(f"Error : '{err}'")

q1="""
select * from customer_details;
"""
connection=create_db_connection("localhost","root",pw,db)
results=read_query(connection,q1)
for result in results:
	print(result)


q2="""
select cname,review  from customer_details where review=5;
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q2)
print('Excellent review')
for result in result1:
	print(result)

q3="""
select cname,review  from customer_details where review=4;
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q3)
print('good review')
for result in result1:
	print(result)

q4="""
select cname,review  from customer_details where review=3;
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q4)
print('Average review')
for result in result1:
	print(result)
 
q5="""
select cname,review  from customer_details where review=2;
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q5)
print('Below Average review')
for result in result1:
	print(result)
  
q6="""
select cname,review  from customer_details where review=1;
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q6)
print('Poor review')
for result in result1:
	print(result)
  
q7="""
select cname,review  from customer_details order by review;
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q7 )
print('From Poor to Excellent review')
for result in result1:
	print(result)
  
q8="""
select cname,review  from customer_details where pname='perfume';
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q8 )
print('Review on Perfume')
for result in result1:
	print(result)
  

q9="""
select cname,review  from customer_details where pname='water bottles';
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q9 )
print('Review on Water Bottle')
for result in result1:
	print(result)  

q10="""
select cname,review  from customer_details where pname='watch';
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q10 )
print('Review on Watch')
for result in result1:
	print(result)	

q11="""
select cname,review  from customer_details where pname='mask';
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q11 )
print('Review on mask')
for result in result1:
	print(result)	
  
q12="""
select cname,review  from customer_details where pname='sanitizer';
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q12 )
print('Review on sanitizer')
for result in result1:
	print(result)	

q13="""
select cname,review  from customer_details where pname='lipstick';
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q13 )
print('Review on lipstick')
for result in result1:
	print(result)
  
q14="""
select cname,review  from customer_details where pname='handwash';
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q14 )
print('Review on handwash')
for result in result1:
	print(result)	
  
q15="""
select cname,pname,review  from customer_details where Year(rdate)='2019';
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q15 )
print('product review in the year of 2019')
for result in result1:
	print(result)	

q16="""
select cname,pname,review  from customer_details where Year(rdate)='2020';
"""
connection=create_db_connection("localhost","root",pw,db)
result1=read_query(connection,q16 )
print('product review in the year of 2020')
for result in result1:
	print(result)	
  
