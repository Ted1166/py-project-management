from cgitb import text
from email.mime import application
from logging import root
from sqlite3 import connect
from tkinter import*
from tkinter import ttk
import random
from tkinter import font
import tkinter.messagebox
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr
from unittest import result

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x670+0+0")
        
        notebook = ttk.Notebook(self.root)
        self.TabControl1 =ttk.Frame(notebook)
        self.TabControl2 =ttk.Frame(notebook)
        notebook.add(self.TabControl1, text = 'Student Details')
        notebook.add(self.TabControl2, text = 'Records')
        
        notebook.grid()
        
        #============================================variable====================================================
        self.Firstname =StringVar()
        self.Surname =StringVar()
        self.StudentID =StringVar()
        self.Admissionnum =StringVar()
        self.Gender =StringVar()
        self.Email =StringVar()
        self.UniversityEmail=StringVar()
        self.DOB =StringVar()
        self.Mobile =StringVar()
        self.Address =StringVar()
        self.Residence = StringVar()

        self.School =StringVar()
        self.Course =StringVar()
        self.Units =StringVar()
        self.Stage = StringVar()
        self.YOS = StringVar()
        self.Dean = StringVar()
        self.Accomodation = StringVar()
        
        self.MaritalStatus = StringVar()
        self.Parent = StringVar()
        self.Country = StringVar()
        self.County = StringVar()
        
        #============================================Frame====================================================
        
        MainFrame = Frame(self.TabControl1, bd=10, width=1200, height=670, relief=RIDGE)
        MainFrame.grid(padx=5,pady=10)
        
        Tab2Frame = Frame(self.TabControl2, bd=10, width=1200, height=670, relief=RIDGE)
        Tab2Frame.grid(padx=10)
        
        TopFrame3 = Frame(MainFrame, bd=5, width=1150, height=500, relief=RIDGE)
        TopFrame3.grid()
        
        RightFrame1 = Frame(TopFrame3, bd=5, width=550, height=550, padx=2, bg="blue", relief=RIDGE)
        RightFrame1.pack(side=RIGHT,pady=1)
        
        LeftFrame = Frame(TopFrame3, bd=5, width=550, height=550, padx=2, bg="blue", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        
        StudentStatusFrame = Frame(RightFrame1, bd=5, width=280, height=400, padx=2, relief=RIDGE)
        StudentStatusFrame.pack(side=TOP)
        
        StudentFrame = Frame(LeftFrame, bd=5, width=280, height=400, padx=2, relief=RIDGE)
        StudentFrame.pack(side=TOP)
        
        CourseFrame = Frame(RightFrame1, bd=5, width=280, height=400, padx=2, relief=RIDGE)
        CourseFrame.pack(side=TOP)
        
        ButtonFrame = Frame(LeftFrame, bd=5, width=320, height=50, padx=4, bg="cadetblue", relief=RIDGE)
        ButtonFrame.pack(side=LEFT)
        
        #============================================Function=Exit===================================================
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Management System", "Do you want to Exit?")
            if iExit > 0:
                root.destroy()
                return
            
        #============================================Function=Reset===================================================
        
        def Reset():
             self.Firstname.set("") 
             self.Surname.set("")
             self.StudentID.set("")
             self.Admissionnum.set("")
             self.Gender.set("")
             self.Email.set("")
             self.UniversityEmail.set("")
             self.DOB.set("")
             self.Mobile.set("")
             self.Address.set("")
             self.Residence.set("")

             self.School.set("")
             self.Course.set("")
             self.Units.set("0")
             self.Stage.set("")
             self.YOS.set("")
             self.Dean.set("")
             self.Accomodation.set("")
        
             self.MaritalStatus.set("")
             self.Parent.set("")
             self.Country.set("")
             self.County.set("") 
        
        #============================================CourseData=====================================================
        
        def CourseData(event):
            if self.Course.get()=='Information Technology':
                self.School.set("COMPUTING AND INFORMATICS")
                self.Dean.set("Mr. Caleb Oula")
                self.Units.set("7")
                
            elif self.Course.get()=='Nursing':
                self.School.set("MEDICINE")
                self.Dean.set("Mrs Wendy Jane")
                self.Units.set("10")
                
            elif self.Course.get()=='Teaching':
                self.School.set("EDUCATION")
                self.Dean.set("Mr. Otieno Osodo")
                self.Units.set("11")
                
            elif self.Course.get()=='Linguistics':
                self.School.set("EDUCATION")
                self.Dean.set("Mr. Otieno Osodo")
                self.Units.set("10")
            
            elif self.Course.get()=='Phsycology':
                self.School.set("EDUCATION")
                self.Dean.set("Mr. Otieno Osodo")
                self.Units.set("7")
                
            elif self.Course.get()=='Farming':
                self.School.set("AGRICULTURE & FOOD SECURITY")
                self.Dean.set("Mr. Joash Okelo")
                self.Units.set("6")
                
            elif self.Course.get()=='Accounting':
                self.School.set("BUSINESS & ECONOMICS")
                self.Dean.set("Mr. George Omono")
                self.Units.set("6")
                
            elif self.Course.get()=='Laboratory Technician':
                self.School.set("MEDICINE")
                self.Dean.set("Mrs Wendy Jane")
                self.Units.set("9")
        
        #============================================Widget===========================================================
        
        TopFrame11 = Frame(Tab2Frame, bd=10, width=1200, height=60, relief=RIDGE)
        TopFrame11.grid(row=0, column=0)
        
        TopFrame12 = Frame(Tab2Frame, bd=5, width=1150, height=500, relief=RIDGE)
        TopFrame12.grid(row=1, column=0)
        
        #============================================Widget===========================================================
        
        self.lblTitle = Label(TopFrame11, font=('arail',40,'bold'), text="Student Records Management System",
                              justify=CENTER)
        self.lblTitle.grid(padx=160)
        
        #============================================Widget===========================================================
        
        scroll_x=Scrollbar(TopFrame12, orient=HORIZONTAL)
        scroll_y=Scrollbar(TopFrame12, orient=VERTICAL)
        
        self.Student_records = ttk.Treeview(TopFrame12, height=22, columns=("StudentID", "Firstname","Surname","Admission_num",
                                             "Gender","DOB","Mobile", "Address","Email", "UniversityEmail","Course","Stage"),
                                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=BOTTOM, fill=Y)
        
        self.Student_records.heading("StudentID", text="Student ID")
        self.Student_records.heading("Firstname", text="First Name")
        self.Student_records.heading("Surname", text="Surname")
        self.Student_records.heading("Admission_num", text="Admn Number")
        self.Student_records.heading("Gender", text="Gender")
        self.Student_records.heading("DOB", text="DOB")
        self.Student_records.heading("Mobile", text="Mobile")
        self.Student_records.heading("Address", text="Address")
        self.Student_records.heading("Email", text="Email")
        self.Student_records.heading("UniversityEmail", text="University Email")
        self.Student_records.heading("Course", text="Course")
        self.Student_records.heading("Stage", text="Stage")
        
        self.Student_records['show'] = 'headings'
        
        self.Student_records.column("StudentID", width=100)
        self.Student_records.column("Firstname", width=90)
        self.Student_records.column("Surname", width=90)
        self.Student_records.column("Admission_num", width=110)
        self.Student_records.column("Gender", width=80)
        self.Student_records.column("DOB", width=100)
        self.Student_records.column("Mobile", width=100)
        self.Student_records.column("Address", width=90)
        self.Student_records.column("Email", width=120)
        self.Student_records.column("UniversityEmail", width=120)
        self.Student_records.column("Course", width=160)
        self.Student_records.column("Stage", width=130)
        
        self.Student_records.pack(fill=BOTH, expand=1)
        self.Student_records.bind("<ButtonRelease-1>")
        
        #============================================AddData===========================================================
        
        def addData():
            if self.StudentID.get()=="" or self.Firstname.get()=="" or self.Surname.get()=="":
                tkinter.messagebox.showerror("Enter the Student details correctly")
            else:
                sqlCon= connect(host= "localhost", user="root", password = "12345", database="School")
                cur = sqlCon.cur()
                cur.Execute("insert into School values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            
                            (
                                self.StudentID.get(),
                                self.Firstname.get(),
                                self.Surname.get(),
                                self.Admissionnum.get(),
                                self.Gender.get(),
                                self.Email.get(),
                                self.UniversityEmail.get(),
                                self.DOB.get(),
                                self.Mobile.get(),
                                self.Address.get(),
                                self.Residence.get(),
                                self.School.get(),
                                self.Course.get(),
                                self.Units.get(),
                                self.Stage.get(),
                                self.YOS.get(),
                                self.Dean.get(),
                                self.Accomodation.get(),
                                self.MaritalStatus.get(),
                                self.Parent.get(),
                                self.Country.get(),
                                self.County.get(),
                            ))
                sqlCon.Commit()
                DisplayData()
                sqlCon.close()
                tkinter.messagebox.showinfo("Student Management System", "Record Entered Successfully")
        
        #============================================DisplayData===========================================================
        
        def DisplayData():
            sqlCon= connect(host= "localhost", user="root", password = "12345", database="School")
            cur = sqlCon.cur()
            cur.execute("select * from school")
            result = cur.fetchall()
            if len(result)!=0:
                self.Student_records.delete(*self.Student_records.get_children())
                for row in result:
                    self.Student_records.insert('', END, values=row)
                sqlCon.Commit()
            sqlCon.close()
                    
        #============================================Widget===========================================================
        
            
                         
        
        #============================================Widget===========================================================
        
        self.lblStudentID = Label(StudentFrame, font=('arial',12,'bold'), text='Student ID', bd=7, anchor='w', justify=LEFT)
        self.lblStudentID.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtStudentID = Entry(StudentFrame, font=('arail',12,'bold'), bd=5, width=35, justify='left',
                                  textvariable=self.StudentID)
        self.txtStudentID.grid(row=0, column=1)
        
        self.lblFirstname = Label(StudentFrame, font=('arial',12,'bold'), text='Firstname', bd=7, anchor='w', justify=LEFT)
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtfirstname = Entry(StudentFrame, font=('arail',12,'bold'), bd=5, width=35, justify='left',
                                  textvariable=self.Firstname)
        self.txtfirstname.grid(row=1, column=1)
        
        self.lblSurname = Label(StudentFrame, font=('arial',12,'bold'), text='Surname', bd=7, anchor='w', justify=LEFT)
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtSurname = Entry(StudentFrame, font=('arail',12,'bold'), bd=5, width=35, justify='left',
                                  textvariable=self.Surname)
        self.txtSurname.grid(row=2, column=1)
        
        self.lblAdmissionnum = Label(StudentFrame, font=('arial',12,'bold'), text='Admission_num', bd=7, anchor='w', justify=LEFT)
        self.lblAdmissionnum.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtAdmissionnum = Entry(StudentFrame, font=('arail',12,'bold'), bd=5, width=35, justify='left',
                                  textvariable=self.Admissionnum)
        self.txtAdmissionnum.grid(row=3, column=1)
        
        self.lblGender = Label(StudentFrame, font=('arial',12,'bold'), text='Gender', bd=7, justify=LEFT)
        self.lblGender.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.cboGender = ttk.Combobox(StudentFrame, textvariable=self.Gender,
                                      font=('arail',12,'bold'), width=35, state = 'randomly', justify='left')
        self.cboGender['value'] = ('','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=4, column=1)
        
        self.lblDOB = Label(StudentFrame, font=('arial',12,'bold'), text='DOB', bd=7, anchor='w', justify=LEFT)
        self.lblDOB.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.txtDOB = Entry(StudentFrame, font=('arail',12,'bold'), bd=5, width=35, justify='left',
                                  textvariable=self.DOB)
        self.txtDOB.grid(row=5, column=1)
        
        self.lblMobile = Label(StudentFrame, font=('arial',12,'bold'), text='Mobile', bd=7, anchor='w', justify=LEFT)
        self.lblMobile.grid(row=6, column=0, sticky=W, padx=5, pady=5)
        self.txtMobile = Entry(StudentFrame, font=('arail',12,'bold'), bd=5, width=35, justify='left',
                                  textvariable=self.Mobile)
        self.txtMobile.grid(row=6, column=1)
        
        self.lblEmail = Label(StudentFrame, font=('arial',12,'bold'), text='Email', bd=7, anchor='w', justify=LEFT)
        self.lblEmail.grid(row=7, column=0, sticky=W, padx=5, pady=5)
        self.txtEmail = Entry(StudentFrame, font=('arail',12,'bold'), bd=5, width=35, justify='left',
                                  textvariable=self.Email)
        self.txtEmail.grid(row=7, column=1)
        
        self.lblUniversityEmail = Label(StudentFrame, font=('arial',12,'bold'), text='UniversityEmail', bd=7, anchor='w', justify=LEFT)
        self.lblUniversityEmail.grid(row=8, column=0, sticky=W, padx=5, pady=5)
        self.txtUniversityEmail = Entry(StudentFrame, font=('arail',12,'bold'), bd=5, width=35, justify='left',
                                  textvariable=self.UniversityEmail)
        self.txtUniversityEmail.grid(row=8, column=1)
        
        self.lblAddress = Label(StudentFrame, font=('arial',12,'bold'), text='Address', bd=7, anchor='w', justify=LEFT)
        self.lblAddress.grid(row=9, column=0, sticky=W, padx=5, pady=5)
        self.txtAddress = Entry(StudentFrame, font=('arail',12,'bold'), bd=5, width=35, justify='left',
                                  textvariable=self.Address)
        self.txtAddress.grid(row=9, column=1)
        
        #============================================CourseFrame====================================================
        
        self.lblDean = Label(CourseFrame, font=('arial',12,'bold'), text='Dean', bd=7, justify=RIGHT)
        self.lblDean.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.cboDean = ttk.Combobox(CourseFrame, textvariable=self.Dean,
                                      font=('arail',12,'bold'), width=42, state = 'randomly', justify='left')
        self.cboDean['value'] = ('','Mr. George Omono','Mr. Caleb Oula','Mrs Wendy Jane', 'Mrs Phoebe Awuor', 
                                   'Mr. Joash Okelo', 'Mr. Otieno Osodo')
        self.cboDean.grid(row=2, column=1)
        
        self.lblSchool = Label(CourseFrame, font=('arial',12,'bold'), text='School', bd=7, justify=RIGHT)
        self.lblSchool.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.cboSchool = ttk.Combobox(CourseFrame, textvariable=self.School,
                                      font=('arail',12,'bold'), width=42, state = 'randomly', justify='left')
        self.cboSchool['value'] = ('','COMPUTING AND INFORMATICS','MEDICINE','BUSINESS & ECONOMICS', 'NURSING', 
                                   'AGRICULTURE & FOOD SECURITY', 'ARTS & SOCIAL SCIENCES', 'EDUCATION')
        self.cboSchool.grid(row=1, column=1)
        
        self.lblCourse = Label(CourseFrame, font=('arial',12,'bold'), text='Course', bd=7, justify=RIGHT)
        self.lblCourse.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.cboCourse = ttk.Combobox(CourseFrame, textvariable=self.Course,
                                      font=('arail',12,'bold'), width=42, state = 'randomly', justify='left')
        self.cboCourse['value'] = ('','Information Technology','Nursing','Teaching', 'Linguistics','Phsycology', 
                                   'Farming', 'Accounting', 'Laboratory Technician')
        self.cboCourse.grid(row=0, column=1)
        self.cboCourse.bind('<<ComboboxSelected>>', CourseData)
        
        self.lblUnits = Label(CourseFrame, font=('arial',12,'bold'), text='Units', bd=7, justify=RIGHT)
        self.lblUnits.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.cboUnits = ttk.Combobox(CourseFrame, textvariable=self.Units,
                                      font=('arail',12,'bold'), width=42, state = 'randomly', justify='left')
        self.cboUnits['value'] = ('0','11','10', '7', '6', '9')
        self.cboUnits.grid(row=3, column=1)
        
        self.lblStage = Label(CourseFrame, font=('arial',12,'bold'), text='Stage', bd=7, justify=RIGHT)
        self.lblStage.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.cboStage = ttk.Combobox(CourseFrame, textvariable=self.Stage,
                                      font=('arail',12,'bold'), width=42, state = 'randomly', justify='left')
        self.cboStage['value'] = ('','Year1 Semister1','Year1 Semister2','Year2 Semister1', 'Year2 Semister2', 
                                   'Year3 Semister1', 'Year3 Semister2', 'Year4 Semister1','Year4 Semister1')
        self.cboStage.current(0)
        self.cboStage.grid(row=4, column=1)
        
        self.lblYOS = Label(CourseFrame, font=('arial',12,'bold'), text='Year of Study', bd=7, justify=RIGHT)
        self.lblYOS.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.txtYOS= Entry(CourseFrame, font=('arail',12,'bold'), bd=5, width=42, justify='left',
                                  textvariable=self.YOS)
        self.txtYOS.grid(row=5, column=1)
        
        self.lblAccommodation = Label(CourseFrame, font=('arial',12,'bold'), text='Accommodation', bd=7, justify=RIGHT)
        self.lblAccommodation.grid(row=6, column=0, sticky=W, padx=5, pady=5)
        self.cboAccommodation = ttk.Combobox(CourseFrame, textvariable=self.Accomodation,
                                      font=('arail',12,'bold'), width=42, state = 'randomly', justify='left')
        self.cboAccommodation['value'] = ('','Yes', 'No')
        self.cboAccommodation.current(0)
        self.cboAccommodation.grid(row=6, column=1)
       
        #============================================StudentStatusFrame====================================================
        
        self.lblMaritalStatus = Label(StudentStatusFrame, font=('arial',12,'bold'), text='Marital Status', bd=7, justify=RIGHT)
        self.lblMaritalStatus.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.cboMaritalStatus = ttk.Combobox(StudentStatusFrame, textvariable=self.MaritalStatus,
                                      font=('arail',12,'bold'), width=44, state = 'randomly', justify='left')
        self.cboMaritalStatus['value'] = ('','Single','Married')
        self.cboMaritalStatus.current(0)
        self.cboMaritalStatus.grid(row=0, column=1)
        
        self.lblParent = Label(StudentStatusFrame, font=('arial',12,'bold'), text='Parent', bd=7, justify=RIGHT)
        self.lblParent.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.cboParent = ttk.Combobox(StudentStatusFrame, textvariable=self.Parent,
                                      font=('arail',12,'bold'), width=44, state = 'randomly', justify='left')
        self.cboParent['value'] = ('','Father', 'Mother', 'Both parents Present', 'Both parents diseased')
        self.cboParent.current(0)
        self.cboParent.grid(row=1, column=1)
        
        self.lblCountry = Label(StudentStatusFrame, font=('arial',12,'bold'), text='Country', bd=7, justify=RIGHT)
        self.lblCountry.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtCountry= Entry(StudentStatusFrame, font=('arail',12,'bold'), bd=5, width=44, justify='left',
                                  textvariable=self.Country)
        self.txtCountry.grid(row=2, column=1)
        
        self.lblCounty = Label(StudentStatusFrame, font=('arial',12,'bold'), text='County', bd=7, justify=RIGHT)
        self.lblCounty.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtCounty= Entry(StudentStatusFrame, font=('arail',12,'bold'), bd=5, width=44, justify='left',
                                  textvariable=self.County)
        self.txtCounty.grid(row=3, column=1)
        
        #=============================================ButtonFrame====================================================
        
        self.btnAddNew = Button(ButtonFrame, pady=1, bd=4, font=('arial',16), padx=11,
                                width=5, text="Add New", command= addData).grid(row=0, column=0, padx=2)
        
        self.btnUpdate = Button(ButtonFrame, pady=1, bd=4, font=('arial',16), padx=12,
                                width=5, text="Update").grid(row=0, column=1, pady=5)
        
        self.btnDelete = Button(ButtonFrame, pady=1, bd=4, font=('arial',16), padx=12,
                                width=5, text="Delete").grid(row=0, column=2, pady=5)
        
        self.btnReset = Button(ButtonFrame, pady=1, bd=4, font=('arial',16), padx=12,
                                width=5, text="Reset", command=Reset).grid(row=0, column=3, pady=5)
        
        self.btnExit = Button(ButtonFrame, pady=1, bd=4, font=('arial',16), padx=12,
                                width=5, text="Exit", command= iExit).grid(row=0, column=4, pady=5)
        
        
if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
        