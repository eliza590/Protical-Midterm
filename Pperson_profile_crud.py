import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title ("Student Management System")
root.geometry("700x500")

title_label = tk.label(
     root,
     text = "Student Management System",
     foot = ('arial',18, "bold")
     )

title_label.pack(pady = 10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(
     input_frame,
     text = "Name:"
     ).grid(row = 0, column = 0, padx = 5, pady = 5)

name_entry = tk.Entry(input_frame,width=30)
name_enrty.grid(row = 0,column = 1,padx = 5,pady = 5)

tk.Label(
     input_frame,
     text = "Course:"
     ).grid(row = 0, column = 0, padx = 5, pady = 5)

course_entry = tk.Entry(input_frame,width=30)
course_enrty.grid(row = 0,column = 1,padx = 5,pady = 5)

button_frame = tk.Frame(root)
button_frame.pack(pady = 10)

tk.Button(
    buttom_frame,
    text = "Add",
    width = 50,
    commad = " add_ student"
    ).grid(row = 0, column =1, padx = 5)

tk.Button(
    buttom_frame,
    text = "Updte",
    width = 200,
    commad = " update_ student"
    ).grid(row = 0, column =1, padx = 5)

tk.Button(
    buttom_frame,
    text = "Delete",
    width = 80,
    commad = " Delete_ student"
    ).grid(row = 0, column =1, padx = 5)

k.Button(
    buttom_frame,
    text = "Clear",
    width = 200,
    commad = "Clear_ student"
    ).grid(row = 0, column =1, padx = 5)

tree = ttk.Treeview(
    root,
    column =("ID","Name","Age","Course")
    show = "heading"
    )

tree.heading("ID",text = "ID")
tree.heading("Name",text = "Name")
tree.heading("Age",text = "Age")
tree.heading("Course",text = "Course")

tree.column("ID",withd = 50)
tree.column("Name",withd = 200)
tree.column("Age",withd = 80)
tree.column("Course",withd = 200)

tree.pack(
    fill = "both"
    expand = True
    padx = 10
    pady = 10
    )

conn =aqlite3,connect("student.db")
consor = conn.cunsor ()

cusor.execute("""
CREATE TABLE IF NOT EXIST Student(
id Interger,Primary key,Auto Increment
name :Text,Not Null
email:Integer,Not Null
phone: text,Not Null
city:text,Not Null
age:text,Not Null
)
""")

conn.comit()

def add_student ():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    if name == "" or age == "" or course == "":
        messagebox.showwaring(
            "Warning"
            "Please fill in all fields"
            )
           return

        try:(
            age = int (age)
            except ValueError:
                "Error"
                "Age must be a number"
                )
                return

            consor. execute (

                "INSERT INTO Students(name,age,course)Value (?,?,?,?)",
                (name,age,phone,city)
                )


        conn.commit()

        messagebox.showinfo(
            "Success"
            "Student added successfully."
            )

        clear_fields()
        display_students()

        def display_students()
        for item in tree.get_children():
            tree.delete(item)

            cunsor.execute("SELECT * FROM Students")
            student = cunsor.fetchall()

            for student in students:
                tree.insert("", tk.END,value=student)
            
            





    
    

    

    
    
    
    

    



