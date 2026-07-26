import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

# حذف همزمان بر اساس قیمت 

def tkinter():
    global Name,Price,PDate,EDate,QTy
    name=Name.get()
    price=Price.get()
    Pdate=PDate.get()
    Edate=EDate.get()
    Qty=QTy.get()

class product:
    def __init__(self,name,price,Pdate,Edate,Qty):
        self.nameClass=name
        self.priceClass=price
        self.PdateClass=Pdate
        self.EdateClass=Edate
        self.QtyClass=Qty
        # برای overload کردن تابع پرینت در کلاس می توان از تابع __str__ استفاده کرد 
    def __str__(self):
        return(
        f"name:{self.nameClass} \n"
        f"price:{self.priceClass} \n"
        f"Pdate:{self.PdateClass} \n"
        f"Edate:{self.EdateClass} \n"
        f"Qty:{self.QtyClass}"
        )
class anbar:
    def __init__(self):
        self.products=[]
        # return self.products
    def add_product(self):
        try:
            name=Name.get()
            price=int(Price.get())
            pdate=PDate.get()
            edate=EDate.get()
            qty=int(QTy.get())
            p=product(name,price ,pdate , edate , qty)
            self.products.append(p)
            msg.showinfo(title="Success",message= "Product added!")
        except:
            msg.showerror("error" , "invalid input!")
            
    def update_product(self , name ):
        update_list=[]
        for p in self.products:
            if p.nameClass.lower()==name.lower():
                update_list.append(p)
        return update_list
            
    def show_data_by_tkinter(self):
        dataWindow=tk.Toplevel(win)
        dataWindow.title('Show data...')
        # اماده کردن بستر خروجی برای مشاهده ی اطلاعات
        table=ttk.Treeview(dataWindow,columns=("Name","Price","PDate","EDate", "QTy"), show="headings")
        table.heading("Name", text="نام ")
        table.heading("Price", text="قیمت ")
        table.heading("PDate", text="تاریخ تولید ")
        table.heading("EDate", text="تاریخ انقضا ")
        table.heading("QTy", text="تعداد محصول ")


        table.column("Name", width=120)
        table.column("Price", width=120)
        table.column("PDate", width=80)
        table.column("EDate", width=60)
        table.column("QTy", width=60)
        
        for item in self.products:
            table.insert("","end",values=(item.nameClass, item.priceClass, item.PdateClass, item.EdateClass, item.QtyClass))

        table.pack(padx=2, pady=10, fill=tk.BOTH, expand=True)
            
            
    # def show(self):
    #     try:
    #         my_product=self.products
    #         for product in my_product:
    #             print(product)
    #     except:
    #         msg.showerror("error" , "there is nothing to show !")
            
    def search_product_by_name(self, name):
        list_product=[]
        try:
            for p in self.products:
                if p.nameClass.lower() == name.lower():
                    list_product.append(p)
                    
            return list_product
        except:
            msg.showinfo("error","invalid input!")
            
    def search_product_by_price(self  , price ):
        list_product=[]
        for p in self.products:
            if p.priceClass >= price:
                list_product.append(p)
        return list_product

    def delete_product(self , name):
        try:
            for p in self.products:
                if p.nameClass.lower() == name.lower():
                    self.products.remove(p)
                    return True
            return False    
        except:
            msg.showerror("error" , "invalid input !")
 
def ShowSerach_by_name():
    wind2=tk.Toplevel(win)
    wind2.title('Search Item by name')
    wind2.geometry("300x150")

    tk.Label( wind2 , text="Search Entry : ").grid(row=0, column=0)
    searchEntry= tk.Entry(wind2)
    searchEntry.grid(row=0, column=1, padx=5, pady=5)
    def do_search_by_name():
        name = searchEntry.get()
        result = myShop.search_product_by_name(name)
        #این میره ببینه برای یه اسم که از ورودی دریافت میشه چه کاری بکند 
        #و برای همین میره به تابع سرچ محصول اونجا که گفتیم هربرو داخل لیست محصولات 
        # بگرد . همون لیستی که تابع سازنده ی کلاس انبار بود و اونجا هر چیزی را دیدی که 
        # با محصول وارد شده اسمش برابر بود را بیا نمایش بده 
        if len(result)!=0:
            dataWindow=tk.Toplevel(win)
            dataWindow.title('search data by name ...')
            # اماده کردن بستر خروجی برای مشاهده ی اطلاعات
            table=ttk.Treeview(dataWindow,columns=("Name","Price","PDate","EDate", "QTy"), show="headings")
            table.heading("Name", text="نام ")
            table.heading("Price", text="قیمت ")
            table.heading("PDate", text="تاریخ تولید ")
            table.heading("EDate", text="تاریخ انقضا ")
            table.heading("QTy", text="تعداد محصول ")


            table.column("Name", width=120)
            table.column("Price", width=120)
            table.column("PDate", width=80)
            table.column("EDate", width=60)
            table.column("QTy", width=60)
            
            for item in result:
                table.insert("","end",values=(item.nameClass, item.priceClass, item.PdateClass, item.EdateClass, item.QtyClass))

            table.pack(padx=2, pady=10, fill=tk.BOTH, expand=True)
            # for i in result:
            #     print(i)
        else:
            msg.showerror("Error", "Product not found")
    btn = tk.Button(wind2 , text="show" , command=do_search_by_name)
    btn.grid(row=1, column=0)
    
def ShowSerach_by_price():
    windprice=tk.Toplevel(win)
    windprice.title('Search Item by price')
    windprice.geometry("300x150")

    tk.Label( windprice , text="Search Entry : ").grid(row=0, column=0)
    searchPriceEntry= tk.Entry(windprice)
    searchPriceEntry.grid(row=0, column=1, padx=5, pady=5)
    
    def do_search_by_price():
        price = float(searchPriceEntry.get())
        result = myShop.search_product_by_price(price)
        #این میره ببینه برای یه اسم که از ورودی دریافت میشه چه کاری بکند 
        #و برای همین میره به تابع سرچ محصول اونجا که گفتیم هربرو داخل لیست محصولات 
        # بگرد . همون لیستی که تابع سازنده ی کلاس انبار بود و اونجا هر چیزی را دیدی که 
        # با محصول وارد شده اسمش برابر بود را بیا نمایش بده 
        # if len(result)!=0:
        if len(result) != 0:
            dataWindow=tk.Toplevel(win)
            dataWindow.title('searhc data by price ...')
            # اماده کردن بستر خروجی برای مشاهده ی اطلاعات
            table=ttk.Treeview(dataWindow,columns=("Name","Price","PDate","EDate", "QTy"), show="headings")
            table.heading("Name", text="نام ")
            table.heading("Price", text="قیمت ")
            table.heading("PDate", text="تاریخ تولید ")
            table.heading("EDate", text="تاریخ انقضا ")
            table.heading("QTy", text="تعداد محصول ")

            table.column("Name", width=120)
            table.column("Price", width=120)
            table.column("PDate", width=80)
            table.column("EDate", width=60)
            table.column("QTy", width=60)
            
            for item in result:
                table.insert("","end",values=(item.nameClass, item.priceClass, item.PdateClass, item.EdateClass, item.QtyClass))

            table.pack(padx=2, pady=10, fill=tk.BOTH, expand=True)
            # for i in result:
            #     print(i)
        else:
            msg.showerror("Error", "Product not found")
    btn = tk.Button(windprice , text="show" , command=do_search_by_price)
    btn.grid(row=1, column=0)

def Showdelete():
    wind3=tk.Toplevel(win)
    wind3.title('Delete Item')
    wind3.geometry("300x150")

    tk.Label( wind3 , text="Delete Entry : ").grid(row=0, column=0)
    deleteEntry= tk.Entry(wind3)
    deleteEntry.grid(row=0, column=1, padx=5, pady=5)
    def do_delete():
        name=deleteEntry.get()
        result = myShop.delete_product(name)
        if result:
            msg.showinfo(title="Result", message="product deleted successfuly !")
        else:
            msg.showerror("Error", "Product not deleted !")
    btn = tk.Button(wind3 , text="delete" , command=do_delete)
    btn.grid(row=1, column=0)
def ShowUpdate():
    updatewind=tk.Toplevel(win)
    updatewind.title('update Item')
    updatewind.geometry("300x150")

    tk.Label( updatewind , text="product name Entry : ").grid(row=0, column=0)
    UpdatenameEntry= tk.Entry(updatewind)
    UpdatenameEntry.grid(row=0, column=1, padx=5, pady=5)
    
    # tk.Label( updatewind , text="update Entry : ").grid(row=1, column=0)
    # updateEntry= tk.Entry(updatewind)
    # updateEntry.grid(row=1, column=1, padx=5, pady=5)
    
    def do_update():
        name = UpdatenameEntry.get()
        # update=updateEntry.get()
        result = myShop.update_product(name)
        #این میره ببینه برای یه اسم که از ورودی دریافت میشه چه کاری بکند 
        #و برای همین میره به تابع سرچ محصول اونجا که گفتیم هربرو داخل لیست محصولات 
        # بگرد . همون لیستی که تابع سازنده ی کلاس انبار بود و اونجا هر چیزی را دیدی که 
        # با محصول وارد شده اسمش برابر بود را بیا نمایش بده 
        if len(result)!=0:
            # for item in result:
            #     myShop[item].name=update
            item=result[0]
                
            dataWindow=tk.Toplevel(win)
            dataWindow.title('update products...')
            
            tk.Label(dataWindow, text="Name").grid(row=0, column=0)
            nameEntry = tk.Entry(dataWindow)
            nameEntry.grid(row=0, column=1)
            # مقدار قبلی را نمایش می دهیم
            nameEntry.insert(0, item.nameClass)
            
            tk.Label(dataWindow, text="Price").grid(row=1, column=0)
            priceEntry = tk.Entry(dataWindow)
            priceEntry.grid(row=1, column=1)
            priceEntry.insert(0, item.priceClass)

            tk.Label(dataWindow, text="PDate").grid(row=2, column=0)
            pdateEntry = tk.Entry(dataWindow)
            pdateEntry.grid(row=2, column=1)
            pdateEntry.insert(0, item.PdateClass)
            
            tk.Label(dataWindow, text="EDate").grid(row=3, column=0)
            edateEntry = tk.Entry(dataWindow)
            edateEntry.grid(row=3, column=1)
            edateEntry.insert(0, item.EdateClass)
            
            tk.Label(dataWindow, text="Quantity").grid(row=4, column=0)
            qtyEntry = tk.Entry(dataWindow)
            qtyEntry.grid(row=4, column=1)
            qtyEntry.insert(0, item.QtyClass)
            
            def save_changes():

                item.nameClass = nameEntry.get()
                item.priceClass = priceEntry.get()
                item.PdateClass = pdateEntry.get()
                item.EdateClass = edateEntry.get()
                item.QtyClass = qtyEntry.get()
                msg.showinfo("Done", "Product Updated Successfully")
            btnSave=tk.Button(dataWindow , text="update" , command=save_changes)
            btnSave.grid(row=6 , column=1) 
        else:
            msg.showerror("Error", "Product Not Found")
    btn = tk.Button(updatewind,text="Search",command=do_update)
    btn.grid(row=1, column=1)
        

            # اماده کردن بستر خروجی برای مشاهده ی اطلاعات
            # table=ttk.Treeview(dataWindow,columns=("Name","Price","PDate","EDate", "QTy"), show="headings")
            # table.heading("Name", text="نام ")
            # table.heading("Price", text="قیمت ")
            # table.heading("PDate", text="تاریخ تولید ")
            # table.heading("EDate", text="تاریخ انقضا ")
            # table.heading("QTy", text="تعداد محصول ")


            # table.column("Name", width=120)
            # table.column("Price", width=120)
            # table.column("PDate", width=80)
            # table.column("EDate", width=60)
            # table.column("QTy", width=60)
            
            # for item in result:
            #     table.insert("","end",values=(item.nameClass, item.priceClass, item.PdateClass, item.EdateClass, item.QtyClass))

            # table.pack(padx=2, pady=10, fill=tk.BOTH, expand=True)
            # for i in result:
            #     print(i)
    #     else:
    #         msg.showerror("Error", "Product not found")
    # btn = tk.Button(updatewind , text="update" , command=do_update)
    # btn.grid(row=2, column=0)

myShop=anbar()

win=tk.Tk()
win.title("classProject")
win.geometry("500x300")

tk.Label( win , text="name").grid(row=0, column=0)
Name = tk.Entry(win)
Name.grid(row=0, column=1, padx=5, pady=5)

tk.Label( win , text="price").grid(row=1, column=0)
Price = tk.Entry(win)
Price.grid(row=1, column=1, padx=5, pady=5)

tk.Label( win , text="Pdate").grid(row=2, column=0)
PDate = tk.Entry(win)
PDate.grid(row=2, column=1, padx=5, pady=5)

tk.Label( win , text="Edate").grid(row=3, column=0)
EDate = tk.Entry(win)
EDate.grid(row=3, column=1, padx=5, pady=5)

tk.Label( win , text="Qty").grid(row=4, column=0)
QTy = tk.Entry(win)
QTy.grid(row=4, column=1, padx=5, pady=5)

btn1 = tk.Button(win , text="add data" , command=myShop.add_product)
btn1.grid(row=5, column=1)

btn2 = tk.Button(win , text="search by name " , command=ShowSerach_by_name)
btn2.grid(row=7, column=1)

btn5 = tk.Button(win , text="search by price " , command=ShowSerach_by_price)
btn5.grid(row=8, column=1)

btn3 = tk.Button(win , text="show data" , command=myShop.show_data_by_tkinter)
btn3.grid(row=9, column=1)

btn4 = tk.Button(win , text="delete data" , command=Showdelete)
btn4.grid(row=10, column=1)

btn = tk.Button(win , text="update data" , command=ShowUpdate)
btn.grid(row=11, column=1)

win.mainloop()
