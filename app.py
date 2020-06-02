########################CREATED BY MUHAMMAD HANAN ASGHAR###########################

#Library To Connect Connection With Mysql
import mysql.connector
#Library to perform tasks about system
import os

con = mysql.connector.connect(
            user = "root",
            password = "",
            host = "127.0.0.1",
            database = "python"
        )



#Second Class For Todos
class ToDos:
    def main(self,user,passw):
        os.system('cls||clear')
        print('''
        
 .----------------.   .----------------.   .----------------.   .----------------. 
| .--------------. | | .--------------. | | .--------------. | | .--------------. |
| |  _________   | | | |     ____     | | | |  ________    | | | |     ____     | |
| | |  _   _  |  | | | |   .'    `.   | | | | |_   ___ `.  | | | |   .'    `.   | |
| | |_/ | | \_|  | | | |  /  .--.  \  | | | |   | |   `. \ | | | |  /  .--.  \  | |
| |     | |      | | | |  | |    | |  | | | |   | |    | | | | | |  | |    | |  | |
| |    _| |_     | | | |  \  `--'  /  | | | |  _| |___.' / | | | |  \  `--'  /  | |
| |   |_____|    | | | |   `.____.'   | | | | |________.'  | | | |   `.____.'   | |
| |              | | | |              | | | |              | | | |              | |
| '--------------' | | '--------------' | | '--------------' | | '--------------' |
 '----------------'   '----------------'   '----------------'   '----------------' 

        ''')
        print()
        print('Welcome To Your TodoApp')
        print("""
        1.New Todo
        2.View All Todos
        3.Quit
        """)
        a = int(input('Enter Choice Number : '))
        if a==1:
            #Function To Create Todo
            self.__createTodo()
        if a==2:
            #Function to get All Todos
            self.__getAll()
        if a==3:
            exit()
        
    
    def __createTodo(self):
        os.system('cls||clear')
        print('Create Your New Todo')
        #Taking Credentials From user
        todo_name = input('Enter Todo Title: ')
        todo_subject = input('Enter Todo Subject: ')
        #Creating Cursor Object to Perform
        cursor = con.cursor()
        #Adding Data
        try:
            cursor.execute(f"INSERT INTO todo VALUES('{todo_name}','{todo_subject}')")
            #Line To Inisert or update data in mysql
            con.commit()
        except:
            #Return Error
            con.rollback()
        print()
        print("Your Data is Inserted")
        print()
        con.close()


    def __getAll(self):
        #Line to Clear the terminal
        os.system("cls||clear")
        print('Your All Todos Are : ')
        print()
        cursor = con.cursor()
        #View Data
        cursor.execute("SELECT TodoName,TodoSubject FROM todo")
        #Storing response in varibale
        result = cursor.fetchall()
        #Now Showing
        # cursor.execute("SELECT TodoSubject FROM todo")
        # #Storing response in varibale
        # result2 = cursor.fetchall()
        #Now Showing
        for i,j in result:
            print(f"{str(i)} : {str(j)}")



#Main Class
class Login(ToDos):
    def __init__(self,user,passw):
        self.user = user
        self.passw = passw
        #Encapsulation
        self.__database(self.user,self.passw)
    def __database(self,user,passw):
#Connection Details

    #Create Cursor Object to Crawl Over Data in Database
        cursor = con.cursor()
        cursor.execute(f"SELECT Username FROM login WHERE Username = '{self.user}' ")
            #Line Used To Fetch all Data According to this query
        result = cursor.fetchall()
            # Query To Execute To Get Data From Mysql
        cursor.execute(f"SELECT password FROM login WHERE password = '{int(self.passw)}'")
            #Line Used To Fetch all Data According to this query
        result2 = cursor.fetchall()
            #Conditional Statement To Check Authentication
        #Exception Handling
        try:
            if self.user in result[0] or self.passw in result2[0]:
                self.main(self.user,self.passw)
        except:
            if self.user not in  result[0] or self.passw not in result2[0]:
                print('Your Credentials Are Not Correct')


print('Welcome To Login System By Muhammad Hanan Asghar')
print("""            
        

 /$$              /$$$$$$         /$$$$$$        /$$$$$$       /$$   /$$
| $$             /$$__  $$       /$$__  $$      |_  $$_/      | $$$ | $$
| $$            | $$  \ $$      | $$  \__/        | $$        | $$$$| $$
| $$            | $$  | $$      | $$ /$$$$        | $$        | $$ $$ $$
| $$            | $$  | $$      | $$|_  $$        | $$        | $$  $$$$
| $$            | $$  | $$      | $$  \ $$        | $$        | $$\  $$$
| $$$$$$$$      |  $$$$$$/      |  $$$$$$/       /$$$$$$      | $$ \  $$
|________/       \______/        \______/       |______/      |__/  \__/
                                                                        
                                                                        
                                                                        

                                
""")
#get username input from User
user_name = input('Enter Username: ')
pass_word = int(input('Enter Password: '))
l = Login(user_name.lower(),pass_word)


########################CREATED BY MUHAMMAD HANAN ASGHAR###########################
