nome = input("Olá pessoa aventureira! Para começar, digite seu nome: ")

print("Prazer em te conhecer",nome)

idade = int(input("Qual a sua idade? "))

#crianças n jogam pq com o tempo esse jogo fica pesado
if idade < 15:
  print("Você não tem idade suficiente para jogar, desculpe.")
  
else:
  resposta_inicio = input("Legal, você quer jogar? (s/n)")
  #Se jogador n quiser jogar...
  if resposta_inicio == "n":
    print("Ok, até a próxima", nome,"!")
    
  else:
    print("Show! Vc comeca com 100 de vida e 100 de mana.") #A parte da mana serve para a classe bruxa, mas por hora todo mundo tem
    vida = 100 
    mana = 100
    
    #Primeira escolha
    resposta_start = input("Agora escolha: Esquerda ou direita? (e/d) \n ")

    if resposta_start == "e":
      resposta_lago = int(input("Você encontrou um lago de águas pantanosas e com muitas árvores ao redor.\n 1.Ser valente e nadar até o outro lado \n 2.Ser prudente e contornar o lago indo pelo caminho mais longo \n(1/2)"))

      if resposta_lago == 1:
        print("Você entra no lago porém é mordido por um peixe venenoso, sentindo suas forcas se esvairem rapidamente e morre por afogamento antes de chegar a outra margem. Parabens pela valentia, ela te levou direto aos braços da morte hahahahaha")

      else:
        resposta_bifurca = input("Voce escolhe o caminho mais longo e acaba em uma bifurcacao, onde de um lado há uma casa com a porta aberta que parece estranhamente imaculada e de outro um bosque com árvores que balancam ao sabor do vento. Qual vc escolhe? (casa/bosque) ")  

        if resposta_bifurca == "casa":
          resposta_casa = int(input("Voce entra na casa e se depara com uma cozinha que parece ter sido usada ha nao muito tempo atrás, já que no fogão há uma panela ainda quente e na mesa há um prato sujo. Você quer: \n 1. Explorar a casa e ver se encontra alguém(ou algo) \n 2. Sair correndo da casa enquanto ainda dá tempo (1/2)"))

        else:
          resposta_bosque = input("Voce resolve adentrar o bosque e logo sente o cheiro da natureza: O ar puro, o vento gentil que passa pelo seu corpo e o cheiro da terra macia sob seus pés. Mas há algo mais, ao que parece ser sua esquerda há um barulho estranho ecoando, ao mesmo tempo que esbarrando na sua perna um animal passa correndo, mas você nao consegue ver que tipo de animal é. Voce : \n 1. Decide ir em direcao do barulho \n 2. Ir atrás do animal\n 3. Permanecer onde está e olhar ao redor (1/2/3) ")  

    else:
      print("Você encontrou um abismo,mas ao olhar para baixo tropeça e morre. Que azar hein?")
