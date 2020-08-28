import random
import time

game_active = True
player_starting_health = 10
starting_damage_dealt = 1
monster_starting_health = 5
current_monster = "goblin"
current_monster_hit_chance = 5
current_monster_damage_dealt = 1
move_in_direction = None
random_encounter = random.randint(1,5)






while game_active:

    try:
        print(f"You encounter a {current_monster}! What do you want to do? attack or run?")

        your_dodge_chance = random.randint(1, 10) + 3
        value_to_hit = random.randint(1, 10)
        current_damage_dealt = starting_damage_dealt

        action_to_take = str(input("What do you do?: "))

        if action_to_take == "attack":
            if value_to_hit >= current_monster_hit_chance:
                print(f"You hit the {current_monster} causing {current_damage_dealt} damage!")
                monster_starting_health = monster_starting_health - current_damage_dealt
                if monster_starting_health <= 0:
                    print(f"You defeat the {current_monster}!")
                    print(f"Your health is now at {player_starting_health}")
                    break
                if your_dodge_chance <= current_monster_hit_chance:
                    print(f"The {current_monster} attacks you back, dealing {current_monster_damage_dealt}!")
                    player_starting_health = player_starting_health - current_monster_damage_dealt
                    print(f"Your life total is now {player_starting_health}")

                elif your_dodge_chance > current_monster_hit_chance:
                    print(f"The {current_monster} attack you back, but misses!")
                    print(f"Your current health is {player_starting_health}")

            else:
                print(f"You swing and miss as the {current_monster} dodges your attack!")
                if your_dodge_chance <= current_monster_hit_chance:
                    print(f"The {current_monster} attacks you back, dealing {current_monster_damage_dealt}!")
                    player_starting_health = player_starting_health - current_monster_damage_dealt
                    print(f"Your life total is now {player_starting_health}")

                elif your_dodge_chance > current_monster_hit_chance:
                    print(f"The {current_monster} attack you back, but misses!")
                    print(f"Your current health is {player_starting_health}")
        elif action_to_take == "run":
            print("You try to run away")
            time.sleep(1)
            if value_to_hit >= current_monster_hit_chance:
                print("You sucessfully escape!")
                break
            else:
                print("You fail to run away!")
                print(f"The {current_monster} attacks you when you try, dealing {current_monster_damage_dealt}!")
                player_starting_health = player_starting_health - current_monster_damage_dealt
                print(f" Your life total is now {player_starting_health}")



    except Exception:
        break





