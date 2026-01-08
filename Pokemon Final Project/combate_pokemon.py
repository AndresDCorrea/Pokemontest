import random
from pokeload import get_all_pokemons
from fight_functions import (effectiveness, machine_pokemon_choose, available_attacks, player_attack,
                             effectiveness_msg, attack_result, get_player_profile,
                             any_player_pokemon_lives, switch_turns, loot, player_action)






def fight(player_profile, enemy_pokemon, pokemon_list):
    global target_pokemon

    #Turno del jugador:
    action = None
    catch = False
    currently_playing = None
    player_pokemon = None
    if not enemy_pokemon:
        enemy_pokemon = machine_pokemon_choose(pokemon_list)
    target_pokemon = enemy_pokemon
    while not action:
        action = player_action(player_profile, enemy_pokemon,catch)
        if isinstance(action, dict):
            player_pokemon = action


        if player_pokemon:
            while player_pokemon['current_health'] > 0:

                if enemy_pokemon['current_health'] != enemy_pokemon['base_health']:
                    choice = input('Quieres intentar capturar este pokemon? Y/N: ').lower()
                    if choice == 'y':
                        break

                currently_playing, target_pokemon = switch_turns(currently_playing, player_pokemon, enemy_pokemon)
                print('Es el turno de {}'.format(currently_playing['name']))
                attacks = available_attacks(currently_playing)
                chosen_attack = player_attack(attacks)

                #resultado ataque:
                attack_result(chosen_attack, target_pokemon)
                input()

                #check avance de ronda
                if target_pokemon == enemy_pokemon and enemy_pokemon['current_health'] <= 0 or catch:
                    enemy_pokemon['current_health'] = 0
                    player_profile['combats'] += 1
                    player_profile['loot_chance'] = True

                    player_pokemon['current_xp'] += player_pokemon['level'] * 50
                    print('Derrotaste a {}. Avanzaste una ronda!\n'
                          'Ganaste {} XP'.format(enemy_pokemon['name'], player_pokemon['current_xp']))

                    if player_pokemon['current_xp'] == player_pokemon['level'] * 100:
                        player_pokemon['level'] += 1
                        print('Subiste de nivel. Tu nivel actual es: {}'. format(player_pokemon['level']))
                        player_pokemon['current_xp'] = 0
                        player_pokemon['current_health'] = 100
                        print('Al subir de nivel, recuperaste toda tu vida')

                    loot(player_profile)
                    return None

                #Turno de la máquina
                currently_playing, target_pokemon = switch_turns(currently_playing,player_pokemon, enemy_pokemon)
                print('Es el turno de {}'.format((currently_playing['name'])))
                attacks = available_attacks(currently_playing)

                #Try para que no crashee cuando no hay ataques
                try:
                    chosen_attack = random.choice(attacks)
                    print('{} eligio {}'.format(currently_playing['name'], chosen_attack['att_name']))

                    # resultado ataque:
                    multiplier = effectiveness(chosen_attack['move_type'], player_pokemon['type'])
                    print(effectiveness_msg(multiplier))
                    attack_dmg = chosen_attack['power'] * multiplier
                    target_pokemon['current_health'] -= attack_dmg
                    print('El ataque hizo {} de daño'.format(attack_dmg))
                    print('La vida de {} es de: {}'.format(target_pokemon['name'], target_pokemon['current_health']))
                    input()

                except IndexError:
                    print('No hay ataques disponibles')
            return enemy_pokemon



#Main loop:
def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    enemy_pokemon = None
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = fight(player_profile, enemy_pokemon, pokemon_list)
    print('Has perdido en el combate N°: {}'.format(player_profile['combats']))



if __name__ == '__main__':
    main()
