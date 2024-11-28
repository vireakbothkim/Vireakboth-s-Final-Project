from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
import os


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("AUPP Academic Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "white")
        
        #icon
        self.logo_dash = ImageTk.PhotoImage(file = "Images/AUPPLogo.png")
        
        #title
        title = Label(self.root,text = "AUPP Academic Management Systsem",padx = 10, compound = LEFT, image = self.logo_dash, font=("Helvetica", 20, "bold"), bg = "#033054", fg = "white").place(x=0, y=0, relwidth=1, height=50)

        #menu
        M_Frame = LabelFrame(self.root, text = "Menus", font = ("Helvetica", 15), bg = "white")
        M_Frame.place(x = 10, y = 70, width = 1340, height = 80)

        btn_course = Button(M_Frame, text = "Course", font = ("Helvetica", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2", command = self.add_course).place(x = 20, y = 5, width = 200, height = 40)
        btn_student = Button(M_Frame, text = "Student", font = ("Helvetica", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2", command = self.add_student).place(x = 240, y = 5, width = 200, height = 40)
        btn_result = Button(M_Frame, text = "Result", font = ("Helvetica", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2", command = self.add_result).place(x = 460, y = 5, width = 200, height = 40)
        btn_view = Button(M_Frame, text = "View Student Results", font = ("Helvetica", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2", command = self.add_report).place(x = 680, y = 5, width = 200, height = 40)
        btn_logout = Button(M_Frame, text = "Log Out", font = ("Helvetica", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2", command = self.logout).place(x = 900, y = 5, width = 200, height = 40)
        btn_exit = Button(M_Frame, text = "Exit", font = ("Helvetica", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2", command = self.exit).place(x = 1120, y = 5, width = 200, height = 40)

        # content window
        self.bg_img = Image.open("images/school.jpg")
        self.bg_img = self.bg_img.resize((520, 350),Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image = self.bg_img).place(x = 200, y = 180, width = 920, height = 350)

        # #update datails
        # self.lbl_course = Label(self.root, text='Total Courses\n[ 0 ]', 
        #                         font=('Helvetica', 20), bd=10, relief=RIDGE, 
        #                         bg='#e43b06', fg='white')
        # self.lbl_course.place(x=400, y=530, width=350, height=100)

        # self.lbl_student = Label(self.root, text='Total Students\n[ 0 ]', 
        #                          font=('Helvetica', 20), bd=10, relief=RIDGE, 
        #                          bg='#e43b06', fg='white')
        # self.lbl_student.place(x=710, y=530, width=300, height=100)

        # self.lbl_result = Label(self.root, text='Total Results\n[ 0 ]', 
        #                         font=('Helvetica', 20), bd=10, relief=RIDGE, 
        #                         bg='#e43b06', fg='white')
        # self.lbl_result.place(x=1020, y=530, width=300, height=100)
        
        
        
        #footer
        footer = Label(self.root, text = "SRMS = Student Results Management System\nContact Us for any Technical Sissues: 123456789", font = ("helvetica", 12), bg = "#262626", fg = "white").pack(side = BOTTOM, fill = X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent = self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        op = messagebox.askyesno("Confirm", "Do you really want to exit?", parent = self.root)
        if op == True:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()