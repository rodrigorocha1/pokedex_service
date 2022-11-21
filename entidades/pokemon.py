

class Pokemom:
    def __init__(self, **kwargs):
        for chave, valor in kwargs.items():
            if type(valor) is dict:
                self.img = valor['official-artwork']['front_default']
            if type(valor) is list:
                self.tipos = [tipos['type']['name'] for tipos in valor]
            else:
                self.nome = kwargs['name']
                self.id = kwargs['id']

    def __str__(self):
        stc = self.img, self.tipos, self.nome, self.id
        return str(stc)
