from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image , ImageTk, ImageDraw
import pymysql 
from math import*
import sqlite3
import dashboard
import os

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Log In")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "darkblue")
        
        # frame
        login_frame = Frame(self.root, bg = 'white')
        login_frame.place(x=250, y=100, width = 800, height = 500)

        title = Label(login_frame, text = 'LOG IN HERE', font = ('helvetica', 30, 'bold'), bg = 'white', fg = '#08A3D2')
        title.place(x=300, y=50)

        email = Label(login_frame, text = 'Email or Username', font = ('helvetica', 25, 'bold'), bg = 'white', fg = 'lightgray')
        email.place(x=300, y=150)
        self.txt_email = Entry(login_frame, font = ('helvetica', 25, 'bold'), bg = 'lightgray', fg = 'black')
        self.txt_email.place(x=250, y=180, width=350, height=35)

        password = Label(login_frame, text = 'Password', font = ('helvetica', 25, 'bold'), bg = 'white', fg = 'lightgray')
        password.place(x=360, y=250)
        self.txt_password = Entry(login_frame, font = ('helvetica', 25, 'bold'), bg = 'lightgray', fg = 'black')
        self.txt_password.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, text = "Sign Up", font = ('helvetica', 14), bg = 'white', bd = 0, fg = '#800857', cursor='hand2', command = self.register_window)
        btn_reg.place(x=250, y=320)

        btn_forget = Button(login_frame, text = "Forgot Password?", font = ('helvetica', 14), bg = 'white', bd = 0, fg = 'red', cursor='hand2', command = self.forget_password_window)
        btn_forget.place(x=450, y=320)

        btn_login = Button(login_frame, text = "Log In", font = ('helvetica', 20, 'bold'), bg = 'white', fg = '#800857', cursor='hand2', command = self.login)
        btn_login.place(x=340, y=360, width=180, height=40)


    def reset(self):
        self.cmb_quest.current(0)
        self.txt_newpw.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_email.delete(0, END)
        



    def forget_password(self):
        if self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_newpw.get() == "":
            messagebox.showerror("Error", "All fields are required",parent = self.root2)
        else:
            try:
                con = sqlite3.connect(database='rms.db')
                cur = con.cursor()
                cur.execute('select * from register where email = ? and question = ? and answer = ?', (self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Erorr", "Please confirm by provide your correct security question and answer", parent = self.root2)
                else:
                    cur.execute('update register set password = ? where email = ?', (self.txt_newpw.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your password has been changed")
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent = self.root)





    def forget_password_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Error", "Please enter an email to reset your password", parent = self.root)
        else:
            try:
                # mysql
                # con = pymysql.connect(host='localhost', user='root', password='bothiccka', database='student')
                # cur = con.cursor()
                # cur.execute("SELECT * FROM student WHERE email = %s", (self.txt_email.get(),))
                # row = cur.fetchone()
                # sqllite3
                con = sqlite3.connect(database='rms.db')
                cur = con.cursor()
                cur.execute('select * from register where email = ?', (self.txt_email.get(),))
                row = cur.fetchone()
                # Check if user exists
                if row is None:
                    messagebox.showerror("Error", "Invalid Email", parent=self.root)  # Corrected error message
                else:
                    # Proceed with password reset if email exists
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget password")
                    self.root2.geometry("400x400+495+150")
                    self.root2.config(bg='white')
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text='Forget Password', font=('helvetica', 20, 'bold'), bg='white', fg='red')
                    t.place(x=0, y=10, relwidth=1)

                    question = Label(self.root2, text="Security Question", font=('helvetica', 20, 'bold'), bg='white', fg='green')
                    question.place(x=50, y=100)
                    self.cmb_quest = ttk.Combobox(self.root2, font=('helvetica', 20), state='readonly', justify=CENTER)
                    self.cmb_quest['values'] = ('Select', "Your First Pet's Name", "Your Secret Word", "Your Best Friend's Name")
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)  # Set default selection to 'Select'

                    answer = Label(self.root2, text="Answer", font=('helvetica', 20, 'bold'), bg='white', fg='green')
                    answer.place(x=50, y=180)
                    self.txt_answer = Entry(self.root2, font=('helvetica', 20), bg='lightgray')
                    self.txt_answer.place(x=50, y=210, width=250)

                    newpw = Label(self.root2, text="New Password", font=('helvetica', 20, 'bold'), bg='white', fg='green')
                    newpw.place(x=50, y=260)
                    self.txt_newpw = Entry(self.root2, font=('helvetica', 20), bg='lightgray')
                    self.txt_newpw.place(x=50, y=290, width=250)

                    btn_changepw = Button(self.root2, command = self.forget_password, text='Reset Password', bg='green', fg='black', font=('helvetica', 15, 'bold'))
                    btn_changepw.place(x=50, y=340)

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)



    def register_window(self):
        self.root.destroy()
        import register


    def login(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Connect to MySQL
                # con = pymysql.connect(host='localhost', user='root', password='bothiccka', database='student')
                # cur = con.cursor()
                # cur.execute(
                #     "SELECT * FROM student WHERE LOWER(email) = %s AND password = %s",
                #     (self.txt_email.get().lower(), self.txt_password.get())
                # )
                # row = cur.fetchone()

                # sqllite
                con = sqlite3.connect(database='rms.db')
                cur = con.cursor()
                cur.execute('select * from register where email = ? and password = ?', (self.txt_email.get(), self.txt_password.get()))
                row = cur.fetchone()

                # Check if user exists
                if row == None:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome!", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()

                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()



