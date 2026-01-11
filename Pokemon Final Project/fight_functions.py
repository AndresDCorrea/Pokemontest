import copy
import random


def effectiveness(attack_type, target_types):
    table = {
        'fire': {
            'fire': 0.5, 'water': 0.5, 'grass': 2, 'electric': 1,
            'ice': 2, 'rock': 0.5, 'bug': 2, 'ground': 1,
            'dragon': 0.5, 'steel': 2
        },
        'water': {
            'fire': 2, 'water': 0.5, 'grass': 0.5,
            'electric': 1, 'rock': 2, 'ground': 2, 'dragon': 0.5
        },
        'grass': {
            'fire': 0.5, 'water': 2, 'grass': 0.5, 'rock': 2,
            'ground': 2, 'bug': 0.5, 'dragon': 0.5, 'poison': 0.5
        },
        'electric': {
            'water': 2, 'grass': 0.5, 'ground': 0,
            'flying': 2, 'dragon': 0.5
        },
        'ice': {
            'fire': 0.5, 'water': 0.5, 'grass': 2, 'ground': 2,
            'dragon': 2, 'flying': 2, 'steel': 0.5
        },
        'fighting': {
            'normal': 2, 'rock': 2, 'steel': 2, 'ice': 2,
            'bug': 0.5, 'psychic': 0.5, 'flying': 0.5, 'ghost': 0
        },
        'poison': {
            'grass': 2, 'fairy': 2, 'rock': 0.5,
            'ghost': 0.5, 'steel': 0
        },
        'ground': {
            'fire': 2, 'rock': 2, 'steel': 2,
            'grass': 0.5, 'bug': 0.5, 'electric': 2
        },
        'flying': {
            'grass': 2, 'fighting': 2, 'bug': 2,
            'rock': 0.5, 'steel': 0.5, 'electric': 0.5
        },
        'psychic': {
            'fighting': 2, 'poison': 2, 'steel': 0.5, 'dark': 0
        },
        'bug': {
            'grass': 2, 'psychic': 2, 'dark': 2,
            'fire': 0.5, 'fighting': 0.5, 'flying': 0.5, 'ghost': 0.5
        },
        'rock': {
            'fire': 2, 'ice': 2, 'flying': 2, 'bug': 2,
            'fighting': 0.5, 'ground': 0.5, 'steel': 0.5
        },
        'ghost': {
            'ghost': 2, 'dark': 0.5, 'normal': 0, 'psychic': 2
        },
        'dragon': {
            'dragon': 2, 'steel': 0.5, 'fairy': 0
        },
        'dark': {
            'psychic': 2, 'ghost': 2, 'fighting': 0.5, 'fairy': 0.5
        },
        'steel': {
            'ice': 2, 'rock': 2, 'fairy': 2,
            'fire': 0.5, 'water': 0.5, 'electric': 0.5, 'steel': 0.5
        },
        'fairy': {
            'fighting': 2, 'dragon': 2, 'dark': 2,
            'fire': 0.5, 'steel': 0.5
        }
    }

    attack_type = str(attack_type).lower()

    if isinstance(target_types,str):
        target_types = [target_types]

    target_types = [str(t).lower() for t in target_types]

    result = 1.0

    for target_type in target_types:
        multiplier = table.get(attack_type, {}).get(target_type, 1.0)

        result *= multiplier
    return result

def player_action(player_profile, target_pokemon):
    while True:
        print(
            'Que quieres hacer?\n'
            '1 - Pelear\n'
            '2 - Curar un pokemon\n'
            '3 - Capturar un pokemon\n'
        )

        try:
            action = int(input())

            if action == 1:
                return pokemon_choose(player_profile)

            elif action == 2:
                pokemon_heal(player_profile)
                return None

            elif action == 3:
                return pokemon_catch(player_profile, target_pokemon)

        except ValueError:
            print('Ingrese un numero...')


def pokemon_catch(player_profile, target_pokemon):
    print('Tienes {} pokebolas'.format(player_profile['poke-balls']))

    if player_profile['poke-balls'] <= 0:
        print('No tienes pokebolas disponibles')
        return False, target_pokemon

    life_percentage = int(target_pokemon['current_health'] * 100 / target_pokemon['base_health'])
    catch_probability = 100 - life_percentage
    chance = random.randint(1, 100)

    catch = chance <= catch_probability
    player_profile['poke-balls'] -= 1

    if catch:
        print('Atrapaste al pokemon {}!'.format(target_pokemon['name']))
        player_profile['pokemon_inventory'].append(copy.deepcopy(target_pokemon))
        return True, None   # enemigo desaparece

    else:
        print('El pokemon se ha escapado!')
        return False, target_pokemon

def pokemon_heal(player_profile):
    print('Tienes {} pociones de curación'.format(player_profile['health_potion']))
    if player_profile['health_potion'] > 0:
        selection = pokemon_inventory(player_profile)
        selected_pokemon = player_profile['pokemon_inventory'][selection]
        selected_pokemon['current_health'] += selected_pokemon['base_health'] / 2
        print('Curaste a tu pokemon!. \n'
              'La vida actual de {} es de {}'.format(selected_pokemon['name'],
                                                     selected_pokemon['current_health']))
        player_profile['health_potion'] -= 1
        return

    else:
        print('Lo siento, no tienes pociones disponibles')
    return
def pokemon_inventory(player_profile):
    global selection
    print('Lista de pokemones: ')
    for index, pokemon in enumerate(player_profile['pokemon_inventory']):
        print('{} - {} {}. Salud: {}/{}. Nivel: {}. Puntos de XP: {}'.format(index, pokemon['name'],
                                                                             pokemon['type'],
                                                                             pokemon['current_health'],
                                                                             pokemon['base_health'],
                                                                             pokemon['level'],
                                                                             pokemon['current_xp']))
    try:
        selection = int(input('Seleccione un pokemon: '))
    except ValueError:
        print('Ingrese un numero...')
    return selection

def pokemon_choose(player_profile):
    chosen_pokemon = None
    while not chosen_pokemon:
        selection = pokemon_inventory(player_profile)

        if 0 <= selection < len(player_profile['pokemon_inventory']):
                chosen_pokemon = player_profile['pokemon_inventory'][selection]
                if chosen_pokemon['current_health'] < 0:
                    print('Este pokemon aun no se ha recuperado!.')
                else:
                    print('Has elegido a: {}.'.format(chosen_pokemon['name']))
        else:
                print('Selección invalida...')
    return chosen_pokemon

def machine_pokemon_choose(pokemon_list):
    enemy_pokemon = copy.deepcopy(random.choice(pokemon_list))
    print('El enemigo ha elegido ha: {} {}'.format(enemy_pokemon['name'], enemy_pokemon['type']))
    return enemy_pokemon

def available_attacks(pokemon_playing):
    attacks = []
    for attack in pokemon_playing['attacks']:
        if attack['lvl_min'] <= pokemon_playing['level']:
            attacks.append(attack)
    return attacks

def player_attack(attacks):
    chosen_attack = None
    while not chosen_attack:
        print('Lista de ataques: ')
        for index, attack in enumerate(attacks):
            print('{} - {}. Tipo de ataque: {}. Poder: {}'.format(index, attack['att_name'],
                                                                  attack['move_type'],
                                                                  attack['power']))

        try:
            selection = int(input('Selecciona un ataque: '))

            if 0 <= selection < len(attacks):
                chosen_attack = attacks[selection]
            else:
                print('Selección invalida...')
        except ValueError:
            print('Ingrese un numero...')
    print('Elegiste: {}'.format(chosen_attack['att_name']))
    return chosen_attack

def effectiveness_msg(multiplier):
    if multiplier > 1:
        msg = f"SUPER EFECTIVO ({multiplier}x) ⚡"
    elif multiplier == 1:
        msg = f"Normal ({multiplier}x)"
    elif multiplier == 0.5:
        msg = f"NO MUY EFECTIVO ({multiplier}x) 💤"
    elif multiplier == 0:
        msg = f"NO AFECTA ({multiplier}x) 🛡️"
    else:
        msg = f"({multiplier}x)"
    return msg

def attack_result(chosen_attack, target_pokemon):
    multiplier = effectiveness(chosen_attack['move_type'], target_pokemon['type'])
    print(effectiveness_msg(multiplier))
    attack_dmg = chosen_attack['power'] * multiplier
    target_pokemon['current_health'] -= attack_dmg
    print('El ataque hizo {} de daño'.format(attack_dmg))
    print('La vida del pokemon enemigo es de: {}'.format(target_pokemon['current_health']))

def get_pokemon_info(player_profile):
    return [pokemon for pokemon in player_profile['pokemon_inventory']]

def get_player_profile(pokemon_list):
    return {
        'player_name': input('Cual es tu nombre?: '),
        'pokemon_inventory': [copy.deepcopy(random.choice(pokemon_list)) for a in range (3)],
        'combats': 0,
        'poke-balls': 0,
        'health_potion':0,
        'loot_chance' : False

    }

def any_player_pokemon_lives(player_profile):
    return sum([pokemon['current_health'] for pokemon in player_profile['pokemon_inventory']]) > 0

def switch_turns(currently_playing, player_pokemon, enemy_pokemon):
    if currently_playing == player_pokemon:
        next_player = enemy_pokemon
        target_pokemon = player_pokemon
    else:
        next_player = player_pokemon
        target_pokemon = enemy_pokemon

    return next_player, target_pokemon

def loot(player_profile):
    if player_profile['loot_chance'] == True:
        loot_chance = random.randint(1, 4)
        if loot_chance == 1:
            print('Lo siento, no hay recompensas esta vez')
        elif loot_chance == 2:
            player_profile['poke-balls'] += 1
            print('Ganaste una pokebola!')
        elif loot_chance == 3:
            player_profile['health_potion'] += 1
            print('Ganaste una pocion de curacion!')
    player_profile['loot_chance'] = False
    return player_profile
