# -*- coding utf-8 -*-
import pymysql
class MenuDB:
    
    def __init__(self, login, passwrd):
        self.conn = pymysql.connect("localhost", "root", "taja", "shopjwlry") #connect to database
        self.cursor = self.conn.cursor()   	
        self.login = login
        self.passwrd = passwrd
        self.log_in()
        
    def log_in(self):         #log in
        self.sql2 = 'SELECT * FROM login WHERE login=%s AND pass=%s'
        self.cursor.execute(self.sql2,(self.login, self.passwrd))
        
        if(self.cursor.rowcount == 1):
            row=self.cursor.fetchone()
            if row[1]=="admin":
                print('Dear ADMIN, you have been successfully logged in!')
                o2=Admin(row[0])             
            else:
                print('Dear User, you have been successfully logged in!')
                o3=User(row[0])        
        else:
            print('Login failed. Invalid username or password. Try again.')
            o1=MenuDB(input('Your login: '),input('Your password: ')  )
       
            
class User:
    def __init__(self, id_user):
        self.conn = pymysql.connect("localhost", "root", "taja", "shopjwlry") #connect to database
        self.cursor = self.conn.cursor()
        self.id_user=id_user
        self.menu()
        
    def menu(self):
        self.i = input('What you want to do next: \n(S)-show MY orders,\n(L)-login & security, \n(P)-show me all available products, \n(D)-delete my account, \n(Q)-LOG OUT')
        if(self.i == 'S'or self.i == 's'):
            print('My Orders')
            self.view_ord()
            self.menu()
                
        elif(self.i == 'L' or self.i == 'l'):
            print('My account')
            #self.read_pd()
            self.mod2()
                
        elif(self.i =='P'or self.i == 'p'):
            print('Available products')
            self.read_prdcts()
            self.menu()
                
        elif(self.i =='D' or self.i == 'd'):
            print('Delete your account')
            self.delete_ac()
            self.menu()
                
        elif(self.i =='Q' or self.i== 'q'):
            print('You have been successfully logged out')
                
        else:
            print('Wrong choice :( try again!')
            self.menu()
          
    def view_ord(self, id_user=None): #here you can view your orders
        if id_user is None:
            id_user=self.id_user        
        self.sql1 = "SELECT * FROM users_orders where users_orders.id_user=%s"   						 
        self.cursor.execute(self.sql1, (id_user))
        
        self.results = self.cursor.fetchall()   					 
        print ("%-10s%-10s%-15s%-15s%-15s%-15s%-15s" % ("id_user"," name_us","Surname","id_product","order_nr","category","price") )   		 
        for row in self.results:
            self.id_user = row[0]
            self.name_us = row[1]
            self.surname = row[2]
            self.id_product = row[3]
            self.order_nr = row[4] 
            self.category = row[5]
            self.price = row[6]
            print ("%-10s%-10s%-15s%-15s%-15s%-15s%-15s" % (self.id_user, self.name_us, self.surname, self.id_product, self.order_nr, self.category, self.price))        
    
    def mod2(self, id_user=None): #here you can modify your personal data
        if id_user is None:
            id_user=self.id_user
        self.sql2 = "SELECT * FROM users where users.id_user=%s" 
        self.cursor.execute(self.sql2, (id_user))
        
        self.results=self.cursor.fetchall()
        print("%-10s%-15s%-15s%-15s%-30s%-15s" % ("id_user", "name_us","surname", "city", "email", "mobile"))
        for row in self.results:
            self.id_user= row[0]
            self.name_us = row[1]
            self.surname = row[2]
            self.city = row[3]
            self.email = row[4] 
            self.mobile = row[5]            
            print("%-10s%-15s%-15s%-15s%-30s%-15s" % (self.id_user, self.name_us, self.surname, self.city, self.email, self.mobile))
        self.k= input('\nAre you sure to UPDATE your personal data?: \n(N)-NO, go back to Menu , \n(Y)-Yes, I want to update my personal details')
        if (self.k=='Y' or self.k=='y' ):        
            print('\n Please provide all informations below: ')
            self.name_us=input('Your name:')
            self.surname=input('Your surname:')
            self.city=input('Your city:')
            self.email=input('Your email:')
            self.mobile=input('Your mobile:')
            print("%-10s%-15s%-15s%-15s%-30s%-15s" % (self.name_us, self.surname, self.city, self.email, self.mobile))
        else:
            print('\nData has been not updated')
        
        self.k1= input('\nAre you sure to CHANGE your personal data?: \n(N)-NO, go back to Menu , \n(Y)-Yes, I want to CHANGE my personal details')
        if (self.k1=='Y' or self.k=='y' ):
            self.data_update='insert into users(name_us, surname, city, email, mobile ) values (%s,%s,%s,%s,%s)'
            self.cursor.execute(self.data_update,(self.name_us, self.surname,self.city, self.email, self.mobile))
            self.conn.commit()
            print('\nData has been updated')
            self.menu()
        
        else:
            print('\nData has been not updated')
            self.menu()        
            
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
    
    def delete_ac(self):
        print("You have no rights to delete your account, please contact Admin")
    
class Admin:
    def __init__(self, id_user):
        self.conn = pymysql.connect("localhost", "root", "taja", "shopjwlry") #connect to database
        self.cursor = self.conn.cursor()
        self.id_user=id_user
        self.menu2()
        
    def menu2(self):
            self.j = input('What you want to do next: \n(S)-show ALL orders,\n(U)-Users & security, \n(P)-show me all products, \n(D)-delete User, \n(Q)-LOG OUT')
            if(self.j == 'S'or self.j == 's'):
                print('All orders')
                self.view_ord()
                self.menu2()
            elif(self.j == 'U' or self.j == 'u'):
                print('All users & security')
                self.read_pd()
                #self.edit()
                #self.read_pd()
                self.menu2()
            elif(self.j =='P'or self.j == 'p'):
                print('All available products')
                self.read_prdcts()
                self.menu2()
            elif(self.j =='D' or self.j == 'd'):
                print('here you can manage users accounts')
                print('To delete account please contact your Boss ;) ')
                self.menu2()
            elif(self.j =='Q' or self.j== 'q'):
                print('You have been successfully logged out')
            else:
                print('Wrong choice :( try again!')
                self.menu2()
          
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
