from re import match
import random
import math

# Between 18-20, the better proficiency = lower the floor, keep the ceiling

def LineLoop():
    for x in range(1, 25):
        print("\n")

def menu(name, warriorSelect, wizardSelect, archerSelect):
    menuSelect = int(input("Please Select One:\n\n1. Battle\n2. Barracks\n3. Settings\n"))
    LineLoop()
    if warriorSelect == True:
        if menuSelect == 1:
            Battle(name, 250, 50)
    if wizardSelect == True:
        if menuSelect == 1:
            Battle(name, 100, 25)
    if archerSelect == True:
        if menuSelect == 1:
            Battle(name, 150, 35)


def Battle(name, HP, Defense):
    print("Goblin has spawned!\n\nHP: 100\n\n")
    attackLoop = True
    specialAttackBar = 100
    goblinHP = 100
    while(attackLoop):
        print("Defense: ",int(math.ceil(Defense)))
        print("Special attack:" , specialAttackBar)
        attackChoice = int(input("1. Auto Attack\n2. Special Attack\n3. Defend\n4. Flee\n\nChoice: "))
        LineLoop()
        if attackChoice == 1:
            attackDamage = random.randint(0,25)
            print("\n\nYou deal " , attackDamage , "!")
            goblinHP = goblinHP - attackDamage
            NPCdamage = random.randint(50, 60)
            NPCdamage = NPCdamage - Defense
            HP = HP - NPCdamage
            print("\nGoblin hits you for " , NPCdamage , "!\n")
            if HP >= 0:
                print(name, ": " ,int(math.ceil(HP)))
                attackLoop = True
            if HP <=0:
                print("You lose. . .")
                HP = 0
                attackLoop = False
                menu(name, True, False, False)

            if goblinHP > 0:
                print("Goblin: " , goblinHP)
                attackLoop = True

            if goblinHP <= 0:
                goblinHP = 0
                print("Victory!")
                attackLoop = False
                menu(name, True, False, False)

        elif attackChoice == 3:
            if Defense <=50 and Defense >= 0:
                print("You defend 80% of the attack! You also gain 25 points for your special meter bar. . . ")
                NPCdamage = random.randint(50, 60)
                NPCdamage = NPCdamage - Defense
                blockDamage = NPCdamage * 0.80
                NPCdamage = NPCdamage - blockDamage
                HP = HP - NPCdamage
                print("\nGoblin hits you for " , int(math.ceil(NPCdamage)) , "!\n")
                print("\nYour defenses decrease. . .\n\n")
                Defense = Defense - NPCdamage
                if specialAttackBar < 100:
                    specialAttackBar = specialAttackBar + 25
                if Defense <=0:
                    Defense = 0
                if HP >= 0:
                    print(name, ": " ,int(math.ceil(HP)))
                    attackLoop = True
                if HP <= 0:
                    print("You lose. . .")
                    HP = 0
                    attackLoop = False
                    menu(name, True, False, False)

                if goblinHP > 0:
                    print("Goblin: " , goblinHP)
                    attackLoop = True
            else:
                print("\nYou no longer have any defenses.\n")

        elif specialAttackBar < 50:
            print("\nYou do not have enough special attack meter! Defend to gain more. (Requires 50)\n")
            print(name, ": " ,int(math.ceil(HP)))
            print("Goblin: " , goblinHP)
        elif specialAttackBar == 0:
            print("\nYou do not have anymore special attack left!\n")
            print(name, ": " ,int(math.ceil(HP)))
            print("Goblin: " , goblinHP)

        elif attackChoice == 2 and specialAttackBar != 0:
            print("\nYou use a special attack!")
            specialAttackBar = specialAttackBar - 50
            specialAttack = random.randint(10,50)
            print("\n\nYou deal " , specialAttack , "!")
            goblinHP = goblinHP - specialAttack
            NPCdamage = random.randint(0, 10)
            HP = HP - NPCdamage
            print("\nGoblin hits you for " , NPCdamage , "!\n")

            if HP >= 0:
                print(name, ": " ,int(math.ceil(HP)))
                attackLoop = True
            if HP <= 0:
                print("You lose. . .")
                HP = 0
                attackLoop = False
                menu(name, True, False, False)

            if goblinHP > 0:
                print("Goblin: " , goblinHP)
                attackLoop = True
            if goblinHP <= 0:
                goblinHP = 0
                print("Victory!")
                attackLoop = False
                menu(name, True, False, False)

        


loop = True
print("Welcome to my RPG Game!\n\n")

name = input("Let's get started! Enter a name: ")

print("\n\nPerfect... " + name + "! Now let's get started with your class.")
while(loop):
    job = int(input("\n\n1. Warrior\n2. Mage\n3. Archer\n\nYour Destiny: "))
    match (job):
        case 1:
            warriorChoice = input("\nHuzzah! The Warrior... Strong-armed, strong conviction and wields a giant axe. This class is for those who seek strength and vitality build.\n\nAre you sure you want this class? (Y/N): ")
            if warriorChoice.lower() == "y":
                print("\n\nYour destiny is sealed.\n\nNow commencing warrior playthrough. . .\n")
                warriorSelect = True
                menu(name, True, False, False)
                loop = False
            elif warriorChoice.lower() == "n":
                print("\n\nIt takes a strong mind to wield the axe... Maybe, it is not for you. . .\n")
                loop = True
        case 2:
            wizardChoice = input("\nWizard... Excels in magicks and tomes, a wizard uses intelligence and mana to cast strong spells to slay their foes. This class is for those who seek high power, low defense build.\n\nAre you sure you want this class? (Y/N): ")
            if wizardChoice.lower() == "y":
                print("\n\nYour destiny is sealed.\n\nNow commencing wizard playthrough. . .\n")
                wizardSelect = True
                menu(name, False, True, False)
                loop = False
            elif wizardChoice.lower() == "n":
                print("\n\nLack of intelligence and poor mana management will not bode well with this class... Maybe, it is not for you. . .\n")
                loop = True
        case 3:
            archerChoice = input("\nThe Archer... Precise and deadly, the archer seeks to attack vital points of their enemy leaving them stunned and in an instant drowning in their own blood. This class is for those who seek dexterity and evasive build.\n\nAre you sure you want this class? (Y/N):  ")
            if archerChoice.lower() == "y":
                print("\n\nYour destiny is sealed.\n\nNow commencing archer playthrough. . .\n")
                archerSelect = True
                menu(name, False, False, True)
                loop = False
            elif archerChoice.lower() == "n":
                print("\n\nIt takes agility and precision to master this class... Maybe, it is not for you. . .\n")
                loop = True


