from service.pokeservice import PokeAPI

c = PokeAPI()
pokemon = c.obter_dados_pokemon_id(904)

print(pokemon.name)
print(pokemon.img)
print(pokemon.id)
print(pokemon.tipos)
print(pokemon.cor)
print(pokemon.estatisticas)
print(pokemon.habilidade)
