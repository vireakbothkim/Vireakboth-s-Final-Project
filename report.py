from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("AUPP Academic Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg = "white")
        self.root.focus_force()
       
        # title       
        title = Label(self.root, text="View Student Result", font=("Helvetica", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)


        # # search
        # self.var_search = StringVar()
        # self.var_id = ""
        # lbl_search = Label(self.root, text = "Search By Roll No.", font = ('Helvetica', 20, 'bold'), bg = 'white').place(x = 280, y = 100)
        # txt_search = Entry(self.root, textvariable = self.var_search, text = "Search By Roll Number", font = ('Helvetica', 20, 'bold'), bg = 'lightyellow').place(x = 500, y = 100, width = 150)
        # btn_search = Button(self.root, text = 'Search', font = ('helvetica', 20, 'bold'), bg = '#2196f3', fg = 'black', cursor = 'hand2', command = self.search).place(x = 680, y = 100, width = 100, height = 35)
        # btn_clear = Button(self.root, text = 'Clear', font = ('helvetica', 20, 'bold'), bg = '#2196f3', fg = 'black', cursor = 'hand2', command = self.clear).place(x = 800, y = 100, width = 100, height = 35)

        # Search
        self.var_search = StringVar()
        self.var_id = ""
        lbl_search = Label(self.root, text="Search By Roll No.", font=('Helvetica', 20, 'bold'), bg='white')
        lbl_search.place(x=280, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search, font=('Helvetica', 20, 'bold'), bg='lightyellow')
        txt_search.place(x=500, y=100, width=150)
        btn_search = Button(self.root, text='Search', font=('Helvetica', 20, 'bold'), bg='#2196f3', fg='black', cursor='hand2', command=self.search)
        btn_search.place(x=680, y=100, width=100, height=35)
        btn_clear = Button(self.root, text='Clear', font=('Helvetica', 20, 'bold'), bg='#2196f3', fg='black', cursor='hand2', command=self.clear)
        btn_clear.place(x=800, y=100, width=100, height=35)

        # label
        lbl_roll = Label(self.root, text = "Roll No", font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE).place(x = 150, y = 230, width = 150, height = 50)
        lbl_name = Label(self.root, text = "Name", font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE).place(x = 300, y = 230, width = 150, height = 50)
        lbl_course = Label(self.root, text = "Course", font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE).place(x = 450, y = 230, width = 150, height = 50)
        lbl_marks = Label(self.root, text = "Marks Obtained", font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE).place(x = 600, y = 230, width = 150, height = 50)
        lbl_full = Label(self.root, text = "Total Marks", font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE).place(x = 750, y = 230, width = 150, height = 50)
        lbl_per = Label(self.root, text = "Percentage", font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE).place(x = 900, y = 230, width = 150, height = 50)


        self.roll = Label(self.root, font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE)
        self.roll.place(x = 150, y = 280, width = 150, height = 50)
        self.name = Label(self.root, font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE)
        self.name.place(x = 300, y = 280, width = 150, height = 50)
        self.course = Label(self.root, font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE)
        self.course.place(x = 450, y = 280, width = 150, height = 50)
        self.marks = Label(self.root, font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE)
        self.marks.place(x = 600, y = 280, width = 150, height = 50)
        self.full = Label(self.root, font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE)
        self.full.place(x = 750, y = 280, width = 150, height = 50)
        self.per = Label(self.root, font = ('Helvetica', 15, 'bold'), bg = 'white', bd =2 , relief = GROOVE)
        self.per.place(x = 900, y = 280, width = 150, height = 50)

        # button delete
        btn_delete = Button(self.root, text = 'Delete', font = ('helvetica', 15), bg = 'red', fg = 'white', cursor = 'hand2', command = self.delete).place(x=500, y=350, width=150, height=35)

        # search
    def search(self):
        con = sqlite3.connect(database = 'rms.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll number is required", parent = self.root)
            else:
                cur.execute("select * from result where roll = ?", (self.var_search.get(),))
                row = cur.fetchone()
                if row != None:
                    self.var_id = row[0]
                    self.roll.config(text = row[1])
                    self.name.config(text = row[2])
                    self.course.config(text = row[3])
                    self.marks.config(text = row[4])
                    self.full.config(text = row[5])
                    self.per.config(text = row[6])
                else:
                    messagebox.showerror("Error", "No Record found", parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_id = ""
        self.roll.config(text = "")
        self.name.config(text = "")
        self.course.config(text = "")
        self.marks.config(text = "")
        self.full.config(text = "")
        self.per.config(text = "")      
        self.var_search.set("")  


    # def delete(self):
    #     con = sqlite3.connect(database='rms.db')
    #     cur = con.cursor()
    #     try:
    #         if self.var_id == "":
    #             messagebox.showerror("Error", "Search Student Result First", parent=self.root)
    #         else:
    #             cur.execute("SELECT * FROM result WHERE rid = ?", (self.var_id,))
    #             row = cur.fetchone()
    #             if row is None:
    #                 messagebox.showerror("Error", "Invalid Student Result", parent=self.root)
    #             else:
    #                 op = messagebox.askyesno('Confirm', "Do you really want to delete?", parent=self.root)
    #                 if op:
    #                     # Correct DELETE query
    #                     cur.execute('DELETE FROM result WHERE rid = ?', (self.var_id))
    #                     con.commit()
    #                     messagebox.showinfo('Delete', "Result deleted successfully", parent=self.root)
    #                     self.clear()  # Assuming clear resets the form fields and updates the display
    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
    #     finally:
    #         con.close()

    def delete(self):
        con = sqlite3.connect(database='rms.db')
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error", "Search Student Result First", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE rid = ?", (self.var_id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Student Result", parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm', "Do you really want to delete?", parent=self.root)
                    if op:
                        # Corrected DELETE query
                        cur.execute('DELETE FROM result WHERE rid = ?', (self.var_id,))
                        con.commit()
                        messagebox.showinfo('Delete', "Result deleted successfully", parent=self.root)
                        self.clear()  # Reset form fields and update display
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()




if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()