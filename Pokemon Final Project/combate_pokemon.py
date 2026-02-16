import os
import random
from pokeload import get_all_pokemons
from fight_functions import (effectiveness, machine_pokemon_choose, available_attacks, player_attack,
                             effectiveness_msg, attack_result, get_player_profile,
                             any_player_pokemon_lives, switch_turns, loot, player_action, end_round,
                             show_combat_status)






def fight(player_profile, enemy_pokemon, pokemon_list):
    os.system('cls')

    if not enemy_pokemon:
        enemy_pokemon = machine_pokemon_choose(pokemon_list)

    player_pokemon = None
    currently_playing = None

    while True:

        show_combat_status(player_pokemon, enemy_pokemon, player_profile)

        # ───────── TURNO DEL JUGADOR ─────────
        action = player_action(player_profile, enemy_pokemon)

        # Elegir Pokémon para pelear
        if isinstance(action, dict):
            player_pokemon = action

        # Curar (consume turno)
        elif action is None:
            pass

        # Intentar capturar
        elif isinstance(action, tuple):

            caught, enemy_pokemon = action
            if caught:
                end_round(player_profile,pokemon_list,player_pokemon,enemy_pokemon)
                loot(player_profile)
                return None

        # ───────── ATAQUE DEL JUGADOR ─────────
        if player_pokemon:


            currently_playing, target_pokemon = switch_turns(
                currently_playing,
                player_pokemon,
                enemy_pokemon
            )

            print(f"Es el turno de {currently_playing['name']}")
            attacks = available_attacks(currently_playing)
            chosen_attack = player_attack(attacks)

            attack_result(chosen_attack, target_pokemon)
            input()

            # Enemigo derrotado
            if enemy_pokemon['current_health'] <= 0:
                enemy_pokemon['current_health'] = 0
                end_round(player_profile, pokemon_list, player_pokemon, enemy_pokemon)
                loot(player_profile)
                return None   # combate terminado

        # ───────── TURNO DE LA MÁQUINA ─────────
        if player_pokemon is None:
            continue
        currently_playing, target_pokemon = switch_turns(
            currently_playing,
            player_pokemon,
            enemy_pokemon
        )

        print(f"Es el turno de {currently_playing['name']}")
        attacks = available_attacks(currently_playing)

        try:
            chosen_attack = random.choice(attacks)
            print(f"{currently_playing['name']} eligió {chosen_attack['att_name']}")

            multiplier = effectiveness(chosen_attack['move_type'], player_pokemon['type'])
            print(effectiveness_msg(multiplier))

            attack_dmg = chosen_attack['power'] * multiplier
            player_pokemon['current_health'] -= attack_dmg

            print(f"El ataque hizo {attack_dmg} de daño")
            print(f"La vida de {player_pokemon['name']} es {player_pokemon['current_health']}")


        except IndexError:
            print("No hay ataques disponibles")

        # ───────── Pokémon del jugador derrotado ─────────
        if player_pokemon['current_health'] <= 0:
            player_pokemon['current_health'] = 0
            print(f"{player_pokemon['name']} fue derrotado")
            player_pokemon = None

        input('Presione cualquier tecla para continuar...')




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
