import requests
from requests import exceptions as ex
from entidades.pokemon import Pokemom
from typing import Type


class PokeAPI:
    def __init__(self):
        self.__base_url = 'https://pokeapi.co/api/'

    def obter_dados_pokemon_id(self, id_pokemon: int) -> Type[Pokemom]:
        """
        Faz a chamada da api e retorna em um objeto
        :param id_pokemon: id do pokemon int
        :return: objeto do tipo pokemon
        """
        url = f'{self.__base_url}/v2/pokemon/{id_pokemon}/'
        try:
            req = requests.get(url)

            pokemon = Pokemom(**req.json())
            return pokemon
        except ex.HTTPError as errh:
            print("Http Error:", errh)
        except ex.ConnectionError as errc:
            print("Error Connecting:", errc)
        except ex.Timeout as errt:
            print("Timeout Error:", errt)
        except ex.RequestException as err:
            print("OOps: Something Else", err)
        except Exception as e:
            print(e)





