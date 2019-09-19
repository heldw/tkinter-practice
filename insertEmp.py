
# HW 3: Instert an Employee into the testdb employee table

# import needed libraries
import os
import pymysql as mdb
import tkinter as tk
from tkinter import messagebox

# define a  class to set up the gui
class App(object):
    def __init__(self, window):

        # set window title
        window.wm_title("Insert an Employee")

        # set the currrent row to zero
        self.current_row=0

        #first name
        self.fname_label = tk.Label(window, text= "First Name: ")
        self.fname_label.grid(row= self.current_row, column=0)
        self.fname_text = tk.StringVar()
        self.fname_entry = tk.Entry(window, textvariable=self.fname_text)
        self.fname_entry.grid(row=self.current_row, column=1)
        self.current_row+=1

        #last name
        self.lname_label = tk.Label(window, text= "Last Name: ")
        self.lname_label.grid(row= self.current_row, column=0)
        self.lname_text = tk.StringVar()
        self.lname_entry = tk.Entry(window, textvariable=self.lname_text)
        self.lname_entry.grid(row=self.current_row, column=1)
        self.current_row+=1

        #age
        self.age_label = tk.Label(window, text= "Age: ")
        self.age_label.grid(row= self.current_row, column=0)
        self.age_text = tk.IntVar()
        self.age_entry = tk.Entry(window, textvariable=self.age_text)
        self.age_entry.grid(row=self.current_row, column=1)
        self.current_row+=1

        #sex
        self.sex_label = tk.Label(window, text= "Sex: ")
        self.sex_label.grid(row= self.current_row, column=0)
        self.sex_text = tk.StringVar()
        self.sex_entry = tk.Entry(window, textvariable=self.sex_text)
        self.sex_entry.grid(row=self.current_row, column=1)
        self.current_row+=1

        #Income
        self.income_label = tk.Label(window, text= "Income: ")
        self.income_label.grid(row= self.current_row, column=0)
        self.income_text = tk.IntVar()
        self.income_entry = tk.Entry(window, textvariable=self.income_text)
        self.income_entry.grid(row=self.current_row, column=1)
        self.current_row+=1

        # send query button
        self.query_button = tk.Button(window, text= "Send Query")
        self.query_button.configure(command=self.sendQuery)
        self.query_button.grid(row=self.current_row, column=0, columnspan=2)
        self.current_row+=1


        #self.message
        

    def sendQuery(self):

        # store user input into local variable
        fname = self.fname_text.get()
        lname = self.lname_text.get()
        age = self.age_text.get()
        sex = self.sex_text.get()
        income = self.income_text.get()
        
        #connect to the db
        db = mdb.connect("localhost", "testuser", "test123", "testdb")
        # prepare a cursor object user cursor() method
        cursor = db.cursor()
         # drop table if it already exists using execute() method
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

        #create table as per requirement
        self.query = """ create table employee (
            first_name char(20) not null,
            last_name char(20),
            age int,
            sex char(1),
            income float)"""

        cursor.execute(self.query)

        # execute DML statements to insery data
        self.query = """INSERT INTO employee(first_name,last_name, age, sex, income)
                        VALUES('%s', '%s', %d, '%s', %d)""" %(fname, lname, age, sex, income)


        try:
            # execute the SQL command
            cursor.execute(self.query)
           # commit changes to db
            db.commit()

        except:
            # rollback in case there is any error
            db.rolllback()
            
        #Tell the user their insert was successful
        messagebox.showinfo('Success!', 'The New Employee has been successfully added to the Table')
    
# define main class implement execution loop
def main():
    window = tk.Tk()
    start = App(window)
    window.mainloop()

# run the main function
if __name__=="__main__":
    main()
