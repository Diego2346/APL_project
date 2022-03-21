from tkinter import *
from tkinter import ttk,messagebox
import gym

class Page(Frame):
    def __init__(self,root):
        Frame.__init__(self)
    def show(self):
        self.lift()
        self.wait_window()


   
class home(Page):
 def __init__(self, root,user,db):
  Page.__init__(self, root)
  global DB,USER
  DB=db
  USER=user
  Button(self,text="Logout",command=self.destroy, bg="red", width = 10).place(relx=0.9, rely=0.04)
  Label(self,text = "I tuoi dati", font=("Calibri",30)).place(relx=0.05,rely=0.1)
  Label(self,text = "ID:  " +str(USER.userId)).place(relx=0.05,rely=0.20)
  Label(self,text = "Nome:  "+USER.nome).place(relx=0.05,rely=0.25)
  Label(self,text = "Cognome:  "+USER.cognome).place(relx=0.05,rely=0.30)
  Label(self,text = "Indirizzo:  "+USER.indirizzo).place(relx=0.05,rely=0.35)
  Label(self,text = "Data di nascita:  "+USER.dataDiNascita).place(relx=0.05,rely=0.40)
  Label(self,text = "Data di iscrizione:  "+USER.dataIscrizione).place(relx=0.05,rely=0.45)
  self.email=StringVar()
  Label(self,text = "Email: ").place(relx=0.05,rely=0.5)
  e=Entry(self,textvariable = self.email, width = "20")
  e.insert(0,USER.email)
  e.place(relx=0.12, rely=0.5)
  
  self.username=StringVar()
  Label(self,text = "Username: ").place(relx=0.05,rely=0.55)
  u=Entry(self,textvariable = self.username, width = "20")
  u.insert(0,USER.username)
  u.place(relx=0.12, rely=0.55) 
  
  self.password=StringVar()
  Label(self,text = "Password: ").place(relx=0.05,rely=0.60)
  p=Entry(self,textvariable = self.password, width = "20")
  p.insert(0,USER.password)
  p.place(relx=0.12, rely=0.60)
  
  Button(self,text="Modifica",command=self.clicked_modify_user, bg="#94b9ff",height = 1, width =14).place(relx=0.08, rely=0.7)

     
     
  Label(self,text = "I tuoi Corsi", font=("Calibri",30)).place(relx=0.4,rely=0.03) 
  self.table1 = ttk.Treeview(self , columns = ("1" , "2" , "3" , "4" ) )
  self.table1.column("#0", width=100, minwidth=100)
  self.table1.heading("#0", text = "Nome")
  self.table1.heading("1", text = "Giorni")
  self.table1.heading("2", text = "Costo")
  self.table1.heading("3", text = "Tenuto da")
  self.table1.place(relx=0.4,rely=0.15,width=650,height=150)
  Button(self,text="Disiscriviti",command=self.clicked_remove_membership, bg="#ff8585",height = 1, width =14).place(relx=0.4, rely=0.45)
  
  Label(self,text = "Altri Corsi", font=("Calibri",30)).place(relx=0.4,rely=0.5) 
  self.table2 = ttk.Treeview(self , columns = ("1" , "2" , "3" , "4" ) )
  self.table2.column("#0", width=100, minwidth=100)
  self.table2.heading("#0", text = "Nome")
  self.table2.heading("1", text = "Giorni")
  self.table2.heading("2", text = "Costo")
  self.table2.heading("3", text = "Tenuto da")
  self.table2.place(relx=0.4,rely=0.6,width=650,height=150)
  Button(self,text="Iscriviti",command=self.clicked_add_membership, bg="#adffb3",height = 1, width =14).place(relx=0.4, rely=0.9)
  self.show_tables() 
  
 def show_tables(self):
    self.table1.delete(*self.table1.get_children())
    self.table2.delete(*self.table2.get_children())
    myCourses=[]
    for x in gym.getAllCourses(DB):
        #TABELLA 1
        for y in gym.getAllMemberships(DB): 
            for z in gym.getAllInstructors(DB):
             if y.userId==USER.userId and x.courseName==y.courseName and x.instructorId==z.instructorId:
               self.table1.insert( '', END,text=x.courseName, values=([x.days],str(x.monthlyCost)+' ' +'\u20ac',(z.name,z.surname)))
        for child in self.table1.get_children(): myCourses=self.table1.item(child)["text"]
        #TABELLA 2
        for z in gym.getAllInstructors(DB):
         if(myCourses!=x.courseName and x.instructorId==z.instructorId):
             self.table2.insert( '', END,text=x.courseName, values=(x.days,str(x.monthlyCost)+' ' +'\u20ac',(z.name,z.surname)))               
    self.after(20000, self.show_tables)
    
 def clicked_remove_membership(self):
     gym.removeMembership(USER.userId,self.table1.item(self.table1.focus(),'text'),DB)
     self.show_tables()
     
 def clicked_add_membership(self):
     new_membership=gym.Membership(self.table2.item(self.table2.focus(),'text'),USER.userId)
     gym.createMembership(new_membership,DB)
     self.show_tables()
 def clicked_modify_user(self):
      try:
         gym.modifyUser(USER.userId,self.email.get(),self.username.get(),self.password.get(),DB)
         messagebox.showinfo('Gym', 'Dati modificati')
      except:
         messagebox.showerror('Gym', 'Impossibile modificare')
         
         
         
         
         