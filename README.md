# QuakeParser
Um Parser para o jogo Quake 3, que lê o arquivo de log (.txt), agrupa os dados de cada partida e organiza as informações em um .json

<h2>Funcionamento do Main</h2>
<p>O programa separa o arquivo .txt linha por linha e as transforma em listas. O arquivo então analisa as linhas e busca alterações na partida e de acordo com as alterações, cria e modifica um dicionario que contem as informações da partida.</p>
<p>O programa então agrupa os dicionarios das partidas em uma grande lista de partidas e finaliza o inserindo em um .json</p>
<p>Listas e Variaveis do programa:</p>
<ul>
<li><b>players (list):</b> Armazena os jogadores da partida. A lista é reiniciada a cada jogo</li>
<li><b>game_count (int):</b> Contabiliza o numero de partidas</li>
<li><b>total_kills (int):</b> Contabiliza o numero de mortes da partida. É reiniciado a cada jogo</li>
<li><b>game_list (list):</b> Contém todas as partidas jogadas. É inserida no .json no final do programa</li>
</ul>
<p>Analisando as linhas, o programa executa tarefas especificas de acordo com o que o log diz:</p>
<ul>
  <li><b>ClientConnect:</b> Adiciona um dicionario do jogador junto com seu id</li>
  <li><b>ClientDisconnect:</b> Remove o dicionario do jogador mencionado</li>
  <li><b>ClientUserinfoChanged:</b> Altera o nome do jogador caso haja necessidade</li>
  <li><b>Kill:</b> Adiciona uma kill global para a partida e altera os valores de kill dos jogadores de acordo com as informações da linha</li>
  <li><b>ShutdownGame:</b> Finaliza um jogo, armazenando as informações da partida em um dicionario e o adiciona na lista de partidas. Logo em seguida reinicia as variaveis, pronto para um novo jogo.</li>
</ul>

<h2>Funções criadas</h2>

<h3>addPlayer(id)</h3>
<p>Cria um dicionario para o jogador e o adiciona na lista de jogadores
</br>A função adiciona o id como um item no dicionario</p>
<ul>
  <li><b>id (int):</b> id do jogador</li>
</ul>
<h3>findPlayer(id)</h3>
<p>Retorna a posição de um jogador na lista de jogadores após busca-lo de acordo com o id.
</br>Caso a função não encontre o jogador ela retorna -1</p>
<ul>
  <li><b>id (int):</b> id do jogador</li>
</ul>
<h3>changeName(pos, new_name)</h3>
<p>Altera o nome de um jogador e atualiza a lista de nomes antigos.
</br>A função verifica se o novo nome esta na lista dos nomes antigos e o remove caso esteja. Caso contrario, a função adiciona o nome na lista de nomes antigos.
</br>Logo em seguida, ela altera o nome atual pelo novo.</p>
<ul>
  <li><b>pos (int):</b> posição do jogador na lista de jogadores</li>
  <li><b>new_name (string):</b> novo nome do jogador</li>
</ul>
<h3>killCount(killer_id, killed_id)</h3>
<p>Adiciona uma kill para o jogador que eliminou
</br>Remove uma kill do jogador que morreu, caso o mesmo tenha morrido para o "mundo"</p>
<ul>
  <li><b>killer_id (int):</b> id do jogador que matou</li>
  <li><b>killed_id (int):</b> id do jogador que morreu</li>
</ul>
<h3>finish(game_count, total_kills, game_list)</h3>
<p>Insere os valores e informações da partida em uma camada de dicionarios e adiciona o dicionario da partida na lista de partidas.
<ul>
  <li><b>game_count (int):</b> Valor do jogo atual</li>
  <li><b>total_kills (int):</b> Valor total de mortes que ocorreram no jogo</li>
  <li><b>game_list (list):</b> Contém todas as partidas jogadas.</li>
</ul>
