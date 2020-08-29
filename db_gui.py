from tkinter import *
from datetime import datetime
import sqlite3

root = Tk()
root.title("Symptom-Medication Database")
root.geometry("400x600")

#Create A Database
conn = sqlite3.connect('symptom-med.db')
#Create a Cursor:
c = conn.cursor()

def save():
	#Connect To Database
	conn = sqlite3.connect('symptom-med.db')
	#Create a Cursor:
	c = conn.cursor()
	record_id = delete_box.get()
	c.execute("""UPDATE symptoms SET
		nausea = :nausea,
		chest_pain = :chestpain,
		fatigue = :fatigue,
		stomach_pain = :stomachpain,
		anxiety = :anxiety,
		sleep_quality = :sleepquality
		medication = :medication
		dt = :dt
		WHERE oid = :oid
		WHERE dt = :dt""",
		{'nausea' : n_name_editor.get(),
		'chestpain': cp_name_editor.get(),
		'fatigue' : f_name_editor.get(),
		'stomachpain' : sp_name_editor.get(),
		'anxiety' : a_name_editor.get(),
		'sleepquality' : sq_name_editor.get(),
		'medication' : m_name_editor.get(),
		'dt' : datetime.today(),
		'oid': record_id,
		})

	#Commit Changes
	conn.commit()
	#Close Connection
	conn.close()
	editor.destroy()

# Edit Record Function
def edit():
	global editor
	editor = Tk()
	editor.title("Update A Record")
	editor.geometry("400x200")
	#Connect To Database
	conn = sqlite3.connect('symptom-med.db')
	#Create a Cursor:
	c = conn.cursor()
	record_id = delete_box.get()
	#Query The DB
	c.execute("SELECT *, oid FROM symptoms WHERE oid = " + record_id)
	records = c.fetchall()	
	#Commit Changes
	conn.commit()
	#Close Connection
	conn.close()
	#Global Vars
	global n_name_editor, cp_name_editor, f_name_editor, sp_name_editor, sq_name_editor, m_name_editor
	#Create Text Boxes
	n_name_editor = Entry(editor,width=30)
	n_name_editor.grid(row=0,column=1, padx=20, pady=(20,0)) #tuple adds 10 to the top, no padding to the bottom
	cp_name_editor = Entry(editor,width=30)
	cp_name_editor.grid(row=1,column=1, padx=20)
	f_name_editor = Entry(editor,width=30)
	f_name_editor.grid(row=2,column=1, padx=20)
	sp_name_editor = Entry(editor,width=30)
	sp_name_editor.grid(row=3,column=1, padx=20)
	a_name_editor = Entry(editor,width=30)
	a_name_editor.grid(row=3,column=1, padx=20)
	sq_name_editor = Entry(editor,width=30)
	sq_name_editor.grid(row=4,column=1, padx=20)
	m_name_editor = Entry(editor,width=30)
	m_name_editor.grid(row=5,column=1, padx=20)

	#Create Text Box Labels
	n_name_label = Label(editor, text="Nausea")
	n_name_label.grid(row=0, column=0, pady=(20,0))
	cp_name_label = Label(editor, text="Chest Pain")
	cp_name_label.grid(row=1, column=0)
	f_name_label = Label(editor, text="Fatigue")
	f_name_label.grid(row=2, column=0)
	sp_name_label = Label(editor, text="Stomach Pain")
	sp_name_label.grid(row=3, column=0)
	a_name_label = Label(editor, text="Anxiety")
	a_name_label.grid(row=3, column=0)
	sq_name_label = Label(editor, text="Sleep Quality")
	sq_name_label.grid(row=4, column=0)
	m_name_label = Label(editor, text="Medication")
	m_name_label.grid(row=5, column=0)

	# Loop Thru Results
	for record in records:
		n_name_editor.insert(0,record[0])
		cp_name_editor.insert(0,record[1])
		f_name_editor.insert(0,record[2])
		sp_name_editor.insert(0,record[3])
		a_name_editor.insert(0,record[4])
		sq_name_editor.insert(0,record[5])
		m_name_editor.insert(0,record[6])

	#Create Save Button
	save_btn = Button(editor, text="Save Record", command=save)
	save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=142)

# Delete Record Function
def delete():
	#Connect To Database
	conn = sqlite3.connect('symptom-med.db')
	#Create a Cursor:
	c = conn.cursor()
	#Delete a Record:
	c.execute("DELETE from symptoms WHERE oid= " + delete_box.get())
	#Commit Changes
	conn.commit()
	#Close Connection
	conn.close()

#Submit Function for DB
def submit():
	#Connect To Database
	conn = sqlite3.connect('symptom-med.db')
	#Create a Cursor:
	c = conn.cursor()
	#Insert Into Table
	c.execute("INSERT INTO symptoms VALUES (:n_name, :cp_name, :f_name, :sp_name, :a_name, :sq_name, :m_name, :dt)", 
			{
			'n_name': n_name.get(),
			'cp_name': cp_name.get(),
			'f_name': f_name.get(),
			'sp_name': sp_name.get(),
			'a_name': a_name.get(),
			'sq_name': sq_name.get(),
			'm_name': m_name.get(),
			'dt' : datetime.today()
			})

	#Commit Changes
	conn.commit()
	#Close Connection
	conn.close()

	# Clear The Text Boxes
	n_name.delete(0, END)
	cp_name.delete(0, END)
	f_name.delete(0, END)
	sp_name.delete(0, END)
	a_name.delete(0, END)
	sq_name.delete(0, END)
	m_name.delete(0, END)

# Create Query Function
def query():
	#Connect To Database
	conn = sqlite3.connect('symptom-med.db')
	#Create a Cursor:
	c = conn.cursor()
	#Query The DB
	c.execute("SELECT *, oid FROM symptoms")
	records = c.fetchall()
	#print(records)
	#Loop Thru Results
	print_records = ''
	for record in records:
		print_records += str(record) + '\n'

	query_lbl = Label(root, text=print_records)
	query_lbl.grid(row=9, column=0, columnspan=2)
	#Commit Changes
	conn.commit()
	#Close Connection
	conn.close()

#Create Text Boxes
n_name = Entry(root,width=30)
n_name.grid(row=0,column=1, padx=20, pady=(20,0)) #tuple adds 10 to the top, no padding to the bottom
cp_name = Entry(root,width=30)
cp_name.grid(row=1,column=1, padx=20)
f_name = Entry(root,width=30)
f_name.grid(row=2,column=1, padx=20)
sp_name = Entry(root,width=30)
sp_name.grid(row=3,column=1, padx=20)
a_name = Entry(root,width=30)
a_name.grid(row=4,column=1, padx=20)
sq_name = Entry(root,width=30)
sq_name.grid(row=5,column=1, padx=20)
m_name = Entry(root,width=30)
m_name.grid(row=6,column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=10,column=1)

#Create Text Box Labels
n_name_label = Label(root, text="Nausea")
n_name_label.grid(row=0, column=0, pady=(20,0))
cp_name_label = Label(root, text="Chest Pain")
cp_name_label.grid(row=1, column=0)
f_name_label = Label(root, text="Fatigue")
f_name_label.grid(row=2, column=0)
sp_name_label = Label(root, text="Stomach Pain")
sp_name_label.grid(row=3, column=0)
a_name_label = Label(root, text="Anxiety")
a_name_label.grid(row=4, column=0)
sq_name_label = Label(root, text="Sleep Quality")
sq_name_label.grid(row=5, column=0)
m_name_label = Label(root, text="Medication")
m_name_label.grid(row=6, column=0)
delete_box_lbl = Label(root, text="ID #")
delete_box_lbl.grid(row=10,column=0)

#Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

#Create Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create A Delete Button
dlt_btn = Button(root, text="Delete Record", command=delete)
dlt_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create an Update Button
upd_btn = Button(root, text="Edit Record", command=edit)
upd_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=142)

#Commit Changes
conn.commit()
#Close Connection
conn.close()

root.mainloop()