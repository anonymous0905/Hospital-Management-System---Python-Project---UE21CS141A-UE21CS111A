import pyodbc
from tkinter import *
import tkinter as tk
from datetime import datetime
from fpdf import FPDF
import random
from tkinter import ttk
from tkinter import messagebox as msgbox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
server = 'tcp:pesuhms.database.windows.net'
database = 'pesuhms'
username = 'shashank'
password = 'Encoder@1992'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()