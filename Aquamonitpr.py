# AquaMonitor - An Aquarium Monitoring Application

# Import necessary libraries
import time

# Define a class for an aquarium
class Aquarium:
    def __init__(self, name, size, fish=[]):
        self.name = name
        self.size = size
        self.fish = fish

    def add_fish(self, fish_name):
        self.fish.append(fish_name)

    def display_info(self):
        print(f"Aquarium Name: {self.name}")
        print(f"Size: {self.size} gallons")
        print("Fish:")
        for fish in self.fish:
            print(f"  - {fish}")

# Create instances of Aquarium
aquarium1 = Aquarium("Tropical Paradise", 30, ["Guppy", "Neon Tetra", "Angelfish"])
aquarium2 = Aquarium("Reef Oasis", 55, ["Clownfish", "Blue Tang", "Damsel"])

# Main function
def main():
    while True:
        print("\n--- AquaMonitor ---")
        print("1. Display Aquarium Info")
        print("2. Add Fish to an Aquarium")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            aquarium1.display_info()
            aquarium2.display_info()
        elif choice == "2":
            aquarium_name = input("Enter the aquarium name: ")
            fish_name = input("Enter the fish name to add: ")
            if aquarium_name == aquarium1.name:
                aquarium1.add_fish(fish_name)
            elif aquarium_name == aquarium2.name:
                aquarium2.add_fish(fish_name)
            else:
                print("Aquarium not found!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
