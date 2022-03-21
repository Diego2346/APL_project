from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import gym,Home_admin,Home_user

def connect():
    db=gym.db()
    try:   
        db.connectDB(db.getConn(), "localhost", "root", "root", 3306, "gym")
        return db
    except: 
        return False
    
def login_admin(username,psw):
   if( gym.validateAdmin(db,username,psw)):
      admin= gym.validateAdmin(db,username,psw)
      h1 = Home_admin.home(root,admin,db)
      h1.place(in_=loginframe ,x=0, y=0, relwidth=1, relheight=1) 
      h1.show()
   else:
       Label(root, text = "Errore login", fg="red" ).place(relx=0.7, rely=0.5,anchor=CENTER)
       
       
def login_user(username,psw):
    if(gym.validateUser(db,username,psw)):
       user= gym.validateUser(db,username,psw)
       h2= Home_user.home(root,user,db)
       h2.place(in_=loginframe ,x=0, y=0, relwidth=1, relheight=1)  
       h2.show()
    else:
       Label(root, text = "Errore login", fg="red" ).place(relx=0.3, rely=0.5,anchor=CENTER)

def signup_admin():
  window = Toplevel(root)
  window.geometry("400x500")
  Label(window,text = "NUOVO AMMINISTRATORE ",font=("Calibri",20)).place(relx=0.15, rely=0.01)
  #NOME
  name = StringVar()
  Label(window,text = "Nome ",).place(relx = 0.05, rely = 0.1)
  Entry(window,textvariable = name, width = "30").place(relx = 0.05, rely = 0.15)
  #COGNOME
  surname = StringVar()
  Label(window,text = "Cognome ",).place(relx = 0.05, rely = 0.20)
  Entry(window,textvariable = surname, width = "30").place(relx = 0.05, rely = 0.25)
  #SESSO
  gender= StringVar()
  Label(window,text = "Sesso ",).place(relx = 0.55, rely = 0.20)
  Radiobutton(window, text="Maschio", variable=gender,value="M").place(relx = 0.55, rely = 0.25)
  Radiobutton(window, text="Femmina", variable=gender,value="F",tristatevalue=0).place(relx = 0.55, rely = 0.30)
  gender.set('M')
  #NASCITA
  birth=DateEntry(window, width = "27",year=1997, date_pattern="dd/mm/yyyy")
  birth.place(relx = 0.05, rely = 0.35)
  #EMAil
  email = StringVar()
  Label(window,text = "Email ",).place(relx = 0.05, rely = 0.4)
  Entry(window,textvariable = email, width = "30").place(relx = 0.05, rely = 0.45)
  #INDIRIZZO
  address = StringVar()
  Label(window,text = "Indirizzo ",).place(relx = 0.05, rely = 0.5)
  Entry(window,textvariable = address, width = "30").place(relx = 0.05, rely = 0.55)
  #uSERNAME
  username = StringVar()
  Label(window,text = "Username ",).place(relx = 0.05, rely = 0.60)
  Entry(window,textvariable = username, width = "30").place(relx = 0.05, rely = 0.65)
  #PASSWORD
  psw = StringVar()
  Label(window,text = "Password ",).place(relx = 0.05, rely = 0.7)
  Entry(window,textvariable = psw, width = "30").place(relx = 0.05, rely = 0.75)

  def clicked_signup(): 
    try: 
        if(''not in (name.get(),surname.get(),birth.get(),address.get(),email.get()
                          ,username.get(),psw.get())):
           new_admin=gym.Admin(name.get(),surname.get(),gender.get(),address.get(),birth.get(),email.get()
                          ,username.get(),psw.get(),True)
           gym.createAdmin(new_admin,db)
           messagebox.showinfo('Gym','Registrato')
           window.withdraw()
         
    except RuntimeError: 
         messagebox.showerror('ERRORE', 'Impossibile registrarsi')
     
         

         
  Button(window,text="Salva",command=clicked_signup, bg="plum2",height = 1, width =14).place(relx=0.25,rely=0.85)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x600")
    root.title("Gym")
    loginframe = Frame()
    loginframe.pack(side="top",fill="both" ,expand=True)
    canvas = Canvas()
    canvas.create_line(0, 0, 0, 900, width=10, fill="blue")
    canvas.place(relx=0.5, rely=0.2)

    if(connect()):
        Label(root, text = "DATABASE CONNESSO", fg="green" ).place(relx=0.5, rely=0.7,anchor=CENTER)
        db=connect()
    else:
        Label(root, text = "ERRORE CONNESIONE DATABASE", fg="red" ).place(relx=0.5, rely=0.7,anchor=CENTER)
    
    
    #ADMIN
    Label(text = "Amministratore ",font=("Calibri", 20)).place(relx=0.7, rely=0.1, anchor=CENTER)
    #Username admin
    username_a = StringVar()
    Label(text = "Username ",).place(relx=0.7, rely=0.3, anchor=CENTER)
    Entry(textvariable = username_a, width = "30").place(relx=0.7, rely=0.35, anchor=CENTER)
    #PSW ADMIN
    psw_a=StringVar()
    Label(text = "Password ",).place(relx=0.7, rely=0.4, anchor=CENTER)
    Entry(textvariable = psw_a,show="*", width = "30").place(relx=0.7, rely=0.45, anchor=CENTER)
    #LOGIN ADMIN
    Button( text="Login", command=lambda: login_admin(username_a.get(),psw_a.get()),bg="azure",height = 1, width =14).place(relx=0.7, rely=0.60, anchor=CENTER)
    Button( text="Registra Amministratore", command=signup_admin,bg="plum2",height = 1, width =20).place(relx=0.7, rely=0.65, anchor=CENTER)

    
    #UTENTE
    Label(text = "Utente ",font=("Calibri", 20)).place(relx=0.3, rely=0.1, anchor=CENTER)
    #Username utente
    username_u = StringVar()
    Label(text = "Username ",).place(relx=0.3, rely=0.3, anchor=CENTER)
    Entry(textvariable = username_u, width = "30").place(relx=0.3, rely=0.35, anchor=CENTER)
    #PSW utente
    psw_u=StringVar()
    Label(text = "Password ",).place(relx=0.3, rely=0.4, anchor=CENTER)
    Entry(textvariable = psw_u,show="*", width = "30").place(relx=0.3, rely=0.45, anchor=CENTER)
    #LOGIN utente
    Button( text="Login", command=lambda: login_user(username_u.get(),psw_u.get()),bg="orange",height = 1, width =14).place(relx=0.3, rely=0.60, anchor=CENTER)
    root.mainloop()
    
