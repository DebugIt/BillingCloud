from tkinter import *
import random
import pymysql

class AddBill(Tk):
    def __init__(self):
        super().__init__()
        # geometry
        self.geometry("1500x700")
        # title
        self.title("Add New Bill")
        # variables
        self.val1 = StringVar()
        self.to = StringVar()
        self.quantity = IntVar()
        self.rate = IntVar()
        self.bill_no = StringVar()
        self.total = StringVar()
        self.x = random.randint(1000, 9999)
        self.bill_no.set(str(self.x))

        global l
        l = []

# icon
        self.iconbitmap("BC_logo-removebg-preview.ico")

    def backgrnd(self):
        self.bg = PhotoImage(file='add bill bg.png')
        self.myLabel = Label(root, image=self.bg)
        self.myLabel.pack()

# label
    def totalLabel(self):
        self.totallabel = Entry(root, textvariable=self.total , bg='#272222', fg='white')
        self.totallabel.place(relx='0.35', rely='0.25')

# product
    def productLabel(self):
        self.productlabel = Label(root, text='Enter your product name:',bg='#272222', fg='white', font='comicsansms 10 bold')
        self.productlabel.place(relx='0.01', rely='0.05')


    def entry(self):
        self.entry1 = Entry(root, textvariable=self.val1, bg='#272222', fg="white")
        self.entry1.place(relx='0.15', rely='0.05')

# to
    def ToLabel(self):
        self.toLab = Label(root, text='To-', bg='#272222', fg='white', font='comicsansms 10 bold')
        self.toLab.place(relx='0.08', rely='0.15')

    def To(self):
        self.toEntry = Entry(root, textvariable=self.to, bg='#272222', fg='white')
        self.toEntry.place(relx='0.15', rely='0.15')

# quantity
    def quanLab(self):
        self.Qlabel = Label(root, text='Enter Quantity:', bg='#272222', fg='white', font='comicsansms 10 bold')
        self.Qlabel.place(relx='0.05', rely='0.25')

    def quanEnt(self):
        self.qEntry = Entry(root, textvariable=self.quantity, bg="#272222", fg='white')
        self.qEntry.place(relx='0.15', rely='0.25')

# rate
    def rateLab(self):
        self.rlabel = Label(root, text='Enter product total:', bg='#272222', fg='white', font='comicsansms 10 bold')
        self.rlabel.place(relx='0.05', rely='0.35')

    def rateEntry(self):
        self.rentry = Entry(root, textvariable=self.rate, bg='#272222', fg='white')
        self.rentry.place(relx='0.15', rely='0.35')

# Bill frame
    def Blabel(self):
        self.bLabel = Label(root, text='**BILL**', bg='#272222', fg='white', font='comicsansms 10 bold')
        self.bLabel.place(relx='0.78', rely='0.05')

    def frameing(self):
        self.F = Frame(root, bd=10)
        self.F.place(relx='0.65', rely='0.10', width="400", height="400")

    def txtArea(self):
        self.scroll_y = Scrollbar(self.F, orient=VERTICAL)
        self.textArea = Text(self.F, yscrollcommand=self.scroll_y)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.textArea.yview)
        self.textArea.pack()
        self.WelcomeUser()


# button
    def AddItemBtn(self):
        self.addItem = Button(root, text='Add Items', bg='#272222', fg='white', command=self.UpdateItems)
        self.addItem.place(relx='0.35', rely='0.05')

    def GenerateBill(self):
        self.genBill = Button(root, text="Generate Bill", bg='#272222', fg='white', command=self.GetBill)
        self.genBill.place(relx='0.35', rely='0.10')

    def SaveDatBtn(self):
        self.sdb = Button(root, text='Save Data To Database', bg='#272222', fg='white', command=self.addData)
        self.sdb.place(relx='0.35', rely='0.15')

    def searchCusBtn(self):
        self.search4cus = Button(root, text='Search Customer', bg='#272222', fg='white', command=self.s4customer)
        self.search4cus.place(relx='0.35', rely='0.20')

# function
    # updates items to list
    def UpdateItems(self):
        # self.val1.get()
        # self.to.get()
        # self.quantity.get()
        # self.rate.get()
# prblm in n
        n = self.rate.get()
        m = self.quantity.get()*n
        l.append(m)
        # 11:29

        self.textArea.insert(END, f'{self.val1.get()}\t  {self.quantity.get()}\t\t{self.rate.get()}\t{m}')
        self.val1.set("")
        self.quantity.set("")
        self.rate.set("")


    def GetBill(self):
        self.WelcomeUser()
        self.textArea.insert(END, f"\n--------------------------------------------")
        self.textArea.insert(END, f"Total Bill :\t\t\t{sum(l)}")
        self.textArea.insert(END, f"\n--------------------------------------------")
        self.totallabel.insert(END, f"{sum(l)}")
        self.totallabel.setvar("")


    def WelcomeUser(self):
        self.textArea.delete(1.0, END)
        self.textArea.insert(END, "\t Welcome to our Retail store")
        self.textArea.insert(END, f'\n\nInvoice Id: \t\t{self.bill_no.get()}')
        self.textArea.insert(END, f'\nCustomer name: \t\t{self.to.get()}')
        self.textArea.insert(END, f"\n============================================")
        self.textArea.insert(END, f"\n Product\t  Quantity\t\tRate\tTotal Rate")
        self.textArea.insert(END, f"\n............................................")


    def addData(self):
        self.b = self.bill_no.get()
        self.t = self.to.get()
        self.s = self.total.get()
        self.connect = pymysql.connect(host='localhost', user='root', password='Debug_it',database='billing_cloud_data')
        self.cursor = self.connect.cursor()
        self.cursor.execute("insert into bill(invoice_id, customer_name, total_bill) values('"+self.b+"', '"+self.t+"', '"+self.s+"') ")
        self.connect.commit()
        print("Record inserted")

# search for customer data page
    def s4customer(self):
        self.s4c = Tk()
        self.s4c.geometry("800x300")
        self.s4c.title("Search Customer Data")
        self.Invoice = StringVar()

        self.s4c.configure(bg='#272222')

        self.custoBtn = Button(self.s4c, text="Fetch Customer Data", bg='#272222', fg='white', command=self.connect)
        self.custoBtn.place(relx='0.65', rely='0.15')

        self.ftLabel = Label(self.s4c, text='Enter Invoice Id to search customer records', bg='#272222', fg='white', font="comicsansms 15 bold")
        self.ftLabel.place(relx='0.35', rely='0.05')

        self.entr1 = Entry(self.s4c, textvariable=self.Invoice, width='35', bg='#272222', fg='white')
        self.entr1.place(relx='0.35', rely='0.15')

        self.lLabel = Label(self.s4c, text='', bg='#272222', fg='white', font='comicsansms 10 bold')
        self.lLabel.place(relx='0.35', rely='0.35')

    def connect(self):
        # connections
        self.connectDb = pymysql.connect(host="localhost", user="root", password="Debug_it", database="billing_cloud_data")
        self.cursor1 = self.connectDb.cursor()

        self.a = self.entr1.get()
        self.statem = "select * from bill where Invoice_id = '"+self.a+"' "
        self.cursor1.execute(self.statem)

        for row in self.cursor1:
            self.lLabel.config(text=f"{row}")






if __name__ == '__main__':
    root = AddBill()

    root.backgrnd()
    # frame
    root.frameing()
    # label
    root.txtArea()
    root.Blabel()
    root.rateLab()
    root.quanLab()
    root.ToLabel()
    root.productLabel()
    # entries
    root.totalLabel()
    root.entry()
    root.To()
    root.quanEnt()
    root.rateEntry()
    # button
    root.searchCusBtn()
    root.SaveDatBtn()
    root.AddItemBtn()
    root.GenerateBill()

    root.mainloop()