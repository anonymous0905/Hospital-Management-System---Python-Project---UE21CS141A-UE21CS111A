import datetime

from doclogout import *

def newpatient() :

    def udetails():
        fname = E1.get()
        lname = E2.get()
        age = int(E3.get())
        gender = menu.get()
        height = int(E4.get())
        weight = int(E5.get())
        inc = E6.get()
        physician = menu1.get()
        iproblem = E7.get()
        idiagnosis = E8.get()
        address = E9.get()
        city = E10.get()
        email = E11.get()
        uid1 = fname[0:3].upper()
        num2 = str(random.randrange(1000, 9999))
        uid1 = uid1 + num2
        time = str(datetime.now())
        cursor.execute("""
            INSERT INTO Patient_data (UID, FirstName, LastName, Age, Gender, Height, Weight, Insurance, Primary_Physician,
            Admission_Time, Initial_problem, Initial_diagnosis, Diagnosis, Discharge_time, Discharge_summary, Address, City, Email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            'NA', 'NA','NA',?, ?,?);""", (
        uid1, fname, lname, age, gender, height, weight, inc, physician, time, iproblem,idiagnosis,address,city, email))
        cnxn.commit()
        uid2 = uid1+"Tests"
        exce1 = "CREATE TABLE {0} (Test_Name varchar(255),Price int,Status varchar(255));".format(uid2)
        cursor.execute(exce1)
        cnxn.commit()
        uid3 = uid1+"Prescription"
        exce2 = "CREATE TABLE {0} (Medicine_Name varchar(255),Price int,Status varchar(255));".format(uid3)
        cursor.execute(exce2)
        cnxn.commit()
        mssg = "Patient Registration Successful \nPatient Name - {0}\nUID - {1}".format((fname+" "+lname),uid1)
        msgbox.showinfo("Registration Successful",mssg)
        registration_window.destroy()

    def clearinp():
        E1.delete(0,'end')
        E2.delete(0, 'end')
        E3.delete(0, 'end')
        menu.set("Select Gender")
        E4.delete(0, 'end')
        E5.delete(0, 'end')
        E6.delete(0, 'end')
        menu.set("Physician")
        E7.delete(0, 'end')
        E8.delete(0, 'end')
        E9.delete(0, 'end')

    def closewin():
        registration_window.destroy()

    def oldpatient():

        def search():

            def addtoactive():
                cmd5 = "INSERT INTO Patient_data SELECT * FROM Patient_data_archive WHERE UID = ?"
                cmd6 = "DELETE FROM Patient_data_archive WHERE UID = ?"
                cursor.execute(cmd5, uid3)
                cnxn.commit()
                cursor.execute(cmd6, uid3)
                cnxn.commit()
                time1 = str(datetime.now())
                physician1 = menu2.get()
                iproblem = E13.get()
                idiagnosis = E14.get()
                cmd = "UPDATE Patient_data SET Admission_time = (?), Discharge_time = (?), Discharge_summary = (?), Initial_problem = (?), Initial_diagnosis = (?), Diagnosis = (?)  WHERE UID = (?)"
                data = [(time1, 'NA', 'NA', iproblem, idiagnosis,'NA', uid3)]
                cursor.executemany(cmd, data)
                uid11 = uid3 + "Tests"
                exce1 = "CREATE TABLE {0} (Test_Name varchar(255),Price int,Status varchar(255));".format(uid11)
                cursor.execute(exce1)
                cnxn.commit()
                uid12 = uid3 + "Prescription"
                exce2 = "CREATE TABLE {0} (Medicine_Name varchar(255),Price int,Status varchar(255));".format(uid12)
                cursor.execute(exce2)
                cnxn.commit()
                msgbox.showinfo("Successful", "Patient Added to active patient list")
                registration_window1.destroy()
                registration_window.destroy()


            uid3 = E12.get()
            lst = cursor.execute('''SELECT UID, FirstName, LastName FROM Patient_data_archive WHERE UID = ? ;''', uid3)
            lst = cursor.fetchall()
            if len(lst)==0:
                msgbox.showerror("Records not found", "Patient records not Found")
                registration_window1.destroy()
                return
            L15 = Label(registration_window1, text = ("UID :- "+lst[0][0]))
            L15.place(x=200, y=210)
            L16 = Label(registration_window1, text=("First Name :- " + lst[0][1]))
            L16.place(x=200, y=240)
            L17 = Label(registration_window1, text=("Last Name :- " + lst[0][2]))
            L17.place(x=200, y=270)
            L18 = Label(registration_window1, text="Physician ")
            L18.place(x=200, y=300)
            menu2 = StringVar()
            menu2.set("Physician")
            drop2 = OptionMenu(registration_window1, menu2, *fdata1)
            drop2.place(x=300, y=295, width=80)
            L19 = Label(registration_window1, text="Initial Problem ")
            L19.place(x=200, y=330)
            E13 = Entry(registration_window1)
            E13.place(x=300, y=330)
            L11 = Label(registration_window1, text="Initial Diagnosis ")
            L11.place(x=200, y=360)
            E14 = Entry(registration_window1)
            E14.place(x=300, y=360)
            B6 = Button(registration_window1, text = "Add to active Patient", command = addtoactive)
            B6.place(x=200, y=390)


        registration_window1 = Tk()
        registration_window1.title("Grey Sloan Memorial Old Patient Search ")
        registration_window1.geometry("3840x2160")
        L15 = Label(registration_window1, text ="Enter patient UID ")
        L15.place(x=200, y=150)
        E12 = Entry(registration_window1)
        E12.place(x=300, y=150)
        B5 = Button(registration_window1, text="Search", command=search)
        B5.place(x=250, y=180)



    registration_window = Tk()
    registration_window.title("Grey Sloan Memorial New Patient Registration ")
    registration_window.geometry("3840x2160")
    L1 = Label(registration_window, text="Enter Patient Details Below ")
    L1.place(x=200, y=150)
    L2 = Label(registration_window, text="First Name ")
    L2.place(x=200, y=180)
    E1 = Entry(registration_window)
    E1.place(x=300, y=180)
    L3 = Label(registration_window, text="Last Name ")
    L3.place(x=200, y=210)
    E2 = Entry(registration_window)
    E2.place(x=300, y=210)
    L4 = Label(registration_window, text="Age ")
    L4.place(x=200, y=240)
    E3 = Entry(registration_window)
    E3.place(x=300, y=240)
    L5 = Label(registration_window, text="Gender ")
    L5.place(x=200, y=270)

    menu = StringVar()
    drop = OptionMenu(registration_window, menu, "Male", "Female", "Non-Binary")
    menu.set("Select Gender")
    drop.place(x=300, y=265, width=80)
    L6 = Label(registration_window, text="Height ")
    L6.place(x=200, y=300)
    E4 = Entry(registration_window)
    E4.place(x=300, y=300)
    L7 = Label(registration_window, text="Weight ")
    L7.place(x=200, y=330)
    E5 = Entry(registration_window)
    E5.place(x=300, y=330)
    L8 = Label(registration_window, text="Insurance ")
    L8.place(x=200, y=360)
    E6 = Entry(registration_window)
    E6.place(x=300, y=360)
    cursor.execute("""SELECT Name FROM ActivePhysicianID""")
    data = cursor.fetchall()
    fdata = [list(i) for i in data]
    fdata1 = []
    for i in range(0,len(fdata)):
        fdata1.append(str(fdata[i][0]))


    L9 = Label(registration_window, text="Physician ")
    L9.place(x=200, y=390)
    menu1 = StringVar()
    menu1.set("Physician")
    drop1 = OptionMenu(registration_window, menu1, *fdata1)
    drop1.place(x=300, y=385, width=80)
    L10 = Label(registration_window, text="Initial Problem ")
    L10.place(x=200, y=420)
    E7 = Entry(registration_window)
    E7.place(x=300, y=420)
    L11 = Label(registration_window, text="Initial Diagnosis ")
    L11.place(x=200, y=450)
    E8 = Entry(registration_window)
    E8.place(x=300, y=450)
    L12 = Label(registration_window, text="Address ")
    L12.place(x=200, y=480)
    E9 = Entry(registration_window)
    E9.place(x=300, y=480)
    L13 = Label(registration_window, text="City ")
    L13.place(x=200, y=510)
    E10 = Entry(registration_window)
    E10.place(x=300, y=510)
    L14 = Label(registration_window, text="Email ")
    L14.place(x=200, y=540)
    E11 = Entry(registration_window)
    E11.place(x=300, y=540)
    B1 = Button(registration_window, text = "Submit", command = udetails)
    B1.place(x=300, y=570)
    B2 = Button(registration_window, text="Clear", command=clearinp)
    B2.place(x=370, y=570)
    B3 = Button(registration_window, text="Close", command=closewin)
    B3.place(x=420, y=570)
    B4 = Button(registration_window, text = "Search By UID", command=oldpatient)
    B4.place(x=400, y=150)
    mainloop()





