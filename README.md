# meddb
A Medication-Symptom Database built using SQL and Tkinter

### Getting Started
1. Make sure you have Python 3 Installed
2. Run db_create.py to create a new SQL database
3. Run db_gui.py to add, remove, view and delete records
  
### Adding A Record
- Enter values into the fields next to each parameter
- Click "Add Record To Database"
- This will add an entry with the parameter values supplied, current date time and record id #

### Viewing / Deleting Records
- Click "Show Records" to see a list of your entries
- The last value in each records represents the record id #
- To delete a record, enter this value in the "ID #" field and click "Delete Record"

### Editing A Previous Record
- Enter the record id # into the "ID #" field and click "Edit Record"
- You will be taken to a window where you can update the values for each parameter
- Click "Save Record" when you are finished

### Built With
* [SQLite3](https://www.sqlite.org/index.html) - SQLite3
* [tkinter](https://docs.python.org/3/library/tkinter.html) - Python GUI
  
### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Credits
* [freeCodeCamp.org](https://www.youtube.com/watch?v=YXPyB4XeYLA) Tkinter Course
