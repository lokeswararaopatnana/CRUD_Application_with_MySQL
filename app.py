from dbdata import DBstore;

def app():
    db = DBstore()
    while True:
        print("******Welcome to CRUD App****** \n")
        print("""\tPress 1 to Insert New User \n
        Press 2 to Display All Users \n
        Press 3 to Display One User \n
        Press 4 to Update a User \n
        Press 5 to Delete a User \n
        Press 6 to Exit the CRUD application
        """) 
        try:
            option = int(input("Select the Options:"))
            if(option == 1):
                # insert user
                UserId = int(input("Enter UserId:"))
                UserName = input("Enter UserName:")
                UserPhone = input("Enter UserPhone Number:")
                db.insert_user(UserId,UserName,UserPhone)

            elif(option == 2):
                # display all users
                db.fetch_all()
            
            elif(option == 3):
                # display one user
                UserId = int(input("Enter UserId:"))
                db.fetch_one(UserId)
                pass

            elif(option == 4):
                # update user
                UserId = int(input("Enter UserId to Update:"))
                UserName = input("Enter New UserName:")
                UserPhone = input("Enter New UserPhone Number:")
                db.update_user(UserId,UserName,UserPhone)
                pass

            elif(option == 5):
                # delete user
                UserId = int(input("Enter UserId to Delete:"))
                db.delete_user(UserId)
                pass

            elif(option == 6):
                # break
                break

            else:
                print("Invalid Input! Try Again")
        except Exception as exp:
            print(exp)
            print("Invaid details! Please enter correct datails...!")

if __name__ == "__main__":
    app()    