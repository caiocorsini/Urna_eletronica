'''----------------------------------------------------------------------'''
'''--------------------------- Variáveis --------------------------------'''
'''----------------------------------------------------------------------'''

# Define várias listas. três listas para cada cargo correspondendo a informações específicas digitadas pelo usuário
# As listas terão indexes "correspodentes", isso é, um index específico para cada candidato
# Por exemplo, o index 1 da lista de números e o index 1 da lista de partido serão todos referentes ao candidato de index 1 na lista de nomes e assim por diante
# São variáveis globais pois serão trabalhadas em todas as funções

# Variáveis de candidatos separados para prefeito, governador e presidente
nomes_prefeito = []
numeros_prefeito = []
partidos_prefeito = []
votos_prefeito = []
votos_brancos_prefeito = 0
votos_nulos_prefeito = 0


nomes_governador = []
numeros_governador = []
partidos_governador = []
votos_governador = []
votos_brancos_governador = 0
votos_nulos_governador = 0

nomes_presidente = []
numeros_presidente = []
partidos_presidente = []
votos_presidente = []
votos_brancos_presidente = 0
votos_nulos_presidente = 0

#Variáveis de eleitores
nomes_eleitores = []
CPFs_eleitores = []
ja_votou = []
prefeitos_escolhidos = []
governadores_escolhidos = []
presidentes_escolhidos = []


'''---------------------------------------------------------------------'''
'''------------------------ Outras funções -----------------------------'''
'''---------------------------------------------------------------------'''

# Função referente à opção 1. Usada para cadastrar candidatos e suas informações
def cad_candidato():
  print("+++ CADASTRAR CANDIDATOS +++")
  print("")

  repetir = True
  while repetir == True:
    # Inputs do usuário. Repete até ele falar que não quer mais.
    nome_candidato = input("Qual o nome do candidato: ")
    numero_candidato = input("Qual é o número do candidato: ")
    partido_candidato = input("Qual é o partido do candidato: ")
    cargo = input("Qual é o cargo do candidato? Prefeito, governador ou presidente. Digite tudo minúsculo: ")

    # Pequena verificação para ver se o cargo foi digitado corretamente
    while cargo != "prefeito" and cargo != "governador" and cargo != "presidente":
      print("String digitada inválida!!! Lembre-se que você deve digitar tudo em minúsculo! Digite novamente.")
      cargo = input("Qual é o cargo do candidato? Prefeito, governador ou presidente. Digite tudo minúsculo: ")

    # Todas as informações passadas pelo usuário são enviadas para as listas dependendo do cargo
    if cargo == "prefeito":
      nomes_prefeito.append(nome_candidato)
      numeros_prefeito.append(numero_candidato)
      partidos_prefeito.append(partido_candidato)
      votos_prefeito.append(0)
    elif cargo == "governador":
      nomes_governador.append(nome_candidato)
      numeros_governador.append(numero_candidato)
      partidos_governador.append(partido_candidato)
      votos_governador.append(0)
    elif cargo == "presidente":
      nomes_presidente.append(nome_candidato)
      numeros_presidente.append(numero_candidato)
      partidos_presidente.append(partido_candidato)
      votos_presidente.append(0)

    # Verifica se o usuário quer cadastrar ainda mais candidatos.
    print("")
    opcao = input("Deseja inserir mais um candidato. 'SIM' para sim e 'NÃO' para não: ")
    print("")
    if opcao == "NÃO":
      repetir = False

      

def cad_eleitor():
    print("+++ CADASTRAR ELEITORES +++")
    print("")

    # Loop até o usuário decidir que não quer mais adicionar eleitores
    repetir = True
    while repetir == True:
        nome_eleitor = input("Qual o nome do eleitor: ")
        CPF_eleitor = input("Qual o CPF do eleitor (apenas números): ")
        print("")
        nomes_eleitores.append(nome_eleitor)
        CPFs_eleitores.append(CPF_eleitor)
        prefeitos_escolhidos.append(".")
        governadores_escolhidos.append(".")
        presidentes_escolhidos.append(".")
        
        opcao = input("Deseja inserir mais um eleitor. 'SIM' para sim e 'NÃO' para não: ")
        print("")
        if opcao == "NÃO":
            repetir = False





def votar():

    #Já que as seguintes variáveis não são listas, é necessário usar global para serem usadas dentro desta função
    global votos_brancos_prefeito
    global votos_nulos_prefeito

    global votos_brancos_governador
    global votos_nulos_governador

    global votos_brancos_presidente
    global votos_nulos_presidente
    
    print("+++ VOTAR +++")
    print("")
    
    qual_eleitor = input("Eleitor, digite o seu CPF: ")

    # Verifica qual dos eleitores da lista de eleitores vai votar no momento
    for i in range(len(CPFs_eleitores)):
      if qual_eleitor == CPFs_eleitores[i]:
          
        print("")
        print("---- Voto para prefeito ----")
        print("")

        print("Caro(a)", nomes_eleitores[i], " em qual prefeito deseja votar? ")

        voto_pref = input("Digite o número dele: ")

        # Procura na lista de números prefeitos, qual prefeito o eleitor quer
        # No caso de -1 ou -2 é selecionado voto branco e nulo respectivamente
        if voto_pref == "-1":
          quer_branco_pref = input("Você deseja votar branco para prefeito? 's' para sim. Outras letras para não: ")
          if quer_branco_pref == "s":
            print("Voto confirmado!")
            prefeitos_escolhidos[i] = "branco"
            votos_brancos_prefeito += 1
          else:
            print("Voto cancelado!")
              
        elif voto_pref == "-2":
          quer_nulo_pref = input("Você deseja votar nulo para prefeito? 's' para sim. Outras letras para não: ")
          if quer_nulo_pref == "s":
            print("Voto confirmado!")
            prefeitos_escolhidos[i] = "nulo"
            votos_nulos_prefeito += 1
          else:
            print("Voto cancelado!")

        else:
          for w in range(len(numeros_prefeito)):
            if voto_pref == numeros_prefeito[w]:
              print("Você deseja votar em", nomes_prefeito[w], "do partido", partidos_prefeito[w], "?")
              quer = input("'s' para sim ou qualquer outra letra para não: ")
              if quer == "s":
                print("Voto confirmado!")
                votos_prefeito[w] += 1
                prefeitos_escolhidos[i] = nomes_prefeito[w]
              else:
                print("Voto cancelado!")
                continue


              # Mesma lógica aplicada para prefeitos é usada para os cargos de governador e presidente
        print("")
        print("---- Voto para governador ----")
        print("")

        print("Caro(a)", nomes_eleitores[i], " em qual governador deseja votar? ")

        voto_gov = input("Digite o número dele: ")

        if voto_gov == "-1":
          quer_branco_gov = input("Você deseja votar branco para governador? 's' para sim. Outras letras para não: ")
          if quer_branco_gov == "s":
            print("Voto confirmado!")
            governadores_escolhidos[i] = "branco"
            votos_brancos_governador += 1
          else:
            print("Voto cancelado!")
              
        elif voto_gov == "-2":
          quer_nulo_gov = input("Você deseja votar nulo para governador? 's' para sim. Outras letras para não: ")
          if quer_nulo_gov == "s":
            print("Voto confirmado!")
            governadores_escolhidos[i] = "nulo"
            votos_nulos_governador += 1
          else:
            print("Voto cancelado!")

        else:
          for w in range(len(numeros_governador)):
            if voto_gov == numeros_governador[w]:
              print("Você deseja votar em", nomes_governador[w], "do partido", partidos_governador[w], "?")
              quer = input("'s' para sim ou qualquer outra letra para não: ")
              if quer == "s":
                print("Voto confirmado!")
                votos_governador[w] += 1
                governadores_escolhidos[i] = nomes_governador[w]
              else:
                print("Voto cancelado!")
                continue



              
        print("")
        print("---- Voto para presidente ----")
        print("")

        print("Caro(a)", nomes_eleitores[i], " em qual presidente deseja votar? ")

        voto_presi = input("Digite o número dele: ")

        if voto_presi == "-1":
          quer_branco_presi = input("Você deseja votar branco para presidente? 's' para sim. Outras letras para não: ")
          if quer_branco_presi == "s":
            print("Voto confirmado!")
            presidentes_escolhidos[i] = "branco"
            votos_brancos_presidente += 1
          else:
            print("Voto cancelado!")
              
        elif voto_presi == "-2":
          quer_nulo_presi = input("Você deseja votar nulo para presidente? 's' para sim. Outras letras para não: ")
          if quer_nulo_presi == "s":
            print("Voto confirmado!")
            presidentes_escolhidos[i] = "nulo"
            votos_nulos_presidente += 1
          else:
            print("Voto cancelado!")

        else:
          for w in range(len(numeros_presidente)):
            if voto_presi == numeros_presidente[w]:
              print("Você deseja votar em", nomes_presidente[w], "do partido", partidos_presidente[w], "?")
              quer = input("'s' para sim ou qualquer outra letra para não: ")
              if quer == "s":
                print("Voto confirmado!")
                votos_presidente[w] += 1
                presidentes_escolhidos[i] = nomes_presidente[w]
              else:
                print("Voto cancelado!")
                continue       




def apurar():
    print("+++ APURAR RESULTADOS +++")
    print("")

    # Como as variáveis a seguir não são listas, é necessário usar global para usá-las nesta função
    global votos_brancos_prefeito
    global votos_nulos_prefeito

    global votos_brancos_governador
    global votos_nulos_governador

    global votos_brancos_presidente
    global votos_nulos_presidente

    presidentes_nomes_decrescente = []
    presidentes_partidos_decrescente = []
    presidentes_votos_decrescente = []

    governadores_nomes_decrescente = []
    governadores_partidos_decrescente = []
    governadores_votos_decrescente = []

    prefeitos_nomes_decrescente = []
    prefeitos_partidos_decrescente = []
    prefeitos_votos_decrescente = []

    index_atual = 0
    mais_votado_atual = 0

    

    # Listas são 'clonadas', para preservar as listas originais
    # Clonadas com um loop de for. Apenas igualar seria uma passagem por referência

    nomes_prefeito_clone = []
    votos_prefeito_clone = []
    partidos_prefeito_clone = []
    for i in nomes_prefeito:
      nomes_prefeito_clone.append(i)
    for i in votos_prefeito:
      votos_prefeito_clone.append(i)
    for i in partidos_prefeito:
      partidos_prefeito_clone.append(i)

    nomes_governador_clone = []
    votos_governador_clone = []
    partidos_governador_clone = []
    for i in nomes_governador:
      nomes_governador_clone.append(i)
    for i in votos_governador:
      votos_governador_clone.append(i)
    for i in partidos_governador:
      partidos_governador_clone.append(i)

    nomes_presidente_clone = []
    votos_presidente_clone = []
    partidos_presidente_clone = []
    for i in nomes_presidente:
      nomes_presidente_clone.append(i)
    for i in votos_presidente:
      votos_presidente_clone.append(i)
    for i in partidos_presidente:
      partidos_presidente_clone.append(i)


    # Organizando os dados de forma decrescente, respeitando os indexes
    # As listas de nomes, votos e partidos serão organizadas de forma a respeitar o alinhamento de seus indexes

    # Organizando prefeitos em ordem decrescente
    for i in range(len(votos_prefeito_clone)):
      index_atual = 0

      maior_atual = max(votos_prefeito_clone)
      index_atual = votos_prefeito_clone.index(maior_atual)

      prefeitos_nomes_decrescente.append(nomes_prefeito_clone[index_atual])
      prefeitos_partidos_decrescente.append(partidos_prefeito_clone[index_atual])
      prefeitos_votos_decrescente.append(votos_prefeito_clone[index_atual])

      votos_prefeito_clone.pop(index_atual)
      nomes_prefeito_clone.pop(index_atual)
      partidos_prefeito_clone.pop(index_atual)

      
    # Organizando governadores em ordem decrescente
    for i in range(len(votos_governador_clone)):
      index_atual = 0

      maior_atual = max(votos_governador_clone)
      index_atual = votos_governador_clone.index(maior_atual)

      governadores_nomes_decrescente.append(nomes_governador_clone[index_atual])
      governadores_partidos_decrescente.append(partidos_governador_clone[index_atual])
      governadores_votos_decrescente.append(votos_governador_clone[index_atual])

      votos_governador_clone.pop(index_atual)
      nomes_governador_clone.pop(index_atual)
      partidos_governador_clone.pop(index_atual)


    # Organizando presidentes em ordem decrescente
    for i in range(len(votos_presidente_clone)):
      index_atual = 0

      maior_atual = max(votos_presidente_clone)
      index_atual = votos_presidente_clone.index(maior_atual)

      presidentes_nomes_decrescente.append(nomes_presidente_clone[index_atual])
      presidentes_partidos_decrescente.append(partidos_presidente_clone[index_atual])
      presidentes_votos_decrescente.append(votos_presidente_clone[index_atual])

      votos_presidente_clone.pop(index_atual)
      nomes_presidente_clone.pop(index_atual)
      partidos_presidente_clone.pop(index_atual)


    # Somando a quantidade total de votos
    total_votos_pref = 0
    total_votos_gov = 0
    total_votos_presi = 0

    for i in prefeitos_escolhidos:
      if i != ".":
        total_votos_pref += 1
    for i in governadores_escolhidos:
      if i != ".":
        total_votos_gov += 1
    for i in presidentes_escolhidos:
      if i != ".":
        total_votos_presi += 1

    # Somando a quantidade total de votos válidos (não branco ou nulo)

    total_votos_validos_pref = total_votos_pref - votos_brancos_prefeito - votos_nulos_prefeito
    total_votos_validos_gov = total_votos_gov - votos_brancos_governador - votos_nulos_governador
    total_votos_validos_presi = total_votos_presi - votos_brancos_presidente - votos_nulos_presidente

  

    # Agora, com todas as informações já preparadas, é hora de passar os resultados
    # Impressão feita de forma a simular uma tabela
    print("------------ RANKING DO RESULTADO PARA PREFEITO -------------")
    print("-- Nome -- / -- Partido -- / Total de Votos / % votos válidos")
    porc = 0
    for i in range(len(prefeitos_nomes_decrescente)):
      # Cálculo das porcentagens de votos válidos
      porc = (prefeitos_votos_decrescente[i]/total_votos_validos_pref) * 100
      porc = round(porc, 1)
      print(i+1, prefeitos_nomes_decrescente[i], "      ", prefeitos_partidos_decrescente[i],"             ", prefeitos_votos_decrescente[i],"            ", porc, "%")
    porc = 0

    # Cálculos das porcentagens de brancos e nulos são feitas dentro dos próprios prints
    print("Total de votos =", total_votos_pref)
    print("Total de votos válidos e % =", total_votos_validos_pref,"(", (total_votos_validos_pref/total_votos_presi)*100, "% )")
    print("Total de brancos e % =", votos_brancos_prefeito, "(", (votos_brancos_prefeito/total_votos_pref)*100, "% )")
    print("Total de nulos e % =", votos_nulos_prefeito, "(", (votos_nulos_prefeito/total_votos_pref)*100, "% )")
    print("")

    # Mesma lógica aplicada anteriormente é repetida para os outros 2 cargos
    print("----------- RANKING DO RESULTADO PARA GOVERNADOR ------------")
    print("-- Nome -- / -- Partido -- / Total de Votos / % votos válidos")
    porc = 0
    for i in range(len(governadores_nomes_decrescente)):
      porc = (governadores_votos_decrescente[i]/total_votos_validos_gov) * 100
      porc = round(porc, 1)
      print(i+1, governadores_nomes_decrescente[i], "      ", governadores_partidos_decrescente[i],"             ", governadores_votos_decrescente[i],"            ", porc, "%")
    porc = 0

    print("Total de votos =", total_votos_gov)
    print("Total de votos válidos e % =", total_votos_validos_gov,"(", (total_votos_validos_gov/total_votos_gov)*100, "% )")
    print("Total de brancos e % =", votos_brancos_governador, "(", (votos_brancos_governador/total_votos_gov)*100, "% )")
    print("Total de nulos e % =", votos_nulos_governador, "(", (votos_nulos_governador/total_votos_gov)*100, "% )")
    print("")

    print("----------- RANKING DO RESULTADO PARA PRESIDENTE ------------")
    print("-- Nome -- / -- Partido -- / Total de Votos / % votos válidos")
    porc = 0
    for i in range(len(presidentes_nomes_decrescente)):
      porc = (presidentes_votos_decrescente[i]/total_votos_validos_gov) * 100
      porc = round(porc, 1)
      print(i+1, presidentes_nomes_decrescente[i], "      ", presidentes_partidos_decrescente[i],"             ", presidentes_votos_decrescente[i],"            ", porc, "%")
    porc = 0

    print("Total de votos =", total_votos_presi)
    print("Total de votos válidos e % =", total_votos_validos_presi,"(", (total_votos_validos_presi/total_votos_presi)*100, "% )")
    print("Total de brancos e % =", votos_brancos_presidente, "(", (votos_brancos_presidente/total_votos_presi)*100, "% )")
    print("Total de nulos e % =", votos_nulos_presidente, "(", (votos_nulos_presidente/total_votos_presi)*100, "% )")
    print("")





def stats():
    print("+++ RELATÓRIO E ESTATÍSTICAS +++")
    print("")

    # Nesta lista só serão incluidos eleitores que votaram nos três cargos
    so_eleitores_que_votaram = []
    for i in range(len(nomes_eleitores)):
      if prefeitos_escolhidos[i] != "." or governadores_escolhidos[i] != "." or presidentes_escolhidos[i] != ".":
        so_eleitores_que_votaram.append(nomes_eleitores[i])

    so_eleitores_que_votaram = sorted(so_eleitores_que_votaram)

    print("Eleitores que Votaram em ordem alfabética:")
    print(*so_eleitores_que_votaram)

    print("")

    # Auditoria
    if len(so_eleitores_que_votaram) == len(nomes_eleitores):
      print("Total de Eleitores é igual ao total de votos (auditoria):", len(nomes_eleitores))
    else:
      print("Total de Eleitores não é igual ao total de votos (auditoria):")
      print("Temos", len(nomes_eleitores), "eleitores para apenas", len(so_eleitores_que_votaram), "votos")

    print("")

    # Fazer uma lista de partidos que participaram
    # Fazer uma lista de número de eleitos por partido respeitando os indexes
    # Para não colocar duplicatas, usa 'not in'
    lista_partidos = []
    eleitos_por_partido = []

    for i in range(len(partidos_prefeito)):
      if partidos_prefeito[i] not in lista_partidos:
        lista_partidos.append(partidos_prefeito[i])
    for i in range(len(partidos_governador)):
      if partidos_governador[i] not in lista_partidos:
        lista_partidos.append(partidos_governador[i])
    for i in range(len(partidos_presidente)):
      if partidos_presidente[i] not in lista_partidos:
        lista_partidos.append(partidos_presidente[i])

    # Lista de número de eleitos por partido é inicializada com zero para todos
    for i in lista_partidos:
      eleitos_por_partido.append(0)

    # Contabilizador de pontos para cada partido
    index_do_pref_vencedor = votos_prefeito.index(max(votos_prefeito))
    partido_vencedor = partidos_prefeito[index_do_pref_vencedor]
    for i in range(len(lista_partidos)):
      if lista_partidos[i] == partido_vencedor:
        eleitos_por_partido[i] += 1

    index_do_pref_vencedor = votos_governador.index(max(votos_governador))
    partido_vencedor = partidos_governador[index_do_pref_vencedor]
    for i in range(len(lista_partidos)):
      if lista_partidos[i] == partido_vencedor:
        eleitos_por_partido[i] += 1

    index_do_pref_vencedor = votos_presidente.index(max(votos_presidente))
    partido_vencedor = partidos_presidente[index_do_pref_vencedor]
    for i in range(len(lista_partidos)):
      if lista_partidos[i] == partido_vencedor:
        eleitos_por_partido[i] += 1

    # Remove os partidos que não elegeram nenhum candidato
    for i in range(len(eleitos_por_partido)):
      if eleitos_por_partido[i] == 0:
        del eleitos_por_partido[i]
        del lista_partidos[i]

    # Declarar qual é o partido com mais políticos eleitos
    index_vencedor_de_todos = eleitos_por_partido.index(max(eleitos_por_partido))
    print("Partido que elegeu mais políticos:", lista_partidos[index_vencedor_de_todos],"(", eleitos_por_partido[index_vencedor_de_todos], ")")

    index_perdedor_de_todos = eleitos_por_partido.index(min(eleitos_por_partido))
    print("Partido que elegeu menos políticos:", lista_partidos[index_perdedor_de_todos],"(", eleitos_por_partido[index_perdedor_de_todos], ")")





'''---------------------------------------------------------------------------'''
'''---------------------------- Função Main ----------------------------------'''
'''---------------------------------------------------------------------------'''

# Menu do sistema de votação. Os prints vázios servem para criar espaço entre as linhas imprimidas
# Loop infinito para repetir o menu até o usuário decidir parar
print("Bem vindo ao programa de votação. Por favor, digite o número correspondente à funcionalidade que deseja usar.")

while True:
  print("")
  print("+++++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO +++++++")
  print("")
  print("1. Cadastrar Candidatos")
  print("2. Cadastrar Eleitores")
  print("3. Votar")
  print("4. Apurar Resultados")
  print("5. Relatório e Estatísticas")
  print("6. Encerrar")
  print("")
  
  opcao_menu = int(input("Opção escolhida: "))
    
  
  #Por meio da opção escolhida, seleciona a função correspondente.
  if opcao_menu == 1:
    print("")
    cad_candidato()
  elif opcao_menu == 2:
    print("")
    cad_eleitor()
  elif opcao_menu == 3:
    print("")
    votar()
  elif opcao_menu == 4:
    print("")
    apurar()
  elif opcao_menu == 5:
    print("")
    stats()
  elif opcao_menu == 6:
    print("")
    print("Operação encerrada.")
    break
