from Online_consult import *

def doconline():

    def verify():

        def reply(inp):

            def sendemail():
                reply = T1.get(1.0, "end-1c")
                fromaddr = "pesuhmsproject@gmail.com"
                toaddr = lst3[0][4]

                # instance of MIMEMultipart
                msg = MIMEMultipart()

                # storing the senders email address
                msg['From'] = fromaddr

                # storing the receivers email address
                msg['To'] = toaddr

                # storing the subject
                msg['Subject'] = "Online Consultation Grey Sloan Memorial"

                # string to store the body of the mail
                body = '''Patient Name - {0} {1} \nAge - {2} \nGender - {3} \nEmail - {4} \nPhysician - {5} \nProblem / Symptoms - {6} \nReply from Doctor - {7} \nIn case of further questions you can reply to this Email or Contact us on 1800-0000-56'''.format(lst3[0][0], lst3[0][1], lst3[0][2], lst3[0][3], lst3[0][4], lst3[0][5], lst3[0][6],reply)

                msg.attach(MIMEText(body, 'plain'))

                s = smtplib.SMTP('smtp.gmail.com', 587)

                # start TLS for security
                s.starttls()

                # Authentication
                s.login("pesuhmsproject@gmail.com", "pesu@123")

                # Converts the Multipart msg into a string
                text = msg.as_string()

                # sending the mail
                s.sendmail(fromaddr, toaddr, text)

                # terminating the session
                s.quit()
                cmd6 = "DELETE FROM Online_consult WHERE FirstName = ?"
                cursor.execute(cmd6, inp[0])
                cnxn.commit()
                onlineconsult_window1.destroy()
                onlineconsult_window.destroy()
                msgbox.showinfo("Successful", "Message sent Successfully")

            onlineconsult_window1 = Tk()
            onlineconsult_window1.title("Grey Sloan Memorial Online Consultation Physician Portal response ")
            onlineconsult_window1.geometry("3840x2160")
            lst3 = cursor.execute('''SELECT FirstName, LastName, Age, Gender, Email, Physician, Problem FROM Online_consult WHERE FirstName = (?) ;''',(inp[0]))
            lst3 = cursor.fetchall()


            L1 = Label(onlineconsult_window1, text = "Name : "+str(lst3[0][0])+" "+str(lst3[0][1]))
            L1.place(x=200,y=150)
            L2 = Label(onlineconsult_window1, text="Age : " + str(lst3[0][2]))
            L2.place(x=200, y=180)
            L3 = Label(onlineconsult_window1, text="Gender : " + str(lst3[0][3]))
            L3.place(x=200, y=210)
            L4 = Label(onlineconsult_window1, text="Problem : " + str(lst3[0][6]))
            L4.place(x=200, y=240)
            L5 = Label(onlineconsult_window1,text = "Enter Diagnosis / Prescription ")
            L5.place(x=200, y=270)
            T1 = Text(onlineconsult_window1, height=6, width=60)
            T1.place(x=400, y=270)
            B1 = Button(onlineconsult_window1, text = "Submit", command = sendemail)
            B1.place(x = 300, y = 320)


        user = str(E1.get())
        psd = str(E2.get())
        user.upper()
        user.upper()
        cursor.execute("""
               SELECT Username, Password, Name 
                   FROM PhysicianID
                   WHERE Username = (?)""", (user))
        data = cursor.fetchall()
        fdata = [list(i) for i in data]
        if fdata[0][1] == str(psd):
            lst2 = cursor.execute('''SELECT FirstName, LastName FROM Online_consult WHERE Physician = (?) ;''', (fdata[0][2]))
            lst2 = cursor.fetchall()
            if len(lst2) == 0:
                msgbox.showinfo("No online consultations ", "No online consultations")
                onlineconsult_window.destroy()
                return
            L5 = Label(onlineconsult_window, text="Select Patient ")
            L5.place(x=250, y=340)
            menu = StringVar()
            drop = OptionMenu(onlineconsult_window, menu, *lst2, command = reply)
            menu.set("Select Patient")
            drop.place(x=360, y=340, width=80)
        else :
            onlineconsult_window.destroy()
            msgbox.showerror("Login Error", "Invalid credentials please try again")

    onlineconsult_window = Tk()
    onlineconsult_window.title("Grey Sloan Memorial Online Consultation Physician Portal ")
    onlineconsult_window.geometry("3840x2160")
    L1 = Label(onlineconsult_window, text="Username ")
    L1.place(x=250, y=250)
    E1 = Entry(onlineconsult_window)
    E1.place(x=310, y=250)
    L2 = Label(onlineconsult_window, text="Password ")
    L2.place(x=250, y=280)
    E2 = Entry(onlineconsult_window, show='*')
    E2.place(x=310, y=280)
    B1 = Button(onlineconsult_window, text = "Login", command = verify)
    B1.place(x=250, y=310)
    mainloop()

