#pokemons
class Pokemon:
    def __init__(self, type, abilities):
        self.type = type
        self.abilities = abilities

pikachu_one = Pokemon("type", "abilities")
pikachu_one.type = "Type: Electric"
pikachu_one.abilities = "Abilities: Static, Lightning Rod"

charmander = Pokemon("type", "abilities")
charmander.type = "Type: Fire"
charmander.abilities = "Abilities: Blaze"

bulbasaur = Pokemon("type", "abilities")
bulbasaur.type = "Type: Electric"
bulbasaur.abilities = "Abilities: Static, Lightning Rod"

pokemons = ['Pikachu.1', 'Pikachu.2', 'Charmander', 'Bulbasaur', 'Squirtle.1', 'Squirtle.2', 'Charizard', 'Shidinja', 'Zacian']
pokemons.sort()
print (pokemons)
