from enuns.pokeenuns import Cor


class Pokemom:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.id = kwargs['id']
        self.tipos = [tipos['type']['name'] for tipos in kwargs.get('types')]
        self.cor = ''.join(
            [cor.value for cor in Cor
             if [tipos['type']['name']
                 for tipos in kwargs.get('types')][0] in cor.name])
        self.habilidade = [habilidades['ability']['name'] for habilidades in kwargs['abilities']]
        self.estatisicas = [
            {
                'nome': j['stats'][chave]['stat']['name'],
                'valor': j['stats'][chave]['base_stat']
            } for chave, _ in enumerate(kwargs['stats'])
        ]

    def __str__(self):
        stc = self.img, self.tipos, self.nome, self.id
        return str(stc)
