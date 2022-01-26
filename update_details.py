from order_tests import *


def updatedetials():
    def update(patient1):
        def udetails(update3):

            def uname():

                def sqlupdate():
                    fname1 = E1.get()
                    fname2 = E2.get()
                    cmd = "UPDATE Patient_data SET FirstName = (?), LastName = (?) WHERE UID = (?)"
                    data = [(fname1, fname2, patient1)]
                    cursor.executemany(cmd, data)
                    cnxn.commit()
                    msgbox.showinfo("Success", "Name Updated Successfully")
                    updatedetials2_window.destroy()
                    updatedetials1_window.destroy()
                    updatedetials_window.destroy()

                updatedetials2_window = Tk()
                updatedetials2_window.title("Grey Sloan Memorial Update Patient Name ")
                updatedetials2_window.geometry("3840x2160")
                L1 = Label(updatedetials2_window, text="First Name")
                L1.place(x=200, y=150)
                E1 = Entry(updatedetials2_window)
                E1.place(x=300, y=150)
                L2 = Label(updatedetials2_window, text="Last Name")
                L2.place(x=200, y=180)
                E2 = Entry(updatedetials2_window)
                E2.place(x=300, y=180)
                B1 = Button(updatedetials2_window, text='Submit', command=sqlupdate)
                B1.place(x=250, y=210)

            def uage():

                def sqlupdate():
                    age1 = E1.get()
                    age1 = int(age1)
                    cmd = "UPDATE Patient_data SET Age = (?) WHERE UID = (?)"
                    data = [(age1, patient1)]
                    cursor.executemany(cmd, data)
                    cnxn.commit()
                    msgbox.showinfo("Success", "Age Updated Successfully")
                    updatedetials2_window.destroy()
                    updatedetials1_window.destroy()
                    updatedetials_window.destroy()

                updatedetials2_window = Tk()
                updatedetials2_window.title("Grey Sloan Memorial Update Patient Age ")
                updatedetials2_window.geometry("3840x2160")
                L1 = Label(updatedetials2_window, text="Age")
                L1.place(x=200, y=150)
                E1 = Entry(updatedetials2_window)
                E1.place(x=300, y=150)

                B1 = Button(updatedetials2_window, text='Submit', command=sqlupdate)
                B1.place(x=250, y=210)

            def ugender():

                def sqlupdate():
                    gender1 = menu.get()

                    cmd = "UPDATE Patient_data SET Gender = (?) WHERE UID = (?)"
                    data = [(gender1, patient1)]
                    cursor.executemany(cmd, data)
                    cnxn.commit()
                    msgbox.showinfo("Success", "Gender Updated Successfully")
                    updatedetials2_window.destroy()
                    updatedetials1_window.destroy()
                    updatedetials_window.destroy()

                updatedetials2_window = Tk()
                updatedetials2_window.title("Grey Sloan Memorial Update Patient Gender ")
                updatedetials2_window.geometry("3840x2160")
                L1 = Label(updatedetials2_window, text="Select Gender")
                L1.place(x=200, y=150)
                menu = StringVar()
                drop = OptionMenu(updatedetials2_window, menu, "Male", "Female", "Non-Binary")
                menu.set("Select Gender")
                drop.place(x=300, y=150, width=80)

                B1 = Button(updatedetials2_window, text='Submit', command=sqlupdate)
                B1.place(x=250, y=210)

            def uheight():

                def sqlupdate():
                    height1 = E1.get()
                    height1 = int(height1)
                    cmd = "UPDATE Patient_data SET Height = (?) WHERE UID = (?)"
                    data = [(height1, patient1)]
                    cursor.executemany(cmd, data)
                    cnxn.commit()
                    msgbox.showinfo("Success", "Height Updated Successfully")
                    updatedetials2_window.destroy()
                    updatedetials1_window.destroy()
                    updatedetials_window.destroy()

                updatedetials2_window = Tk()
                updatedetials2_window.title("Grey Sloan Memorial Update Patient Height ")
                updatedetials2_window.geometry("3840x2160")
                L1 = Label(updatedetials2_window, text="Height")
                L1.place(x=200, y=150)
                E1 = Entry(updatedetials2_window)
                E1.place(x=300, y=150)

                B1 = Button(updatedetials2_window, text='Submit', command=sqlupdate)
                B1.place(x=250, y=210)

            def uweight():

                def sqlupdate():
                    weight1 = E1.get()
                    weight1 = int(weight1)
                    cmd = "UPDATE Patient_data SET Weight = (?) WHERE UID = (?)"
                    data = [(weight1, patient1)]
                    cursor.executemany(cmd, data)
                    cnxn.commit()
                    msgbox.showinfo("Success", "Weight Updated Successfully")
                    updatedetials2_window.destroy()
                    updatedetials1_window.destroy()
                    updatedetials_window.destroy()

                updatedetials2_window = Tk()
                updatedetials2_window.title("Grey Sloan Memorial Update Patient Weight ")
                updatedetials2_window.geometry("3840x2160")
                L1 = Label(updatedetials2_window, text="Height")
                L1.place(x=200, y=150)
                E1 = Entry(updatedetials2_window)
                E1.place(x=300, y=150)

                B1 = Button(updatedetials2_window, text='Submit', command=sqlupdate)
                B1.place(x=250, y=210)

            def udiagnosis():

                def sqlupdate():
                    diagnosis1 = E1.get()

                    cmd = "UPDATE Patient_data SET Diagnosis = (?) WHERE UID = (?)"
                    data = [(diagnosis1, patient1)]
                    cursor.executemany(cmd, data)
                    cnxn.commit()
                    msgbox.showinfo("Success", "Diagnosis Updated Successfully")
                    updatedetials2_window.destroy()
                    updatedetials1_window.destroy()
                    updatedetials_window.destroy()

                updatedetials2_window = Tk()
                updatedetials2_window.title("Grey Sloan Memorial Update Patient Diagnosis ")
                updatedetials2_window.geometry("3840x2160")
                L1 = Label(updatedetials2_window, text="Diagnosis")
                L1.place(x=200, y=150)
                E1 = Entry(updatedetials2_window)
                E1.place(x=300, y=150)

                B1 = Button(updatedetials2_window, text='Submit', command=sqlupdate)
                B1.place(x=250, y=210)

            def uinsurance():

                def sqlupdate():
                    insurance1 = E1.get()

                    cmd = "UPDATE Patient_data SET Insurance = (?) WHERE UID = (?)"
                    data = [(insurance1, patient1)]
                    cursor.executemany(cmd, data)
                    cnxn.commit()
                    msgbox.showinfo("Success", "Insurance Details Updated Successfully")
                    updatedetials2_window.destroy()
                    updatedetials1_window.destroy()
                    updatedetials_window.destroy()

                updatedetials2_window = Tk()
                updatedetials2_window.title("Grey Sloan Memorial Update Patient Insurance Details ")
                updatedetials2_window.geometry("3840x2160")
                L1 = Label(updatedetials2_window, text="Insurance Details")
                L1.place(x=200, y=150)
                E1 = Entry(updatedetials2_window)
                E1.place(x=300, y=150)

                B1 = Button(updatedetials2_window, text='Submit', command=sqlupdate)
                B1.place(x=250, y=210)

            def uaddress():

                def sqlupdate():
                    address1 = E1.get()

                    cmd = "UPDATE Patient_data SET Address = (?) WHERE UID = (?)"
                    data = [(address1, patient1)]
                    cursor.executemany(cmd, data)
                    cnxn.commit()
                    msgbox.showinfo("Success", "Address Updated Successfully")
                    updatedetials2_window.destroy()
                    updatedetials1_window.destroy()
                    updatedetials_window.destroy()

                updatedetials2_window = Tk()
                updatedetials2_window.title("Grey Sloan Memorial Update Patient Address ")
                updatedetials2_window.geometry("3840x2160")
                L1 = Label(updatedetials2_window, text="Address")
                L1.place(x=200, y=150)
                E1 = Entry(updatedetials2_window)
                E1.place(x=300, y=150)

                B1 = Button(updatedetials2_window, text='Submit', command=sqlupdate)
                B1.place(x=250, y=210)

            def ucity():

                def sqlupdate():
                    city1 = E1.get()

                    cmd = "UPDATE Patient_data SET City = (?) WHERE UID = (?)"
                    data = [(city1, patient1)]
                    cursor.executemany(cmd, data)
                    cnxn.commit()
                    msgbox.showinfo("Success", "City Updated Successfully")
                    updatedetials2_window.destroy()
                    updatedetials1_window.destroy()
                    updatedetials_window.destroy()

                updatedetials2_window = Tk()
                updatedetials2_window.title("Grey Sloan Memorial Update Patient City ")
                updatedetials2_window.geometry("3840x2160")
                L1 = Label(updatedetials2_window, text="City")
                L1.place(x=200, y=150)
                E1 = Entry(updatedetials2_window)
                E1.place(x=300, y=150)

                B1 = Button(updatedetials2_window, text='Submit', command=sqlupdate)
                B1.place(x=250, y=210)

            def uemail():

                def sqlupdate():
                    city1 = E1.get()

                    cmd = "UPDATE Patient_data SET Email = (?) WHERE UID = (?)"
                    data = [(city1, patient1)]
                    cursor.executemany(cmd, data)
                    cnxn.commit()
                    msgbox.showinfo("Success", "Email Updated Successfully")
                    updatedetials2_window.destroy()
                    updatedetials1_window.destroy()
                    updatedetials_window.destroy()

                updatedetials2_window = Tk()
                updatedetials2_window.title("Grey Sloan Memorial Update Patient Email ")
                updatedetials2_window.geometry("3840x2160")
                L1 = Label(updatedetials2_window, text="Email")
                L1.place(x=200, y=150)
                E1 = Entry(updatedetials2_window)
                E1.place(x=300, y=150)

                B1 = Button(updatedetials2_window, text='Submit', command=sqlupdate)
                B1.place(x=250, y=210)

            if update3 == 'Name':
                uname()
            elif update3 == 'Age':
                uage()
            elif update3 == 'Gender':
                ugender()
            elif update3 == 'Height':
                uheight()
            elif update3 == 'Weight':
                uweight()
            elif update3 == 'Insurance':
                uinsurance()
            elif update3 == 'Diagnosis':
                udiagnosis()
            elif update3 == 'Address':
                uaddress()
            elif update3 == 'City':
                ucity()
            elif update3 == 'Email':
                uemail()
            else:
                msgbox.showwarning("Warning", "Invalid Selection")

        patient1 = patient1[0:7]

        updatedetials1_window = Tk()
        updatedetials1_window.title("Grey Sloan Memorial Update Patient Details ")
        updatedetials1_window.geometry("3840x2160")
        L1 = Label(updatedetials1_window, text="Select Field to Update ")
        L1.place(x=200, y=150)
        lst1 = ['Name', 'Age', 'Gender', 'Height', 'Weight', 'Insurance', 'Diagnosis', 'Address', 'City', 'Email']
        update2 = StringVar()
        update2.set("Field Selection")
        drop = OptionMenu(updatedetials1_window, update2, *lst1, command=udetails)
        drop.place(x=350, y=150, )

    updatedetials_window = Tk()
    updatedetials_window.title("Grey Sloan Memorial Update Patient Details ")
    updatedetials_window.geometry("3840x2160")

    lst = cursor.execute("""SELECT UID, FirstName, LastName, Primary_Physician FROM Patient_data""")
    lst = cursor.fetchall()

    lst1 = []
    for i in range(0, len(lst)):
        lst1.append(lst[i][0] + " - " + lst[i][1])

    L1 = Label(updatedetials_window, text="Select Patient ")
    L1.place(x=200, y=150)
    patient = StringVar()
    patient.set("Patient Selection")
    drop = OptionMenu(updatedetials_window, patient, *lst1, command=update)
    drop.place(x=300, y=150, )
    mainloop()

# updatedetials()