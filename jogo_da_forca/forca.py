#!/usr/bin/env python3
# -- coding: utf-8 --

import csv
from logging.config import dictConfig
from operator import itemgetter
from os import remove, system
from csv import reader, writer
from pickle import TRUE
import random
from turtle import color, update
from xml.etree.ElementInclude import include

dados = [(1, 'PLAYSTATION', 'médio', 8,0,0,0),(2,'COMPUTADOR', 'fácil', 4,0,0,0),(3,'PARALELEPIPEDO', 'médio', 8,0,0,0 ),(4, 'YAKSOBA', 'difícil', 12,0,0,0),(5,'AMARELO','fácil',4,0,0,0),(6,'AMIGO','fácil',4,0,0,0),(7,'AMOR','fácil',4,0,0,0),(8,'AVE','fácil',4,0,0,0),(9,'BOLO','fácil',4,0,0,0),(10,'BRANCO','fácil',4,0,0,0),(11,'CANECA','fácil',4,0,0,0),(12,'CELULAR','fácil',4,0,0,0),(13,'CLUBE','fácil',4,0,0,0),(14,'ELEFANTE','fácil',4,0,0,0),(15,'ESCOLA','fácil',4,0,0,0),(16,'ESTOJO','fácil',4,0,0,0),(17,'GELEIA','fácil',4,0,0,0),(18,'GIRAFA','fácil',4,0,0,0),(19,'LIMONADA','fácil',4,0,0,0),(20,'PIJAMA','fácil',4,0,0,0),(21,'ACENDER','médio',8,0,0,0),(22,'AFILHADO','médio',8,0,0,0),(23,'ARDILOSO','médio',8,0,0,0),(24,'ASTERISCO','médio',8,0,0,0),(25,'BASQUETE','médio',8,0,0,0),(26,'CAMINHO','médio',8,0,0,0),(27,'CHAMPAGNE','médio',8,0,0,0),(28,'CHICLETE','médio',8,0,0,0),(29,'CHUVEIRO','médio',8,0,0,0),(30,'CONTEXTO','médio',8,0,0,0),(31,'DESALMADO','médio',8,0,0,0),(32,'ELOQUENTE','médio',8,0,0,0),(33,'ESFIRRA','médio',8,0,0,0),(34,'GOROROBA','médio',8,0,0,0),(35,'MODERNIDADE','médio',8,0,0,0),(36,'VICISSITUDE','difícil',12,0,0,0),(37,'QUARTZO','difícil',12,0,0,0),(38,'VERTIGINOSO','difícil',12,0,0,0),(39,'BARTENDER','difícil',12,0,0,0),(40,'DESEMBARGADOR','difícil',12,0,0,0),(41,'ENDOCRINOLOGISTA','difícil',12,0,0,0),(42,'PIZZAIOLO','difícil',12,0,0,0),(43,'QUIROPRATA','difícil',12,0,0,0),(44,'ALBATROZ','difícil',12,0,0,0),(45,'ESCARAVELHO','difícil',12,0,0,0),(46,'CANDELABRO','difícil',12,0,0,0),(47,'DESFIBRILADOR','difícil',12,0,0,0),(48,'NEBULIZADOR','difícil',12,0,0,0),(49,'BERGAMOTA','difícil',12,0,0,0),(50,'CRANBERRY','difícil',12,0,0,0),(51,'JENIPAPO','difícil',12,0,0,0)]
print (dados)

arquivo=open('_dados/ArquivoCSV_forca.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(arquivo, delimiter=";")

csv_writer.writerows(dados)

arquivo.close()

arquivo=open('_dados/ArquivoCSV_forca.csv', encoding='utf-8',newline='')
csv_reader = csv.reader(arquivo)

lista_palavras = []
for lista_palavras in csv_reader:
    continue
print('Bem-vindo(a) ao jogo da Forca!\nDESENVOLVIDO POR THIAGO PACHECO')

arquivo.close()

# Menu de opções
def Menu():
    print('Escolha:')
    print('1. Adicionar uma nova palavra')
    print('2. Remover uma palavra')
    print('3. Consultar uma palavra')
    print('4. Listar todas as palavras')
    print('5. Buscar uma palavra')
    print('6. Listar todas as palavras de uma determinada dificuldade')
    print('7. Apresentar as estatísticas')
    print('8. Jogar')
    print('9. Sair')
    return int(input('Sua opção: '))

escolha = 1
while escolha == 1:
        escolha_opcao_menu = Menu()
        if escolha_opcao_menu == 1: 
            nova_palavra= input('Qual palavra você deseja que seja adicionada? ')
            for cont in dados:
                if nova_palavra == cont[1]:
                    print('A palavra escolhida já está incluída no jogo!')
                    break
            if nova_palavra != cont[1]:
                    novos_atributos = []
                    id_nova_palavra = 1
                    for i in range(len(dados)):
                        id_nova_palavra += 1
                    novos_atributos.append(id_nova_palavra)    
                    novos_atributos.append(nova_palavra)
                    dificuldade = input('Qual a dificuldade da mesma? (fácil, médio ou difícil) ')
                    novos_atributos.append(dificuldade)
                    if novos_atributos[2] == 'fácil':
                        qtd_chances = 4
                        novos_atributos.append(qtd_chances)
                    if novos_atributos[2] == 'médio':
                        qtd_chances = 8
                        novos_atributos.append(qtd_chances)
                    if novos_atributos[2] == 'difícil':
                        qtd_chances = 12
                        novos_atributos.append(qtd_chances)
                    jogadas = 0
                    novos_atributos.append(jogadas)
                    acertos = 0
                    novos_atributos.append(acertos)
                    erros = 0
                    novos_atributos.append(erros)
                    novos_atributos=(novos_atributos[0],novos_atributos[1],novos_atributos[2],novos_atributos[3],novos_atributos[4],novos_atributos[5],novos_atributos[6])
                    dados = list(dados)
                    dados.append(novos_atributos)
                    dados = tuple(dados)
                    dados = sorted(dados,key=itemgetter(0))
                    with open('_dados/ArquivoCSV_forca.csv', 'rb') as inp, open('_dados/ArquivoCSV_forca.csv', 'wb') as out:
                        writer = csv.writer(out)
                        arquivo.close()
                    arquivo=open('_dados/ArquivoCSV_forca.csv', 'w', encoding='utf-8', newline='')
                    csv_writer = csv.writer(arquivo, delimiter=";")
                    csv_writer.writerows(dados)
                    arquivo.close()
                    arquivo=open('_dados/ArquivoCSV_forca.csv', encoding='utf-8',newline='')
                    csv_reader = csv.reader(arquivo)
                    reader_object = reader(arquivo, delimiter=";")
                    arquivo.close()
                    print(dados)

        if escolha_opcao_menu == 2:
            remover_palavra = input('Qual palavra você deseja que seja removida? ')
            words_ants = []
            for cont in dados:
                words_ants.append(cont[1])
                if remover_palavra == cont[1]:
                    valor_removido = cont[1]
                    dados.remove(cont)     
            words_dps = []
            for cont in dados:
                words_dps.append(cont[1])
            if remover_palavra == words_ants and remover_palavra != words_dps:
                print('A palavra escolhida não está incluída no jogo!')
            with open('_dados/ArquivoCSV_forca.csv', 'rb') as inp, open('_dados/ArquivoCSV_forca.csv', 'wb') as out:
                writer = csv.writer(out)
                arquivo.close()
            arquivo=open('_dados/ArquivoCSV_forca.csv', 'w', encoding='utf-8', newline='')
            csv_writer = csv.writer(arquivo, delimiter=";")
            csv_writer.writerows(dados)
            arquivo.close()
            arquivo=open('_dados/ArquivoCSV_forca.csv', encoding='utf-8',newline='')
            csv_reader = csv.reader(arquivo)
            reader_object = reader(arquivo, delimiter=";")
            arquivo.close()
            print(dados)

        if escolha_opcao_menu == 3:
            consultar_palavra = input('Qual palavra você deseja que seja consultada? ')
            words_cons = []
            for cont in dados:
                words_cons.append(cont[1])
                if consultar_palavra == cont[1]:
                    print (cont)
            não_incluida = True
            for i in range(len(words_cons)):
                if consultar_palavra == words_cons[i]:
                    não_incluida = False
            if não_incluida == True:
                print('A palavra escolhida não está incluída no jogo!')

        if escolha_opcao_menu == 4:
            for cont in dados:
                print (cont[1])

        if escolha_opcao_menu == 5:
            parte_palavra = input('Digite a parte da palavra para que o sistema liste todas as palavras que contenham essa parte: ')
            for cont in dados:
                if parte_palavra in cont[1]:
                    print (cont[1])


        if escolha_opcao_menu == 6:
            dif = input('Qual dificuldade você deseja? ')
            for cont in dados:
                if dif == 'fácil':
                    if cont[2] == 'fácil':
                        print (cont[1])
                if dif == 'médio':    
                    if cont[2] == 'médio':
                        print (cont[1])
                if dif == 'difícil':
                    if cont[2] == 'difícil':
                        print (cont[1])

        if escolha_opcao_menu == 7:
            ordenar_mais_jogadas = []
            ordenar_mais_jogadas = sorted(dados,key=itemgetter(4), reverse=True)
            temp_5_mais_jogadas = []
            for cont in ordenar_mais_jogadas:
                temp_5_mais_jogadas.append(cont[1])  
            i = 0
            Cinco_mais_jogadas = []
            for i in range(0,5):
                Cinco_mais_jogadas.append(temp_5_mais_jogadas[i])
            print(f'As cinco palavras mais jogadas foram: {Cinco_mais_jogadas}')
            
            ordenar_mais_acertos = []
            ordenar_mais_acertos = sorted(dados,key=itemgetter(5), reverse=True)
            temp_5_mais_acertos = []
            for cont in ordenar_mais_acertos:
                temp_5_mais_acertos.append(cont[1])  
            i = 0
            Cinco_mais_acertos = []
            for i in range(0,5):
                Cinco_mais_acertos.append(temp_5_mais_acertos[i])
            print(f'As cinco palavras com mais acertos foram: {Cinco_mais_acertos}')
            
            ordenar_mais_erros = []
            ordenar_mais_erros = sorted(dados,key=itemgetter(6), reverse=True)
            temp_5_mais_erros = []
            for cont in ordenar_mais_erros:
                temp_5_mais_erros.append(cont[1])   
            i = 0
            Cinco_mais_erros = []
            for i in range(0,5):
                Cinco_mais_erros.append(temp_5_mais_erros[i])
            print(f'As cinco palavras com mais erros foram: {Cinco_mais_erros}')
        
        # Começando jogo      
        if escolha_opcao_menu == 8:
            linhas_txt = """
X==:===
X  :  =
X     =    
X     =
X     =
X     = 
=======

"""
            linhas = []
            for linha in linhas_txt.splitlines():
                linhas.append(list(linha))  
            letras_inseridas = []
            tentativas = 0
            palavras_jogo = []
            qtd_acertos = 0
            # qual palavra será escolhida
            for cont in dados:
                palavras_jogo.append(cont[1])
                palavra = random.choice(palavras_jogo)
            for cont in dados:
                if palavra == cont[1]:
                    valor = cont 
            for cont in dados:
                if palavra == cont[1]:     
                    dados = list(dados)
                    cont = list(cont)
                    cont[4] = cont[4] + 1
                    cont = tuple(cont)
                    dados.append(cont)
            removeu = False
            temp = []
            for cont in dados:
                if cont != valor or removeu:
                    temp.append(cont)
                else:
                    removeu = True
            dados = temp
            dados = sorted(dados,key=itemgetter(0))
            with open('_dados/ArquivoCSV_forca.csv', 'rb') as inp, open('_dados/ArquivoCSV_forca.csv', 'wb') as out:
                writer = csv.writer(out)
                arquivo.close()
            arquivo=open('_dados/ArquivoCSV_forca.csv', 'w', encoding='utf-8', newline='')
            csv_writer = csv.writer(arquivo, delimiter=";")
            csv_writer.writerows(dados)
            arquivo.close()
            arquivo=open('_dados/ArquivoCSV_forca.csv', encoding='utf-8',newline='')
            csv_reader = csv.reader(arquivo)
            reader_object = reader(arquivo, delimiter=";")
            arquivo.close()
            
            tam = len(palavra)
            estado_inicial = "_" * len(palavra)

            qtd_chances = cont[3]

            nivel = cont[2]
            print(f'Essa palavra é {nivel}! Você tem {qtd_chances} chances para descobrir:\n{estado_inicial}\n')

            erros = 0

            while tentativas != qtd_chances:
                letra = input('Escolha uma letra: ')
                letra = letra.upper() 
                if len(letra) > 1:
                    print('ERRO. Só pode ser escolhida uma letra apenas!')
                    continue

            # verficando se a letra escolhida pelo usuario tem na palavra sorteada
                if letra in palavra:
                    print('Você acertou uma letra! :)')
                    qtd_acertos += 1 
                else:
                    print('Você errou uma letra! :(')
                    qtd_chances -= 1
                    erros +=1
                    if erros == 1:
                        linhas[3][3] = "O"
                    elif erros == 2:
                        linhas[4][3] = "|"
                    elif erros == 3:
                        linhas[4][2] = "\\"
                    elif erros == 4:
                        linhas[4][4] = "/"
                    elif erros == 5:
                        linhas[5][2] = "/"
                    elif erros == 6:
                        linhas[5][4] = "\\"
                for l in linhas:
                    print("".join(l))
                letras_inseridas.append(letra) # inserindo as letras na lista

                print('As letras inseridas até o momento foram: ')
                for letra_secreta in letras_inseridas:
                     if letra_secreta in palavra:
                         print('{}{}{}'.format('\033[0;32m',letra_secreta,'\033[0;0m'), end=" ")
                         
                     else: 
                         print('{}{}{}'.format('\033[0;31m',letra_secreta,'\033[0;0m'), end=" ")
                         
            # cada letra da palavra iremos ver se ela esta na lista de letras que o usuario digitou
                secreto_temporario = ''
                for letra_secreta in palavra:
                     if letra_secreta in letras_inseridas:
                         secreto_temporario += letra_secreta 
                     else: 
                         secreto_temporario += '_'    

            # checando se o usuário ganhou ou ainda não
                if secreto_temporario == palavra:
                    print('\nParabéns! Você venceu! :)')
                    print(f'A palavra era: {palavra}')
                    for cont in dados:
                        if palavra == cont[1]:
                            v_ganhou = cont 
                    for cont in dados:
                        if palavra == cont[1]:     
                            dados = list(dados)
                            cont = list(cont)
                            cont[5] = cont[5] + 1
                            cont = tuple(cont)
                            dados.append(cont)
                    removeu = False
                    temp_ganhou = []
                    for cont in dados:
                        if cont != v_ganhou or removeu:
                            temp_ganhou.append(cont)
                        else:
                            removeu = True
                    dados = temp_ganhou
                    dados = sorted(dados,key=itemgetter(0))
                    with open('_dados/ArquivoCSV_forca.csv', 'rb') as inp, open('_dados/ArquivoCSV_forca.csv', 'wb') as out:
                        writer = csv.writer(out)
                        arquivo.close()
                    arquivo=open('_dados/ArquivoCSV_forca.csv', 'w', encoding='utf-8', newline='')
                    csv_writer = csv.writer(arquivo, delimiter=";")
                    csv_writer.writerows(dados)
                    arquivo.close()
                    arquivo=open('_dados/ArquivoCSV_forca.csv', encoding='utf-8',newline='')
                    csv_reader = csv.reader(arquivo)
                    reader_object = reader(arquivo, delimiter=";")
                    arquivo.close()
                    escolha = int(input('Deseja jogar novamente? 1(S)/2(N): '))
                    if escolha == 1:
                        system('cls')
                        print('DESENVOLVIDO POR THIAGO PACHECO')
                    break
                else:
                    print(f'\nPalavra: {secreto_temporario}')

            # qtd de chances que o usuário ainda tem
                print(f'Chances restantes: {qtd_chances}')
                print(f'Acertos: {qtd_acertos}')
                print(f'Erros: {erros}\n') 

            # quando o usuário perder o jogo    
            if tentativas == qtd_chances:
                print('Que pena, você perdeu :(')
                print(f'A palavra era: {palavra}')
                for cont in dados:
                    if palavra == cont[1]:
                            v_ganhou = cont 
                for cont in dados:
                    if palavra == cont[1]:     
                        dados = list(dados)
                        cont = list(cont)
                        cont[6] = cont[6] + 1
                        cont = tuple(cont)
                        dados.append(cont)
                removeu = False
                temp_perdeu = []
                for cont in dados:
                    if cont != v_ganhou or removeu:
                        temp_perdeu.append(cont)
                    else:
                        removeu = True
                dados = temp_perdeu
                dados = sorted(dados,key=itemgetter(0))
                with open('_dados/ArquivoCSV_forca.csv', 'rb') as inp, open('_dados/ArquivoCSV_forca.csv', 'wb') as out:
                    writer = csv.writer(out)
                    arquivo.close()
                arquivo=open('_dados/ArquivoCSV_forca.csv', 'w', encoding='utf-8', newline='')
                csv_writer = csv.writer(arquivo, delimiter=";")
                csv_writer.writerows(dados)
                arquivo.close()
                arquivo=open('_dados/ArquivoCSV_forca.csv', encoding='utf-8',newline='')
                csv_reader = csv.reader(arquivo)
                reader_object = reader(arquivo, delimiter=";")
                arquivo.close()
                escolha = int(input('Deseja jogar novamente? 1(S)/2(N): '))
                if escolha == 1:
                    system('cls')
                    print('Jogo da forca')
                    print('DESENVOLVIDO POR THIAGO PACHECO')
                              
        if escolha_opcao_menu == 9:
            break
