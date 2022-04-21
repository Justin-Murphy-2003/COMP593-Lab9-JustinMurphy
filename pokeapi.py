import requests

def get_pokemon_info(name):
    """
    Gets dictionary of info from PokeAPI for specified pokemon.

    :param name: Specified Pokemon's Name or index number
    """

    print("Getting Pokemon information...", end="")

    if name is None:
        return

    name = name.lower().strip()

    if name == '':
        return

    URL = 'https://pokeapi.co/api/v2/pokemon/'+str(name)
    response = requests.get(URL)

    if response.status_code == 200:
        print("success!")
        return response.json()
    else:
        print("failed. Response code",response.status_code)
        return
