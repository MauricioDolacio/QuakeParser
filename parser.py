import json

#le o arquivo e fds
with open("Quake.txt", "r") as arquivo:
    quake_lines = arquivo.readlines()

game = 0
total_kills = 0
players = []

for line in quake_lines:
    line = line.strip()
    line = line.split(" ", 3)

    #ClientUserinfoChanged
    if line[1] == "ClientUserinfoChanged:":
        line[3] = line[3].split("\\")

        #verificar se o id do jogador ja foi registrado
        result = 0
        for i in range(0, len(players)):
            if players[i]['id'] == int(line[2]) - 1:
                if players[i]['nome'] == line[3][1]: #jogador ja esta listado e não alterou o nome
                    result = -1
                    break
                else: #jogador alterou o nome
                    pos = i
                    result = 1
                    break
        
        #troca o nome do jogador
        if result == 1:
            #verifica se o nome atual do jogador esta registrado na lista de nomes antigos
            v = 0
            for name in players[pos]['old_names']:
                if line[3][1] == name:
                    players[pos]['old_names'].remove(name)
                    v = 1
                    break
            if v == 0:
                players[pos]['old_names'].append(players[pos]['nome'])
            players[pos]['nome'] = line[3][1]
        #adiciona o jogador na lista de players
        elif result == 0:
            player = {
                "id": int(line[2]) - 1,
                "nome": line[3][1],
                "kills": 0,
                "old_names": []
            }
            players.append(player)
    
    #Kill
    if line[1] == "Kill:":
        total_kills += 1
        
    
    #Shutdown
    elif line[1] == "ShutdownGame:":
        game += 1
        print(game)
        print(players)
        print(total_kills)
        total_kills = 0
        players = []

#deve retornar isso
#[{"game": 1,
#  "status": { "total_kills": 45, "players": [{ "id": 1, "nome": "Mocinha", "kills": 5, "old_names": ["Dono da bola"] }, 
#                                             { "id": 2, "nome": "Isgalamido","kills": 18, "old_names": [] }, 
#                                             { "id": 3, "nome": "Zeh", "kills": 20, "old_names": [] } ] } 
#  }
#]
