# meddb
A Medication-Symptom Database built using SQL and Tkinter

### Getting Started
1) Make sure you have Python 3 Installed
2) Run db_create.py to create a new SQL database
3) Run db_gui.py to add, remove, view and delete records
  
### Adding A Record
1) Enter values into the fields next to each parameter
2) Click "Add Record To Database"
3) This will add an entry with the parameter values supplied, current date time and record id #

### Viewing / Deleting Records
1) Click "Show Records" to see a list of your entries
2) The last value in each records represents the record id #
3) To delete a record, enter this value in the "ID #" field and click "Delete Record"

### Editing A Previous Record
1) Enter the record id # into the "ID #" field and click "Edit Record"
2) You will be taken to a window where you can update the values for each parameter
3) Click "Save Record" when you are finished

### Built With
* [SQLite3](https://www.sqlite.org/index.html) - SQLite3
* [tkinter](https://docs.python.org/3/library/tkinter.html) - Python GUI
  
### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Credits
* [freeCodeCamp.org](https://www.youtube.com/watch?v=YXPyB4XeYLA) Tkinter Course
