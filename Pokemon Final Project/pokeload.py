import pickle
import copy
from requests_html import HTMLSession

pokemon_base = {
    'name': '',
    'type': [],
    'attacks': [],
    'current_health': 100,
    'base_health': 100,
    'level': 1,
    'current_xp': 0
}

URL_BASE = "https://pokemondb.net/pokedex/"



def get_pokemon(index):
    url = '{}{}'.format(URL_BASE, index)
    session = HTMLSession()
    pokemon_page = session.get(url)
    new_pokemon = copy.deepcopy(pokemon_base)
    #nombre
    new_pokemon['name'] = pokemon_page.html.find("main h1",first=True).text
    #tipo
    rows = pokemon_page.html.find("table.vitals-table tr")
    for row in rows:
        if row.find("th", first=True).text == "Type":
            new_pokemon ['type'] = [a.text for a in row.find("a")]

    #ataques
    pokemon_page = session.get(url + '/moves/1')
    table = pokemon_page.html.find("table.data-table", first=True)
    rows = table.find("tbody tr")

    for row in rows:
        cells = row.find('td')
        lvl_min = int(cells[0].text)
        name = cells[1].find('a.ent-name',first=True).text
        move_type = cells[2].find('a.type-icon',first=True).text
        power_txt = cells[4].text
        if power_txt == '—':
            power = None
        else: power =  int(power_txt)

        attack = {
            'att_name': name,
            'lvl_min': lvl_min,
            'move_type': move_type,
            'power': power
        }
        if power:
            new_pokemon['attacks'].append(attack)

    return new_pokemon

def get_all_pokemons():
    try:
        print('Cargando el archivo...')
        with open('pokefile.pkl', "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)
    except FileNotFoundError:
        print('Archivo no encontrado. Se creara un nuevo archivo...')
        all_pokemons = []
        for index in range(151):
            all_pokemons.append(get_pokemon(index+1))
            print('*', end='')


        with open('pokefile.pkl',"wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)
        print('\nTodos los pokemons han sido descargados!')
    print('Lista de pokemons cargada')
    return all_pokemons


















