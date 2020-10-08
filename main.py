nome = input("Olá pessoa aventureira! Para começar, digite seu nome: ")

print("Prazer em te conhecer",nome)

idade = int(input("Qual a sua idade? "))

if idade < 15:
  print("Você não tem idade suficiente para jogar, desculpe.")
else:
  resposta_inicio = input("Legal, você quer jogar? (s/n)")
  if resposta_inicio == "n":
    print("Ok, até a próxima", nome,"!")
  else:
    print("Show! Vc comeca com 100 de vida e 100 de mana.") 
    vida = 100 
    mana = 100
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
          resposta_bosque = int(input("Voce resolve adentrar o bosque e logo sente o cheiro da natureza: O ar puro, o vento gentil que passa pelo seu corpo e o cheiro da terra macia sob seus pés. Mas há algo mais, ao que parece ser sua esquerda há um barulho estranho ecoando, ao mesmo tempo que esbarrando na sua perna um animal passa correndo, mas você nao consegue ver que tipo de animal é. Voce : \n 1. Decide ir em direcao do barulho \n 2. Ir atrás do animal\n 3. Permanecer onde está e olhar ao redor (1/2/3) "))  
          if resposta_bosque == 1:
            resposta_barulho = input("Cuidadosamente voce vai em direcao ao barulho e depois de caminhar durante um tempo avista o que parece ser um homem, vestido com uma túnica branca e uma mascara preta estranha no rosto.Ele ainda nao te viu, pelo o que parece. O que vai fazer agora?")
          elif resposta_bosque == 2:
            resposta_animal = input("Como Alice, você corre atrás do animal, que percebe ser não um coelho branco, mas um gato preto com rabo branco. Você:\n 1.Continua seguindo-o, pois adora gatos, e sua pelagem diferente lhe chama atencao \n2.Desiste de seguir o gato, afinal sabe-se lá onde ele pode te levar \n (1/2)")
          else:
            resposta_permanecer = input("Você resolve ficar onde está e olhar ao redor, para entender melhor quais são suas opcoes")    
    else:
      print("Você encontrou um abismo,mas ao olhar para baixo tropeça e morre. Que azar hein?")
