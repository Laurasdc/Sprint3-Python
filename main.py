import pandas as pd
import json
import random

# Carrega os dados das peças do arquivo JSON externo
def carregar_dados():
    try:
        with open('pecas.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print("Arquivo JSON não encontrado. Verifique o caminho e o nome do arquivo.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return {}

# Cria um dataframe a partir dos dados
def criar_dataframe(dados):
    return pd.DataFrame(dados).T

# Saúda o usuário e coleta as informações iniciais
def saudacao():
    print("\n" + "="*80)
    print("🚗 🌱  Bem-vindo a SustenRace, promovendo a inovação na Fórmula E! 🌱 🚗")
    print("="*80 + "\n")
    
    nome = input("Por favor, insira seu nome: ")
    while not nome.isalpha():
        print("❌ Nome inválido! Por favor, insira um nome válido.")
        nome = input("Por favor, insira seu nome: ")

    idade = verificacaonumero("Agora, nos informe sua idade: ")
    
    print(f"\n🌟 Olá {nome}, obrigado por participar! Vamos começar sua experiência na SustenRace.")
    return nome, idade

# Exibe as peças disponíveis
def exibir_pecas_disponiveis(dados):
    print("\n📊 Aqui está uma visão geral das peças do carro da Mahindra:")
    print("-"*40)
    for index, peca in enumerate(dados.keys()):
        print(f"{index + 1}. {peca}")
    print("-"*40)

# Exibe a descrição da peça escolhida
def exibir_descricao_peca(dados, escolha):
    pecas = list(dados.keys())
    peca_escolhida = pecas[escolha - 1]
    descricao = dados[peca_escolhida]

    print(f"\n🔧 Peça: {peca_escolhida}")
    print("-"*40)
    for chave, valor in descricao.items():
        if pd.notna(valor):
            print(f"{chave.capitalize()}: {valor}")
    print("-"*40)

# Promove a Fórmula E com uma interação opcional
def promover_formula_e():
    print("\n🚀 Vamos aprender mais sobre a Mahindra e a Fórmula E!")
    interagir = forca_opcao(['sim', 'não'], "\nQuer saber mais sobre como a Mahindra inova na Fórmula E? ")
    if interagir == 'sim':
        print("\nA Mahindra está liderando a revolução elétrica com inovações que estão mudando o cenário do automobilismo.")
        print("🌍 Participe das nossas iniciativas e ajude a construir o futuro da mobilidade sustentável!")

# Força a escolha correta de opções
def forca_opcao(lista_opcoes, msg):
    opcao = input(f"{msg} ({'/'.join(lista_opcoes)}): ").lower()
    while opcao not in lista_opcoes:
        print(f"❌ Opção inválida! Escolha uma das opções: {', '.join(lista_opcoes)}")
        opcao = input(f"{msg} ({'/'.join(lista_opcoes)}): ").lower()
    return opcao

# Verifica se a entrada é um número válido
def verificacaonumero(msg):
    while True:
        verificacao = input(msg)
        if verificacao.isnumeric() and int(verificacao) > 0:
            return int(verificacao)
        else:
            print("❌ Valor inválido. Por favor, digite sua idade novamente.")

# Pergunta ao usuário se deseja ver as peças e exibe a descrição
def questionario(dados):
    while True:
        resposta = forca_opcao(['sim', 'não'], "\nVocê gostaria de ver as peças do carro da Mahindra? ")
        if resposta == 'sim':
            exibir_pecas_disponiveis(dados)
            escolha = verificacaonumero("\nDigite o número da peça que deseja ver (0 para sair): ")
            if escolha == 0:
                print("Saindo...")
                break
            elif 1 <= escolha <= len(dados):
                exibir_descricao_peca(dados, escolha)
            else:
                print("❌ Opção inválida. Tente novamente.")
        elif resposta == 'não':
            break

# Simula a montagem de um carro da Fórmula E
def simulador_montagem(dados):
    print("\n--- Simulador de Montagem de Carro ---")
    
    pecas_necessarias = ["Chassi", "Motor", "Suspensão", "Bateria", "Freios"]
    montagem = {}
    
    for peca in pecas_necessarias:
        print(f"\nEscolha uma {peca} para o seu carro:")
        pecas_disponiveis = [key for key in dados.keys() if peca.lower() in key.lower()]
        
        if pecas_disponiveis:
            for index, item in enumerate(pecas_disponiveis):
                print(f"{index + 1}. {item}")
                
            escolha = verificacaonumero("\nDigite o número da peça escolhida: ")
            if 1 <= escolha <= len(pecas_disponiveis):
                peca_escolhida = pecas_disponiveis[escolha - 1]
                montagem[peca] = dados[peca_escolhida]
            else:
                print(f"❌ Escolha inválida para {peca}.")
        else:
            print(f"❌ Peças de {peca} não disponíveis.")

    nome_carro = input("\nEscolha um nome para o seu carro: ")
    velocidade_maxima = random.randint(250, 350)
    
    print(f"\n✅ Montagem completa! Aqui está o resumo do seu carro '{nome_carro}':")
    for peca, descricao in montagem.items():
        print(f"\n🔧 {peca}:")
        for chave, valor in descricao.items():
            if pd.notna(valor):
                print(f"{chave.capitalize()}: {valor}")
            else:
                print(f"{chave.capitalize()}: Informação indisponível")
    
    print(f"\n🚀 Velocidade Máxima Estimada: {velocidade_maxima} km/h")

# Função principal
def main():
    dados = carregar_dados()
    
    if not dados:
        return
    
    df = criar_dataframe(dados)

    nome, idade = saudacao()
    questionario(dados)

    simular = forca_opcao(['sim', 'não'], "\nVocê gostaria de realizar a simulação de montagem de um carro da Mahindra? ")
    if simular == 'sim':
        simulador_montagem(dados)

    promover_formula_e()
    print("\n✨ Obrigado por participar da experiência SustenRace! Continue inovando! 🌍")

if __name__ == "__main__":
    main()
