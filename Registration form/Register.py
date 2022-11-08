from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Form")
        self.root.geometry("1920x1080+0+0")
        #======Bg Image===
        
        
        self.bg=ImageTk.PhotoImage(file="C:/Users/kapil/Desktop/Registration form/Images/bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
    
        #2nd image
        self.second=ImageTk.PhotoImage(file="C:/Users/kapil/Desktop/Registration form/Images/2ndd.jpg")
        second=Label(self.root,image=self.second).place(x=300,y=170,width=950,height=500)
        
        #3rd image
        self.third=ImageTk.PhotoImage(file="C:/Users/kapil/Desktop/Registration form/Images/3rd.jpg")
        third=Label(self.root,image=self.third).place(x=300,y=100,width=950,height=70)
        
        #frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=320,y=190,width=910,height=460)
        
        title=Label(frame1,text="REGISTER/LOGIN",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=50,y=30)
        
        
        
        title=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=70)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=100,width=250)
        
        
        title=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=340,y=70)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=340,y=100,width=250)
        
        
        # title=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=630,y=70)
        # txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=630,y=100,width=250)
        
        title=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=140)
        self.txt_cname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cname.place(x=50,y=170,width=250)
        
        
        title=Label(frame1,text="E-mail",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=340,y=140)
        self.txt_ename=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_ename.place(x=340,y=170,width=250)
        
        
        title=Label(frame1,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=210)
        self.cmb_gender=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_gender['values']=("Select","Male","Female","Others")
        self.cmb_gender.place(x=50,y=240,width=250)
        self.cmb_gender.current(0)
        
        title=Label(frame1,text="D.O.B(yyyy-mm-dd)",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=340,y=210)
        self.txt_dob=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_dob.place(x=340,y=240,width=250)
        
        
        title=Label(frame1,text="Father's Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=280)
        self.txt_father=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_father.place(x=50,y=310,width=250)
        
        
        title=Label(frame1,text="Mother's Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=340,y=280)
        self.txt_mother=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_mother.place(x=340,y=310,width=250)
        
        
        title=Label(frame1,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=350)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=380,width=250)
        
        
        title=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=340,y=350)
        self.txt_cpass=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpass.place(x=340,y=380,width=250)
        
        
        #Terms & conditions---------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=420)
        
        btn_reg=Button(self.root,text="Register Now",font=("times of roman",20,"bold"),bg="green",bd=1,fg="white",cursor="hand2",command=self.register_data).place(x=970,y=350)
        
        btn_log=Button(self.root,text="Sign In",font=("times of roman",20,"bold"),bg="white",bd=2,fg="black",cursor="hand2").place(x=1010,y=440)
        
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_cname.delete(0,END)
        self.txt_ename.delete(0,END)
        self.cmb_gender.current(0)
        self.txt_dob.delete(0,END)
        self.txt_father.delete(0,END)
        self.txt_mother.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpass.delete(0,END)
        
    def register_data(self):
         if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_cname.get()=="" or self.txt_ename.get()=="" or self.cmb_gender.get()=="Select" or self.txt_dob.get()=="" or self.txt_father.get()=="" or self.txt_mother.get()=="" or self.txt_password.get()=="" or self.txt_cpass.get()=="":               
            messagebox.showerror("Error","Something is Wrong")
         elif self.txt_password.get() != self.txt_cpass.get():
            messagebox.showerror("Error","New Password and Confirm Password should be Same")
         elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms And Conditions")
         else:
             try:
                 con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                 cur=con.cursor()
                 cur.execute("select * from employee where ename=%s",self.txt_ename.get())
                 row=cur.fetchone()
                 if row!=None:
                     print(row)
                     messagebox.showerror("Error","User already Exist, Please try with another E-mail",parent=self.root)
                 else:
                     cur.execute("insert into employee (fname,lname,cname,ename,gender,dob,father,mother,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (self.txt_fname.get(),
                               self.txt_lname.get(),
                               self.txt_cname.get(),
                               self.txt_ename.get(),
                               self.cmb_gender.get(),
                               self.txt_dob.get(),
                               self.txt_father.get(),
                               self.txt_mother.get(),
                               self.txt_password.get()
                               ))
                     con.commit()
                     con.close()
                     messagebox.showinfo("Success","Registration Successful",parent=self.root)
                     self.clear()
                 
             except Exception as es:
                 messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

        
root=Tk()
obj=Register(root)
root.mainloop()    