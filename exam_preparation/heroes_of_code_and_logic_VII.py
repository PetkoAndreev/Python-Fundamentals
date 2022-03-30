heroes = {}
monsters = {}

def add_modify_hero(hero, health, mana):
    if hero in heroes:
        if heroes[hero][0] + health <= 100:
            heroes[hero][0] += health
        else:
            heroes[hero][0] = 100
        if heroes[hero][1] + mana <= 200:
            heroes[hero][1] += mana
        else:
            heroes[hero][1] = 200
    else:
        heroes[hero] = [health, mana]

    return heroes

def add_modify_monster(monster, health):
    if monster in monsters:
        if monsters[monster] + health <= 100:
            monsters[monster] += health
        else:
            monsters[monster] = 100
    else:
        monsters[monster] = health

    return monsters

def cast_spell(hero, mana, spell, power, monster):
    if heroes[hero][1] >= mana:
        heroes[hero][1] -= mana
        print(f'{hero} has successfully cast {spell} and now has {heroes[hero][1]} MP!')
        if monsters[monster] - power > 0:
            monsters[monster] -= power
            print(f'{monster} now has {monsters[monster]} left!')
        else:
            print(f'{monster} has been defeated!')
    else:
        print(f'{hero} does not have enough MP to cast {spell}!')

    return heroes


def take_hit(hero, damage, monster):
    if heroes[hero][0] - damage > 0:
        heroes[hero][0] -= damage
        print(f'{hero} was hit for {damage} HP by {monster} and now has {heroes[hero][0]} HP left!')
    else:
        print(f'{hero} has been slain by {monster}!')
        del heroes[hero]

    return heroes


def fill_energy(hero, amount):
    if heroes[hero][1] + amount > 200:
        print(f'{hero} recharged for {200 - heroes[hero][1]} MP!')
        heroes[hero][1] = 200
    else:
        print(f'{hero} recharged for {amount} MP!')
        heroes[hero][1] += amount

    return heroes


def heal(hero, amount):
    if heroes[hero][0] + amount > 100:
        print(f'{hero} healed for {100 - heroes[hero][0]} HP!')
        heroes[hero][0] = 100
    else:
        print(f'{hero} healed for {amount} HP!')
        heroes[hero][0] += amount

    return heroes

# Heroes add
for i in range(1, num_heroes + 1):
    hero, health, mana = input().split()
    health = int(health)
    mana = int(mana)
    add_modify_hero(hero, health, mana)


num_monsters = int(input())
for i in range(1, num_heroes + 1):
    hero, health, mana = input().split()
    health = int(health)
    mana = int(mana)
    add_modify_hero(hero, health, mana)

command_data = input()

while command_data != 'End':
    command_data = command_data.split(' - ')
    command = command_data[0]
    if command == 'CastSpell':
        hero = command_data[1]
        mana = int(command_data[2])
        spell = command_data[3]
        castspell(hero, mana, spell)
    elif command == 'TakeDamage':
        hero = command_data[1]
        damage = int(command_data[2])
        attacker = command_data[3]
        takedamage(hero, damage, attacker)
    elif command == 'Recharge':
        hero = command_data[1]
        amount = int(command_data[2])
        recharge(hero, amount)
    elif command == 'Heal':
        hero = command_data[1]
        amount = int(command_data[2])
        heal(hero, amount)

    command_data = input()

heroes = dict(sorted(heroes.items(), key=lambda s: (-s[1][0], s[0])))

for hero, hp_mp in heroes.items():
    print(hero)
    print(f'  HP: {hp_mp[0]}')
    print(f'  MP: {hp_mp[1]}')