import requests

def get_pokemon_info(name):
    """
    Gets dictionary of info from PokeAPI for specified pokemon.

    :param name: Specified Pokemon's Name or index number
    :returns: Dictionary of pokemon info if success, None if unsuccessful
    """

    print("Getting Pokemon information...", end="")

    if name is None:
        print('error: Missing name parameter')
        return

    name = name.lower().strip()

    if name == '':
        print('error: Empty name parameter')
        return

    URL = 'https://pokeapi.co/api/v2/pokemon/'+str(name)
    response = requests.get(URL)

    if response.status_code == 200:
        print("success!")
        return response.json()
    else:
        print("failed. Response code",response.status_code)
        return

def get_pokemon_list(limit=2000, offset=0):
    """
    Gets list of pokemon from PokeAPI
    """
    print('Getting list of Pokemon...')

    URL = 'https://pokeapi.co/api/v2/pokemon/'
    parameters = {
        'offset' : offset,
        'limit' : limit
    }
    
    response = requests.get(URL,  params=parameters)

    if response.status_code == 200:
        print("success!")
        poke_dict = response.json()
        return [p['name'] for p in poke_dict['results']] #return names of allpokemon in list
    else:
        print("failed. Response code",response.status_code)
        return

def get_pokemon_image_url(name):
    poke_dict = get_pokemon_info(name)
    poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
    return poke_url