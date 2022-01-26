from doclogin import *



def doc_logoutw() :
    login_window = Tk()
    login_window.title("Grey Sloan Memorial Physician Logout ")
    login_window.geometry("3840x2160")

    L1 = Label(login_window, text = "Username ")
    L1.place(x=250, y=250)
    E1 = Entry(login_window)
    E1.place(x=310, y=250)
    L2 = Label(login_window, text="Password ")
    L2.place(x=250, y=280)
    E2 = Entry(login_window, show='*')
    E2.place(x=310, y=280)


    def clearinp():
        E1.delete(0,'end')
        E2.delete(0, 'end')

    def close():
        login_window.destroy()

    def logout():
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

        if len(data) != 0 :
            if fdata[0][1] == str(psd) :
                cursor.execute(
                    """
                    DELETE FROM ActivePhysicianID WHERE Username=(?);
                    """,
                    (fdata[0][0])
                )
                cnxn.commit()

                mssg = "Logout successful {0}".format(fdata[0][2])
                msgbox.showinfo("Logout Successful", mssg)
                login_window.destroy()
            else :
                msgbox.showerror("Logout Failed", "Invalid Password")
                login_window.destroy()
        else:
            msgbox.showerror("Logout Failed", "Invalid Username")
            login_window.destroy()



    B1 = Button(login_window, text="Logout", command=logout)
    B1.place(x=310, y=320)
    B2 = Button(login_window, text="Clear", command=clearinp)
    B2.place(x=350, y=320)
    B3 = Button(login_window, text="Close", command=close)
    B3.place(x=390, y=320)



