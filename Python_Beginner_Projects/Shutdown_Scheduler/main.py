import os

if __name__ == '__main__':
    i = 0
    while i != 1 or 2 or 3 or 4:
        screen = "cls"
        os.system(screen)
        print(''' Welcome to System scheduler 
            Choose one of the following option to execute
            1.Shutdown
            2.Restart
            3. Instant Logout
            4.Exit ''')
        x = int(input())


        def task():
            text = int(input("Enter time for the execution of task!\n"))
            return text


        match x:
            case 1:
                cmd = f"shutdown.exe /s /t {task()}"
                os.system(cmd)
                i = x
                break
            case 2:
                cmd = f"shutdown.exe /r /t {task()}"
                os.system(cmd)
                i = x
                break
            case 3:
                cmd = f"shutdown.exe /l"
                os.system(cmd)
                i = x
                break
            case 4:
                exit()
            case _:
                print("Please enter the valid Choice")
