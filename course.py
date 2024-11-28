from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("AUPP Academic Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg = "white")
        self.root.focus_force()
       
        # title       
        title = Label(self.root, text="Manage Course Details", font=("Helvetica", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        # variable
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search = StringVar()  


        # widget
        lbl_courseName = Label(self.root, text = "Course Name", font = ('Helvetica', 15, 'bold'), bg = 'white').place(x = 10, y = 60)
        lbl_duration = Label(self.root, text = "Duration", font = ('Helvetica', 15, 'bold'), bg = 'white').place(x = 10, y = 100)
        lbl_charges = Label(self.root, text = "Charges", font = ('Helvetica', 15, 'bold'), bg = 'white').place(x = 10, y = 140)
        lbl_description = Label(self.root, text = "Description", font = ('Helvetica', 15, 'bold'), bg = 'white').place(x = 10, y = 180)

        # entry fields

        self.txt_courseName = Entry(self.root, textvariable = self.var_course, font = ('helvetica', 15,'bold'), bg = 'lightyellow')
        self.txt_courseName.place(x = 150, y = 60, width = 200)
        txt_duration = Entry(self.root, textvariable = self.var_duration, font = ('Helvetica', 15, 'bold'), bg = 'lightyellow').place(x = 150, y = 100, width = 200)
        txt_charges = Entry(self.root, textvariable = self.var_charges, font = ('Helvetica', 15, 'bold'), bg = 'lightyellow').place(x = 150, y = 140, width = 200)
        self.txt_description = Text(self.root, font = ('Helvetica', 15, 'bold'), bg = 'lightyellow')
        self.txt_description.place(x = 150, y = 180, width = 500, height = 130)

        # button

        self.btn_add = Button(self.root, text = 'Save', font = ('helvetica', 15, 'bold'), bg = '#2196f3', fg = 'white', cursor = 'hand2', command = self.add)
        self.btn_add.place(x = 150, y = 400, width = 110, height = 40)

        self.btn_update = Button(self.root, text = 'Update', font = ('helvetica', 15, 'bold'), bg = '#4caf50', fg = 'white', cursor = 'hand2', command = self.update)
        self.btn_update.place(x = 270, y = 400, width = 110, height = 40)

        self.btn_delete = Button(self.root, text = 'Delete', font = ('helvetica', 15, 'bold'), bg = '#2196f3', fg = 'white', cursor = 'hand2', command = self.delete)
        self.btn_delete.place(x = 390, y = 400, width = 110, height = 40)

        self.btn_clear = Button(self.root, text = 'Clear', font = ('helvetica', 15, 'bold'), bg = '#2196f3', fg = 'white', cursor = 'hand2', command = self.clear)
        self.btn_clear.place(x = 510, y = 400, width = 110, height = 40)

        # search panel

        self.var_search = StringVar()
        lbl_search_courseName = Label(self.root, text="        Course Name", font=('Helvetica', 15, 'bold'), bg='white').place(x=720, y=60)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=('helvetica', 15, 'bold'), bg='lightyellow').place(x=870, y=60, width=180)
        btn_search = Button(self.root, text = 'Search', font = ('helvetica', 15, 'bold'), bg = '#2196f3', fg = 'black', cursor = 'hand2', command = self.search).place(x = 1070, y = 60, width = 120, height = 28)

        # Content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(
            self.C_Frame, 
            columns=('cid', 'name', 'duration', 'charges', 'description'), 
            xscrollcommand=scrollx.set, 
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.heading('cid', text='Course ID')
        self.CourseTable.heading('name', text='Name')
        self.CourseTable.heading('duration', text='Duration')
        self.CourseTable.heading('charges', text='Charges')
        self.CourseTable.heading('description', text='Description')
        self.CourseTable['show'] = 'headings'
        self.CourseTable.column('cid', width=50)
        self.CourseTable.column('name', width=100)
        self.CourseTable.column('duration', width=100)
        self.CourseTable.column('charges', width=100)
        self.CourseTable.column('description', width=100)
        self.CourseTable.bind('<ButtonRelease-1>', self.get_data)
        self.show()


    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0', END)
        self.txt_courseName.config(state = NORMAL)

    def delete(self):
        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name = ?", (self.var_course.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select a course from the list first", parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm', "Do you really want to delete?", parent=self.root)
                    if op:
                        # Correct DELETE query
                        cur.execute('DELETE FROM course WHERE name = ?', (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo('Delete', "Course deleted successfully", parent=self.root)
                        self.clear()  # Assuming clear resets the form fields and updates the display
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()


        # get data
    def get_data(self, ev):
        self.txt_courseName.config(state = 'readonly')
        self.txt_courseName
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content['values']
        # print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete('1.0', END)
        self.txt_description.insert(END, row[4])



    #     # db
    # def add(self):
    #     con = sqlite3.connect(database = 'rms.db')
    #     cur = con.cursor()
    #     try:
    #         if self.var_course.get()=="":
    #             messagebox.showerror("Error", "Course Name should be required", parent = self.root)
    #         else:
    #             cur.execute("select * from course where name = ?", (self.var_course.get(),))
    #             row = cur.fetchone()
    #             if row != None:
    #                 messagebox.showerror("Error", "Course Name already exist.", parent = self.root)
    #             else:
    #                 cur.execute("Insert Into Course (name, duration, charges, description) values(?, ?, ?, ?)",(
    #                     self.var_course.get(),
    #                     self.var_duration.get(),
    #                     self.var_charges.get(),
    #                     self.txt_description.get('1.0', END),
    #                 )) 
    #                 con.commit()
    #                 messagebox.showinfo("Success", "Course Added Successfully", parent = self.root)
    #                 self.show()

    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error due to {str(ex)}")



    def add(self):
        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                # Check if table is empty and reset auto-increment
                cur.execute("SELECT COUNT(*) FROM course")
                count = cur.fetchone()[0]
                if count == 0:
                    cur.execute("DELETE FROM sqlite_sequence WHERE name='course'")
                    con.commit()

                # Check if course name already exists
                cur.execute("SELECT * FROM course WHERE name = ?", (self.var_course.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Course Name already exists.", parent=self.root)
                else:
                    cur.execute("INSERT INTO course (name, duration, charges, description) VALUES (?, ?, ?, ?)", (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get('1.0', END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()




    # def update(self):
    #     con = sqlite3.connect(database = 'rms.db')
    #     cur = con.cursor()
    #     try:
    #         if self.var_course.get()=="":
    #             messagebox.showerror("Error", "Course Name should be required", parent = self.root)
    #         else:
    #             cur.execute("select * from course where name = ?", (self.var_course.get(),))
    #             row = cur.fetchone()
    #             if row == None:
    #                 messagebox.showerror("Error", "Select Course from List", parent = self.root)
    #             else:
    #                 cur.execute("Update Courses set duration=?, charges=?, description=? where name=?",(
    #                     self.var_duration.get(),
    #                     self.var_charges.get(),
    #                     self.txt_description.get('1.0', END),
    #                     self.var_course.get()
    #                 )) 
    #                 con.commit()
    #                 messagebox.showinfo("Success", "course Updated Successfully", parent = self.root)
    #                 self.show()

    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error due to {str(ex)}")


    def update(self):
        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                # Check if the course exists
                cur.execute("SELECT * FROM course WHERE name = ?", (self.var_course.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select Course from List", parent=self.root)
                else:
                    # Update the course details
                    cur.execute(
                        "UPDATE course SET duration=?, charges=?, description=? WHERE name=?",
                        (
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.txt_description.get('1.0', END),
                            self.var_course.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Course Updated Successfully", parent=self.root)
                    self.show()  # Ensure the `show` method refreshes the data display
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()





    def show(self):
        con = sqlite3.connect(database = 'rms.db')
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END, values = row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    # def search(self):
    #     con = sqlite3.connect(database = 'rms.db')
    #     cur = con.cursor()
    #     try:
    #         cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
    #         rows = cur.fetchall()
    #         self.CourseTable.delete(*self.CourseTable.get_children())
    #         for row in rows:
    #             self.CourseTable.insert('',END, values = row)
    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            # Use the search term to filter courses
            cur.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + self.var_search.get() + '%',))
            rows = cur.fetchall()
            
            # Clear current entries in the Treeview
            self.CourseTable.delete(*self.CourseTable.get_children())
            
            # Insert new results into the Treeview
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()




if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop() 


