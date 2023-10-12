# Organizer - A Simple Task and Event Organizer

# Dictionary to store tasks and events
organizer = {'tasks': [], 'events': []}

# Function to add a task
def add_task(task_name):
    organizer['tasks'].append(task_name)

# Function to add an event
def add_event(event_name):
    organizer['events'].append(event_name)

# Function to list tasks
def list_tasks():
    if not organizer['tasks']:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in organizer['tasks']:
            print(f"- {task}")

# Function to list events
def list_events():
    if not organizer['events']:
        print("No events found.")
    else:
        print("Events:")
        for event in organizer['events']:
            print(f"- {event}")

# Function to remove a task
def remove_task(task_name):
    if task_name in organizer['tasks']:
        organizer['tasks'].remove(task_name)
        print(f"'{task_name}' has been removed from tasks.")
    else:
        print(f"'{task_name}' is not found in tasks.")

# Function to remove an event
def remove_event(event_name):
    if event_name in organizer['events']:
        organizer['events'].remove(event_name)
        print(f"'{event_name}' has been removed from events.")
    else:
        print(f"'{event_name}' is not found in events.")

# Main function
def main():
    while True:
        print("\n--- Organizer ---")
        print("1. Add a Task")
        print("2. Add an Event")
        print("3. List Tasks")
        print("4. List Events")
        print("5. Remove a Task")
        print("6. Remove an Event")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice == "1":
            task_name = input("Enter the task name: ")
            add_task(task_name)
            print(f"'{task_name}' has been added to tasks.")
        elif choice == "2":
            event_name = input("Enter the event name: ")
            add_event(event_name)
            print(f"'{event_name}' has been added to events.")
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            list_events()
        elif choice == "5":
            task_name = input("Enter the task name you want to remove: ")
            remove_task(task_name)
        elif choice == "6":
            event_name = input("Enter the event name you want to remove: ")
            remove_event(event_name)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
