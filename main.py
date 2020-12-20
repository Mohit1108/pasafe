import sqlite3 as sq3
from generator import generate_pass

connection = sq3.connect('passwords.db')
cursor = connection.cursor()

cursor.execute("INSERT INTO passwords VALUES ('gmail', 'www.gmail.com', 1234 )")

def commit_and_close():
    connection.commit()
    connection.close()

def interface():
    print("Welcome To Pass-lock.")
    #print("Thanks for using Pass-lock.")
    print("[0]. Get your Password")
    print("[1]. Add a New Password.")
    print("[2]. Update a Existing Password.")
    print("[3]. See all Passwords")
    print("")
    pass_choice = int(input("enter Choice."))
    if pass_choice == 0:
        get_pass()
    if pass_choice == 1:
        add_pass()
    if pass_choice == 2:
        update_pass()
    if pass_choice == 3:
        pass
    if pass_choice not in [0, 1, 2, 3]:
        print("Wrong Choice.")
        interface()

def get_pass():
    #website_name = input(" Enter Website's Name : ")
    cursor.execute("SELECT * FROM passwords WHERE web_name = 'gmail'")
    data = cursor.fetchall()
    if data is not None:
        print(data)
    else:
        print("No data found.")
    commit_and_close()

def add_pass():
    website_name = input("Enter Website's Name : ")
    website_url = input("Enter Website's URL : ")
    website_password = input("If you want me to generate a password for you"
                             "then press [Y] for YES and [N] for NO.")
    if website_password == 'N' or website_password == 'n':
        website_password = generate_pass()
        print(website_password)
    sql = 'Insert into passwords values (%s, %s, %s)' %(website_name, website_url, website_password)
    cursor.execute(sql)
    commit_and_close()

def update_pass():
    website_name = input("Enter Website/App name : ")
    new_password = input("Enter New Password : ")
    cursor.execute("update passwords set password = %s where web_name = %s" %(new_password, website_name))
    commit_and_close()

def see_all():
    cursor.execute('select * from password')
    data = cursor.fetchall()
    print(data)

if __name__ == '__main__':
    interface()
