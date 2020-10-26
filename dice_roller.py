import random

def main():

  dice_rolls = int(input("The number of dice throws: "))
  dice_size = int(input("The number of sides for a dice: "))
  dice_sum = 0
  while dice_rolls:
    roll = random.randint(1, dice_size)
    if roll == 1:
        print(f'You rolled a {roll}! Critical Fail!')
    elif roll == dice_size:
        print(f'You rolled a {roll}! Critical Success!')
    else:
        print(f'You rolled a {roll}')
    dice_sum += roll
    dice_rolls -= 1
  print(f'You rolled a total of: {dice_sum}')


if __name__== "__main__":
  main()
