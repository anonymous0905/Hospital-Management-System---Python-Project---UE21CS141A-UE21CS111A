from new_patient import *

def order_tests():

    def order(patient):
        def search_return():

            def order1(testordered):
                tname = testordered[0]
                tprice = testordered[1]
                data = [(tname, tprice, "To be conducted")]
                cmd = "INSERT INTO "+ uid +" (Test_Name, Price, Status) VALUES (?,?,?)"
                cursor.executemany(cmd, data)
                cnxn.commit()

                txt = tname+" Ordered Successfully...!!!"

                msgbox.showinfo("Test Ordered Successfully", txt)
                ordtests_window.destroy()

            key = E1.get()
            key = "%"+key+"%"
            lst = cursor.execute('''SELECT Test_Name, Price FROM Tests WHERE Test_name Like (?) ;''',(key))
            lst = cursor.fetchall()
            if len(lst) == 0 :
                msgbox.showerror("No match found", "No match found please try again")
                ordtests_window.destroy()
                return
            test1 = StringVar()
            test1.set("Test Selection")
            drop = OptionMenu(ordtests_window, test1, *lst, command=order1)
            drop.place(x=400, y=210)
        uid = patient[0:7]+"Tests"
        L2 = Label(ordtests_window, text="Enter key word to search ")
        L2.place(x=200, y=180)
        E1 = Entry(ordtests_window)
        E1.place(x=400, y=180)
        B1 = Button(ordtests_window, text="Search", command = search_return)
        B1.place(x=500, y=180)

    ordtests_window = Tk()
    ordtests_window.title("Grey Sloan Memorial Order Tests ")
    ordtests_window.geometry("3840x2160")
    lst = cursor.execute("""SELECT UID, FirstName, LastName, Primary_Physician FROM Patient_data""")
    lst = cursor.fetchall()

    if len(lst)==0:
        msgbox.showerror("No Active Patients", "No Active Patients")
        ordtests_window.destroy()
        return
    lst1 = []
    for i in range(0, len(lst)):
        lst1.append(lst[i][0] + " - " + lst[i][1])

    L1 = Label(ordtests_window, text="Select Patient ")
    L1.place(x=200, y=150)
    patient = StringVar()
    patient.set("Patient Selection")
    drop = OptionMenu(ordtests_window, patient, *lst1, command=order)
    drop.place(x=400, y=150)
    mainloop()


#order_tests()
