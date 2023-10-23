import os
if __name__== '__main__':
    print ("Welcome to the robo speaker 1.1 created by Rounak")
    
    while True:
        
        x= input("Enter the text you want to speak: ")
        if x== "exit":
            os.system ("say 'Goodbye'")
            break
        command= f"say {x}"
        os.system(command)
        