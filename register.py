from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import pymysql
import sqlite3
import login
import os

class Register():
    def __init__ (self, root):
        self.root = root 
        self.root.title('Register Window')
        self.root.geometry("1350x700+0+0")

        # content window
        self.bg_img = Image.open("images/studentstudying.jpg")
        self.bg_img = self.bg_img.resize((456, 500),Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image = self.bg_img).place(x = 50, y = 97)

    # register
        frame1 = Frame(self.root, bg = 'white')
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text = "Register", font = ('helvetica', 30, 'bold'), bg = 'white', fg = 'green')
        title.place(x=50, y=30)

        # row 1
        
        f_name = Label(frame1, text = "First Name", font = ('helvetica', 20, 'bold'), bg = 'white', fg = 'green')
        f_name.place(x=50, y=100)
        self.txt_fname = Entry(frame1, font = ('helvetica', 20), bg = 'lightgray')
        self.txt_fname.place(x= 50, y=130, width=250)

        l_name = Label(frame1, text = "Last Name", font = ('helvetica', 20, 'bold'), bg = 'white', fg = 'green')
        l_name.place(x=370, y=100)
        self.txt_lname = Entry(frame1, font = ('helvetica', 20), bg = 'lightgray')
        self.txt_lname.place(x= 370, y=130, width=250)

        # row 2

        contact = Label(frame1, text = "Contact", font = ('helvetica', 20, 'bold'), bg = 'white', fg = 'green')
        contact.place(x=50, y=170)
        self.txt_contact = Entry(frame1, font = ('helvetica', 20), bg = 'lightgray')
        self.txt_contact.place(x= 50, y=200, width=250)

        email = Label(frame1, text = "Email", font = ('helvetica', 20, 'bold'), bg = 'white', fg = 'green')
        email.place(x=370, y=170)
        self.txt_email = Entry(frame1, font = ('helvetica', 20), bg = 'lightgray')
        self.txt_email.place(x= 370, y=200, width=250)

        # row 3
        question = Label(frame1, text="Security Question", font=('helvetica', 20, 'bold'), bg='white', fg='green')
        question.place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=('helvetica', 20), state='readonly', justify = CENTER)  
        self.cmb_quest['values'] = ('Select', "Your First Pet's Name", "Your Secret Word", "Your Best Friend's Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)  # Set default selection to 'Select'


        answer = Label(frame1, text = "Answer", font = ('helvetica', 20, 'bold'), bg = 'white', fg = 'green')
        answer.place(x=370, y=240)
        self.txt_answer = Entry(frame1, font = ('helvetica', 20), bg = 'lightgray')
        self.txt_answer.place(x= 370, y=270, width=250)

        # row 4
        password = Label(frame1, text = "Password", font = ('helvetica', 20, 'bold'), bg = 'white', fg = 'green')
        password.place(x=50, y=310)
        self.txt_password = Entry(frame1, font = ('helvetica', 20), bg = 'lightgray', show="*")
        self.txt_password.place(x=50, y=340, width=250)

        cfpassword = Label(frame1, text = "Confirm Password", font = ('helvetica', 20, 'bold'), bg = 'white', fg = 'green')
        cfpassword.place(x=370, y=310)
        self.txt_cfpassword = Entry(frame1, font = ('helvetica', 20), bg = 'lightgray', show="*")
        self.txt_cfpassword.place(x= 370, y=340, width=250)

        # term and condition
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, variable = self.var_chk, text = 'I Agree to the Terms and Conditions', bg = 'white', font = 'helvetica', onvalue = 1, offvalue = 0)
        chk.place(x=50, y=380)

        # buttons
        self.register_btn = Button(frame1, text="Register", font=('helvetica', 15, 'bold'), bg='white', cursor='hand2', command = self.register_data)
        self.register_btn.place(x=50, y=410, width = 100)

        alrreg = Label(frame1, text="Already have an account? Log In", font=('helvetica', 15, 'bold'), bg='white', fg='green')
        alrreg.place(x=375, y=380)  # Adjust x and y as necessary
        alrreg.lift()  

        self.login_btn = Button(self.root, text="Log In", font=('helvetica', 15, 'bold'), bd=0, bg='white', cursor='hand2')
        self.login_btn.place(x=850, y=512, width = 100)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")

    def register_data(self):
        print(self.txt_fname.get(),
              self.txt_lname.get(),
              self.txt_contact.get(),
              self.txt_email.get(),
              self.cmb_quest.get(),
              self.txt_answer.get(),
              self.txt_password.get(),
              self.txt_cfpassword.get())
        if (self.txt_fname.get() == "" or 
            self.txt_lname.get() == "" or 
            self.txt_contact.get() == "" or 
            self.txt_email.get() == "" or 
            self.cmb_quest.get() == "Select" or 
            self.txt_answer.get() == "" or 
            self.txt_password.get() == "" or 
            self.txt_cfpassword.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_password.get() != self.txt_cfpassword.get():
            messagebox.showerror("Error", "Passwords do not match", parent = self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree to the Terms and Conditions", parent = self.root)
        else:
            try:
                con = sqlite3.connect(database='rms.db')
                cur = con.cursor()
                cur.execute('select * from register where email = ?', (self.txt_email.get(),))
                row = cur.fetchone()
                # print(row)
                if row != None:
                    messagebox.showerror("Error", "User Already Exists", parent = self.root)
                else:
                    cur.execute("""
                        INSERT INTO register (f_name, l_name, contact, email, question, answer, password) 
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (
                        self.txt_fname.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.cmb_quest.get(),
                        self.txt_answer.get(),
                        self.txt_password.get()
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent = self.root)
                    self.clear()
                    self.login_window()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}")
       
    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_quest.set('Select')
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cfpassword.delete(0, END)




root = Tk()
obj = Register(root)
root.mainloop()        