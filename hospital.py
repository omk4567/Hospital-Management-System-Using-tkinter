from tkinter import*
from tkinter import ttk
import random 
import time
import datetime 
from tkinter import messagebox
import mysql.connector  
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas        

class Hospital:
    # making a construction
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System") #Title of window
        self.root.geometry("1350x600+0+0")   # widthXheight+x-axis start + y-axis start    

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.Expdate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInfomation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine= StringVar()
        self.HowToUseMedication = StringVar() 
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()   
        self.PatientName = StringVar()
        self.DateOfBirth= StringVar()
        self.PatientAddress = StringVar() 
        self.BloodPressure = StringVar()     



        lbltitle = Label(self.root, bd = 15, relief=RIDGE, text = "HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 40, "bold"))    
        lbltitle.pack(side=TOP, fill=X)   

        
        # -------------- Dataframe ----------------
        Dataframe = Frame(self.root, bd = 15, relief=RIDGE)    
        Dataframe.place(x=0, y=130, width=1350, height=400)                

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Patient Information") 
        DataframeLeft.place(x=0, y=5, width=980, height=350)          

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")    
        DataframeRight.place(x=990, y=5, width=322, height=350)  

        # ================ Buttons Frame ==================

        Buttonframe = Frame(self.root, bd = 20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=78)   

         # ================ Details Frame ==================

        Detailsframe = Frame(self.root, bd = 20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1350, height=130)                                       


        # ====================== DataframeLeft ==================

        lblNameTablet = Label(DataframeLeft, text="Names OF Tablet", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0) 
        
        comNametablet=ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets, state="readonly",font=("arial", 12, "bold"), width=33)
        comNametablet["values"] = ("Nice", "Corona Vacacine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan") #tuple of values 
        comNametablet.grid(row=0, column=1)    

        lblref = Label(DataframeLeft, text="Reference No. ", font=("arial", 12, "bold"), padx=2)
        lblref.grid(row=1, column=0, sticky=W)  
        txtref = Entry(DataframeLeft, textvariable=self.ref , font=("arial", 13, "bold"), width=35)  
        txtref.grid(row=1, column=1)  

        lblDose = Label(DataframeLeft, text="Dose: ", font=("arial", 12, "bold"), padx=2, pady=4) 
        lblDose.grid(row=2, column=0, sticky=W)  
        txtDose = Entry(DataframeLeft, textvariable=self.Dose ,font=("arial", 13, "bold"), width=35)  
        txtDose.grid(row=2, column=1)          

        lblNoOftablets = Label(DataframeLeft, text="No. Of Tablets :  ", font=("arial", 12, "bold"), padx=2, pady=6) 
        lblNoOftablets.grid(row=3, column=0, sticky=W)  
        txtNoOftablets = Entry(DataframeLeft, textvariable=self.NumberofTablets,font=("arial", 13, "bold"), width=35)  
        txtNoOftablets.grid(row=3, column=1)        
        
        lblLot = Label(DataframeLeft, text="Lot:  ", font=("arial", 12, "bold"), padx=2, pady=6) 
        lblLot.grid(row=4, column=0, sticky=W)  
        txtLot = Entry(DataframeLeft, textvariable=self.Lot,font=("arial", 13, "bold"), width=35)  
        txtLot.grid(row=4, column=1)        

        lblissueDate = Label(DataframeLeft, text="Issue Date : ", font=("arial", 12, "bold"), padx=2, pady=6) 
        lblissueDate.grid(row=5, column=0, sticky=W)  
        txtissueDate = Entry(DataframeLeft, textvariable=self.Issuedate,font=("arial", 13, "bold"), width=35)  
        txtissueDate.grid(row=5, column=1)   

        lblExpDate = Label(DataframeLeft, text="Expiry Date : ", font=("arial", 12, "bold"), padx=2, pady=6) 
        lblExpDate.grid(row=6, column=0, sticky=W)  
        txtExpDate = Entry(DataframeLeft, textvariable=self.Expdate,font=("arial", 13, "bold"), width=35)  
        txtExpDate.grid(row=6, column=1)   

        lblDailyDose = Label(DataframeLeft, text="Daily Dose : ", font=("arial", 12, "bold"), padx=2, pady=4) 
        lblDailyDose.grid(row=7, column=0, sticky=W)  
        txtDailyDose = Entry(DataframeLeft, textvariable=self.DailyDose,font=("arial", 13, "bold"), width=35)  
        txtDailyDose.grid(row=7, column=1)             

        lblSideEffect = Label(DataframeLeft, text="Side Effect : ", font=("arial", 12, "bold"), padx=2, pady=6) 
        lblSideEffect.grid(row=8, column=0, sticky=W)  
        txtSideEffect = Entry(DataframeLeft,textvariable=self.sideEffect,font=("arial", 13, "bold"), width=35)     
        txtSideEffect.grid(row=8, column=1)     

        lblFurtherinfo = Label(DataframeLeft, text="Further Information : ", font=("arial", 12, "bold"), padx=2) 
        lblFurtherinfo.grid(row=0, column=2, sticky=W)  
        txtFurtherinfo = Entry(DataframeLeft, textvariable=self.FurtherInfomation ,font=("arial", 12, "bold"), width=35)     
        txtFurtherinfo.grid(row=0, column=3)  

        lblBloodPressure = Label(DataframeLeft, text="Blood Pressure : ", font=("arial", 12, "bold"), padx=2, pady=6)     
        lblBloodPressure.grid(row=1, column=2, sticky=W)  
        txtBloodPressure = Entry(DataframeLeft, textvariable=self.BloodPressure,font=("arial", 12, "bold"), width=35)          
        txtBloodPressure.grid(row=1, column=3)   

        lblStorage = Label(DataframeLeft, text="Storage Advice : ", font=("arial", 12, "bold"), padx=2, pady=6)     
        lblStorage.grid(row=2, column=2, sticky=W)      
        txtStorage = Entry(DataframeLeft, textvariable=self.StorageAdvice,font=("arial", 12, "bold"), width=35)             
        txtStorage.grid(row=2, column=3) 

        lblMedicine = Label(DataframeLeft, text="Medication : ", font=("arial", 12, "bold"), padx=2, pady=6)     
        lblMedicine.grid(row=3, column=2, sticky=W)  
        txtMedicine = Entry(DataframeLeft, textvariable=self.HowToUseMedication,font=("arial", 12, "bold"), width=35)          
        txtMedicine.grid(row=3, column=3)        

        lblPatientId = Label(DataframeLeft, text="Patient ID : ", font=("arial", 12, "bold"), padx=2, pady=6)     
        lblPatientId.grid(row=4, column=2, sticky=W)  
        txtPatientId = Entry(DataframeLeft, textvariable=self.PatientId,font=("arial", 12, "bold"), width=35)          
        txtPatientId.grid(row=4, column=3)     

        lblNhsNumber = Label(DataframeLeft, text="NHS Number : ", font=("arial", 12, "bold"), padx=2, pady=6)     
        lblNhsNumber.grid(row=5, column=2, sticky=W)  
        txtNhsNumber = Entry(DataframeLeft, textvariable=self.nhsNumber,font=("arial", 12, "bold"), width=35)          
        txtNhsNumber.grid(row=5, column=3)  

        lblPatientname = Label(DataframeLeft, text="Patient Name : ", font=("arial", 12, "bold"), padx=2, pady=6)     
        lblPatientname.grid(row=6, column=2, sticky=W)  
        txtPatientname = Entry(DataframeLeft, textvariable=self.PatientName,font=("arial", 12, "bold"), width=35)          
        txtPatientname.grid(row=6, column=3)  
                           
 
        lblDateOfBirth = Label(DataframeLeft, text="Date Of Birth : ", font=("arial", 12, "bold"), padx=2, pady=6)     
        lblDateOfBirth.grid(row=7, column=2, sticky=W)  
        txtDateOfBirth = Entry(DataframeLeft, textvariable=self.DateOfBirth,font=("arial", 12, "bold"), width=35)             
        txtDateOfBirth.grid(row=7, column=3)   

        lblPatientAddress = Label(DataframeLeft, text="Patient Address : ", font=("arial", 12, "bold"), padx=2, pady=6)     
        lblPatientAddress.grid(row=8, column=2, sticky=W)  
        txtPatientAddress = Entry(DataframeLeft, textvariable=self.PatientAddress,font=("arial", 12, "bold"), width=35)          
        txtPatientAddress.grid(row=8, column=3)     

        # ============================= DataframeRight =================================================

        self.txtPrescription=Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)      
  
        # ============================= Buttons ======================                    

        btnPrescription = Button(Buttonframe,bg="green", fg="white",command=self.iPrescription,font=("arial", 10, "bold"),text="Prescription" ,width=21, height=2, padx=2, pady=6) 
        btnPrescription.grid(row=0, column=0)  

        btnSave_to_pdf = Button(Buttonframe,bg="green", fg="white",command=self.save_prescription_to_pdf,font=("arial", 10, "bold"),text="Save_Prescription_to_pdf" ,width=21, height=2, padx=2, pady=6) 
        btnSave_to_pdf.grid(row=0, column=1)            


        btnPrescriptionData = Button(Buttonframe,bg="green", fg="white", command=self.iPrescriptionData,font=("arial", 10, "bold"),text="Prescription Data" ,width=21, height=2, padx=2, pady=6)    
        btnPrescriptionData.grid(row=0, column=2)     

        btnUpdate = Button(Buttonframe,bg="green", fg="white",command=self.update_data,font=("arial", 10, "bold"),text="Update" ,width=21, height=2, padx=2, pady=6)  
        btnUpdate.grid(row=0, column=3)

        btnDelete = Button(Buttonframe,bg="green", fg="white",command=self.idelete,font=("arial", 10, "bold"),text="Delete" ,width=21, height=2, padx=2, pady=6) 
        btnDelete.grid(row=0, column=4)   

        btnClear = Button(Buttonframe,bg="green", fg="white",command=self.clear,font=("arial", 10, "bold"),text="Clear" ,width=21, height=2, padx=2, pady=6)    
        btnClear.grid(row=0, column=5)  

        btnExit = Button(Buttonframe,bg="green", fg="white",command=self.iExit,font=("arial", 10, "bold"),text="Exit" ,width=21, height=2, padx=2, pady=6)  
        btnExit.grid(row=0, column=6)                 
 

        # ==================== Table ========================
        # ==================== Scrollbar =================    

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)               

        self.hospital_table = ttk.Treeview(Detailsframe, column=("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)  

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview) 
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftable", text="Name Of Table")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No. Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")   

        self.hospital_table["show"] = "headings"

       

        self.hospital_table.column("nameoftable", width=70)
        self.hospital_table.column("ref", width=70)
        self.hospital_table.column("dose", width=70)
        self.hospital_table.column("nooftablets", width=70)
        self.hospital_table.column("lot", width=70)
        self.hospital_table.column("issuedate", width=70)
        self.hospital_table.column("expdate", width=70)
        self.hospital_table.column("dailydose", width=70)
        self.hospital_table.column("storage", width=70)
        self.hospital_table.column("nhsnumber", width=70)
        self.hospital_table.column("pname", width=70)
        self.hospital_table.column("dob", width=70)
        self.hospital_table.column("address", width=70)  

        
        self.hospital_table.pack(fill=BOTH, expand=1)  
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)     
        self.fetch_data() 
        # ========================= Functionality Declaration ====================================
    
    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")  
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Omkar@2151", database="hospital_management_system") 
            my_cursor = conn.cursor()   
            my_cursor.execute("insert into hospital values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (

                 self.Nameoftablets.get(),
                 self.ref.get(), 
                 self.Dose.get(),
                 self.NumberofTablets.get(), 
                 self.Lot.get(),
                 self.Issuedate.get(), 
                 self.Expdate.get(), 
                 self.DailyDose.get(),
                 self.StorageAdvice.get(), 
                 self.nhsNumber.get(), 
                 self.PatientName.get(), 
                 self.DateOfBirth.get(), 
                 self.PatientAddress.get()

            ))

            conn.commit()
            conn.close()  
            self.fetch_data() 
            messagebox.showinfo("Success", "Record has been inserted")     
    
    def update_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Omkar@2151", database="hospital_management_system") 
        my_cursor = conn.cursor()   
        my_cursor.execute("update hospital set Name_of_tablets=%s, dose=%s, Numberoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s where Reference_No=%s", (

                 self.Nameoftablets.get(),
                 self.Dose.get(),
                 self.NumberofTablets.get(), 
                 self.Lot.get(),
                 self.Issuedate.get(), 
                 self.Expdate.get(), 
                 self.DailyDose.get(),
                 self.StorageAdvice.get(), 
                 self.nhsNumber.get(), 
                 self.PatientName.get(), 
                 self.DateOfBirth.get(), 
                 self.PatientAddress.get(),
                 self.ref.get()     

            ))      
              
        conn.commit()
        conn.close()  
        self.fetch_data()    
        messagebox.showinfo("Success", "Record has been updated succesfully")   


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Omkar@2151", database="hospital_management_system") 
        my_cursor = conn.cursor()   
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall() 
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    

    def get_cursor(self, event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row) 
        row=content["values"]   
        self.Nameoftablets.set(row[0])  
        self.ref.set(row[1])  
        self.Dose.set(row[2])  
        self.NumberofTablets.set(row[3])  
        self.Lot.set(row[4])  
        self.Issuedate.set(row[5])  
        self.Expdate.set(row[6])  
        self.DailyDose.set(row[7])  
        self.StorageAdvice.set(row[8])  
        self.nhsNumber.set(row[9])  
        self.PatientName.set(row[10])  
        self.DateOfBirth.set(row[11])  
        self.PatientAddress.set(row[12])      

    def iPrescription(self):
        self.txtPrescription.insert(END, "Name Of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")   
        self.txtPrescription.insert(END, "Reference No:\t\t\t"+self.ref.get()+"\n") 
        self.txtPrescription.insert(END, "Dose:\t\t\t"+self.Dose.get()+"\n") 
        self.txtPrescription.insert(END, "Number Of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")    
        self.txtPrescription.insert(END, "Lot:\t\t\t"+self.Lot.get()+"\n") 
        self.txtPrescription.insert(END, "Issue Date:\t\t\t"+self.Issuedate.get()+"\n") 
        self.txtPrescription.insert(END, "Expiry Date:\t\t\t"+self.Expdate.get()+"\n") 
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t"+self.DailyDose.get()+"\n") 
        self.txtPrescription.insert(END, "Side Effect:\t\t\t"+self.sideEffect.get()+"\n") 
        self.txtPrescription.insert(END, "Further Information:\t\t\t"+self.FurtherInfomation.get()+"\n") 
        self.txtPrescription.insert(END, "StorageAdvice:\t\t\t"+self.StorageAdvice.get()+"\n") 
        self.txtPrescription.insert(END, "DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n") 
        self.txtPrescription.insert(END, "PatientId:\t\t\t"+self.PatientId.get()+"\n") 
        self.txtPrescription.insert(END, "NHSNumber:\t\t\t"+self.nhsNumber.get()        +"\n") 
        self.txtPrescription.insert(END, "PatientName:\t\t\t"+self.PatientName.get()+"\n")  
        self.txtPrescription.insert(END, "DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")   
        self.txtPrescription.insert(END, "PatientAddress:\t\t\t"+self.PatientAddress.get()+"\n")  


    def idelete(self):  
        if self.ref.get() == "":
            messagebox.showerror("Error", "Reference Number is required for deletion")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Omkar@2151", database="hospital_management_system") 
            my_cursor = conn.cursor()   
            query = "delete from hospital where Reference_No=%s"
            value=(self.ref.get(),)
            my_cursor.execute(query,  value)                                                                 

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient has been deleted successfully")           
    
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInfomation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")  
        self.txtPrescription.delete("1.0", END)   

    
    def save_prescription_to_pdf(self):
      prescription_text = self.txtPrescription.get("1.0", END)
    
      if not prescription_text.strip():
        messagebox.showerror("Error", "Prescription is empty. Please generate the prescription first.")
        return
    
      c = canvas.Canvas("prescription.pdf", pagesize=letter)
    
      x = 50
      y = 750
    
      for line in prescription_text.split("\n"):
        c.drawString(x, y, line)
        y -= 20  # Move down for the next line
        if y < 50:  # Add a new page if necessary
            c.showPage()
            y = 750
    
      c.save()   
      messagebox.showinfo("Success", "Prescription saved as PDF successfully")     


    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return 

    

root = Tk()      
ob = Hospital(root)  
root.mainloop()         



