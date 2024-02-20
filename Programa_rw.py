#Variáveis
#variavel que guarda uma lista com os nomes dos arquivos recem criados
arq_recentes = [" ", " ", " ", " ", " "]
#variavel com para o numero do index
n_index = 0
#variavel que vai aumentar o n° do index, diminuir, e depois estabilizar
one = 1
#impede que o código seja ativado antes do tempo
timer = 0
#registra a entrada(se é a segunda vez entrando não faz a mesma pergunta)
ticket_regist = 0
#Variável que vai iniciar o programa.
start_program = True
#n de opções para trabalhar
opcoes = ("1","2","3","4","5")
#° de opções é: opcoes -1
n_opcoes = 4
#Texto genérico que se repete
text_options = 'Digite: 1 - Para criar um novo arquivo de texto, 2 - Para editar um arquivo de texto, 3 - Para ler um arquivo de texto, 4 - Para mudar o diretório padrão. 5 - Para encerrar o programa.'

#looping para impedir q o programa se encerre antes da hora.
while start_program == True:

#Se for a primeira vez abrindo o programa, pede para registrar um diretório padrão
    if ticket_regist < 1:
    #introdução ao programa:
        #(Só vai ser mostrado uma 1 vez)
        print('Escolha o diretório padrão.')
        directory = input("(Exemplo: /Users/Public/Downloads):")
        print("Bem vindo! Esse é um programa que cria, edita e lê textos, o que você deseja?")
    
    print(text_options)
    #então tudo isso é mostrado no final
    print("Arquivos criados recentemente", arq_recentes)

    #Variáveis que vão registrar a resposta, diretório, e o n° de entradas.
    answer = input(':')
    ticket_regist = 1
 
#Impede que o usuario escolha uma opção que não está listada
    #OBSERVAÇÂO: tentei usar outros códigos mais simples como: while answer != opcoes[0:n_opcoes], mas infelizmente não funcionou
    while answer != opcoes[0] and answer != opcoes[1] and answer != opcoes[2] and answer != opcoes[3] and answer != opcoes[4]:
        print("Opção inválida, tente novamente!")
        print(text_options)
        answer = input(":")
    else:
#Script para Criar - 1
        if answer == "1":
            new_archive = input("Qual vai ser nome do seu arquivo:")
            with open(f"{directory}/{new_archive}.txt", "w") as file:
                cont = input("Escrever no arquivo:")
                file.write(cont)
                print(f"Arquivo {new_archive} criado!")
#variável que vai guardar o ultimo arquivo criado
                ultimo_arquivo = new_archive
#condição para limitar o numero do index
                if n_index > 4:
#nessa situação o n_index = 5, então ele reduz 1
                    n_index -= one
#aqui o timer vai ser desativado, e o código que antes estava desativado vai começar a funcionar
                    timer = 1
#então o numero do index vai se manter no ultimo
                    one = 0
#Aqui o timer, vai ser só ativado na condição correta
                if timer > 0:
#código que registra o movimento dos arquivos da direita pra esquerda
                    arq_recentes[0] = arq_recentes[1]
                    arq_recentes[1] = arq_recentes[2]
                    arq_recentes[2] = arq_recentes[3]
                    arq_recentes[3] = arq_recentes[4]
                    arq_recentes[4] = 0
#então após o movimente ser registrado, a ultima vaga do index é preenchido com o arquivo mais recente
                arq_recentes[n_index] = ultimo_arquivo
#isso aqui vai ser inutilizado após um tempo, modifica o index
                n_index += one
            

#Script para Editar - 2
        elif answer == "2":
            print("Qual arquivo deseja editar?")
            archive = input(":")
            with open(f'{directory}/{archive}.txt', "a" ) as file:
                cont = input("Adicionar linha de texto:")
                file.write(f"\n{cont}")
            
                
#Script para Ler - 3
        elif answer == "3":
            print("Qual arquivo deseja ler?")
            archive = input(":")
            with open(f"{directory}/{archive}.txt", "r") as file:
                print(file.read())
           

#Script para mudar o diretório - 4
        elif answer == "4":
            print("Para qual diretório deseja mudar?")
            directory = input(":")
            print("Diretório redefinido!")

#Script para encerrar o programa
    if answer == "5":
        print("Programa encerrado")
        break
           


    

    

