from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import PIL
import time
from math import *
import pymysql
from tkinter import messagebox



class login_window:

    def __init__(self,root):

        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #title = Label(self.root, text="Analog Clock", font=("Times New Roman", 50, "bold"), bg="#04444a", fg="white").place(x=0,y=50,relwidth=1)

        self.bg = ImageTk.PhotoImage(file="images/saddf.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        '''

        #==============background==========
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)
        
        '''

        # ==========frames===========
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=260,y=155,width=770,height=400)

        title=Label(login_frame,text="LOGIN NOW",font=('times new roman',25,"bold"),bg="white",fg="blue")
        title.place(x=200,y=50)


        fstname=Label(login_frame,text="First Name",font=("times new roman",14,"bold"),bg="white",fg="black")
        fstname.place(x=260,y=120)
        self.txt_fstname=Entry(login_frame,font=('times new roman',12),bg="lightgray")
        self.txt_fstname.place(x=260,y=150,width=200)

        lstname = Label(login_frame, text="Last Name", font=("times new roman", 14, "bold"), bg="white", fg="black")
        lstname.place(x=520, y=120)
        self.txt_lstname = Entry(login_frame, font=('times new roman', 12), bg="lightgray")
        self.txt_lstname.place(x=520, y=150, width=200)

        colid = Label(login_frame, text="Collegeid", font=("times new roman", 14, "bold"), bg="white", fg="black")
        colid.place(x=260, y=200)
        self.txt_colid = Entry(login_frame, font=('times new roman', 12), bg="lightgray")
        self.txt_colid.place(x=260, y=230, width=200)


        btn_reg=Button(login_frame,text="New User? \n Register Now",font=("times new roman",12,"bold"),command=self.register_window,bg="white",cursor="hand2",   fg="red",bd=0)
        btn_reg.place(x=260,y=280)

        btn_log = Button(login_frame, text="Login", font=("times new roman", 16, "bold"),command=self.login,
                         bg="lightgray", fg="black",cursor="hand2", bd=5)
        btn_log.place(x=520, y=230,width=120)


        #=========Clock=====================
        self.lbl=Label(self.root,bg='black',bd=0)
        self.lbl.place(x=140,y=220,height=280,width=280)


        #self.clock_image()
        self.working()


    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_fstname.get()=="" or self.txt_colid.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="studentsinfo")
                cur=con.cursor()
                cur.execute("select * from students where collegeid=%s",self.txt_colid.get())
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error", "User not Found \n Register for new User", parent=self.root)

                else:
                    self.root.destroy()
                    import recognize

                    #messagebox.showinfo("Success","Login Successful")

                con.close()


            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)






    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB", (300, 300), (0, 0, 0))
        draw=ImageDraw.Draw(clock)
        bg=Image.open('images/cccc.png')
        bg =bg.resize((220, 220), Image.ANTIALIAS)
        clock.paste(bg, (40, 50))


        origin=150,156
        #==========hour line
        draw.line((origin, 150+50*sin(radians(hr)), 150-50*cos(radians(hr))), fill='green',width=4)
        # ==========hour line
        draw.line((origin, 160+80*sin(radians(min_)), 160-80*cos(radians(min_))), fill='blue',width=4)
        # ==========hour line
        draw.line((origin, 155+100*sin(radians(sec_)), 155-100*cos(radians(sec_))), fill='red',width=4)
        # ==========hour eclipse
        draw.ellipse((146, 152, 156, 162), fill='black')

        clock.save('images/clock_new.jpg')


    def working(self):

        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr,min_,sec_)
        self.im=PIL.Image.open('images/clock_new.jpg')
        self.img=ImageTk.PhotoImage(self.im)
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

root=Tk()
obj=login_window(root)
root.mainloop()