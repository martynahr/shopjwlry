# -*- coding utf-8 -*-
import pymysql
class MenuDB:
    def __init__(self, login, passwrd):
        self.conn = pymysql.connect("localhost", "newuser", "", "shopjwlry") #connect to database
        self.cursor = self.conn.cursor()   						 
        self.login = login
        self.passwrd = passwrd
        self.log_in()
    def log_in(self):         #log in
        self.sql2 = 'SELECT * FROM login WHERE login=%s AND pass=%s'
        self.cursor.execute(self.sql2,(self.login, self.passwrd))
        if(self.cursor.rowcount == 1):
            print('Success ')
            self.i = input('What you want to do next: \n(S)-show my orders,\n(L)-login & security, \n(P)-show me all products, \n(D)-delete my account, \n(Q)-LOG OUT')
            if(self.i == 'S'or self.i == 's'):
                self.view_ord()
                self.log_in()
            elif(self.i == 'L' or self.i == 'l'):
                self.read_pd()
                self.edit()
                self.read_pd()
                self.log_in()
            elif(self.i =='P'or self.i == 'p'):
                self.read_prdcts()
                self.log_in()
            elif(self.i =='D' or self.i == 'd'):
                self.read()
                self-delete_ac()
                self.log_in()
            else:
                print('You have been successfully logged out')
        else:
            print('Login failed. Invalid username or password.' )
    def view_ord(self): #here you can view your orders
        self.sql1 = "SELECT * FROM users_orders"   						 
        self.cursor.execute(self.sql1)   						 
        self.results = self.cursor.fetchall()   					 
        print ("%5s%10s%15s%5s%5s%10s%5s" % ("id_user"," name_us","Surname","id_product","order_nr","category","price") )   		 
        for row in self.results:
            self.id_user = row[0]
            self.name_us = row[1]
            self.surname = row[2]
            self.id_product = row[3]
            self.order_nr = row[4] 
            self.category = row[5]
            self.price = row[6]
            print ("%5s%10s%15s%5s%5s%10s%5s" % (self.id_user, self.name_us, self.surname, self.id_product, self.order_nr, self.category, self.price))        
    def read_pd(self): #here you can view your personal data
        self.sql = "SELECT * FROM users"   						 
        self.cursor.execute(self.sql)   						 
        self.results = self.cursor.fetchall()   					 
        print ("%5s%10s%15s%15s%20s%15s" % ("id_user","name_us","Surname","City","email", "mobile") )   		 
        for row in self.results:
            self.id_user = row[0]
            self.name_us = row[1]
            self.surname = row[2]
            self.city = row[3]
            self.email = row[4]
            self.mobile = row[5]
            print ("%5s%10s%15s%15s%20s%15s" % (self.id_user, self.name_us, self.surname, self.city, self.email, self.mobile))        
    def edit(self): #here you can modify your personal data
        self.id_user= input('Please put an user_id to modify: ')
        self.name_us = input ('Change your name: ')
        self.surname= input('Change you surname: ')
        self.city= input('Change you city: ')
        self.email=input('Change you email adress: ')
        self.mobile=input('Change you mobile number: ')
        self.sql3='Update users SET name_us=%s, surname=%s, city=%s, email=%s, mobile=%s where id_user=%s'
        self.cursor.execute(self.sql3,(self.name_us, self.surname, self.city, self.email, self.mobile, self.id_user))
        self.conn.commit() 
    def read_prdcts(self): #here you can see all available products
        self.sql4 = "SELECT * FROM products WHERE quantity>0"   						 
        self.cursor.execute(self.sql4)   						 
        self.results = self.cursor.fetchall()   					 
        print ("%5s%10s%5s%10s%5s%5s%5s" % ("id_product","category"," karat","material","price", "promo_price", "quantity") )   		 
        for row in self.results:
            self.id_product = row[0]
            self.category = row[1]
            self.karat = row[2]
            self.material= row[3]
            self.price = row[4]
            self.promo_price = row[5]
            self.quantity = row[6]
            print ("%5s%10s%5s%10s%5s%5s%5s" % (self.id_product, self.category, self.karat, self.material, self.price, self.promo_price, self.quantity))                
    

o1 = MenuDB(input('Your login: '), input('Your password: '))