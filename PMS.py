from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import random
from datetime import datetime
import os
import datetime
from tkinter import messagebox
import mysql.connector



class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Information System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberOfTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffecsts=StringVar()
        self.futherinfo=StringVar()
        self.StorageAdvice=StringVar()
        self.Drivingusingmachine=StringVar()
        self.Howtousemachine=StringVar()
        self.Patientid=StringVar()
        self.nhsnumber=StringVar()
        self.Patientname=StringVar()
        self.DateofBirth=StringVar()
        self.Patientaddress=StringVar()
        self.Bloodpressure=StringVar()
        self.Medicine=StringVar()
        self.Patientname_for_search=StringVar()
        
        lbletitle=Label(self.root,bd=20,relief=RIDGE,text="Patient Inforamtion System",fg="red",bg="white",font=("ComicSans",50,"bold"))
        lbletitle.pack(side=TOP,fill=X)
        
        # ===========================================================
        
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                font=("arial",12,"bold"),text="patient info")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                font=("arial",12,"bold"),text="presciption")
        DataframeRight.place(x=990,y=5,width=460,height=350)
        
        
        #=========================== Buttons Frame ==========================
        
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
         #=========================== Details Frame ==========================
        
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        
        #=============================DataframeLeft===========================
        
        lblNameTablet =Label(DataframeLeft,text="names of tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=33)
        comNametablet["values"]=( "Nice","corona vacine","Acetamine","eno","paracetamol")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)
        
        lblref=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Reference No:",padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        textref=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.ref,width=35)
        textref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Dose",padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        texDose=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Dose,width=35)
        texDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("times new roman",12,"bold"),text="No of tablets",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        texNoOftablets=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.NumberOfTablets,width=35)
        texNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Lot",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        textLot=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Lot,width=35)
        textLot.grid(row=4,column=1)

        lblisseueDate=Label(DataframeLeft,font=("times new roman",12,"bold"),text="issue date",padx=2,pady=6)
        lblisseueDate.grid(row=5,column=0,sticky=W)
        textissueDate=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Issuedate,width=35)
        textissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Exp date",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        textExpDate=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.ExpDate,width=35)
        textExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Daily dose",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        textDailyDose=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DailyDose,width=35)
        textDailyDose.grid(row=7,column=1)

        lblsideEffects=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Side effects",padx=2,pady=6)
        lblsideEffects.grid(row=8,column=0,sticky=W)
        textsideEffects=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.sideEffecsts,width=35)
        textsideEffects.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Further info",padx=10,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        textFurtherinfo=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.futherinfo,width=35)
        textFurtherinfo.grid(row=0,column=3)

        lblBloodpressure=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Blood pressure:",padx=10,pady=6)
        lblBloodpressure.grid(row=1,column=2,sticky=W)
        textBloodpressure=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Bloodpressure,width=35)
        textBloodpressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Storage",padx=10,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        textstorage=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        textstorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("times new roman",12,"bold"),text="medicine",padx=10,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        texmedicine=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Medicine,width=35)
        texmedicine.grid(row=3,column=3)

        lblPatinetid=Label(DataframeLeft,font=("times new roman",12,"bold"),text="patient id",padx=10,pady=6)
        lblPatinetid.grid(row=4,column=2,sticky=W)
        texPaitientid=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Patientid,width=35)
        texPaitientid.grid(row=4,column=3)

        lblNNhsnumber=Label(DataframeLeft,font=("times new roman",12,"bold"),text="NHS number",padx=10,pady=6)
        lblNNhsnumber.grid(row=5,column=2,sticky=W)
        texNhsnukber=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.nhsnumber,width=35)
        texNhsnukber.grid(row=5,column=3)

        lblPatientNAme=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Patientname",padx=10,pady=6)
        lblPatientNAme.grid(row=6,column=2,sticky=W)
        texPatieintNme=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Patientname,width=35)
        texPatieintNme.grid(row=6,column=3)

        lblDob=Label(DataframeLeft,font=("times new roman",12,"bold"),text="DOB",padx=10,pady=6)
        lblDob.grid(row=7,column=2,sticky=W)
        texDob=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DateofBirth,width=35)
        texDob.grid(row=7,column=3)

        lblPatienaddress=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Patient Addrsess",padx=10,pady=6)
        lblPatienaddress.grid(row=8,column=2,sticky=W)
        texPatientAddress=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.Patientaddress,width=35)
        texPatientAddress.grid(row=8,column=3)


        #======================================DAtaframe RIght =========================================

        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=12,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        self.scrollbar = Scrollbar(DataframeRight, command=self.txtPrescription.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # Configure the text widget to use the scrollbar
        self.txtPrescription.config(yscrollcommand=self.scrollbar.set)

        search=Label(DataframeRight,font=("times new roman",12,"bold"),text="Patient name",padx=10,pady=6)
        search.grid(row=1,column=0,sticky=W)
        texSearch=Entry(DataframeRight,font=("arial",12,"bold"),textvariable=self.Patientname_for_search,width=33)
        texSearch.grid(row=1,column=0,sticky=E)

        btnSearch=Button(DataframeRight,command=self.fetch_data_search,text="Search",bg="blue",fg="white",font=("arial",8,"bold"),width=15,height=1,padx=2,pady=6)
        btnSearch.grid(row=2,column=0)

        

        #====================================Buttons================================
        btnPrescription=Button(Buttonframe,command=self.iPrescription,text="prescription",bg="green",fg="white",font=("arial",9,"bold"),width=28,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.iPresctiptionData,text="prescription data",bg="green",fg="white",font=("arial",9,"bold"),width=28,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.updateData,text="Update",bg="green",fg="white",font=("arial",9,"bold"),width=28,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.iDelete,text="Delete",bg="green",fg="white",font=("arial",9,"bold"),width=28,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnReset=Button(Buttonframe,command=self.fetch_data,text="Reset",bg="green",fg="white",font=("arial",9,"bold"),width=28,padx=2,pady=6)
        btnReset.grid(row=0,column=4)

        btnClear=Button(Buttonframe,text="Clear",command=self.clear,bg="green",fg="white",font=("arial",9,"bold"),width=28,padx=2,pady=6)
        btnClear.grid(row=0,column=5)

        btnexit=Button(Buttonframe,command=self.Iexit,text="Exit",bg="green",fg="white",font=("arial",9,"bold"),width=28,padx=2,pady=6)
        btnexit.grid(row=0,column=6)



        #================================Table==============================
        #==========================Scrool bar ===============================

        scrool_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scrool_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("name of tablets","ref","dose",
                                                              "nooftablets","lot","issuedate",
                                                              "expdate","dailydose","storage",
                                                              "nsbnumber","pname","dob","address"),
                                                              xscrollcommand=scrool_x.set,yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)

        scrool_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scrool_x=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("name of tablets", text="Name of Table")
        self.hospital_table.heading("ref", text="Reference")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="Number of Tablets")
        self.hospital_table.heading("lot", text="Lot Number")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Expiry Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nsbnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"
        

        self.hospital_table.column("name of tablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nsbnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        

#===========================Functions==========================
        
    def iPresctiptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","ALL FIELDS ARE REQUIRED")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234567890",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO hospital (Name_Of_Tablets, Reference_number, dose, Number_Of_Tablets, LOT, issuedate, expdate, daily_dose, storage, nsbnumber, Patient_name, dob, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NumberOfTablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsnumber.get(),
                    self.Patientname.get(),
                    self.DateofBirth.get(),
                    self.Patientaddress.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Record has been inserted")
            except mysql.connector.errors.IntegrityError as e:
                messagebox.showwarning("Warning", "Duplicate reference number entered. Please enter a unique reference number.")

    def updateData(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234567890",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Name_Of_Tablets=%s,dose=%s,Number_Of_Tablets=%s,LOT=%s,issuedate=%s,expdate=%s,daily_dose=%s,storage=%s,nsbnumber=%s,Patient_name=%s,dob=%s,address=%s where Reference_number=%s",
                (self.Nameoftablets.get(),
                self.Dose.get(),
                self.NumberOfTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsnumber.get(),
                self.Patientname.get(),
                self.DateofBirth.get(),
                self.Patientaddress.get(),
                self.ref.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been updated")
    
    
    


    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsnumber.set(row[9])
        self.Patientname.set(row[10])
        self.DateofBirth.set(row[11])
        self.Patientaddress.set(row[12])

    from datetime import datetime

    def iPrescription(self):
        self.txtPrescription.delete('1.0', END)
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference number:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"daily dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effects:\t\t\t"+self.sideEffecsts.get()+"\n")
        self.txtPrescription.insert(END,"Further info:\t\t\t"+self.futherinfo.get()+"\n")
        self.txtPrescription.insert(END,"storage advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"patientid:\t\t\t"+self.Patientid.get()+"\n")
        self.txtPrescription.insert(END,"nhssnumber:\t\t\t"+self.nhsnumber.get()+"\n")
        self.txtPrescription.insert(END,"Patientname:\t\t\t"+self.Patientid.get()+"\n")
        self.txtPrescription.insert(END,"date of birth:\t\t\t"+self.DateofBirth.get()+"\n")
        self.txtPrescription.insert(END,"paientaddress:\t\t\t"+self.Patientaddress.get()+"\n")

        # Insert the new prescription data
        prescription_data = [
            "name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n",
            "Reference number:\t\t\t" + self.ref.get() + "\n",
            "Dose:\t\t\t" + self.Dose.get() + "\n",
            "Lot:\t\t\t" + self.Lot.get() + "\n",
            "Issue date:\t\t\t" + self.Issuedate.get() + "\n",
            "Exp date:\t\t\t" + self.ExpDate.get() + "\n",
            "daily dose:\t\t\t" + self.DailyDose.get() + "\n",
            "Side Effects:\t\t\t" + self.sideEffecsts.get() + "\n",
            "Further info:\t\t\t" + self.futherinfo.get() + "\n",
            "storage advice:\t\t\t" + self.StorageAdvice.get() + "\n",
            "patientid:\t\t\t" + self.Patientid.get() + "\n",
            "nhssnumber:\t\t\t" + self.nhsnumber.get() + "\n",
            "Patientname:\t\t\t" + self.Patientid.get() + "\n",
            "date of birth:\t\t\t" + self.DateofBirth.get() + "\n",
            "paientaddress:\t\t\t" + self.Patientaddress.get() + "\n"
        ]

        # Set default filename as Patientid
        default_filename = self.ref.get() + ".txt"

        # Define the directory name
        directory_name = "Patient_Prescriptions"

        # Get the current directory
        current_directory = os.getcwd()

        # Create the folder if it doesn't exist
        folder_path = os.path.join(current_directory, directory_name)
        try:
            os.makedirs(folder_path, exist_ok=True)
            messagebox.showinfo("Success", "Folder created successfully on location: "+ folder_path)
        except OSError as e:
            messagebox.showerror("Error", f"Failed to create folder: {e}")

        # Specify the file path
        file_path = os.path.join(folder_path, default_filename)

        # Read existing data from the file if it exists
        existing_data = []
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                existing_data = file.readlines()

        # Initialize a list to store the updated prescription data
        updated_data = []

        # Update the prescription data
        for line in prescription_data:
            updated_data.append(line + "-----------------------------------------------------------------------------\n")

        # Write the updated prescription data to the file
        with open(file_path, "w") as file:
            file.writelines(updated_data)

        # Display success message
        messagebox.showinfo("Success", "Prescription saved successfully.")


    def iDelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234567890",database="mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_number=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        
        messagebox.showinfo("Delete","Patient have been deleted sucessfully")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234567890",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()

        for record in self.hospital_table.get_children():
            self.hospital_table.delete(record)

        if len(rows)!=0:
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def fetch_data_search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234567890", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital where Patient_name = %s", (self.Patientname_for_search.get(),))  # Pass the value of Patientname_for_search
        rows = my_cursor.fetchall()

        for record in self.hospital_table.get_children():
            self.hospital_table.delete(record)

        if len(rows) != 0:
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            
            # Clear all entry fields
            self.Nameoftablets.set("")
            self.ref.set("")
            self.Dose.set("")
            self.NumberOfTablets.set("")
            self.Lot.set("")
            self.Issuedate.set("")
            self.ExpDate.set("")
            self.DailyDose.set("")
            self.StorageAdvice.set("")
            self.nhsnumber.set("")
            self.Patientname.set("")
            self.DateofBirth.set("")
            self.Patientaddress.set("")

            conn.commit()
        conn.close()


    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberOfTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.nhsnumber.set("")
        self.Patientname.set("")
        self.DateofBirth.set("")
        self.Patientaddress.set("")
        self.txtPrescription.delete("1.0",END)

    def Iexit(self):
        iexit = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
        if iexit:
            self.root.destroy()
            login_window = Login(Tk())
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")

        Dataframe=Frame(self.root,bd=10,relief=RIDGE)
        Dataframe.place(x=0,y=10,width=400,height=290)

        self.username = StringVar()
        self.password = StringVar()

        lblusername = Label(Dataframe, text="Username:", font=("Arial", 14))
        lblusername.grid(row=0, column=0, padx=20, pady=20)
        self.txtusername = Entry(Dataframe, textvariable=self.username, font=("Arial", 14))
        self.txtusername.grid(row=0, column=1)

        lblpassword = Label(Dataframe, text="Password:", font=("Arial", 14))
        lblpassword.grid(row=1, column=0, padx=20, pady=20)
        self.txtpassword = Entry(Dataframe, textvariable=self.password, show="*", font=("Arial", 14))
        self.txtpassword.grid(row=1, column=1)

        btnlogin = Button(Dataframe, text="Login", command=self.login,fg="white",bg="#03f0fc", font=("Arial", 14))
        btnlogin.grid(row=2, columnspan=2)
        btnexit = Button(Dataframe, command=self.Iexit, text="Exit",fg="red", font=("arial", 14))
        btnexit.grid(row=3, columnspan=2,pady=10)

    def Iexit(self):
            iexit = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
            if iexit:
                self.root.destroy()    


    def login(self):
        username = self.username.get()
        password = self.password.get()

        # Check credentials in the database
        conn = mysql.connector.connect(host="localhost", username="root", password="1234567890", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        rows = my_cursor.fetchall()
        conn.close()

        if len(rows) > 0:
            # Login successful, open Hospital class
            self.root.destroy()
            root = Tk()
            ob = Hospital(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password")
        


    







root = Tk()
login_window = Login(root)
root.mainloop()