from discharge import *

def onlineregistration():

    def sqlupdate():
        fname = E1.get()
        lname = E2.get()
        age = E3.get()
        gender = menu.get()
        email = E4.get()
        physician = menu1.get()
        symptoms = T1.get(1.0, "end-1c")
        mobile = E8.get()
        mobile1 = '+91'+mobile
        cursor.execute("""
                    INSERT INTO Online_consult (FirstName, LastName, Age, Gender, Email, Physician, Problem, MobileNO)
                    VALUES (?, ?, ?, ?, ?, ?, ?,?);""", (fname, lname, age, gender, email, physician, symptoms,mobile1))
        cnxn.commit()
        msg = "You will Receive a reply from "+physician+" Shortly \n Thank you for choosing Grey Sloan Memorial"
        onlineconsult_window.destroy()
        msgbox.showinfo("Registration Successful", msg)


    onlineconsult_window = Tk()
    onlineconsult_window.title("Grey Sloan Memorial Online Consultation ")
    onlineconsult_window.geometry("3840x2160")
    L1 = Label(onlineconsult_window, text="Enter Patient Details Below ")
    L1.place(x=200, y=150)
    L2 = Label(onlineconsult_window, text="First Name ")
    L2.place(x=200, y=180)
    E1 = Entry(onlineconsult_window)
    E1.place(x=300, y=180)
    L3 = Label(onlineconsult_window, text="Last Name ")
    L3.place(x=200, y=210)
    E2 = Entry(onlineconsult_window)
    E2.place(x=300, y=210)
    L4 = Label(onlineconsult_window, text="Age ")
    L4.place(x=200, y=240)
    E3 = Entry(onlineconsult_window)
    E3.place(x=300, y=240)
    L5 = Label(onlineconsult_window, text="Gender ")
    L5.place(x=200, y=270)
    menu = StringVar()
    drop = OptionMenu(onlineconsult_window, menu, "Male", "Female", "Non-Binary")
    menu.set("Select Gender")
    drop.place(x=300, y=265, width=80)
    L6 = Label(onlineconsult_window, text = "Email ID ")
    L6.place(x=200, y=300 )
    E4 = Entry(onlineconsult_window)
    E4.place(x=300,y=300)
    L14 = Label(onlineconsult_window, text="Mobile Number ")
    L14.place(x=200, y=330)
    E8 = Entry(onlineconsult_window)
    E8.place(x=300, y=330)
    cursor.execute("""SELECT Name FROM PhysicianID""")
    data = cursor.fetchall()
    fdata = [list(i) for i in data]
    fdata1 = []
    for i in range(0, len(fdata)):
        fdata1.append(str(fdata[i][0]))

    L9 = Label(onlineconsult_window, text="Physician ")
    L9.place(x=200, y=360)
    menu1 = StringVar()
    menu1.set("Physician")
    drop1 = OptionMenu(onlineconsult_window, menu1, *fdata1)
    drop1.place(x=300, y=360, width=80)
    L10 = Label(onlineconsult_window, text="Problem Description / Symptoms ")
    L10.place(x=200, y=390)
    T1 = Text(onlineconsult_window, height=6, width=60)
    T1.place(x=400, y=390)
    B1 = Button(onlineconsult_window, text = "Submit", command = sqlupdate)
    B1.place(x=200, y=520)
    mainloop()

#onlineregistration()

