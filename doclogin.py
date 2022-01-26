from main import *



def doc_loginw() :
    login_window = Tk()
    login_window.title("Grey Sloan Memorial Physician Login ")
    login_window.geometry("3840x2160")

    L1 = Label(login_window, text = "Username ")
    L1.place(x=250, y=250)
    E1 = Entry(login_window)
    E1.place(x=310, y=250)
    L2 = Label(login_window, text="Password ")
    L2.place(x=250, y=280)
    E2 = Entry(login_window, show='**')
    E2.place(x=310, y=280)

    def clearinp():
        E1.delete(0,'end')
        E2.delete(0, 'end')

    def close():
        login_window.destroy()

    def login():
        user = str(E1.get())
        psd = str(E2.get())
        user.upper()
        user.upper()

        cursor.execute("""
        SELECT Username, Password, Name 
            FROM PhysicianID
            WHERE Username = (?)""",(user))
        data = cursor.fetchall()
        fdata = [list(i) for i in data]
        cursor.execute("""
                SELECT Username, Password, Name 
                    FROM ActivePhysicianID
                    WHERE Username = (?)""", (user))
        data1 = cursor.fetchall()
        fdata1 = [list(i) for i in data1]
        if fdata == fdata1:

            msgbox.showerror("Login Error", "Login Error")

            login_window.destroy()
            return

        if len(data) != 0 :
            if fdata[0][1] == str(psd) :
                cursor.execute(
                    """
                    INSERT INTO ActivePhysicianID
                    (Name, Username, Password)
                    VALUES (?, ?, ?)
                    """,
                    (fdata[0][2], fdata[0][0], fdata[0][1])
                )
                cnxn.commit()

                mssg = "Login Successful \n Have a great day {0}".format(fdata[0][2])
                msgbox.showinfo(f"Login Successful", mssg)

                login_window.destroy()
            else :

                msgbox.showerror("Login Error", "Invalid Password")

                login_window.destroy()
        else:

            msgbox.showerror("Invalid Username")

            login_window.destroy()



    B1 = Button(login_window, text="Login", command=login)
    B1.place(x=310, y=320)
    B2 = Button(login_window, text="Clear", command=clearinp)
    B2.place(x=350, y=320)
    B3 = Button(login_window, text="Close", command=close)
    B3.place(x=390, y=320)




