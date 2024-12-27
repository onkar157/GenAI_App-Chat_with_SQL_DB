import sqlite3

#connecting sqlite
connection = sqlite3.connect("student.db")

#cursor object to insert record
cursor=connection.cursor()

#create table

table_info=""" 
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)"""

cursor.execute(table_info)

#inserting record

cursor.execute('''Insert Into STUDENT values('Jacob','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values('Liam','Data Science','B',78)''')
cursor.execute('''Insert Into STUDENT values('Olivia','Data Science','A',89)''')
cursor.execute('''Insert Into STUDENT values('Emma','Cyber Security','A',95)''')
cursor.execute('''Insert Into STUDENT values('Noah','Data Science','C',67)''')
cursor.execute('''Insert Into STUDENT values('Sophia','Cyber Security','B',88)''')
cursor.execute('''Insert Into STUDENT values('Mason','AI','A',92)''')
cursor.execute('''Insert Into STUDENT values('Ethan','AI','C',76)''')
cursor.execute('''Insert Into STUDENT values('Isabella','Cyber Security','A',85)''')
cursor.execute('''Insert Into STUDENT values('Ava','Data Science','B',70)''')
cursor.execute('''Insert Into STUDENT values('William','DEVOPS','B',60)''')
cursor.execute('''Insert Into STUDENT values('James','Data Science','A',99)''')
cursor.execute('''Insert Into STUDENT values('Benjamin','AI','A',72)''')
cursor.execute('''Insert Into STUDENT values('Lucas','Cyber Security','C',68)''')
cursor.execute('''Insert Into STUDENT values('Henry','DEVOPS','A',85)''')
cursor.execute('''Insert Into STUDENT values('Alexander','Data Science','C',75)''')
cursor.execute('''Insert Into STUDENT values('Charlotte','Cyber Security','B',90)''')
cursor.execute('''Insert Into STUDENT values('Amelia','AI','A',88)''')
cursor.execute('''Insert Into STUDENT values('Mia','Data Science','B',73)''')
cursor.execute('''Insert Into STUDENT values('Harper','DEVOPS','C',62)''')
cursor.execute('''Insert Into STUDENT values('Evelyn','Data Science','A',84)''')
cursor.execute('''Insert Into STUDENT values('Abigail','AI','B',93)''')
cursor.execute('''Insert Into STUDENT values('Ella','Cyber Security','A',91)''')
cursor.execute('''Insert Into STUDENT values('Aiden','DEVOPS','A',66)''')
cursor.execute('''Insert Into STUDENT values('Logan','Data Science','C',69)''')
cursor.execute('''Insert Into STUDENT values('Luna','AI','B',89)''')
cursor.execute('''Insert Into STUDENT values('Zoey','Cyber Security','C',87)''')
cursor.execute('''Insert Into STUDENT values('Aria','Data Science','A',94)''')
cursor.execute('''Insert Into STUDENT values('Jackson','DEVOPS','B',58)''')
cursor.execute('''Insert Into STUDENT values('Levi','Data Science','C',63)''')
cursor.execute('''Insert Into STUDENT values('Sebastian','Cyber Security','A',96)''')
cursor.execute('''Insert Into STUDENT values('Gabriel','AI','C',77)''')
cursor.execute('''Insert Into STUDENT values('Matthew','DEVOPS','A',82)''')
cursor.execute('''Insert Into STUDENT values('David','Data Science','B',74)''')
cursor.execute('''Insert Into STUDENT values('Joseph','Cyber Security','C',80)''')
cursor.execute('''Insert Into STUDENT values('Carter','AI','A',65)''')
cursor.execute('''Insert Into STUDENT values('Owen','Data Science','C',81)''')
cursor.execute('''Insert Into STUDENT values('Wyatt','DEVOPS','A',78)''')
cursor.execute('''Insert Into STUDENT values('Jack','AI','B',92)''')
cursor.execute('''Insert Into STUDENT values('Daniel','Cyber Security','B',83)''')
cursor.execute('''Insert Into STUDENT values('Grace','Data Science','A',97)''')
cursor.execute('''Insert Into STUDENT values('Chloe','AI','C',71)''')
cursor.execute('''Insert Into STUDENT values('Lily','Cyber Security','A',86)''')
cursor.execute('''Insert Into STUDENT values('Hannah','Data Science','B',88)''')
cursor.execute('''Insert Into STUDENT values('Zoe','DEVOPS','C',79)''')
cursor.execute('''Insert Into STUDENT values('Nathan','AI','A',90)''')
cursor.execute('''Insert Into STUDENT values('Caleb','Cyber Security','B',68)''')


#display all records
print("The inserted records are")

data=cursor.execute('''select * from STUDENT''')
for i in data:
    print(i)

## Commit your changes in the database
connection.commit()
connection.close()