import random

def roll_dice(num_dice):
  rolls = []
  for i in range(num_dice):
    rolls.append(random.randint(1, 6))
  return rolls

def main():
  num_dice = int(input("How many dice do you want to roll? "))
  rolls = roll_dice(num_dice)

  print("The results are:")
  for roll in rolls:
    print(roll)

if __name__ == "__main__":
  main()
