"""
# Reading
f = open("dontwant.txt")
s = f.readlines()
print(s)
f.close()

# Writing
f = open("dontwant.txt", "w")
f.write("Some line\n")
f.write("More lines\n")
f.close()

# Appending
with open("dontwant.txt", "a") as f:
   # s = f.readlines()
    # print(s)
   f.write("Extra line\n")
   """

# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import functions_lab06

# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Question 5: Loading a saved game
monster_won_recently = False

with open("save.txt", "r") as f:
    lines = f.readlines()
    most_recent_game = lines[-1].strip()
    print(most_recent_game)

if most_recent_game == "Monster has killed the hero previously.":
    monster_won_recently = True
else:
    monster_won_recently = False




# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Question 5 (cont.)
    if monster_won_recently:
        combat_strength += 1
    else:
        m_combat_strength += 1

        print(combat_strength)
        print(m_combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    # Collect Loot
    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")

    # Collect Loot First time
    loot_options, belt = functions_lab06.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")

    # Collect Loot Second time
    loot_options, belt = functions_lab06.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    # Use Loot
    belt, health_points = functions_lab06.use_loot(belt, health_points)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    # Compare Player vs Monster's strength
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))

    # Check the Player's overall strength and health
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                

                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Increase the monster’s combat strength by its power
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        m_combat_strength) + " using the " + power_roll + " magic power")

    # Call Recursive function
    print("    |", end="    ")

    input_invalid = True
    attempts = 0

    while input_invalid and attempts < 3:
        attempts += 1
        num_dream_lvls = input("How many dream levels do you want to go down? (0-3): ")

        if num_dream_lvls.isnumeric():
            num_dream_lvls = int(num_dream_lvls)
            if num_dream_lvls in range(0, 4):
                input_invalid = False
            else:
                print("Your input was not valid. Please enter a number between 0 and 3.")
        else:
            print("Your input was not valid. Please enter a number between 0 and 3.")

    if num_dream_lvls != 0 and input_invalid is False:

        health_points -= 1
        crazy_level = functions_lab06.inception_dream(num_dream_lvls)
        combat_strength += crazy_level
        print("combat strength: " + str(combat_strength))
        print("health points: " + str(health_points))

    # Fight Sequence
    # Loop while the monster and the player are alive. Call fight sequence functions
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    hero_won = False

    while m_health_points > 0 and health_points > 0:
        # Fight Sequence
        print("    |", end="    ")

        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)

        if attack_roll % 2 != 0:  # Player attacks first
            print("    |", end="    ")
            input("You strike (Press enter)")
            m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)

            if m_health_points == 0:
                num_stars = 3
                hero_won = True
                break

            print("    |", end="    ")
            print("------------------------------------------------------------------")
            input("    |    The monster strikes (Press enter)!!!")
            health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)

            if health_points == 0:
                num_stars = 1
                break
            else:
                num_stars = 2

        else:  # Monster attacks first
            print("    |", end="    ")
            input("The Monster strikes (Press enter)")
            health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)

            if health_points == 0:
                num_stars = 1
                break

            print("    |", end="    ")
            print("------------------------------------------------------------------")
            input("The hero strikes!! (Press enter)")
            m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)

            if m_health_points == 0:
                num_stars = 3
                hero_won = True
                break
            else:
                num_stars = 2

    # Final Score Display
    tries = 0
    input_invalid = True

    while input_invalid and tries < 5:
        print("    |", end="    ")
        hero_name = input("Enter your Hero's name (in two words): ").strip()
        name_parts = hero_name.split()

        if len(name_parts) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
        elif not name_parts[0].isalpha() or not name_parts[1].isalpha():
            print("    |    Please enter an alphabetical name")
        else:
            short_name = name_parts[0][:2] + name_parts[1][0]
            print(f"    |    I'm going to call you {short_name} for short")
            input_invalid = False

        tries += 1

    if not input_invalid:
        stars_display = "*" * num_stars
        print(f"    |    Hero {short_name} gets <{stars_display}> stars")

        with open("save.txt", "a") as f:
            if hero_won:
                save_msg = f"Hero {short_name} has killed a monster and gained {num_stars}"
            else:
                save_msg = "Monster has killed the hero previously."

            f.write(save_msg + "\n")

