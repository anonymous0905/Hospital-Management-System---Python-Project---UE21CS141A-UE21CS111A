

from prescription import *

def patientdischarge():

    def discharge1(pname):

        def discharge2():

            def sendemail():
                fromaddr = "patient_records@gsm.com"
                toaddr = lst2[0][17]

                # instance of MIMEMultipart
                msg = MIMEMultipart()

                # storing the senders email address
                msg['From'] = fromaddr

                # storing the receivers email address
                msg['To'] = toaddr

                # storing the subject
                msg['Subject'] = "Patient Discharge Summary - Grey Sloan Memorial"

                # string to store the body of the mail
                body = "Discharge summary for "+lst2[0][1]+" "+lst2[0][2]+" is attached below \nFor further queries you can reply to this Email or contact 1800-0000-56"

                # attach the body with the msg instance
                msg.attach(MIMEText(body, 'plain'))

                # open the file to be sent
                filename = pname + ".pdf"
                attachment = open(filename, "rb")

                # instance of MIMEBase and named as p
                p = MIMEBase('application', 'octet-stream')

                # To change the payload into encoded form
                p.set_payload((attachment).read())

                # encode into base64
                encoders.encode_base64(p)

                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                # attach the instance 'p' to instance 'msg'
                msg.attach(p)

                # creates SMTP session
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

            dtime = datetime.now()
            dtime1 = str(dtime)
            dsummary = T1.get(1.0, "end-1c")
            cmd = "UPDATE Patient_data SET Discharge_time = (?), Discharge_summary = (?) WHERE UID = (?)"
            data = [(dtime1, dsummary, uid)]
            cursor.executemany(cmd, data)
            cnxn.commit()
            lst2 = cursor.execute('''SELECT UID, FirstName, LastName, Age, Gender, Height, Weight, Insurance, Primary_Physician,
                                        Admission_Time, Initial_problem, Initial_diagnosis, Diagnosis, Discharge_time, Discharge_summary, Address, City, Email
                                     FROM Patient_data WHERE UID = (?) ;''',(uid))
            lst2 = cursor.fetchall()
            name = pname + ".txt"
            f = open(name, "x")
            f.close()
            f = open(name, "a")
            f.write("Grey Sloan Memorial - Patient Discharge Summary \n")
            f.write("Patient UID : " + lst2[0][0] + "\n")
            f.write("First Name : " + lst2[0][1] + "\n")
            f.write("Last Name : " + lst2[0][2] + "\n")
            f.write("Age : " + str(lst2[0][3]) + "\n")
            f.write("Gender : " + lst2[0][4] + "\n")
            f.write("Height : " + str(lst2[0][5]) + "\n")
            f.write("Weight : " + str(lst2[0][6]) + "\n")
            f.write("Insurance Company and Policy Number : " + lst2[0][7] + "\n")
            f.write("Primary Physician : " + lst2[0][8] + "\n")
            f.write("Time Admitted to Hospital : " + lst2[0][9] + "\n")
            f.write("Initial Problem Description : " + lst2[0][10] + "\n")
            f.write("Initial Diagnosis : " + lst2[0][11] + "\n")
            f.write("Final Diagnosis : " + lst2[0][12] + "\n")
            f.write("Time of discharge from Hospital : " + lst2[0][13] + "\n")
            f.write("Discharge Summary : " + lst2[0][14] + "\n")
            f.write("Patient Address : " + lst2[0][15] + "\n")
            f.write("City : " + lst2[0][16] + "\n")
            f.write("Email : "+lst2[0][17]+"\n")
            f.write("\n")
            f.write("\n")
            f.write("Grey Sloan Memorial Invoice \n")
            f.write("\n")
            f.write("List of tests Ordered" + "\n")
            f.write("\n")
            f.write("Sl.NO \t Test Name \t \t \t Price \n")
            uid1 = pname[0:7] + "Tests"
            cmd = "SELECT * FROM "+uid1
            medlst = cursor.execute(cmd)
            medlst = cursor.fetchall()
            medtotal = 0
            for i in range(0,len(medlst)) :
                f.write(str(i+1)+"\t"+medlst[i][0]+"\t \t \t"+str(medlst[i][1])+"\n")
                medtotal += medlst[i][1]
            f.write("\n")
            f.write("\n")
            f.write("List of Medications administered \n")
            f.write("\n")
            f.write("Sl.NO \t Medication Name \t \t \t Price \n")
            uid2 = pname[0:7] + "Prescription"
            cmd1 = "SELECT * FROM " + uid2
            tstlst = cursor.execute(cmd1)
            tstlst = cursor.fetchall()
            tsttotal = 0
            for i in range(0,len(tstlst)) :
                f.write(str(i+1)+"\t"+tstlst[i][0]+"\t \t \t"+str(tstlst[i][1])+"\n")
                tsttotal += tstlst[i][1]
            f.write("\n")
            f.write("\n")
            f.write("Total Bill Amount = "+str((medtotal+tsttotal))+"\n")
            f.write("Digitally Signed by "+lst2[0][8]+"\n")
            f.write("\n")
            f.write("This is a Computer Generated Copy, No Signature is Required")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=15)
            f = open(name, "r")
            for x in f:
                pdf.cell(200, 20, txt=x, ln=1, align="L")
            pdf.output(pname + ".pdf")
            sendemail()
            f.close()
            os.remove(name)
            cmd5 = "INSERT INTO Patient_data_archive SELECT * FROM Patient_data WHERE UID = ?"
            cmd6 = "DELETE FROM Patient_data WHERE UID = ?"
            cmd3 = "DROP TABLE "+uid1
            cmd4 = "DROP TABLE "+uid2
            cursor.execute(cmd5,uid)
            cnxn.commit()
            cursor.execute(cmd6,uid)
            cnxn.commit()
            cursor.execute(cmd3)
            cnxn.commit()
            cursor.execute(cmd4)
            cnxn.commit()
            discharge_window.destroy()
            discharge1_window.destroy()
            msgbox.showinfo("Patient Discharged Successfully","Patient Discharged Successfully")





        uid = pname[0:7]
        discharge1_window = Tk()
        discharge1_window.title("Grey Sloan Memorial Discharge Patient ")
        discharge1_window.geometry("3840x2160")

        L1 = Label(discharge1_window, text = "Enter Patient Discharge Summary")
        L1.place(x=200, y=150)
        T1 = Text(discharge1_window, height=6, width=90)
        T1.place(x=400,y=150)
        B1 = Button(discharge1_window, text = "Submit", command = discharge2)
        B1.place(x=300, y=300)

    discharge_window = Tk()
    discharge_window.title("Grey Sloan Memorial Discharge Patient ")
    discharge_window.geometry("3840x2160")
    lst = cursor.execute("""SELECT UID, FirstName, LastName, Primary_Physician FROM Patient_data""")
    lst = cursor.fetchall()

    lst1 = []
    for i in range(0, len(lst)):
        lst1.append(lst[i][0] + " - " + lst[i][1])

    L1 = Label(discharge_window, text="Select Patient ")
    L1.place(x=200, y=150)
    patient = StringVar()
    patient.set("Patient Selection")
    drop = OptionMenu(discharge_window, patient, *lst1, command=discharge1)
    drop.place(x=400, y=150)
    mainloop()

