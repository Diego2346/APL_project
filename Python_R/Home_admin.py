from tkinter import *
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
import gym
import rpy2.robjects as ro

class Page(Frame):
 def __init__(self,root):
   Frame.__init__(self)
 def show(self):
   self.lift()

class Stats(Page):
 def __init__(self,root):
  Page.__init__(self,root)
  self.R=ro.r
  self.R.source("Stats.R")
  
  Label(self,text = "ELENCO PARTECIPANTI\nDI OGNI CORSO ",font=("Calibri",20)).place(relx=0.15, rely=0.1)
  Button(self,text="Scegli corso",command=self.choose_course, bg="light blue",height = 3,width=20).place(relx=0.19,rely=0.3)
  
  Label(self,text = "STATISTICHE ",font=("Calibri",20)).place(relx=0.6, rely=0.1)
  Button(self,text="Numero iscriti per corso",command=self.Stat1, bg="antiquewhite",height = 2,width=20).place(relx=0.6,rely=0.3)
  Button(self,text="Guadagno per corso",command=self.Stat2, bg="bisque",height = 2,width=20).place(relx=0.6,rely=0.4)
  Button(self,text="Corsi tenuti per istruttore",command=self.Stat3, bg="burlywood1",height = 2,width=20).place(relx=0.6,rely=0.5)
  Button(self,text="Numero iscrizioni per data",command=self.Stat4, bg="burlywood2",height = 2,width=20).place(relx=0.6,rely=0.6)
  Button(self,text="Clienti per sesso ed eta",command=self.Stat5, bg="burlywood3",height = 2,width=20).place(relx=0.6,rely=0.7)

 def choose_course(self):
  self.list = Listbox(self, selectmode = "single")
  self.list.place(relx = 0.2, rely = 0.45)
  for x in gym.getAllCourses(DB): self.list.insert(END, x.courseName) 
  Button(self,text="Mostra partecipanti",command=self.show_partecipants, bg="light green",height = 1, width =16).place(relx=0.2,rely=0.8)
    
        
 def show_partecipants(self):
     memberships=[]
     users=[]
     for x in gym.getAllMemberships(DB): memberships.append(x.courseName)  
     course=self.list.get(self.list.curselection())
     if course  not in memberships: 
         messagebox.showinfo('Gym', 'Non ci sono partecipanti in questo corso')
     else: 
         for x in gym.getAllUsers(DB):
          for y in gym.getAllMemberships(DB):
                 if x.userId == y.userId and y.courseName==course: 
                     users.append([x.nome+' '+x.cognome])
         self.R.List_partecipants(course,users)

 def Stat1(self):
    subs=[]
    for x in gym.getAllMemberships(DB): subs.append(x.courseName)
    self.R.Stat1(subs)
    
 def Stat2(self):
   subs=[]
   costs=[]
   for x in gym.getAllMemberships(DB): subs.append(x.courseName)
   for y in gym.getAllCourses(DB):
     if  y.courseName in subs: costs.append(y.monthlyCost)
   self.R.Stat2(subs,costs)
   
 def Stat3(self):
    instructors=[]    
    for x in gym.getAllInstructors(DB):
     for y in gym.getAllCourses(DB):
      if x.instructorId == y.instructorId: instructors.append(x.name+' '+x.surname)
    self.R.Stat3(instructors)

 def Stat4(self):
    date=[]
    for x in gym.getAllUsers(DB):
        date.append(x.dataIscrizione[:10])
    self.R.Stat4(date)
    
 def Stat5(self):
    genders=[]
    birthDates=[]
    for x in gym.getAllUsers(DB):
        genders.append(x.gender)
        birthDates.append(x.dataDiNascita)
    self.R.Stat5(genders,birthDates)
 
 

class Subscription(Page):
 def __init__(self,root):
  Page.__init__(self,root)

  Label(self,text = "ISCRIVI CLIENTE ",font=("Calibri",20)).place(relx=0.1, rely=0.05)
  #NOME
  self.name = StringVar()
  Label(self,text = "Nome ",).place(relx = 0.05, rely = 0.1)
  Entry(self,textvariable = self.name, width = "30").place(relx = 0.05, rely = 0.15)
  #COGNOME
  self.surname = StringVar()
  Label(self,text = "Cognome ",).place(relx = 0.05, rely = 0.20)
  Entry(self,textvariable = self.surname, width = "30").place(relx = 0.05, rely = 0.25)
  #SESSO
  self.gender= StringVar()
  Label(self,text = "Sesso ",).place(relx = 0.25, rely = 0.20)
  Radiobutton(self, text="Maschio", variable=self.gender,value="M").place(relx = 0.25, rely = 0.25)
  Radiobutton(self, text="Femmina", variable=self.gender,value="F",tristatevalue=0).place(relx = 0.25, rely = 0.30)
  self.gender.set('M')
  #NASCITA
  Label(self,text = "Data di nascita ",).place(relx = 0.05, rely = 0.30)
  self.birth=DateEntry(self, width = "27",year=1997, date_pattern="dd/mm/yyyy")
  self.birth.place(relx = 0.05, rely = 0.35)
  #EMAil
  self.email = StringVar()
  Label(self,text = "Email ",).place(relx = 0.05, rely = 0.4)
  Entry(self,textvariable = self.email, width = "30").place(relx = 0.05, rely = 0.45)
  #INDIRIZZO
  self.address = StringVar()
  Label(self,text = "Indirizzo ",).place(relx = 0.05, rely = 0.5)
  Entry(self,textvariable = self.address, width = "30").place(relx = 0.05, rely = 0.55)
  #uSERNAME
  self.username = StringVar()
  Label(self,text = "Username ",).place(relx = 0.05, rely = 0.60)
  Entry(self,textvariable = self.username, width = "30").place(relx = 0.05, rely = 0.65)
  #uSERNAME
  self.psw = StringVar()
  Label(self,text = "Password ",).place(relx = 0.05, rely = 0.7)
  Entry(self,textvariable = self.psw, width = "30").place(relx = 0.05, rely = 0.75)
  #CORSI
  Label(self,text = "Seleziona uno o piu corsi ",).place(relx = 0.25, rely = 0.4)
  self.list = Listbox(self, selectmode = "multiple")
  self.list.place(relx = 0.25, rely = 0.45)
    
  Button(self,text="Salva",command=self.clicked_add_user, bg="#adffb3",height = 1, width =14).place(relx=0.2,rely=0.8)
  
 #CLIENTI
 
  Label(self,text = "CLIENTI ",font=("Calibri",20)).place(relx=0.65, rely=0.05)
  self.table = ttk.Treeview(self , columns = ("1" , "2" , "3" , "4" ) )
  self.table.column("#0", width=50, minwidth=50)
  self.table.heading("#0", text = "ID")
  self.table.column("1", width=100, minwidth=100)
  self.table.heading("1", text = "Nome")
  self.table.column("2", width=100, minwidth=100)
  self.table.heading("2", text = "Cognome")
  self.table.heading("3", text = "email")
  self.table.heading("4", text = "indirizzo")
  self.table.place(relx=0.45,rely=0.15,width=650)
  self.table.insert( '', END,text='1234', values=("Mario","Rossi"))
  self.show_table()
 
  Button(self,text="Rimuovi", command=self.clicked_remove_user, bg="#ff8585",height = 1, width =14).place(relx=0.65, rely=0.7)
  
 
 def show_table(self):
    self.table.delete(*self.table.get_children())
    for x in gym.getAllUsers(DB):  self.table.insert( '', END,text=x.userId, values=(x.nome,x.cognome,x.email,x.indirizzo))
    #LISTA CORSI
    self.list.delete(0,'end')
    for x in gym.getAllCourses(DB): self.list.insert(END, x.courseName) 
    self.after(50000, self.show_table)
    
 def clicked_add_user(self):
    try:
        if(''not in (self.name.get(),self.surname.get(),self.address.get(),self.birth.get(),self.email.get()
                          ,self.username.get(),self.psw.get())):
           new_user=gym.User(self.name.get(),self.surname.get(),self.gender.get(),self.address.get(),self.birth.get(),self.email.get()
                          ,self.username.get(),self.psw.get())
           gym.createUser(new_user,DB)
           for x in gym.getAllUsers(DB):
            if x.username==self.username.get():
              for sub in self.list.curselection():
                   new_membership=gym.Membership(self.list.get(sub),x.userId)
                   gym.createMembership(new_membership,DB)
           messagebox.showinfo('Gym','Cliente aggiunto ')
    except RuntimeError:  messagebox.showerror('Gym','Impossibile aggiungere cliente ')
    self.show_table()
     
 def clicked_remove_user(self):
     gym.removeUser(self.table.item(self.table.focus(),'text'),DB)
     self.show_table()

class Instructor(Page):
 def __init__(self,root):
  Page.__init__(self,root)
  Label(self,text = "AGGIUNGI ISTRUTTORE ",font=("Calibri",20)).place(relx=0.1, rely=0.05)
  #NOME
  self.name = StringVar()
  Label(self,text = "Nome ",).place(relx = 0.05, rely = 0.1)
  Entry(self,textvariable = self.name, width = "30").place(relx = 0.05, rely = 0.15)
  #COGNOME
  self.surname = StringVar()
  Label(self,text = "Cognome ",).place(relx = 0.05, rely = 0.2)
  Entry(self,textvariable = self.surname, width = "30").place(relx = 0.05, rely = 0.25)
 
  Button(self,text="Salva",command=self.clicked_add_instructor, bg="#adffb3",height = 1, width =14).place(relx=0.2,rely=0.5)

 #ISTRUTTORI
 
  Label(self,text = "ISTRUTTORI ",font=("Calibri",20)).place(relx=0.65, rely=0.05)
  self.table = ttk.Treeview(self , columns = ("1" , "2" , "3" , "4" ) )
  self.table.column("#0", width=50, minwidth=50)
  self.table.heading("#0", text = "ID")
  self.table.column("1", width=100, minwidth=100)
  self.table.heading("1", text = "Nome")
  self.table.column("2", width=100, minwidth=100)
  self.table.heading("2", text = "Cognome")
  self.table.place(relx=0.45,rely=0.15,width=650)
  self.show_table()
  
  Button(self,text="Rimuovi",command=self.clicked_remove_instructor, bg="#ff8585",height = 1, width =14).place(relx=0.65, rely=0.7)
  
 def show_table(self):
    self.table.delete(*self.table.get_children())
    for x in gym.getAllInstructors(DB): self.table.insert( '', END,text=x.instructorId, values=(x.name,x.surname))
    self.after(50000, self.show_table)
    
 def clicked_add_instructor(self):
    try:  
         if(''not in (self.name.get(),self.surname.get())):
          new_instructor=gym.Istruttore(self.name.get(),self.surname.get())
          gym.createInstructor(new_instructor,DB)
          messagebox.showinfo('Gym','Istruttore aggiunto')
    except RuntimeError: 
          messagebox.showerror('Gym','Impossibile aggiunger istrutore')
    self.show_table()
     
 def clicked_remove_instructor(self):
     gym.removeInstructor(self.table.item(self.table.focus(),'text'),DB)
     self.show_table()
  
 
class Course(Page):
 def __init__(self,root):
  Page.__init__(self,root)
  
  #CORSI
  Label(self,text = "AGGIUNGI CORSO",font=("Calibri",20)).place(relx=0.1, rely=0.05)
  #NOME
  self.name = StringVar()
  Label(self,text = "Nome corso",).place(relx = 0.05, rely = 0.1)
  Entry(self,textvariable = self.name, width = "30").place(relx = 0.05, rely = 0.15)
  #GIORNI            
  self.days = StringVar()
  Label(self,text = "Giorni ",).place(relx = 0.05, rely = 0.20)
  Entry(self,textvariable = self.days, width = "30").place(relx = 0.05, rely = 0.25)
  #COSTO
  self.cost = DoubleVar()
  Label(self,text = "Costo mensile ",).place(relx = 0.05, rely = 0.30)
  Label(self,text = " \u20ac",).place(relx = 0.105, rely = 0.35)
  Entry(self,textvariable = self.cost, width = "10").place(relx = 0.05, rely = 0.35)
  
  #ISTRUTTORI
  Label(self,text = "Tenuto da ",).place(relx = 0.25, rely = 0.2)
  self.table1 = ttk.Treeview(self , columns = ("1" ) )
  self.table1.column("#0", width=30, minwidth=20)
  self.table1.column("1", width=70, minwidth=30)
  self.table1.heading("#0", text='ID')
  self.table1.heading("1", text='Nome')
  self.table1.place(relx = 0.25, rely = 0.25,width=180,height=180)
  
  Button(self,text="Salva",command=self.clicked_add_course, bg="#adffb3",height = 1, width =14).place(relx=0.2,rely=0.7)
  
  #CORSI
  Label(self,text = "CORSI ",font=("Calibri",20)).place(relx=0.65, rely=0.05)
  self.table2 = ttk.Treeview(self , columns = ("1" , "2" , "3" , "4" ) )
  self.table2.column("#0", width=100, minwidth=100)
  self.table2.heading("#0", text = "Nome")
  self.table2.heading("1", text = "Giorni")
  self.table2.column("2", width=100, minwidth=100)
  self.table2.heading("2", text = "Costo")
  self.table2.heading("3", text = "Tenuto da")
  self.table2.place(relx=0.45,rely=0.15,width=650)
  self.show_tables()
  
  Button(self,text="Rimuovi",command=self.clicked_remove_course,bg="#ff8585",height = 1, width =14).place(relx=0.65, rely=0.7)
  
     
 def show_tables(self):
    self.table1.delete(*self.table1.get_children())
    self.table2.delete(*self.table2.get_children())
    for x in gym.getAllInstructors(DB): 
        self.table1.insert('', END,text=x.instructorId, value=([(x.name,x.surname)])) 
    for x in gym.getAllCourses(DB):  
          for y in gym.getAllInstructors(DB): 
              if(y.instructorId==x.instructorId):
               self.table2.insert( '', END,text=x.courseName, values=(x.days,str(x.monthlyCost)+' ' +'\u20ac',([y.name,y.surname])))
    self.after(50000, self.show_tables)
    
 def clicked_add_course(self):
    selected_id = self.table1.item(self.table1.focus(),'text')
    try:
        if('' not in (self.name.get(),self.days.get(),self.cost.get(),selected_id)):
          new_course=gym.Corso(self.name.get(),self.days.get(),self.cost.get(),selected_id)
          gym.createCourse(new_course,DB)
          messagebox.showinfo('Gym','Corso aggiunto')
    except: messagebox.showerror('Gym','Impossibile aggiungere corso')
    self.show_tables()
     
 def clicked_remove_course(self):
     gym.removeCourse(self.table2.item(self.table2.focus(),'text'),DB)
     self.show_tables()

class home(Page):
 def __init__(self,root,admin,db):
  Page.__init__(self,root)
  self.configure(background='white')
  global DB
  DB=db
  p1 = Subscription(self)
  p2 = Instructor(self)
  p3 = Course(self)
  p4 = Stats(self)
  
  buttonframe = Frame(self)
  container = Frame(self)
  buttonframe.pack(side="top",expand=False)
  container.pack(side="top",fill="both" ,expand=True)
  Label(self,text = "Benvenuto, "+admin.nome+' '+admin.cognome,font=("Calibri",50),bg="white").place( x=5, y=25, relwidth=1, relheight=0.5) 
  Label(self,bg="white").place( x=0, y=300, relwidth=1, relheight=1) 

  #img = PhotoImage(file="gym.png")
  #bg = Label(self,image=img)
  #bg.image=img
  #bg.place(in_=container,y=80, relwidth=1, relheight=1)
 
  p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1) 
  p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
  p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
  p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
  
  b1 = Button(buttonframe, text="Gestione clienti", command=p1.lift,bg="yellow",height = 1, width =14)
  b2 = Button(buttonframe, text="Gestione instruttori", command=p2.lift,bg="CadetBlue1",height = 1, width =14)
  b3 = Button(buttonframe, text="Gestione corsi", command=p3.lift,bg="orange",height = 1, width =14)
  b4 = Button(buttonframe, text="Statistiche", command=p4.lift,bg="lawn green",height = 1, width =14)
  b5 = Button(buttonframe, text="Logout", command=self.destroy,bg="red",height = 1, width =14)
  
  b1.pack(side="left")
  b2.pack(side="left")
  b3.pack(side="left")
  b4.pack(side="left")
  b5.pack(side="left")


  
  
  
