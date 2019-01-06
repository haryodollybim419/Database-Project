import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import time
import os
import platform
from view import*


student_data = ["st", "fc", "hb", "g", "s1", "s2", "s3", "doa", "hoa", "com"]
#insert -> cursor.execute("INSERT INTO <name> WHERE <something> = <something>")
#update -> cursor.exceute("UPDATE <name> SET WHERE <something> = <something>")
#delete -> cursor.execute("DELETE FROM <name> WHERE <something> = <something>")

class Flydatabase:

    def __init__(self, db:str) -> None:
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE  TABLE IF NOT EXISTS flydata_proj(\
        Student_Name TEXT,\
        First_class DATE,Hours_bought INTEGER,\
        Grade NUMERIC, Subject1 TEXT,\
        Subject2 TEXT,\
        Subject3 TEXT,\
        Days_of_attendance DATE,\
        Hours_of_attendance DATE,\
        Comments TEXT)")
        self.conn.commit()

    def view(self)->None:
        self.cursor.execute("SELECT * FROM flydata_proj")
        fly_data = self.cursor.fetchall()
        return fly_data

    def delete(self, name, f_class) -> None:
        val = ("DELETE FROM flydata_proj WHERE Student_Name = '%s' and  First_class = '%s'")\
              %(name, f_class)
        self.cursor.execute(val)
        self.conn.commit()

    def update(self, st:[str], pk:str ) -> None:
        self.cursor.execute("UPDATE flydata_proj SET Student_Name=?, First_class=?,\
                            Hours_bought=?, Grade=?, Subject1=?, Subject2=?, Subject3=?,\
                            Days_of_attendance=?, Hours_of_attendance=?, Comments=? WHERE  Student_Name =?",
                           (st[0], st[1], st[2], st[3],
                            st[4], st[5], st[6], st[7], st[8], st[9], pk))
        self.conn.commit()
        
    def add(self, st:[str]) -> None:
        self.cursor.execute("INSERT INTO flydata_proj VALUES (?,?,?,?,?,?,?,?,?,?)", (st[0], st[1], st[2], st[3],
                            st[4], st[5], st[6], st[7],
                            st[8], st[9]))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



def get_data_popup(val):
    c = Flydatabase(val)
    if len(c.view()) != 0:
        return "Checked"
    else:
        return "Does Not Exist"

        
        

        
class Flydata:
    def __init__(self, master):
         master.title('Fly Data')
         master.resizable(0, 1)
         master.configure(background = '#25818c')

         self.style = ttk.Style()
         self.style.configure('TFrame', background = '#61b8bb')
         self.style.configure('TButton', background = '#e47472', foreground = "#1e482a")
       
         self.style.configure('TLabel', background = '#61b8bb', font = ('Arial', 11))
         self.style.configure('Header.TLabel', font = ('Arial', 18, 'italic'))

  

         self.frame_header = ttk.Frame(master)
         self.frame_header.pack()
        
       
         ttk.Label(self.frame_header, text = '      Fly Data ', style = 'Header.TLabel',
                  width=20).grid(row = 0, column = 1, padx=5, pady=5)

         ttk.Label(self.frame_header, text=' Table ').grid(row = 1, column = 0)
         self.table_entry = ttk.Entry(self.frame_header, width = 25)
         self.table_entry.grid(row=1, column=1)
         
         self.frame_content = ttk.Frame(master)
         self.frame_content.pack()

         ttk.Label(self.frame_content, text = 'Student Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
         ttk.Label(self.frame_content, text = 'Hours Bought:').grid(row = 1, column = 0, padx = 5, sticky = 'sw')
         ttk.Label(self.frame_content, text = 'Grade:').grid(row=2, column=0, padx = 5, sticky = 'sw')
         ttk.Label(self.frame_content, text = 'Subject 1:').grid(row=3, column=0, padx=5, sticky = 'sw')
         ttk.Label(self.frame_content, text = 'Subject 2:').grid(row=4, column=0, padx=5, sticky = 'sw')
         ttk.Label(self.frame_content, text = 'Subject 3:').grid(row=5, column=0, padx=5, sticky = 'sw')
         ttk.Label(self.frame_content, text = 'Days of attendance:').grid(row=6, column=0, padx=5, sticky = 'sw')
         ttk.Label(self.frame_content, text = 'Hours of attendance:').grid(row=7, column=0, padx=5, sticky = 'sw')
         ttk.Label(self.frame_content, text =  'comments:').grid(row =9, column = 0, padx = 5, sticky = 'sw')
         ttk.Label(self.frame_content, text = 'First Class:').grid(row = 8, column = 0, padx = 5, sticky = 'sw')

         self.entry_student_name = ttk.Entry(self.frame_content, width = 25, font = ('Arial', 12))
         self.entry_student_name.grid(row = 0, column = 1, padx = 5)
         self.entry_hours_bought = ttk.Entry(self.frame_content, width = 25, font = ('Arial', 12))
         self.entry_hours_bought.grid(row = 1, column = 1, padx = 5)
         self.entry_grade = ttk.Entry(self.frame_content, width = 25, font = ('Arial', 12))
         self.entry_grade.grid(row = 2, column = 1, padx = 5)
         self.entry_subject_1 = ttk.Entry(self.frame_content, width = 25, font = ('Arial', 12))
         self.entry_subject_1.grid(row = 3, column = 1, padx = 5)
         self.entry_subject_2 = ttk.Entry(self.frame_content, width = 25, font = ('Arial', 12))
         self.entry_subject_2.grid(row = 4, column = 1, padx = 5)
         self.entry_subject_3 = ttk.Entry(self.frame_content, width = 25, font = ('Arial', 12))
         self.entry_subject_3.grid(row = 5, column = 1, padx = 5)
         self.entry_days_of_attendance = ttk.Entry(self.frame_content, width = 25, font = ('Arial', 12))
         self.entry_days_of_attendance.grid(row = 6, column = 1, padx = 5)
         self.entry_hours_of_attendance = ttk.Entry(self.frame_content, width = 25, font = ('Arial', 12))
         self.entry_hours_of_attendance.grid(row = 7, column = 1, padx = 5)
         self.entry_first_class= ttk.Entry(self.frame_content, width = 25, font = ('Arial', 12))
         self.entry_first_class.grid(row=8, column=1)
         self.comments = Text(self.frame_content, width = 55, height = 9, font = ('Arial', 10))
         self.comments.grid(row = 10, column = 0, columnspan = 2, padx = 5)
        
         self.add_button = ttk.Button(self.frame_content,
                                     text = 'Add',
                                     width = 50, command = self.insert_into)
         self.add_button.grid(row = 11, column = 1, padx = 5, pady = 5, sticky = 'e')
         self.delete_button = ttk.Button(self.frame_content, text = 'Delete',
                                        width = 50, command=self.get_it).grid(row=13, column = 1, padx=5, pady=5, sticky='e')
         self.modify_button = ttk.Button(self.frame_content, text = 'Modify',
                                        width = 50, command=self.get_it).grid(row=15, column = 1, padx = 5, pady =5, sticky = 'e')

        
    def insert_into(self):
         self.student_data = [self.entry_student_name.get(),
                  self.entry_first_class.get(),
                  self.entry_hours_bought.get(),
                  self.entry_grade.get(),
                  self.entry_subject_1.get(), self.entry_subject_2.get(),
                  self.entry_subject_3.get(),
                  self.entry_days_of_attendance.get(),
                  self.entry_hours_of_attendance.get(),
                  self.comments.get(1.0, 'end')]
         if self.table_entry.get().endswith(".db"):
            add = Flydatabase(self.table_entry.get())
            add.add(self.student_data)
         else:
            add = Flydatabase(self.table_entry.get()+".db")
            add.add(self.student_data)
            print(add.view())

    def get_it(self):
        self.dialog = simpledialog.askstring("Database Name","Database.db")
        data_bool = get_data_popup(self.dialog)
        if data_bool == "Checked":
            val = View(Tk(),self.dialog)
        else:
            messagebox.showinfo(title = 'The database does not exist', message = 'Try another one!')
        return self.dialog



        
def main():            
    
    root = Tk()
    flydata = Flydata(root)
    root.mainloop()
    
if __name__ == "__main__": main()

    
