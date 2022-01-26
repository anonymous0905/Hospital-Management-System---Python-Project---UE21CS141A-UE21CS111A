from doconlineconsult import *

def showdetails1():
    def display(pname):

        def close():
            details_window.destroy()

        uid = pname[0:7]
        lst2 = cursor.execute('''SELECT UID, FirstName, LastName, Age, Gender, Height, Weight, Insurance, Primary_physician, Admission_Time, Initial_problem, Initial_diagnosis, Diagnosis FROM Patient_data WHERE UID = ? ;''', uid)
        lst2 = cursor.fetchall()
        if len(lst2) == 0:
            msgbox.showerror("Records not found", "Patient records not Found")
            details_window.destroy()
            return
        L2 = Label(details_window, text = "UID :- "+lst2[0][0])
        L2.place(x=200, y=200)
        L3 = Label(details_window, text="First Name :- " + lst2[0][1])
        L3.place(x=200, y=230)
        L4 = Label(details_window, text="Last Name :- " + lst2[0][2])
        L4.place(x=200, y=260)
        L5 = Label(details_window, text="Age :- " + str(lst2[0][3]))
        L5.place(x=200, y=290)
        L6 = Label(details_window, text="Gender :- " + lst2[0][4])
        L6.place(x=200, y=320)
        L7 = Label(details_window, text="Height :- " + str(lst2[0][5])+" cm")
        L7.place(x=200, y=350)
        L8 = Label(details_window, text="Weight :- " + str(lst2[0][6])+" kg")
        L8.place(x=200, y=380)
        L9 = Label(details_window, text="Insurance :- " + lst2[0][7])
        L9.place(x=200, y=410)
        L10 = Label(details_window, text="Primary Physician :- " + lst2[0][8])
        L10.place(x=200, y=440)
        L11 = Label(details_window, text="Admission Time :- " + lst2[0][9])
        L11.place(x=200, y=470)
        L12 = Label(details_window, text="Initial Problem :- " + lst2[0][10])
        L12.place(x=200, y=500)
        L13 = Label(details_window, text="Initial Diagnosis :- " + lst2[0][11])
        L13.place(x=200, y=530)
        L14 = Label(details_window, text="Diagnosis :- " + lst2[0][12])
        L14.place(x=200, y=560)
        B1 = Button(details_window, text = "Close", command=close)
        B1.place(x=200, y=590)




    details_window = Tk()
    details_window.title("Grey Sloan Memorial Patient Details ")
    details_window.geometry("3840x2160")
    lst = cursor.execute("""SELECT UID, FirstName, LastName, Primary_Physician FROM Patient_data""")
    lst = cursor.fetchall()

    lst1 = []
    for i in range(0, len(lst)):
        lst1.append(lst[i][0] + " - " + lst[i][1])

    L1 = Label(details_window, text="Select Patient ")
    L1.place(x=200, y=150)
    patient = StringVar()
    patient.set("Patient Selection")
    drop = OptionMenu(details_window, patient, *lst1, command=display)
    drop.place(x=400, y=150)
    mainloop()

#showdetails1()