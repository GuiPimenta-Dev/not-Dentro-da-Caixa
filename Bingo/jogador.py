from random import randint
from numpy import zeros

# Classe Jogador
class Jogador():

    # Inicializando a classe com os atributos nome,tabuleiro e tabuleiro_Comparacao
    def __init__(self,nome):
        
        # Atributo nome
        self.nome = nome
        
        # Atributo tabuleiro - É criado pela funcao cria_Tabuleiro()
        self.cartela= self.cria_Tabuleiro()
        
        # Atributo tabuleiro_Comparacao - Matriz totalmente nula 4x4
        self.cartela_Comparacao = zeros((4, 4),dtype=int)


    # Funcao responsavel por criar um tabuleiro de Bingo para o jogador
    def cria_Tabuleiro(self):
        
        # Matriz totalmente nula 4x4
        tabuleiro_Jogador = zeros((4, 4),dtype=int)

        # Para cada linha de 0-4
        for i in range(0, 4):
            
            # Para cada coluna de 0-4:
            for j in range(0, 4):
                
                # Gera um número aleatório entre 1 e 50
                elemento_do_Tabuleiro = randint(1, 50)

                # Enquanto o tabuleiro possuir um elemento igual ao candidato gera outro numero aleatorio entre 1 e 50
                while elemento_do_Tabuleiro in tabuleiro_Jogador:
                    elemento_do_Tabuleiro = randint(1, 50)

                # Tabuleiro criado com elementos que nao se repetem
                tabuleiro_Jogador[i][j] = elemento_do_Tabuleiro

        # Retorna tabuleiro_Jogador
        return tabuleiro_Jogador

    # Funcao que verifica se o jogador fez Bingo ou nao
    def jogador_Fez_Bingo(self,resultado_Jogada,indice_linha,indice_coluna):
        
        # Adiciona o elemento na posicao original do tabuleiro do jogador no tabuleiro_Comparacao
        self.cartela_Comparacao[indice_linha][indice_coluna]=resultado_Jogada

        # Se a linha do tabuleiro_Comparacao nao possuir zeros, entao:
        if 0 not in self.cartela_Comparacao[indice_linha]:
            # Retorna True - Jogador fez Bingo
            return True



0
0
0