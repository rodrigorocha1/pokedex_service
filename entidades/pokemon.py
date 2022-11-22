from enuns.pokeenuns import Cor
from typing import Dict, List


class Pokemom:
    def __init__(self, **kwargs):
        self._id = kwargs['id']
        self._name = kwargs['name']
        self._tipos = [tipos['type']['name'] for tipos in kwargs.get('types')]
        self._cor = ''.join([cor.value for cor in Cor if self._tipos[0] in cor.name])
        self._habilidade = [habilidades['ability']['name'] for habilidades in kwargs['abilities']]
        self._img = kwargs['sprites']['other']['official-artwork']['front_default']
        self._estatisicas = [
            {
                'nome': kwargs['stats'][chave]['stat']['name'],
                'valor': kwargs['stats'][chave]['base_stat']
            } for chave, _ in enumerate(kwargs['stats'])
        ]

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> int:
        return self._id

    @property
    def tipos(self) -> List[str]:
        return self._tipos

    @property
    def img(self) -> str:
        return self._img

    @property
    def cor(self) -> str:
        return self._cor

    @property
    def habilidade(self) -> List[str]:
        return self._habilidade

    @property
    def estatisticas(self) -> Dict[str, List[int]]:
        return self._estatisicas


if __name__ == '__main__':
    from service.pokeservice import PokeAPI

    c = PokeAPI()
    pokemon = c.obter_dados_pokemon_id(1)
    print(pokemon.__dict__)
    print(pokemon.__module__)
