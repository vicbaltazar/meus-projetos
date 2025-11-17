import json

musicas_selvagens = [
    ["Massarrara",  "Selvagens à Procura de Lei",  "Rock Nacional"], #1
    ["Despedida",  "Selvagens à Procura de Lei", "Rock Nacional"], #2
    ["Mar Fechado",  "Selvagens à Procura de Lei", "Rock Nacional"], #3
    ["Casona", "Selvagens à Procura de Lei", "Rock Nacional"], #4
    ["Juventude Solitude", "Selvagens à Procura de Lei", "Rock Nacional"], #5
    ["Tarde Livre", "Selvagens à Procura de Lei", "Rock Nacional"], #6
    ["Gostar Só Dela", "Selvagens à Procura de Lei", "Rock Nacional"], #7
    ["Sede ao Pote", "Selvagens à Procura de Lei", "Rock Nacional"], #8
    ["Mucambo Cafundó", "Selvagens à Procura de Lei", "Rock Nacional"], #9
    ["Semana Passada", "Selvagens à Procura de Lei", "Rock Nacional"] #10
]

#salvando arquivo json
with open ("musicas_selvagens.json", "w", encoding="utf-8") as f:
    json.dump(musicas_selvagens, f, ensure_ascii=False, indent=4)

#lendo json para lista python
with open("musicas_selvagens.json", "r", encoding="utf-8") as f:
    musicas_carregadas = json.load(f)

#exibindo
for musica in musicas_carregadas:
    print(musica)