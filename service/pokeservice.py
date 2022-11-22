import requests
from requests import exceptions as ex
from entidades.pokemon import Pokemom


class PokeAPI:
    def __init__(self):
        self.__base_url = 'https://pokeapi.co/api/'

    def obter_dados_pokemon_id(self, id_pokemon: int) -> Pokemom:
        """
        Faz a chamada da api e retorna em um objeto
        :param id_pokemon: id do pokemon int
        :return: objeto do tipo pokemon
        """
        url = f'{self.__base_url}v2/pokemon/{id_pokemon}/'
        try:
            req = requests.get(url)

            pokemon = Pokemom(**req.json())

        except ex.HTTPError as errh:
            raise errh
        except ex.ConnectionError as errc:
            raise errc
        except ex.Timeout as errt:
            raise errt
        except ex.RequestException as err:
            raise err
        except Exception as e:
            raise e
        return pokemon
