from service.pokeservice import PokeAPI

c = PokeAPI()
for i in range(900):
    pokemon = c.obter_dados_pokemon_id(i + 1)

    print(pokemon.name)
    print(pokemon.img)
    print(pokemon.id)
    print(pokemon.tipos)
    print(pokemon.cor)
    print(pokemon.estatisticas)
    print(pokemon.habilidade)
    print('=' * 10)
