from tkinter import*
import mysql.connector
#to connect with mysql use mysql.connecter.connect
mygb= mysql.connector.connect (host="localhost", user ="Aanya", password = "Aanya@123", database = "db")
print(mygb)
#create cursor
crsr=mygb.cursor()
#create database
#crsr.execute("create database db")
#to show all the databses on the screen use 
#f = crsr.execute("show databases")
#for i in mygb:
    #print(i)

#creating a table
#crsr.execute("""create table crm (
    #fname text, 
    #lname text,
    #add1 text,
    #add2 text,
    #acity text,
    #bstate text,
    #czipcode int,
    #dcountry text,
    #phoneno int,
    #eaddress text,
    #paymentm text,
    #dcode int,
    #pricep int                                                                                       
#)""")
#mygb.commit()
def add():
    fa = (e1.get(), e2.get(),e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get(), e10.get(), e11.get(), e12.get(), e13.get())
    s = "insert into crm(fname, lname, add1, add2, acity, bstate, czipcode, dcountry, phoneno, eaddress, paymentm, dcode, pricep)values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" 
   # %s is the temporary value which is being passed in myssql in the place of value which is later on replaces by the actual value. This is because directly value cannot be passed to the values so this is used.
    crsr.execute(s,fa)
    mygb.commit()
screen=Tk()
screen.geometry("700x700")
screen.title("Customer Database")
screen.configure(bg="White")


def delete():
   f=e14.get()
   d="""delete from crm where eaddress = %s"""
   crsr.execute(d,(f,))
   mygb.commit()

def edit():
   data=(e200.get(), e22.get(), e33.get(), e44.get(), e55.get(), e66.get(), e77.get(), e88.get(), e99.get(), e100.get(), e110.get(), e120.get(), e130.get())
   crsr.execute("update crm set fname=%s, lname= %s, add1= %s, add2=%s, acity= %s, bstate=%s, czipcode = %s, dcountry =%s, phoneno = %s, eaddress = %s, paymentm = %s, dcode = %s, pricep = %s where eaddress = %s", data )
   mygb.commit()
   


def update():
 screen2=Tk()
 screen.geometry("700x700")
 screen.title("Customer Database 2")
 screen.configure(bg="White")
 global e200
 global e22
 global e33
 global e44
 global e55
 global e66
 global e77
 global e88
 global e99
 global e100
 global e110
 global e120
 global e130
 l200=Label(screen2, text="First Name",bg="black", fg="white")  
 l200.grid(row=0, column=0)

 e200=Entry(screen2, fg="black", width=90)
 e200.grid(row=0, column=1)
 
 l22=Label(screen2, text="Last Name",bg="black", fg="white")  
 l22.grid(row=2, column=0)

 e22=Entry(screen2, fg="black", width=90)
 e22.grid(row=2, column=1)

 l33=Label(screen2, text="Address 1",bg="black", fg="white")  
 l33.grid(row=3, column=0)

 e33=Entry(screen2, fg="black", width=90)
 e33.grid(row=3, column=1)

 l44=Label(screen2, text="Address 2",bg="black", fg="white")  
 l44.grid(row=4, column=0)

 e44=Entry(screen2, fg="black", width=90)
 e44.grid(row=4, column=1)

 l55=Label(screen2, text="City",bg="black", fg="white")  
 l55.grid(row=5, column=0)

 e55=Entry(screen2, fg="black", width=90)
 e55.grid(row=5, column=1)

 l66=Label(screen2, text="State",bg="black", fg="white")  
 l66.grid(row=6, column=0)

 e66=Entry(screen2, fg="black", width=90)
 e66.grid(row=6, column=1)


 l77=Label(screen2, text="Zipcode",bg="black", fg="white")  
 l77.grid(row=7, column=0)

 e77=Entry(screen2, fg="black", width=90)
 e77.grid(row=7, column=1)


 l88=Label(screen2, text="Country",bg="black", fg="white")  
 l88.grid(row=8, column=0)

 e88=Entry(screen2, fg="black", width=90)
 e88.grid(row=8, column=1)

 l99=Label(screen2, text="Phone Number",bg="black", fg="white")  
 l99.grid(row=9, column=0)

 e99=Entry(screen2, fg="black", width=90)
 e99.grid(row=9, column=1)


 l100=Label(screen2, text="Email address",bg="black", fg="white")  
 l100.grid(row=10, column=0)

 e100=Entry(screen2, fg="black", width=90)
 e100.grid(row=10, column=1)

 l110=Label(screen2, text="Payment Method",bg="black", fg="white")  
 l110.grid(row=11, column=0)

 e110=Entry(screen2, fg="black", width=90)
 e110.grid(row=11, column=1)


 l120=Label(screen2, text="Discount Code",bg="black", fg="white")  
 l120.grid(row=12, column=0)

 e120=Entry(screen2, fg="black", width=90)
 e120.grid(row=12, column=1)

 l130=Label(screen2, text="Price paid",bg="black", fg="white")  
 l130.grid(row=13, column=0)

 e130=Entry(screen2, fg="black", width=90)
 e130.grid(row=13, column=1)

 b11=Button(screen2 ,text="Edit", bg = "black", fg = "white")
 b11.grid(row = 14, column = 0)

 id=e14.get()
 crsr.execute("SELECT * from crm where eaddress=%s", (e14.get(),))

 a=crsr.fetchall()

 b=""

 for c in a:
  e200.insert(0,c[0]),
  e22.insert(0,c[1]),
  e33.insert(0,c[2]),
  e44.insert(0,c[3]),
  e55.insert(0,c[4]),
  e66.insert(0,c[5]),
  e77.insert(0,c[6]),
  e88.insert(0,c[7]),
  e99.insert(0,c[8]),
  e100.insert(0,c[9]),
  e110.insert(0,c[10]),
  e120.insert(0,c[11]),
  e130.insert(0,c[12])
 








def query():
    id=e14.get()
    crsr.execute("SELECT * from crm where eaddress=%s", (e14.get(),))

    a=crsr.fetchall()

    b=""

    for c in a:
        b =str(c[0]) + "\n" +str(c[1])+ "\n" +str(c[2]) + "\n" +str(c[3]) +"\n" +str(c[4])+"\n" +str(c[5]) +"\n"+str(c[6]) +"\n"+str(c[7]) +"\n"+str(c[8]) +"\n"+str(c[9]) +"\n"+str(c[10]) +"\n"+str(c[11]) +"\n"+str(c[12])
     
   #connection.commit()   
    l=Label(screen,text=b)
    l.grid(row=17, column = 0)
l1=Label(screen, text="First Name",bg="black", fg="white")  
l1.grid(row=0, column=0)


e1=Entry(screen, fg="black", width=90)
e1.grid(row=0, column=1)

l2=Label(screen, text="Last Name",bg="black", fg="white")  
l2.grid(row=2, column=0)

e2=Entry(screen, fg="black", width=90)
e2.grid(row=2, column=1)

l3=Label(screen, text="Address 1",bg="black", fg="white")  
l3.grid(row=3, column=0)

e3=Entry(screen, fg="black", width=90)
e3.grid(row=3, column=1)

l4=Label(screen, text="Address 2",bg="black", fg="white")  
l4.grid(row=4, column=0)

e4=Entry(screen, fg="black", width=90)
e4.grid(row=4, column=1)

l5=Label(screen, text="City",bg="black", fg="white")  
l5.grid(row=5, column=0)

e5=Entry(screen, fg="black", width=90)
e5.grid(row=5, column=1)

l6=Label(screen, text="State",bg="black", fg="white")  
l6.grid(row=6, column=0)

e6=Entry(screen, fg="black", width=90)
e6.grid(row=6, column=1)


l7=Label(screen, text="Zipcode",bg="black", fg="white")  
l7.grid(row=7, column=0)

e7=Entry(screen, fg="black", width=90)
e7.grid(row=7, column=1)


l8=Label(screen, text="Country",bg="black", fg="white")  
l8.grid(row=8, column=0)

e8=Entry(screen, fg="black", width=90)
e8.grid(row=8, column=1)

l9=Label(screen, text="Phone Number",bg="black", fg="white")  
l9.grid(row=9, column=0)

e9=Entry(screen, fg="black", width=90)
e9.grid(row=9, column=1)


l10=Label(screen, text="Email address",bg="black", fg="white")  
l10.grid(row=10, column=0)

e10=Entry(screen, fg="black", width=90)
e10.grid(row=10, column=1)

l11=Label(screen, text="Payment Method",bg="black", fg="white")  
l11.grid(row=11, column=0)

e11=Entry(screen, fg="black", width=90)
e11.grid(row=11, column=1)


l12=Label(screen, text="Discount Code",bg="black", fg="white")  
l12.grid(row=12, column=0)

e12=Entry(screen, fg="black", width=90)
e12.grid(row=12, column=1)

l13=Label(screen, text="Price paid",bg="black", fg="white")  
l13.grid(row=13, column=0)

e13=Entry(screen, fg="black", width=90)
e13.grid(row=13, column=1)

b1=Button(screen ,text="Add", bg = "black", fg = "white", command = add)
b1.grid(row = 14, column = 0)

b2=Button(screen ,text="Query", bg = "black", fg = "white", command = query)
b2.grid(row = 15, column = 0)

b3=Button(screen ,text="Update", bg = "black", fg = "white", command = update)
b3.grid(row = 14, column = 1)

b4=Button(screen ,text="Delete", bg = "black", fg = "white", command = delete)
b4.grid(row = 15, column = 1)

l14=Label(screen, text = "Enter your Email ID", fg = "black" )
l14.grid(row=16, column = 0)
global e14
e14=Entry(screen, fg = "black", bg = "white")
e14.grid(row = 16, column = 1)


   




mainloop()