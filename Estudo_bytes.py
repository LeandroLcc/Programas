import os


#Variáveis
diretorio = input("Escolha o diretório:") #variavel para definir o diretório
ii_cont = 0 #usado para indexar cada caracter 0 e 1 do valor em binário
data_bin_list = [] # crio uma lista para guardar esse valor em binário 
cont_bin = 0 #usado para indexar os bytes em binários
status_for = 0 #usado para encerrar o looping



with open(f"C:\\{diretorio}\\file.bin", "rb") as data_file: #Primeiro abro o arquivo bin em modo de leitura como 'data_file', após isso, registro algumas váriáveis
    data_reader = data_file.read() #variável que pérmite ler o arquivo;
    data_file_length = os.path.getsize(f"C:\\{diretorio}\\file.bin")#variável que guarda, o total de bytes do arquivo
um_porcent = (data_file_length//3)//100
dez_porcent = (data_file_length//3)//10
#==================================!!!!FUNÇÃO MERAMENTE COM OBJETIVO DE IDENTIFICAÇÃO VISUA!!!!!====================================
def porcentagem(valor):
    if valor <= dez_porcent:
        n = 0    
        if valor >= um_porcent*10: return "10%"
        if valor >= um_porcent*9: return f"{n}9%"
        if valor >= um_porcent*8: return f"{n}8%"
        if valor >= um_porcent*7: return f"{n}7%"
        if valor >= um_porcent*6: return f"{n}6%"
        if valor >= um_porcent*5: return f"{n}5%"
        if valor >= um_porcent*4: return f"{n}4%"
        if valor >= um_porcent*3: return f"{n}3%"
        if valor >= um_porcent*2: return f"{n}2%"
        if valor >= um_porcent: return f"{n}1%"
        if valor <= um_porcent: return "0%"

    if valor <= dez_porcent*2:
        n = 1    
        if valor >= um_porcent*20: return "20%"
        if valor >= um_porcent*19: return f"{n}9%"
        if valor >= um_porcent*18: return f"{n}8%"
        if valor >= um_porcent*17: return f"{n}7%"
        if valor >= um_porcent*16: return f"{n}6%"
        if valor >= um_porcent*15: return f"{n}5%"
        if valor >= um_porcent*14: return f"{n}4%"
        if valor >= um_porcent*13: return f"{n}3%"
        if valor >= um_porcent*12: return f"{n}2%"
        if valor >= um_porcent*11: return f"{n}1%"
        if valor >= um_porcent*10: return "10%"

    if valor <= dez_porcent*3:
        n = 2    
        if valor >= um_porcent*30: return "30%"
        if valor >= um_porcent*29: return f"{n}9%"
        if valor >= um_porcent*28: return f"{n}8%"
        if valor >= um_porcent*27: return f"{n}7%"
        if valor >= um_porcent*26: return f"{n}6%"
        if valor >= um_porcent*25: return f"{n}5%"
        if valor >= um_porcent*24: return f"{n}4%"
        if valor >= um_porcent*23: return f"{n}3%"
        if valor >= um_porcent*22: return f"{n}2%"
        if valor >= um_porcent*21: return f"{n}1%"
        if valor >= um_porcent*20: return "20%"
        
    if valor <= dez_porcent*4:
        n = 3    
        if valor >= um_porcent*40: return "40%"
        if valor >= um_porcent*39: return f"{n}9%"
        if valor >= um_porcent*38: return f"{n}8%"
        if valor >= um_porcent*37: return f"{n}7%"
        if valor >= um_porcent*36: return f"{n}6%"
        if valor >= um_porcent*35: return f"{n}5%"
        if valor >= um_porcent*34: return f"{n}4%"
        if valor >= um_porcent*33: return f"{n}3%"
        if valor >= um_porcent*32: return f"{n}2%"
        if valor >= um_porcent*31: return f"{n}1%"
        if valor >= um_porcent*30: return "30%"

    if valor <= dez_porcent*5:
        n = 4    
        if valor >= um_porcent*50: return "50%"
        if valor >= um_porcent*49: return f"{n}9%"
        if valor >= um_porcent*48: return f"{n}8%"
        if valor >= um_porcent*47: return f"{n}7%"
        if valor >= um_porcent*46: return f"{n}6%"
        if valor >= um_porcent*45: return f"{n}5%"
        if valor >= um_porcent*44: return f"{n}4%"
        if valor >= um_porcent*43: return f"{n}3%"
        if valor >= um_porcent*42: return f"{n}2%"
        if valor >= um_porcent*41: return f"{n}1%"
        if valor >= um_porcent*50: return "40%"

    if valor <= dez_porcent*6:
        n = 5    
        if valor >= um_porcent*60: return "60%"
        if valor >= um_porcent*59: return f"{n}9%"
        if valor >= um_porcent*58: return f"{n}8%"
        if valor >= um_porcent*57: return f"{n}7%"
        if valor >= um_porcent*56: return f"{n}6%"
        if valor >= um_porcent*55: return f"{n}5%"
        if valor >= um_porcent*54: return f"{n}4%"
        if valor >= um_porcent*53: return f"{n}3%"
        if valor >= um_porcent*52: return f"{n}2%"
        if valor >= um_porcent*51: return f"{n}1%"
        if valor >= um_porcent*50: return "50%"

    if valor <= dez_porcent*7:
        n = 6    
        if valor >= um_porcent*70: return "70%"
        if valor >= um_porcent*69: return f"{n}9%"
        if valor >= um_porcent*68: return f"{n}8%"
        if valor >= um_porcent*67: return f"{n}7%"
        if valor >= um_porcent*66: return f"{n}6%"
        if valor >= um_porcent*65: return f"{n}5%"
        if valor >= um_porcent*64: return f"{n}4%"
        if valor >= um_porcent*63: return f"{n}3%"
        if valor >= um_porcent*62: return f"{n}2%"
        if valor >= um_porcent*61: return f"{n}1%"
        if valor >= um_porcent*50: return "60%"

    if valor <= dez_porcent*8:
        n = 7    
        if valor >= um_porcent*80: return "80%"
        if valor >= um_porcent*79: return f"{n}9%"
        if valor >= um_porcent*78: return f"{n}8%"
        if valor >= um_porcent*77: return f"{n}7%"
        if valor >= um_porcent*76: return f"{n}6%"
        if valor >= um_porcent*75: return f"{n}5%"
        if valor >= um_porcent*74: return f"{n}4%"
        if valor >= um_porcent*73: return f"{n}3%"
        if valor >= um_porcent*72: return f"{n}2%"
        if valor >= um_porcent*71: return f"{n}1%"
        if valor >= um_porcent*50: return "70%"


    if valor <= dez_porcent*9:
        n = 8    
        if valor >= um_porcent*90: return "90%"
        if valor >= um_porcent*89: return f"{n}9%"
        if valor >= um_porcent*88: return f"{n}8%"
        if valor >= um_porcent*87: return f"{n}7%"
        if valor >= um_porcent*86: return f"{n}6%"
        if valor >= um_porcent*85: return f"{n}5%"
        if valor >= um_porcent*84: return f"{n}4%"
        if valor >= um_porcent*83: return f"{n}3%"
        if valor >= um_porcent*82: return f"{n}2%"
        if valor >= um_porcent*81: return f"{n}1%"
        if valor >= um_porcent*50: return "80%"


    if valor <= data_file_length:
        n = 9    
        if valor >= um_porcent*100: return "100%"
        if valor >= um_porcent*99: return f"{n}9%"
        if valor >= um_porcent*98: return f"{n}8%"
        if valor >= um_porcent*97: return f"{n}7%"
        if valor >= um_porcent*96: return f"{n}6%"
        if valor >= um_porcent*95: return f"{n}5%"
        if valor >= um_porcent*94: return f"{n}4%"
        if valor >= um_porcent*93: return f"{n}3%"
        if valor >= um_porcent*92: return f"{n}2%"
        if valor >= um_porcent*91: return f"{n}1%"
        if valor >= um_porcent*50: return "90%"


for i in range(data_file_length//3): # utilizo o for para criar um ciclo que manipula todos os bytes do arquivo
    print(porcentagem(i))
    if status_for == 1:
        break

    else:
        for iii in range(3): #for usado pra converter 3 bytes por vez
            data_bin = bin(data_reader[cont_bin])# transforma cada byte indexado em binário
            data_bin_length = len(data_bin) #registro o tamanho do valor binário, para então futuramente inverter o valor
            data_len_short = data_bin_length - 2 #Varíavel que retira o '0b' do binário

            for ii in range(data_len_short):
                data_bin_list.append(data_bin[ii+2:ii+3]) #adiciono o valor do binário na lista sem o "0b"
                if data_bin[ii+2:ii+3] == " ": #verifica se o valor adicionado está vazio,se sim encerra o looping
                    status_for = 1
                    continue

                if data_bin_list[ii_cont] == "0": #Aqui um conversor para inverter cada valor em binário
                    data_bin_list[ii_cont] = "1"
                   
                else:
                    data_bin_list[ii_cont] = "0"
                

                if ii_cont == 0: #escreve o valor binário convertido no arquivo
                    with open(f"C:\\{diretorio}\\arquivo_convertido.bin", "w") as conv_file: #cria o arquivo, caso não tenha sido anteriormente
                        conv_file.write(data_bin_list[ii_cont])
                else:
                    with open(f"C:\\{diretorio}\\arquivo_convertido.bin", "a") as conv_file: #caso o arquivo já esteja criado, apenas adiciona
                        conv_file.write(data_bin_list[ii_cont])
                ii_cont += 1
            cont_bin += 1
        
    
print("Processo finalizado!")
    
