from showdetails import *

main_window = Tk()
main_window.title("Grey Sloan Memorial Hospital")
main_window.geometry("800x800")
def command1(action):
    if action =="Doctor Login":
        doc_loginw()
    elif action == "Doctor Logout" :
        doc_logoutw()
    elif action == "New Patient Registration":
        newpatient()
    elif action == "Order Tests" :
        order_tests()
    elif action == "Update Patient Details" :
        updatedetials()
    elif action == "Order Prescription" :
        order_medications()
    elif action == "Discharge":
        patientdischarge()
    elif action == "Online Consultation":
        onlineregistration()
    elif action == "Online Consultation Doctor Login":
        doconline()
    elif action == "Show Patient Details":
        showdetails1()
    else :
        msgbox.showinfo("Invalid Selection")

command_button = ["Doctor Login", "Doctor Logout", "New Patient Registration","Order Tests", "Show Patient Details","Order Prescription","Update Patient Details","Discharge","Online Consultation","Online Consultation Doctor Login"]
maincmd = StringVar()
L1 = Label(main_window, text = "")
maincmd.set("Select Action")
dropdown = OptionMenu(main_window, maincmd, *command_button, command=command1)
dropdown.place(x=400, y=150)
mainloop()
