import sqlite3

#Create A Database
conn = sqlite3.connect('symptom-med.db')
#Create a Cursor:
c = conn.cursor()

#Create Table Using SQL:
c.execute("""CREATE TABLE symptoms (
		nausea integer,
		chest_pain integer,
		fatigue integer,
		stomach_pain integer,
		anxiety integer,
		sleep_quality integer,
		medication text,
		dt datetime)""")

#Commit Changes
conn.commit()
#Close Connection
conn.close()