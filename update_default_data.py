import pyodbc
# code updates the physician ID table with default login and passwords
# to be executed only once
server = 'tcp:hmspesu.database.windows.net' #server to be replaced with your azure server
database = 'pesuhms' #database to be replaced with your azure database
username = 'shashank'#username to be replaced with your authorized user for the above server
password = 'Encoder@1992'#Password to be replaced with your server password
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
physician_list = ["Dr. Grey", "Dr. Shepard", "Dr. Baily", "Dr. Hunt", "Dr. Karev", "Dr. Avery", "Dr. Yang", "Dr. Wilson", "Dr. Robbins"]
login_list = ["GREY921", "SHPD245", "BALY734", "HUNT459", "KREV843", "AVRY432", "YANG389", "WLSN643", "RBNS851"]
psd = ["921", "245", "734", "459", "843", "432", "389", "643", "851"]
for i in range(0,len(physician_list)):
    cursor.execute(
        """
        INSERT INTO PhysicianID
        (Name, Username, Password)
        VALUES (?, ?, ?)
        """,
        (physician_list[i], login_list[i], psd[i])
    )
    cnxn.commit()
