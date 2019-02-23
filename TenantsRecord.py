from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import time
from datetime import datetime
import sqlite3

#===========================backend=====================================================================================
class DB:
    def __init__(self):
        self.conn=sqlite3.connect("tenantsRecord.db")
        self.cursor=self.conn.cursor()
        self.conn.execute("CREATE TABLE IF NOT EXISTS tenantsRecord(id INTEGER PRIMARY KEY ,Tenant text ,HouseNumber text ,MeterNumber text ,PreviousReading text ,PrevReadingDate text ,CurrentReading text ,CurrReadingDate text ,UnitsConsumed text ,Rate text ,Tarrif text ,BillType text ,Total text)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def ViewData(self):
        self.cursor.execute("SELECT * FROM tenantsRecord")
        rows=self.cursor.fetchall()
        return rows

    def addten(self,Tenant,HouseNumber,MeterNumber,PreviousReading,PrevReadingDate,CurrentReading,CurrReadingDate,UnitsConsumed,Rate,tarrif,BillType,Total):
        self.cursor.execute("INSERT INTO tenantsRecord VALUES  (NULL,?,?,?,?,?,?,?,?,?,?,?,?)",(Tenant,HouseNumber,MeterNumber,PreviousReading,PrevReadingDate,CurrentReading,CurrReadingDate,UnitsConsumed,Rate,tarrif,BillType,Total))
        self.conn.commit()
        self.ViewData()

    def search(self,Tenant="",HouseNumber="",MeterNumber=""):
        self.cursor.execute("SELECT * FROM tenantsRecord WHERE Tenant=? OR HouseNumber=? OR MeterNumber=?",(Tenant, HouseNumber,MeterNumber))
        found_rows=self.cursor.fetchall()
        return found_rows

    def update(self,id,Tenant,HouseNumber,MeterNumber,PreviousReading,PrevReadingDate,CurrentReading,CurrReadingDate,UnitsConsumed,Rate,tarrif,BillType,Total):
        self.cursor.execute("UPDATE books SET Tenant=?,HouseNumber=?,MeterNumber=?,Previousreading=?,PrevReadingDate=?,CurrentReading=?,CurrreadingDate=?,UnitsConsumed=?,Rate=?,tarrif=?,BillType=?,Total=?, WHERE id=?",(Tenant,HouseNumber,MeterNumber,PreviousReading,PrevReadingDate,CurrentReading,CurrReadingDate,UnitsConsumed,Rate,tarrif,BillType,Total))
        self.ViewData()
    def DeleteRec(self,id):
        self.cursor.execute("DELETE FROM tenantsRecord WHERE id=?",(id))
        self.conn.commit()
        self.ViewData()

db=DB()
def get_selected_row(event):
            global selected_tuple
            index = self.tenantlist.curselection()[0]
            selected_tuple=self.tenantlist.get(index)
            txttena1.delete(0,END)
            txttena1.insert(END,selected_tuple[1])
            self.txttena2.delete(0,END)
            self.txttena2.insert(END,selected_tuple[2])
            self.txttena3.delete(0,END)
            self.txttena3.insert(END,selected_tuple[3])
            self.txttena4.delete(0,END)
            self.txttena4.insert(END,selected_tuple[4])
            self.txttena5.delete(0,END)
            self.txttena5.insert(END,selected_tuple[5])
            self.txttena6.delete(0,END)
            self.txttena6.insert(END,selected_tuple[6])
            self.txttena7.delete(0,END)
            self.txttena7.insert(END,selected_tuple[7])
            self.txttena8.delete(0,END)
            self.txttena8.insert(END,selected_tuple[8])
            self.txttena9.delete(0,END)
            self.txttena9.insert(END,selected_tuple[9])
            self.txttena10.delete(0,END)
            self.txttena10.insert(END,selected_tuple[10])
            self.txttena11.delete(0,END)
            self.txttena11.insert(END,selected_tuple[11])
            self.txttena12.delete(0,END)
            self.txttena12.insert(END,selected_tuple[12])
    
     
#=======================================================================================================================================
class WaterBill:
    def __init__(self,root):

        self.root = root
        self.root.title("Water bill Database System ")
        #self.root.grid(width=900,height=550)
        self.root.config(bg="cadet Blue")

        Tenant=StringVar() 
        HouseNumber=StringVar()
        MeterNumber=StringVar()
        PreviousReading=StringVar()
        PrevReadingDate=StringVar()
        CurrentReading=StringVar()
        CurrReadingDate=StringVar()
        UnitsConsumed=StringVar()
        Rate=StringVar()
        Tarrif=StringVar()
        BillType=StringVar()
        Total=StringVar()
        Dateissued=StringVar()

        #==============================function=============================================================================
        Rate.set("3305")
        Tarrif.set("NWSC tarrif Rate")
        BillType.set("Institutional")
        def CostOfWater():
            #item1=float(UnitsConsumed.get())
            #item2=float(Rate.get())
            item3=int(PreviousReading.get())
            item4=int(CurrentReading.get())

            Consumed=(item4-item3)
            UnitsConsumed.set(Consumed)

            BillTotal=(Consumed*3000)
            

            Total.set(BillTotal)
            #imglabel = Label(root,image=img).grid(row=1, column=1)
            Dateissued.set(time.strftime("%d/%m/%Y"))
            self.txtBill.insert(END,"   MAKERERE UNIVERSITY WATER BILL\n\n")
            self.txtBill.insert(END,"====================================" "\n")
            self.txtBill.insert(END,"Tenant:  "+Tenant.get()+"\t\t\t"+Dateissued.get()+ "\n\n")
            self.txtBill.insert(END,"House Number:-----------------\t\t"+HouseNumber.get()+"\n\n")
            self.txtBill.insert(END,"Meter Number:-----------------\t\t"+MeterNumber.get()+"\n\n")
            self.txtBill.insert(END,"Bill Type:-----------------\t\t"+BillType.get()+"\n\n")
            self.txtBill.insert(END,"Previous Reading:-------------\t\t"+PreviousReading.get()+"\n\n")
            self.txtBill.insert(END,"Previous reading date:--------\t\t"+PrevReadingDate.get()+"\n\n")
            self.txtBill.insert(END,"Current Reading:--------------\t\t"+CurrentReading.get()+"\n\n")
            self.txtBill.insert(END,"Current Reading Date:---------\t\t"+CurrReadingDate.get()+"\n\n")
            self.txtBill.insert(END,"Rate:-------------------------\t\t"+Rate.get()+"\n\n\n")
            self.txtBill.insert(END,"=====================================" "\n")
            self.txtBill.insert(END,"Units Consumed:---------------\t\t"+UnitsConsumed.get()+"\n")
            self.txtBill.insert(END,"Total:\t\t\t"+Total.get()+"\n")
            self.txtBill.insert(END,"=====================================" "\n")

        #==================================Database Function================================================
        def addData():
            db.addten(Tenant.get(),HouseNumber.get(),MeterNumber.get(),PreviousReading.get(),PrevReadingDate.get(),CurrentReading.get(),CurrReadingDate.get(),UnitsConsumed.get(),Rate.get(),Tarrif.get(),BillType.get(),Total.get())
            tenantlist.delete(0,END)
            tenantlist.insert(END,(Tenant.get(),HouseNumber.get(),MeterNumber.get(),PreviousReading.get(),PrevReadingDate.get(),CurrentReading.get(),CurrReadingDate.get(),UnitsConsumed.get(), Rate.get(),Tarrif.get(),BillType.get(),Total.get()))


        def displayData():
             tenantlist.delete(0,END)
             for row in db.ViewData():
                 tenantlist.insert(END, row)

        

       # def updateData():
         #   db.update()
            
        
        #===================================================================================================

        def Reset():
            self.txtBill.delete("1.0",END)
            Tenant.set("")
            HouseNumber.set("")
            MeterNumber.set("")
            PreviousReading.set("")
            PrevReadingDate.set("")
            CurrentReading.set("")
            CurrReadingDate.set("")
            UnitsConsumed.set("")
            Total.set("")


        def on_closing():
            dd=db
            if tkinter.messagebox.askyesno("Are you sure you want to exit"):
                root.destroy()
                del dd
        root.protocol("WM_DELETE_WINDOW",on_closing)

        def delete_command():
            db.DeleteRec(selected_tuple[0])

        def update_command():
            db.update(selected_tuple[0],Tenant.get(),HouseNumber.get(),MeterNumber.get(),PreviousReading.get(),PrevReadingDate.get(),CurrentReading.get(),CurrReadingDate.get(),UnitsConsumed.get(),Rate.get(),Tarrif.get(),BillType.get(),Total.get())
        



#==================================Frame=======================================
        MainFrame = Frame(self.root,bg="cadet blue")
        MainFrame.grid()
        #self.lblTitle = Label(MainFrame,text="\t\t   Makerere University water bill system\t    ",font=('Times New Roman',30,'bold')
        #,pady=9,bd=5,bg='AliceBlue', fg="Black",justify=CENTER).grid(row=0,column=2)

        DataFrame2= Frame(MainFrame,bd=1,width=1350, height=400,padx=20,relief=RIDGE,bg="cadet blue")
        DataFrame2.pack(side=BOTTOM)

        ListFrame=Frame(DataFrame2,bd=2,width=1330,height=280,padx=18,pady=10,relief=RIDGE,bg="cadet blue")
        ListFrame.pack(side=TOP)
        ButtonFrame=Frame(DataFrame2,bd=2,width=1322,height=50,padx=18,pady=10,relief=RIDGE,bg="cadet Blue")
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=1,width=1350,height=400,padx=20,pady=20,relief=RIDGE,bg="cadet blue")
        DataFrame.pack(side=TOP)

        DataFrameLeft=LabelFrame(DataFrame,bd=1,width=900,height=200,padx=20,pady=6,relief=RIDGE,bg="AliceBlue",font=("Arial",18,'bold'),text='tenant Details\n')
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight=LabelFrame(DataFrame,bd=1,width=440,height=200,padx=31,pady=6,relief=RIDGE,bg="powder blue",font=('Arial',18,'bold'),text='water Bill\n')
        DataFrameRight.pack(side=RIGHT)

        #==========================================================================================================================================
        self.lbltena1=Label(DataFrameLeft,font=('arial',14,'bold'),text='Tenant:\n',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena1.grid(row=0,column=0,sticky=W)
        self.txttena1=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=Tenant,width=20)
        self.txttena1.grid(row=0,column=1)

        self.lbltena2=Label(DataFrameLeft,font=('arial',14,'bold'),text=' House Number:\n',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena2.grid(row=0,column=2,sticky=W) 
        self.txttena2=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=HouseNumber,width=20)
        self.txttena2.grid(row=0,column=3)

        self.lbltena3=Label(DataFrameLeft,font=('arial',14,'bold'),text='Meter Number:\n',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena3.grid(row=1,column=0,sticky=W)
        self.txttena3=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=MeterNumber,width=20)
        self.txttena3.grid(row=1,column=1)
        
        self.lbltena4=Label(DataFrameLeft,font=('arial',14,'bold'),text=' Rate:\n',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena4.grid(row=1,column=2,sticky=W)
        self.txttena4=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=Rate,width=20)
        self.txttena4.grid(row=1,column=3)

        self.lbltena5=Label(DataFrameLeft,font=('arial',14,'bold'),text='Tarrif:\n',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena5.grid(row=2,column=0,sticky=W)
        self.txttena5=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=Tarrif,width=20)
        self.txttena5.grid(row=2,column=1)

        self.lbltena6=Label(DataFrameLeft,font=('arial',14,'bold'),text=' Bill Type:\n',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena6.grid(row=2,column=2,sticky=W)
        self.txttena6=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=BillType,width=20)
        self.txttena6.grid(row=2,column=3)

        self.lbltena7=Label(DataFrameLeft,font=('arial',14,'bold'),text='Previous Reading:\n',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena7.grid(row=3,column=0,sticky=W)
        self.txttena7=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=PreviousReading,width=20)
        self.txttena7.grid(row=3,column=1)

        self.lbltena8=Label(DataFrameLeft,font=('arial',14,'bold'),text=' Previous Reading Date:\n',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena8.grid(row=3,column=2,sticky=W)
        self.txttena8=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=PrevReadingDate,width=20)
        self.txttena8.grid(row=3,column=3)
 
        self.lbltena9=Label(DataFrameLeft,font=('arial',14,'bold'),text='Current Reading:\n',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena9.grid(row=4,column=0,sticky=W)
        self.txttena9=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=CurrentReading,width=20)
        self.txttena9.grid(row=4,column=1)

        self.lbltena10=Label(DataFrameLeft,font=('arial',14,'bold'),text=' Current Reading Date:\n',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena10.grid(row=4,column=2,sticky=W)
        self.txttena10=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=CurrReadingDate,width=20)
        self.txttena10.grid(row=4,column=3)
        
        self.lbltena11=Label(DataFrameLeft,font=('arial',14,'bold'),text='Units Consumed:',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena11.grid(row=5,column=0,sticky=W)
        self.txttena11=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=UnitsConsumed,width=20)
        self.txttena11.grid(row=5,column=1)

        self.lbltena12=Label(DataFrameLeft,font=('arial',14,'bold'),text=' Total:',padx=2,pady=2,fg='Black',bg='AliceBlue')
        self.lbltena12.grid(row=5,column=2,sticky=W)
        self.txttena12=Entry(DataFrameLeft,font=('arial',14,'bold'),textvariable=Total,width=20)
        self.txttena12.grid(row=5,column=3)

        #================================bill==================================================
        self.txtBill = Text(DataFrameRight,height=15,width=40,bd=1,font=('arial',12,'bold'))
        self.txtBill.grid(row=0,column=0)
        #======================================listframe=================================================

        scrollbar=Scrollbar(ListFrame)
        scrollbar.grid(row=0, column=1,sticky='ns')

        tenantlist=Listbox(ListFrame,width=140,height=11,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        tenantlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=tenantlist.yview)

        #======================================Buttonframe=================================================
        self.TotalData=Button(ButtonFrame,text='Total',font=('arial',12,'bold'),height=1,width=11,bd=2,padx=13,command=CostOfWater)
        self.TotalData.grid(row=0,column=0)

        self.btnUpdate=Button(ButtonFrame,text='Update',font=('arial',12,'bold'),height=1,width=11,bd=2,padx=13,command=update_command)
        self.btnUpdate.grid(row=0,column=1)

        self.printData=Button(ButtonFrame,text='Print',font=('arial',12,'bold'),height=1,width=11,bd=2,padx=13)
        self.printData.grid(row=0,column=2)

        self.btnDisplay=Button(ButtonFrame,text='Display Tenants',font=('arial',12,'bold'),height=1,width=11,bd=2,padx=13,command=displayData)
        self.btnDisplay.grid(row=0,column=3)

        self.btnSearch=Button(ButtonFrame,text='Search',font=('arial',12,'bold'),height=1,width=11,bd=2,padx=13)
        self.btnSearch.grid(row=0,column=4)

        self.btnView=Button(ButtonFrame,text='View',font=('arial',12,'bold'),height=1,width=11,bd=2,padx=13,command=get_selected_row)
        self.btnView.grid(row=0,column=5)

        self.btnAddData=Button(ButtonFrame,text='Add New',font=('arial',12,'bold'),height=1,width=11,bd=2,padx=13,command=addData)
        self.btnAddData.grid(row=0,column=6)

        self.btnDelete=Button(ButtonFrame,text='Delete',font=('arial',12,'bold'),bg='Red',height=1,width=11,bd=2,padx=13,command=delete_command)
        self.btnDelete.grid(row=0,column=7)

        self.btnClear=Button(ButtonFrame,text='Reset',font=('arial',12,'bold'),height=1,width=11,bd=2,padx=13,command=Reset)
        self.btnClear.grid(row=0,column=8)

        

        



        



        

        



 
if __name__=='__main__':
    root = Tk()
    application = WaterBill(root)
    root.mainloop()