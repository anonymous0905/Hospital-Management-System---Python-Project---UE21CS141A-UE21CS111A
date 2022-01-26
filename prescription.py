

from update_details import *

def order_medications():

    def orders(patient):
        def search_return():

            def order_med (medicine):
                med_name = medicine[0]
                med_price = medicine[1]
                data = [(med_name, med_price, "Medicine Ordered")]
                cmd = "INSERT INTO "+ uid +" (Medicine_Name, Price, Status) VALUES (?,?,?)"
                cursor.executemany(cmd, data)
                cnxn.commit()

                txt = med_name+" Ordered Successfully...!!!"

                msgbox.showinfo("Test Ordered Successfully", txt)
                med_window.destroy()

            key = E1.get()
            key = "%"+key+"%"
            lst = cursor.execute('''SELECT Medicine_Name, Price FROM Prescription WHERE Medicine_name Like (?) ;''',(key))
            lst = cursor.fetchall()
            if len(lst) == 0 :
                msgbox.showerror("No match found", "No match found please try again")
                med_window.destroy()
                return
            med1 = StringVar()
            med1.set("Patient Selection")
            drop = OptionMenu(med_window, med1, *lst, command=order_med)
            drop.place(x=400, y=210)
        uid = patient[0:7]+"Prescription"
        L2 = Label(med_window, text="Enter the medicine name: ")
        L2.place(x=200, y=180)
        E1 = Entry(med_window)
        E1.place(x=400, y=180)
        B1 = Button(med_window, text="Search", command = search_return)
        B1.place(x=500, y=180)

    med_window = Tk()
    med_window.title("Order Medicines ")
    med_window.geometry("3840x2160")
    lst = cursor.execute("""SELECT UID, FirstName, LastName, Primary_Physician FROM Patient_data""")
    lst = cursor.fetchall()
    if len(lst)==0:
        msgbox.showerror("No Active Patients", "No Active Patients")
        med_window.destroy()
        return

    lst1 = []
    for i in range(0, len(lst)):
        lst1.append(lst[i][0] + " - " + lst[i][1])

    L1 = Label(med_window, text="Select Patient ")
    L1.place(x=200, y=150)
    patient = StringVar()
    patient.set("Patient Selection")
    drop = OptionMenu(med_window, patient, *lst1, command=orders)
    drop.place(x=400, y=150)
    mainloop()



