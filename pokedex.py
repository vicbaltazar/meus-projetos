from pymongo import MongoClient

#conectar conector local
client = MongoClient("mongodb://localhost:27017/")
db = client["pokedex"]
pokemons = db["pokemons"]

#inserir pokemons
mimikyu = {
    "_id": 778,
    "nome": "Mimikyu",
    "tipos": ["Fantasma", "Fada"],
    "status_base": {"hp": 55, "ataque": 90},
    "fraquezas": ["Aço"]
}

phantump = {
    "_id": 708,
    "nome": "Phantump",
    "tipos": ["Fantasma", "Planta"],
    "status_base": {"hp": 43, "ataque": 70},
    "fraquezas": ["Fogo", "Fantasma", "Sombrio"]
}

gothitelle = {
    "_id": 576,
    "nome": "Gothitelle",
    "tipos": ["Psíquico"],
    "status_base": {"hp": 70, "ataque": 55},
    "fraquezas": ["Inseto", "Fantasma", "Sombrio"]
}

pokemons.delete_many({})

pokemons.insert_many([mimikyu, phantump, gothitelle])

#buscar por tipo
print("Pokémons do tipo Fantasma:")
for p in pokemons.find({"tipos": "Fantasma"}):
    print(f"- {p['nome']}")

#adicionar campo de regiao em cada
pokemons.update_one({"_id": 778}, {"$set": {"regiao": "Alola"}})
pokemons.update_one({"_id": 708}, {"$set": {"regiao": "Kalos"}})
pokemons.update_one({"_id": 576}, {"$set": {"regiao": "Unova"}})

#deletar: exemplo gothitelle
resultado = pokemons.delete_one({"_id": 576})
print(f"Documentos removidos: {resultado.deleted_count}")