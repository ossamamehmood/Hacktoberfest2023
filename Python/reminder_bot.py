import time

class ReminderBot:

    def __init__(self):
        self.tasks = []

    def add_task(self, task, delay_in_seconds):
        """Add a task to the bot's list of tasks."""
        self.tasks.append((task, delay_in_seconds))
        
    def start(self):
        """Start the bot and remind users of their tasks."""
        for task, delay in self.tasks:
            time.sleep(delay)
            print(f"Reminder: {task}")

if __name__ == "__main__":
    bot = ReminderBot()
    
    print("Reminder Bot is now active. Add your tasks!")
    while True:
        task = input("What do you want to be reminded about? ")
        delay = int(input("After how many seconds do you want the reminder? "))
        
        bot.add_task(task, delay)
        cont = input("Do you want to add another task? (yes/no) ").strip().lower()
        
        if cont == 'no':
            break

    print("\nAll tasks added! Waiting to remind you...")
    bot.start()
