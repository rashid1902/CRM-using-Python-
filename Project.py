from tkinter import *
from PIL import ImageTk,ImageTk
import mysql.connector
import csv
from tkinter import ttk
from test2 import *





root = Tk()
root.title("CUSTOMER RELATIONSHIP MANAGEMENT")
root.geometry("620x600")
root.configure(bg = "#6C5B7B")

def Query():
	Query_ = Tk()
	Query_.Ask()

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "R@shid7860",
	auth_plugin='mysql_native_password',
	database = "CRM",
	)
# Check to see if Connection to MYSQL was created
#print(mydb)

#Create a cursor and initialize it
my_cursor = mydb.cursor()


# Create database
#my_cursor.execute("CREATE DATABASE CRM")


#TEst to see if database was created
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#	print(db)

#Drop table
#my_cursor.execute("DROP TABLE customers")


#Clear Text fields
def clear_fields():
	first_name_box.delete(0, END)
	last_name_box.delete(0, END)
	address_1_box.delete(0, END)
	address_2_box.delete(0, END)
	city_box.delete(0, END)
	state_box.delete(0, END)
	pincode_box.delete(0, END)
	country_box.delete(0, END)
	phone_box.delete(0, END)
	email_box.delete(0, END)
	payment_method_box.delete(0, END)
	discount_code_box.delete(0, END)
	price_paid_box.delete(0, END)

# Add Customers
def add_customers():
	sql_command = "INSERT INTO customers (first_name, last_name, address_1, address_2, city, state, pincode, country, phone, email, payment_method, discount_code, price_paid) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	values = (first_name_box.get(), last_name_box.get(), address_1_box.get(), address_2_box.get(), city_box.get(), state_box.get(), pincode_box.get(), country_box.get(), phone_box.get(), email_box.get(), payment_method_box.get(), discount_code_box.get(), price_paid_box.get())
	my_cursor.execute(sql_command, values)
    # Commit the changes to the database
	mydb.commit()
    #clear fields after submit
	clear_fields()


#Costumer's List
def list_customers():
	list_customers_query = Tk()
	list_customers_query.title("Customer's List")
	list_customers_query.geometry("800x800")
	list_customers_query.configure(bg = "#c39f7f")
	# Query the Database
	my_cursor.execute("SELECT * FROM customers")
	output = my_cursor.fetchall()
	
	for index,x in enumerate(output):
		num = 0
		for y in x:
			lookup_label = Label(list_customers_query, text = y,bg = "#c39f7f")
			lookup_label.grid(row = index, column = num)
			num = num + 1
	csv_button = Button(list_customers_query, text = "Save to Excel",bg = "#2F9599", command = lambda: write_to_csv(output))
	csv_button.grid(row = index + 1, column = 0)
    

#write to cvs
def write_to_csv(output):
	with open('customers.csv', 'a',newline = "") as f:
		w = csv.writer(f,dialect = 'excel')
		for record in output:
			w.writerow(record)
		

# Search Customers
def search_customers():
	search_customers = Tk()
	search_customers.title("Customer's List")
	search_customers.geometry("1000x1000")
	search_customers.configure(bg = "#355C7D")
	def update():
		sql_command =  """UPDATE customers SET first_name = %s, last_name = %s,pincode = %s, price_paid = %s, email = %s, address_1 = %s, address_2 = %s, city = %s, state = %s, country = %s, payment_method = %s, discount_code = %s WHERE user_id = %s"""

		first_name = first_name_box2.get()
		last_name = last_name_box2.get()
		pincode = pincode_box2.get()
		price_paid = price_paid_box2.get()
		email =  email_box2.get()
		address_1 = address_2_box2.get()
		address_2 = address_2_box2.get()
		city = city_box2.get()
		state = state_box2.get()
		country = country_box2.get()
		phone = phone_box2.get()
		payment_method = payment_method_box2.get()
		discount_code = discount_code_box2.get()

		id_value = id_box2.get()
		inputs = (first_name, last_name ,pincode, price_paid, email, address_1, address_2, city, state, country, payment_method, discount_code, id_value)
		
		my_cursor.execute(sql_command,inputs)
		mydb.commit()

		search_customers.destroy()

	def update_now(id,index):
		sql2 = "SELECT * FROM customers WHERE user_id = %s"
		name2 = (id,)
		output2 = my_cursor.execute(sql2,name2)
		output2 = my_cursor.fetchall()
		index = index + 1
        #form for update field
		first_name_label = Label(search_customers, text = "First Name",bg = "#355C7D")
		first_name_label.grid(row = index + 1, column =0, sticky = W, padx = 10,pady = 10)
		last_name_label = Label(search_customers,text = "Last Name",bg = "#355C7D")
		last_name_label.grid(row = index +2, column = 0, sticky = W, padx = 10)
		address_1_label = Label(search_customers, text = "Address 1",bg = "#355C7D")
		address_1_label.grid(row = index + 3,column = 0, sticky = W,padx = 10)
		address_2_label = Label(search_customers, text = "Address 2",bg = "#355C7D")
		address_2_label.grid(row = index + 4, column = 0, sticky = W, padx = 10)
		city_label = Label(search_customers, text = "City",bg = "#355C7D")
		city_label.grid(row = index + 5, column = 0, sticky = W, padx = 10)
		state_label = Label(search_customers, text = "State",bg = "#355C7D")
		state_label.grid(row = index + 6, column = 0, sticky = W, padx = 10)
		pincode_label = Label(search_customers, text = "Pincode",bg = "#355C7D")
		pincode_label.grid(row = index + 7,column =0,sticky = W, padx = 10)
		country_label = Label(search_customers, text = "Country",bg = "#355C7D")
		country_label.grid(row = index + 8, column =0,sticky = W, padx = 10)
		phone_label = Label(search_customers, text = "Phone Number",bg = "#355C7D")
		phone_label.grid(row = index +9, column =0,sticky = W,padx =10)
		email_label = Label(search_customers, text = "Email Address",bg = "#355C7D")
		email_label.grid(row = index + 10, column = 0,sticky = W, padx = 10)
		payment_method_label = Label(search_customers, text = "Payment Method",bg = "#355C7D")
		payment_method_label.grid(row = index + 11, column = 0, sticky = W, padx = 10)
		discount_code_label = Label(search_customers, text = "Discount Code",bg = "#355C7D")
		discount_code_label.grid(row = index + 12, column = 0, sticky = W, padx = 10)
		price_paid_label = Label(search_customers, text = "Price Paid",bg = "#355C7D")
		price_paid_label.grid(row = index + 13, column = 0, sticky = W, padx = 10)
		id_label = Label(search_customers, text = "User Id",bg = "#355C7D")
		id_label.grid(row = index + 14, column = 0, sticky =W, padx = 10)
		# Create Entry Boxes
		global first_name_box2
		first_name_box2 = Entry(search_customers,bg = "#355C7D")
		first_name_box2.grid(row = index + 1 , column = 1, pady = 10)
		first_name_box2.insert(0, output2[0][0])
		global last_name_box2
		last_name_box2 = Entry(search_customers,bg = "#355C7D")
		last_name_box2.grid(row = index + 2, column = 1, pady = 5)
		last_name_box2.insert(0, output2[0][1])
		global address_2_box2
		address_1_box2 = Entry(search_customers,bg = "#355C7D")
		address_1_box2.grid(row = index + 3, column = 1, pady = 5)
		address_1_box2.insert(0, output2[0][6])
		global address_2_box2
		address_2_box2 = Entry(search_customers,bg = "#355C7D")
		address_2_box2.grid(row = index + 4,  column = 1, pady = 5)
		address_2_box2.insert(0, output2[0][7])
		global city_box2
		city_box2 = Entry(search_customers,bg = "#355C7D")
		city_box2.grid(row = index + 5,  column = 1, pady = 5)
		city_box2.insert(0, output2[0][8])
		global state_box2
		state_box2 = Entry(search_customers,bg = "#355C7D")
		state_box2.grid(row = index +6, column = 1, pady = 5)
		state_box2.insert(0, output2[0][9])
		global pincode_box2
		pincode_box2 = Entry(search_customers,bg = "#355C7D")
		pincode_box2.grid(row = index + 7,  column = 1, pady = 5)
		pincode_box2.insert(0, output2[0][2])
		global country_box2
		country_box2 = Entry(search_customers,bg = "#355C7D")
		country_box2.grid(row = index + 8, column = 1, pady = 5)
		country_box2.insert(0, output2[0][10])
		global phone_box2
		phone_box2 = Entry(search_customers,bg = "#355C7D")
		phone_box2.grid(row = index + 9,  column = 1, pady = 5)
		phone_box2.insert(0, output2[0][11])
		global email_box2
		email_box2 = Entry(search_customers,bg = "#355C7D")
		email_box2.grid(row = index + 10, column = 1, pady = 5)
		email_box2.insert(0, output2[0][5])
		global payment_method_box2
		payment_method_box2 = Entry(search_customers,bg = "#355C7D")
		payment_method_box2.grid(row = index + 11, column = 1, pady = 5)
		payment_method_box2.insert(0, output2[0][12])
		global discount_code_box2
		discount_code_box2 = Entry(search_customers,bg = "#355C7D")
		discount_code_box2.grid(row = index + 12, column = 1, pady = 5)
		discount_code_box2.insert(0, output2[0][13])
		global price_paid_box2
		price_paid_box2 = Entry(search_customers,bg = "#355C7D")
		price_paid_box2.grid(row = index + 13, column = 1, pady = 5)
		price_paid_box2.insert(0, output2[0][3])
		global id_box2
		id_box2 = Entry(search_customers,bg = "#355C7D")
		id_box2.grid(row = index +14, column = 1, pady = 5)
		id_box2.insert(0, output2[0][4])

		save_record =Button(search_customers, text = "Update Record",bg = "#99B898", command = update)
		save_record.grid(row = index + 15 ,column = 0, padx = 10)
	def search_now():
		selected = drop.get()
		sql = ""
		if selected == "Search By...":
			test = Label(search_customers, text = "OOPs! You forgot to pick Drop-Down Selection",bg = "#99B898")
			test.grid(row = 2, column =0)
		if selected == "Last Name":
			sql = "SELECT * FROM customers WHERE last_name = %s"
			
		if selected == "Email Address":
			sql = "SELECT * FROM customers WHERE email = %s"
			
		if selected == "Customer ID":
			sql = "SELECT * FROM customers WHERE user_id = %s"

		searching = search_box.get()
		#sql = "SELECT * FROM customers WHERE last_name = %s"
		name = (searching,)
		output = my_cursor.execute(sql,name)
		output = my_cursor.fetchall()
		if not output:
			output = "Record Not Found...."
			lookup_label = Label(search_customers,text=output,bg = "#99B898")
			lookup_label.grid(row = 2, column = 0)
		else:
			for index, x in enumerate(output):
			    num = 0
			    index  = index + 2
			    id_reference = str(x[4])
			    update_btn = Button(search_customers,text = "Edit",bg = "#99B898", command = lambda: update_now(id_reference,index))
			    update_btn.grid(row = index,column = num )
			    for y in x:
				    lookup_label = Label(search_customers,text=y,bg = "#355C7D")
				    lookup_label.grid(row = index, column = num +1)
				    num = num + 1
			csv_button = Button(search_customers, text = "Save to Excel",bg = "#99B898", command = lambda: write_to_csv(output))
			csv_button.grid(row = index + 1, column = 0)
	     
		
		#searching_label = Label(search_customers, text = output)
		#searching_label.grid(row = 3, column = 0, padx =10,columnspan = 3)
		

	


	# Entry box to search customer

	search_box = Entry(search_customers,bg = "#355C7D")
	search_box.grid(row = 0, column = 1, pady = 10)

	# Entry box Label search for customer
	search_box_label = Label(search_customers,text = "Customer Search By: ",bg = "#355C7D")
	search_box_label.grid(row = 0, column = 0, padx = 10, pady= 10)

	#Entry box search Button for Customers
	search_btn = Button(search_customers,text = "Search Customers",bg = "#99B898",command = search_now)
	search_btn.grid(row = 1,column = 0,padx = 10)
	# Drop Down box 
	drop = ttk.Combobox(search_customers, values = ["Search By...","Last Name","Email Address","Customer ID"])
	drop.current(0)
	drop.grid(row = 0, column = 2 )


# Create a table
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers(first_name VARCHAR(255),\
	last_name VARCHAR(255),\
	pincode int(10),\
	price_paid DECIMAL(10,2),\
	user_id INT AUTO_INCREMENT PRIMARY KEY) ")

#Alter Table
"""
my_cursor.execute("ALTER TABLE customers ADD(\
	email VARCHAR(255),\
	address_1 VARCHAR(255),\
	address_2 VARCHAR(255),\
	city VARCHAR(255),\
	state VARCHAR(255),\
	country VARCHAR(255),\
	phone VARCHAR(255),\
	payment_method VARCHAR(50),\
	discount_code VARCHAR(255))")
"""
#Show table
"""
my_cursor.execute("SELECT *FROM customers")
#print(my_cursor.description)
for i in my_cursor.description:
	print(i)
"""
#CREATE A LABEL
title_label = Label(root,text = "Learning Website Customer Database",font = ("Helvetica", 18),fg = "red",bg = "#6C5B7B")
title_label.grid(row = 0,column = 0, columnspan = 2, pady = "10")

#Create form to enter Customer data
first_name_label = Label(root,text ="First Name", fg = "#F7DB4F",bg = "#6C5B7B")
first_name_label.grid(row=1,column =0,sticky = W,padx =10)
last_name_label = Label(root,text ="Last Name", fg = "#F7DB4F",bg = "#6C5B7B")
last_name_label.grid(row=2,column =0,sticky = W,padx =10)
address_1_label = Label(root,text ="Address 1", fg = "#F7DB4F",bg = "#6C5B7B")
address_1_label.grid(row=3,column =0,sticky = W,padx =10)
address_2_label = Label(root,text ="Address 2", fg = "#F7DB4F",bg = "#6C5B7B")
address_2_label.grid(row=4,column =0,sticky = W,padx =10)
city_label = Label(root,text ="City", fg = "#F7DB4F",bg = "#6C5B7B")
city_label.grid(row=5,column =0,sticky = W,padx =10)
state_label =  Label(root,text ="State", fg = "#F7DB4F",bg = "#6C5B7B")
state_label.grid(row=6,column =0,sticky = W,padx =10)
pincode_label = Label(root,text ="Pincode", fg = "#F7DB4F",bg = "#6C5B7B")
pincode_label.grid(row=7,column =0,sticky = W,padx =10)
country_label = Label(root,text ="Country", fg = "#F7DB4F",bg = "#6C5B7B")
country_label.grid(row=8,column =0,sticky = W,padx =10)
phone_label = Label(root,text ="Phone Number", fg = "#F7DB4F",bg = "#6C5B7B")
phone_label.grid(row=9,column =0,sticky = W,padx =10)
email_label = Label(root,text ="Email Address", fg = "#F7DB4F",bg = "#6C5B7B")
email_label.grid(row=10,column =0,sticky = W,padx =10)
payment_method_label = Label(root,text ="Payment Method", fg = "#F7DB4F",bg = "#6C5B7B")
payment_method_label.grid(row=11,column =0,sticky = W,padx =10)
discount_code_label = Label(root,text ="Discount Code", fg = "#F7DB4F",bg = "#6C5B7B")
discount_code_label.grid(row=12,column =0,sticky = W,padx =10)
price_paid_label = Label(root,text ="Price Paid", fg = "#F7DB4F",bg = "#6C5B7B")
price_paid_label.grid(row=13,column =0,sticky = W,padx =10)

#Create Entry Box
first_name_box=Entry(root,bg = "#6C5B7B")
first_name_box.grid(row = 1, column = 1)

last_name_box=Entry(root,bg = "#6C5B7B")
last_name_box.grid(row = 2, column = 1,pady =5)

address_1_box=Entry(root,bg = "#6C5B7B")
address_1_box.grid(row = 3, column = 1,pady =5)

address_2_box=Entry(root,bg = "#6C5B7B")
address_2_box.grid(row = 4, column = 1,pady =5)
city_box=Entry(root,bg = "#6C5B7B")
city_box.grid(row = 5, column = 1,pady =5)

state_box=Entry(root,bg = "#6C5B7B")
state_box.grid(row =6, column = 1,pady =5)

pincode_box=Entry(root,bg = "#6C5B7B")
pincode_box.grid(row = 7, column = 1,pady =5)

country_box=Entry(root,bg = "#6C5B7B")
country_box.grid(row = 8, column = 1,pady =5)

phone_box=Entry(root,bg = "#6C5B7B")
phone_box.grid(row = 9, column = 1,pady =5)

email_box=Entry(root,bg = "#6C5B7B")
email_box.grid(row = 10, column = 1,pady =5)


payment_method_box=Entry(root,bg = "#6C5B7B")
payment_method_box.grid(row = 11, column = 1,pady =5)

discount_code_box=Entry(root,bg = "#6C5B7B")
discount_code_box.grid(row = 12, column = 1,pady =5)

price_paid_box = Entry(root,bg = "#6C5B7B")
price_paid_box.grid(row = 13, column = 1,pady =5)

# Create Buttons
add_customers_button = Button(root,text = "Add Customer To Database",bg = "#355C7D",command = add_customers)
add_customers_button.grid(row = 14, column = 0, padx = 10, pady = 10 )
clear_fields_button = Button(root, text = "Clear Fields",bg = "#355C7D", command = clear_fields)
clear_fields_button.grid(row = 14, column =1)

# list customers buttons
list_customers_button = Button(root, text = "Customer's List",bg = "#355C7D",command = list_customers)
list_customers_button.grid(row = 15, column = 0, sticky = W, padx = 10)

# Search Customers
search_customers_btn = Button(root, text = "Search Customer/Update Customer",bg = "#355C7D", command = search_customers)
search_customers_btn.grid(row = 15, column= 1,sticky = W, padx = 10)

Query_btn = Button(root, text = "Help desk", command = Ask)
Query_btn.grid(row = 16, column = 0, padx = 10,sticky = W ,pady = 10)

root.mainloop()



