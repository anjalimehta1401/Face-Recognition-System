from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql


class register:

    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry('1350x700+0+0')

        #===========bg image==========

        self.bg= ImageTk.PhotoImage(file="images/trgf.jpg")
        bg = Label(self.root, image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        im= Image.open('images/frm.jpg')
        im= im.resize((400,400))

        self.lfbg = ImageTk.PhotoImage(im)
        lfbg = Label(self.root, image=self.lfbg).place(x=80, y=130)

        #=======register frame=====
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=80, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("Times New Roman", 20, "bold"), bg="white",fg="green").place(x=30,y=30)

        #-----------details----------

        f_name = Label(frame1,text="First Name", font=("Times New Roman", 15, "bold"), bg="white",fg="black").place(x=30,y=90)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=30, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("Times New Roman", 15, "bold"), bg="white", fg="black").place(
            x=400, y=90)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=400, y=130, width=250)

        #----------contact------------

        Pno = Label(frame1, text="Contact No", font=("Times New Roman", 15, "bold"), bg="white", fg="black").place(
            x=30, y=170)
        self.txt_Pno = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_Pno.place(x=30, y=200, width=250)


        email = Label(frame1, text="Email Id", font=("Times New Roman", 15, "bold"), bg="white", fg="black").place(
            x=400, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=400, y=200, width=250)


        #--------------Branch-------------

        Branch = Label(frame1, text="Branch", font=("Times New Roman", 15, "bold"), bg="white", fg="black").place(
            x=30, y=240)
        self.cmb_Branch = ttk.Combobox(frame1, font=("times new roman", 12),state='readonly',justify=CENTER)
        self.cmb_Branch['values']=("Select","Computer Science" , "information Technology", "Electronics And communications","Electrical ","Mechanical","Ciivil")
        self.cmb_Branch.place(x=30, y=270, width=250)
        self.cmb_Branch.current(0)

        college_id = Label(frame1, text="College Id", font=("Times New Roman", 15, "bold"), bg="white", fg="black").place(
            x=400, y=240)
        self.txt_college_id = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_college_id.place(x=400, y=270, width=250)


        #---------Buttons---------
        self.var_chk= IntVar()
        chk= Checkbutton(frame1,text=" I Agree with The Terms & Conditions Mentioned ",font=("times new roman",12),variable=self.var_chk,onvalue=1,offvalue=0).place(x=30,y=370)


        reg_button=Button(frame1,text="REGISTER FACE",font=("times new roman",15,"bold"),bd=6,bg='lightgrey',cursor="hand2",command=self.register_working).place(x=400,y=370,width=180)
        login_button = Button(self.root, text="Login", font=("times new roman", 15,"bold"),command=self.login_wind, bd=8, bg='white',
                            cursor="hand2").place(x=380, y=535, width=100)


    def login_wind(self):
        self.root.destroy()
        import login

    def clearall(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_Pno.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_college_id.delete(0, END)
        self.cmb_Branch.current(0)


    def register_working(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_Pno.get()=="" or self.txt_college_id.get()=="" or self.cmb_Branch.get()=="Select" or self.txt_email.get()=="" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)

        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Agree to Terms & Conditions", parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="studentsinfo")
                cur=con.cursor()
                cur.execute("select * from students where collegeid=%s",self.txt_college_id.get())
                row=cur.fetchone()
                #print(row)

                if row!=None:
                    messagebox.showerror("Error", " User Already Exists ", parent=self.root)

                else:
                    cur.execute(
                        "insert into students (fname,lname,pno,email,branch,collegeid) values(%s,%s,%s,%s,%s,%s)",
                        (
                            self.txt_fname.get(),
                            self.txt_lname.get(),
                            self.txt_Pno.get(),
                            self.txt_email.get(),
                            self.cmb_Branch.get(),
                            self.txt_college_id.get()

                        ))
                    con.commit()
                    con.close()

                    #messagebox.showinfo("success", "Registered Successfully", parent=self.root)
                    self.clearall()
                    self.root.destroy()
                    import train



            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)









root=Tk()
obj=register(root)
root.mainloop()