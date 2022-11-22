from enuns.pokeenuns import Cor


class Pokemom:
    def __init__(self, **kwargs):
        self._name = kwargs['name']
        self._id = kwargs['id']
        self._tipos = [tipos['type']['name'] for tipos in kwargs.get('types')]
        self._cor = ''.join(
            [cor.value for cor in Cor
             if [tipos['type']['name']
                 for tipos in kwargs.get('types')][0] in cor.name])
        self._habilidade = [habilidades['ability']['name'] for habilidades in kwargs['abilities']]
        self._estatisicas = [
            {
                'nome': kwargs['stats'][chave]['stat']['name'],
                'valor': kwargs['stats'][chave]['base_stat']
            } for chave, _ in enumerate(kwargs['stats'])
        ]

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def tipos(self):
        return self._tipos

    @property
    def cor(self):
        return self._cor

    @property
    def habilidade(self):
        return self._habilidade

    @property
    def estatisticas(self):
        return self._estatisicas
