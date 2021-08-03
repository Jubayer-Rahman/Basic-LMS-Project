from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1450x750+0+0")

        # =========================SQL Server=====================
        
        # =========================Variables=====================
        self.id_no_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.phone_var = StringVar()
        self.email_var = StringVar()
        self.adress_var = StringVar()
        self.blood_group_var = StringVar()
        self.member_type_var = StringVar()
        self.book_id_var = StringVar()
        self.book_title_var = StringVar()
        self.auther_var = StringVar()
        self.borrowed_var = StringVar()
        self.days_on_book_var = StringVar()
        self.return_date_var = StringVar()
        self.days_due_var = StringVar()
        self.fine_var = StringVar()

    
        lbl_title = Label(self.root, text="Advance Library", bg="white",fg="navy blue",bd=1,relief=RIDGE,font=("sens-serif",30,"bold"),padx=2,pady=6)
        lbl_title.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=2, relief=RIDGE, padx=20,bg="white")
        frame.place(x=18,y=85,width=1410,height=400)

        #=======================DataFrameLeft====================
        DataFrameLeft = LabelFrame(frame, text="Member Info", bg="white",fg="navy blue",bd=2,relief=GROOVE,font=("sens-serif",15,"bold"))
        DataFrameLeft.place(x=0,width=900,height=390)
        
        lbl_id_no = Label(DataFrameLeft, text="ID No.", bg="white", font=("sens-serif",16), padx=8,pady=8)
        lbl_id_no.grid(row=0,column=0,sticky="w")
        txt_id_no = Entry(DataFrameLeft, textvariable=self.id_no_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_id_no.grid(row=0,column=1)

        lbl_first_name = Label(DataFrameLeft, text="First Name", bg="white", font=("sens-serif",16), padx=9,pady=8)
        lbl_first_name.grid(row=1,column=0,sticky="w")
        txt_first_name = Entry(DataFrameLeft, textvariable=self.first_name_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_first_name.grid(row=1,column=1)

        lbl_last_name = Label(DataFrameLeft, text="Last Name", bg="white", font=("sens-serif",16), padx=9,pady=8)
        lbl_last_name.grid(row=2,column=0,sticky="w")
        txt_last_name = Entry(DataFrameLeft, textvariable=self.last_name_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_last_name.grid(row=2,column=1)

        lbl_phone = Label(DataFrameLeft, text="Phone", bg="white", font=("sens-serif",16), padx=9,pady=8)
        lbl_phone.grid(row=3,column=0,sticky="w")
        txt_phone = Entry(DataFrameLeft, textvariable=self.phone_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_phone.grid(row=3,column=1)

        lbl_email = Label(DataFrameLeft, text="Email", bg="white", font=("sens-serif",16), padx=9,pady=8)
        lbl_email.grid(row=4,column=0,sticky="w")
        txt_email = Entry(DataFrameLeft, textvariable=self.email_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_email.grid(row=4,column=1)

        lbl_adress = Label(DataFrameLeft, text="Adress", bg="white", font=("sens-serif",16), padx=9,pady=8)
        lbl_adress.grid(row=5,column=0,sticky="w")
        txt_adress = Entry(DataFrameLeft, textvariable=self.adress_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_adress.grid(row=5,column=1)

        lbl_blood = Label(DataFrameLeft, text="Blood Group", bg="white", font=("sens-serif",16), padx=9,pady=8)
        lbl_blood.grid(row=6,column=0,sticky="w")
        txt_blood = Entry(DataFrameLeft, textvariable=self.blood_group_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_blood.grid(row=6,column=1)

        lbl_member = Label(DataFrameLeft, text="Member Type", bg="white", font=("sens-serif",16), padx=9,pady=8)
        lbl_member.grid(row=7,column=0,sticky="w")

        com_member = ttk.Combobox(DataFrameLeft, textvariable=self.member_type_var, width=20, font=("sens-serif",15,'normal'), state="readonly")
        com_member["values"] = ("Admin Staff","Teacher","Student")
        com_member.current(2)
        com_member.grid(row=7,column=1)

        lbl_book_id = Label(DataFrameLeft, text="Book Id", bg="white", font=("sens-serif",16))
        lbl_book_id.grid(row=0,column=2, padx=20,pady=8, sticky="w")
        txt_book_id = Entry(DataFrameLeft, textvariable=self.book_id_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_book_id.grid(row=0,column=3)

        lbl_book_title = Label(DataFrameLeft, text="Book Title", bg="white", font=("sens-serif",16))
        lbl_book_title.grid(row=1,column=2, padx=20,pady=8, sticky="w")
        txt_book_title = Entry(DataFrameLeft, textvariable=self.book_title_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_book_title.grid(row=1,column=3)

        lbl_auther = Label(DataFrameLeft, text="Auther Name", bg="white", font=("sens-serif",16))
        lbl_auther.grid(row=2,column=2, padx=20,pady=8, sticky="w")
        txt_auther = Entry(DataFrameLeft, textvariable=self.auther_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_auther.grid(row=2,column=3)

        lbl_borrow = Label(DataFrameLeft, text="Date Borrowed", bg="white", font=("sens-serif",16))
        lbl_borrow.grid(row=3,column=2, padx=20,pady=8, sticky="w")
        txt_borrow = Entry(DataFrameLeft, textvariable=self.borrowed_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_borrow.grid(row=3,column=3)

        lbl_days_on_book = Label(DataFrameLeft, text="Days On Book", bg="white", font=("sens-serif",16))
        lbl_days_on_book.grid(row=4,column=2, padx=20,pady=8, sticky="w")
        txt_days_on_book = Entry(DataFrameLeft, textvariable=self.days_on_book_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_days_on_book.grid(row=4,column=3)

        lbl_returned = Label(DataFrameLeft, text="Return Date", bg="white", font=("sens-serif",16))
        lbl_returned.grid(row=5,column=2, padx=20,pady=8, sticky="w")
        txt_returned = Entry(DataFrameLeft, textvariable=self.return_date_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_returned.grid(row=5,column=3)

        lbl_days_due = Label(DataFrameLeft, text="Days Due", bg="white", font=("sens-serif",16))
        lbl_days_due.grid(row=6,column=2, padx=20,pady=8, sticky="w")
        txt_days_due = Entry(DataFrameLeft, textvariable=self.days_due_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_days_due.grid(row=6,column=3)

        lbl_fine = Label(DataFrameLeft, text="Late Return Fine", bg="white", font=("sens-serif",16))
        lbl_fine.grid(row=7,column=2, padx=20,pady=8, sticky="w")
        txt_fine = Entry(DataFrameLeft, textvariable=self.fine_var, width=22,bd=2,relief=GROOVE, font=("sens-serif",15,'normal'))
        txt_fine.grid(row=7,column=3)

        #=======================DataFrameRight====================
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="white",fg="navy blue",bd=2,relief=GROOVE,font=("sens-serif",15,"bold"))
        DataFrameRight.place(x=910,width=460,height=390)

        txt_box = Text(DataFrameRight, font=("sens-serif",15,'normal'), width=19,height=15,bd=2,relief=GROOVE)
        txt_box.grid(row=0,column=2,padx=10,pady=6)

        list_scrollbar = ttk.Scrollbar(DataFrameRight,orient=VERTICAL)
        list_scrollbar.grid(row=0,column=1,sticky="ns")

        list_book = ["Python Basics",'Java','C#','Django','Tkinter']
        
        def SelectBook(events=""):
            value = str(listbox.get(listbox.curselection()))
            if value=="Python Basics":
                self.book_id_var.set("B11001")
                self.book_title_var.set("Python Manual")
                self.auther_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.days_on_book_var.set(15)
                self.return_date_var.set(d3)
                self.days_due_var.set("NO")
                self.fine_var.set("TK 100")
        
        listbox = Listbox(DataFrameRight,font=("times new roman",12,'bold'), width=24,height=17,bd=2,relief=GROOVE)
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0,column=0,padx=5,pady=2)
        list_scrollbar.config(command=listbox.yview)

        for item in list_book:
            listbox.insert(END,item)

        #=======================Buttons Frame====================
        frm_button = Frame(self.root, bd=2, relief=RIDGE, padx=20,bg="white")
        frm_button.place(x=18,y=480,width=1410,height=50)

        btn_add_data = Button(frm_button,command=self.add_data,text="Add",font=("arial",12,"bold"),bd=2,width=16,bg="gray89",relief=RAISED)
        btn_add_data.grid(row=0,column=0,padx=5,pady=7)

        btn_add_data = Button(frm_button,command=self.show_data, text="Show",font=("arial",12,"bold"),bd=2,width=16,bg="gray89",relief=RAISED)
        btn_add_data.grid(row=0,column=1,padx=5,pady=7)

        btn_add_data = Button(frm_button,text="Update",font=("arial",12,"bold"),bd=2,width=16,bg="gray89",relief=RAISED)
        btn_add_data.grid(row=0,column=2,padx=5,pady=7)

        btn_add_data = Button(frm_button,text="Delete",font=("arial",12,"bold"),bd=2,width=16,bg="gray89",relief=RAISED)
        btn_add_data.grid(row=0,column=3,padx=5,pady=7)

        btn_add_data = Button(frm_button,text="Reset",font=("arial",12,"bold"),bd=2,width=16,bg="gray89",relief=RAISED)
        btn_add_data.grid(row=0,column=4,padx=5,pady=7)

        #=======================Information Frame====================
        frm_details = Frame(self.root, bd=2, relief=RIDGE, padx=20,bg="white")
        frm_details.place(x=18,y=535,width=1410,height=200)

        frm_table = Frame(frm_details, bd=2, relief=RIDGE, bg="white")
        frm_table.place(x=2,y=5,width=1365,height=190)

        xscroll=ttk.Scrollbar(frm_table,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(frm_table,orient=VERTICAL)
        
        self.library_table = ttk.Treeview(frm_table, column=("#1","#2",'#3','#4','#5','#6','#7','#8','#9','#10','#12','#12','#13','#14','#15','#16'),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill="x")
        yscroll.pack(side=RIGHT,fill="y")

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("#1",text="id_no")
        self.library_table.heading("#2",text="first_name")
        self.library_table.heading("#3",text="last_name")
        self.library_table.heading("#4",text="phone")
        self.library_table.heading("#5",text="email")
        self.library_table.heading("#6",text="adress")
        self.library_table.heading("#7",text="blood_group")
        self.library_table.heading("#8",text="member_type")
        self.library_table.heading("#9",text="book_id")
        self.library_table.heading("#10",text="book_title")
        self.library_table.heading("#11",text="auther")
        self.library_table.heading("#12",text="borrowed")
        self.library_table.heading("#13",text="days_on_book")
        self.library_table.heading("#14",text="return_date")
        self.library_table.heading("#15",text="days_due")
        self.library_table.heading("#16",text="fine")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("#2",width=100)
        self.library_table.column("#1",width=100)
        self.library_table.column("#3",width=100)
        self.library_table.column("#4",width=100)
        self.library_table.column("#5",width=100)
        self.library_table.column("#6",width=100)
        self.library_table.column("#7",width=100)
        self.library_table.column("#8",width=100)
        self.library_table.column("#9",width=100)
        self.library_table.column("#10",width=100)
        self.library_table.column("#11",width=100)
        self.library_table.column("#12",width=100)
        self.library_table.column("#13",width=100)
        self.library_table.column("#14",width=100)
        self.library_table.column("#15",width=100)
        self.library_table.column("#16",width=100)

        self.fetch_data()
        self.library_table.bind("<<ButtonRelease-1>>",self.get_cursor)


    def add_data(self):
        conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=LAPTOP-I5GH0ROF;'
        'Database=LMS;'
        'Trusted_Connection=yes;'
        )
        cursor = conn.cursor()
        insert_records = '''INSERT INTO info values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        cursor.execute(insert_records,(self.id_no_var.get(),self.first_name_var.get(), self.last_name_var.get(),
                                        self.phone_var.get(),self.email_var.get(),self.adress_var.get(),
                                        self.blood_group_var.get(),self.member_type_var.get(),self.book_id_var.get(),
                                        self.book_title_var.get(),self.auther_var.get(),self.borrowed_var.get(),
                                        self.days_on_book_var.get(),self.return_date_var.get(),self.days_due_var.get(),
                                        self.fine_var.get()))

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member added successfully")

    def fetch_data(self):
        conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=LAPTOP-I5GH0ROF;'
        'Database=LMS;'
        'Trusted_Connection=yes;'
        )
        cursor = conn.cursor()
        fetch_records = '''SELECT * FROM info'''
        cursor.execute(fetch_records)
        rows=cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()  

    def get_cursor(self,event=""):
        cursor_row = self.library_table.focus()
        content =  self.library_table.item(cursor_row)
        row=content['values']

        self.id_no_var.set(row[0]),
        self.first_name_var.set(row[1]), 
        self.last_name_var.set(row[2]),
        self.phone_var.set(row[3]),
        self.email_var.set(row[4]),
        self.adress_var.set(row[5]),
        self.blood_group_var.set(row[6]),
        self.member_type_var.set(row[7]),
        self.book_id_var.set(row[8]),
        self.book_title_var.set(row[9]),
        self.auther_var.set(row[10]),
        self.borrowed_var.set(row[11]),
        self.days_on_book_var.set(row[12]),
        self.return_date_var.set(row[13]),
        self.days_due_var.set(row[14]),
        self.fine_var.set(row[15])


    def show_data(self):
        self.txt_box.insert(END,"Member Type: "+self.member_type_var.get()+"\n")


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()