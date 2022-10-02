import random

print("Welcome to the Python RPG!")

HerculesDict = {
  "Name" : "Hercules",
  "Health": 200,
  "Attack Power": 20,
  "Mighty Slash": 1.5,
  "Shield Bash": 1.5,
  "Holy Right": 5.0

}

AlucardDict = {
    "Name" : "Alucard",
    "Health" : 400,
    "Attack Power" : 50
}

def Attack(target_health,attack_power, skill):
    attack_damage = attack_power * skill
    target_health -= attack_damage
    return target_health

def random_enemy_attack(attack_list):
    attack = random.choice(attack_list)
    return attack



