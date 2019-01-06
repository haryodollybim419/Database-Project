import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import os
import platform
from flydata import*


class View:
    def __init__(self, master, db):
        self.db = db
        master.title("records")
        master.configure(background = '#25818c', width=500, height=500)

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#61b8bb')
        self.style.configure('TButton', background = '#e47472', foreground = "#1e482a")
        self.style.configure('TLabel', background = '#61b8bb', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'italic'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()


        ttk.Label(self.frame_header, text=' search').grid(row = 1, column = 0)
        self.table_entry = ttk.Entry(self.frame_header, width = 25)
        self.table_entry.grid(row=1, column=1)

        self.get_data = Flydatabase(self.db)
        self.message = Label(self.frame_header,text= '', fg='red')
        self.message.grid(row=2, column =0)
        self.submit = ttk.Button(self.frame_header, text="update", command=self.update)
        self.submit.grid(row=2, column=1, sticky = N)
        self.delete = ttk.Button(self.frame_header, text='delete', command=self.delete)
        self.delete.grid(row=3, column=1, sticky=N)
        self.add = ttk.Button(self.frame_header, text='add', command=self.add)
        self.add.grid(row=4, column = 1, sticky =N)
        self.tree = ttk.Treeview(self.frame_header, columns=("student name",
                                                             "first class",
                                                             "hours bought", "grade","subject 1",
                                                             "subject 2", "subject 3", "days of attend",
                                                             "hours of attend", "comments"))
        
        self.tree.heading('#0', text='student name')
        self.tree.heading('#1', text='first class')
        self.tree.heading('#2', text='hours bought')
        self.tree.heading('#3', text='grade')
        self.tree.heading('#4', text='subject 1')
        self.tree.heading('#5', text='subject 2')
        self.tree.heading('#6', text='subject 3')
        self.tree.heading('#7', text='days of attend')
        self.tree.heading('#8', text='hours of attend')
        self.tree.heading('#9', text='comments')
        self.tree.column('#0', stretch=YES)
        self.tree.column('#1', stretch=YES)
        self.tree.column('#2', stretch=YES)
        self.tree.column('#3', stretch=YES)
        self.tree.column('#4', stretch=YES)
        self.tree.column('#5', stretch=YES)
        self.tree.column('#6', stretch=YES)
        self.tree.column('#7', stretch=YES)
        self.tree.column('#8', stretch=YES)
        self.tree.column('#9', stretch=YES)
        self.tree.grid(row=5, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        self.insert_data()

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

    
    def insert_data(self):
        height = self.get_data.view()
        cpt = 0
        for row in height:
            self.treeview.insert('', 'end', text=str(cpt), values=(row[0], row[1], row[2],
                                                                   row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            cpt += 1
       
    def add(self):
        self.student_data = [self.entry_student_name.get(),
                  self.entry_first_class.get(),
                  self.entry_hours_bought.get(),
                  self.entry_grade.get(),
                  self.entry_subject_1.get(),
                  self.entry_subject_2.get(),
                  self.entry_subject_3.get(),
                  self.entry_days_of_attendance.get(),
                  self.entry_hours_of_attendance.get(),
                  self.comments.get(1.0, 'end')]
        self.get_data.add(self.student_data)
        self.message['text'] = 'record(s) added'
        self.entry_student_name.delete(0, END),
        self.entry_first_class.delete(0, END),
        self.entry_hours_bought.delete(0, END),
        self.entry_grade.delete(0, END),
        self.entry_subject_1.delete(0, END), self.entry_subject_2.delete(0, END),
        self.entry_subject_3.delete(0, END),
        self.entry_days_of_attendance.delete(0, END),
        self.entry_hours_of_attendance.delete(0, END),
        self.comments.get(1.0, 'end')
        self.insert_data()

    def delete(self):
        self.message ['text'] = ' '
        try:
            self.treeview.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'choose a record, please!'
            return 
        name = self.tree.item(self.tree.selection())['text']
        self.message['text'] = ' deleted ! %s'%(name)
        val = self.get_data.view()[int(name)]
        self.get_data.delete(val[0], val[1])
        self.insert_data()
        self.message['text'] = ' deleted ! %s'%(name)

    def update(self):
        self.update = Toplevel()
        self.student = ttk.Label(self.update, text="Student name").grid(row=0, column=0)
        self.first_class= ttk.Label(self.update, text="first class").grid(row=2, column = 0)
        self.hours_bought= ttk.Label(self.update, text="hours bought").grid(row=4, column = 0)
        self.grade= ttk.Label(self.update, text="grade").grid(row=6, column = 0)
        self.subject_1= ttk.Label(self.update, text="subject 1").grid(row=8, column = 0)
        self.subject_2= ttk.Label(self.update, text="subject 2").grid(row=10, column = 0)
        self.subject_3= ttk.Label(self.update, text="subject 3").grid(row=12, column = 0)
        self.days_of_attendance= ttk.Label(self.update, text="days of attendance").grid(row=14, column = 0)
        self.hours_of_attendance= ttk.Label(self.update, text="hours of attendance").grid(row=16, column = 0)
        self.comments_1= ttk.Label(self.update, text="comments").grid(row=18, column = 0)
        
        self.entry_name = ttk.Entry(self.update, width = 25, font = ('Arial', 12))
        self.entry_name.grid(row = 1, column = 0, padx = 5)
        name = self.tree.item(self.tree.selection())['text']
        val = self.get_data.view()[int(name)]
        self.entry_name.insert(0,  val[0])
            
        self.entry_hours= ttk.Entry(self.update, width = 25, font = ('Arial', 12))
        self.entry_hours.grid(row = 3, column = 0, padx = 5)
        self.entry_hours.insert(0, val[1])

        
        self.ent_grade = ttk.Entry(self.update, width = 25, font = ('Arial', 12))
        self.ent_grade.grid(row = 5, column = 0, padx = 5)
        self.ent_grade.insert(0, val[2])


        
        self.ent_subject_1 = ttk.Entry(self.update, width = 25, font = ('Arial', 12))
        self.ent_subject_1.grid(row = 7, column = 0, padx = 5)
        self.ent_subject_1.insert(0, val[3])
        
        self.ent_subject_2 = ttk.Entry(self.update, width = 25, font = ('Arial', 12))
        self.ent_subject_2.grid(row = 9, column = 0, padx = 5)
        self.ent_subject_2.insert(0, val[4])
        
        self.ent_subject_3= ttk.Entry(self.update, width = 25, font = ('Arial', 12))
        self.ent_subject_3.grid(row = 11, column = 0, padx = 5)
        self.ent_subject_3.insert(0, val[5])
        
        self.ent_days_of_attendance = ttk.Entry(self.update, width = 25, font = ('Arial', 12))
        self.ent_days_of_attendance.grid(row = 13, column = 0, padx = 5)
        self.ent_days_of_attendance.insert(0, val[6])
        
        self.ent_hours_of_attendance = ttk.Entry(self.update, width = 25, font = ('Arial', 12))
        self.ent_hours_of_attendance.grid(row = 15, column = 0, padx = 5)
        self.ent_hours_of_attendance.insert(0, val[7])

        self.ent_first_class= ttk.Entry(self.update, width = 25, font = ('Arial', 12))
        self.ent_first_class.grid(row=17, column=0)
        self.ent_first_class.insert(0, val[8])
        
        self.ent_comments = Text(self.update, width = 55, height = 9, font = ('Arial', 10))
        self.ent_comments.grid(row = 19, column = 0, columnspan = 2, padx = 5)
        self.ent_comments.insert('1.0', val[9])

        ttk.Button(self.update, text="update", command=lambda: self.update_button(self.entry_name.get(),\
                                                                             self.entry_hours.get(), self.ent_grade.get(), self.ent_subject_1.get(),
                                                                             self.ent_subject_2.get(), self.ent_subject_3.get(), self.ent_days_of_attendance.get(),
                                                                             self.ent_hours_of_attendance.get(), self.ent_first_class.get(), self.ent_comments.get('1.0', END), val[0])).grid(row = 22, column=1)


        self.update.mainloop()

    def update_button(self, nm, hr, gr, sb1,sb2,sb3,da,ha,fc,c, pk):
        self.get_data.update([nm, hr, gr, sb1,sb2,sb3,da,ha,fc,c] ,pk)
        self.insert_data()
        name = self.tree.item(self.tree.selection())['text']
        val = self.get_data.view()[int(name)]
        self.message['text'] = '  %s student %s as being updated! '%(name, val[0])

        
def main():            
    root = Tk()
    view = View(root, Flydata(Tk()).get_it())
    root.mainloop()
    
if __name__ == "__main__":
    main()
        
