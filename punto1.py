# Estructura de datos para almacenar los Pokémon 
pokemon_data = {
  "nombre": {},
  "numero": {},
  "tipo": {}
}

# Lista de Pokémon
pokemon_list = [
  {"nombre": "Pikachu", "numero": 25, "tipo": ["Eléctrico"]},
  {"nombre": "Charizard", "numero": 6, "tipo": ["Fuego", "Volador"]},
  {"nombre": "Bulbasaur", "numero": 1, "tipo": ["Planta", "Veneno"]},
  {"nombre": "Squirtle", "numero": 7, "tipo": ["Agua"]},
  {"nombre": "Psyduck", "numero": 54, "tipo": ["Agua", "Psíquico"]},
  {"nombre": "Snorlax", "numero": 143, "tipo": ["Normal"]},
  {"nombre": "Gengar", "numero": 94, "tipo": ["Fantasma", "Veneno"]},
  {"nombre": "Dragonite", "numero": 149, "tipo": ["Dragón", "Volador"]},
]

# Llenar los árboles con los datos de los Pokémon
for pokemon in pokemon_list:

  # Por nombre
  nombre = pokemon["nombre"]
  pokemon_data["nombre"][nombre] = pokemon

  # Por número
  numero = pokemon["numero"]
  pokemon_data["numero"][numero] = pokemon

  # Por tipo
  tipos = pokemon["tipo"]
  for tipo in tipos:
    if tipo not in pokemon_data["tipo"]:
      pokemon_data["tipo"][tipo] = []
    pokemon_data["tipo"][tipo].append(pokemon)

# Resto del código...

# Modificar algunos tipos
pokemon_data["tipo"]["Fuego"].remove(pokemon_data["nombre"]["Charizard"]) 
pokemon_data["tipo"]["Fuego"].append(pokemon_data["nombre"]["Psyduck"])
pokemon_data["tipo"]["Agua"].remove(pokemon_data["nombre"]["Psyduck"])
pokemon_data["tipo"]["Agua"].append(pokemon_data["nombre"]["Charizard"])

# Mostrar nuevos tipos
print(pokemon_data["tipo"]["Fuego"]) 
print(pokemon_data["tipo"]["Agua"])