import random #importa a biblioteca para gerar números aleatórios
import matplotlib
import matplotlib.pyplot as plt #Importa a Matplotlib usada para criar gráficos

# Organização do código, é dividido em pequenas funções com objetivos específicos
# Funções internas definidas dentro da main
# Geração de dados - criados com a biblioteca random
# Visualização de dados - o matplotlib permite transformar números em gráficos


def main():
    # Função interna para gerar vendas aleatórias
    def gerar_vendas(meses):
        return [random.randint(80,220) for _ in meses]
    
    # Função interna para calcular a média
    def calcular_media(valores):
        return sum(valores) / len(valores)
    
    # Função interna para mostrar um resumo no terminal
    def mostrar_resumo(meses, vendas,media):
        print("=== RELATÓRIO DE VENDAS ===")
        for mes, valor in zip(meses, vendas):
            print(f"{mes}: {valor} vendas")

            melhor_mes = meses[vendas.index(max(vendas))]
            pior_mes = meses[vendas.index(min(vendas))]

            print(f"\nMédia de vendas: {media:.2f}")
            print(f"Melhor mês: {melhor_mes}")
            print(f"Pior mês: {pior_mes}")

    # Função interna para criar o gráfico
    def criar_grafico(meses, vendas, media):
        plt.figure(figsize=(10, 6))

        barras = plt.bar(meses, vendas) # ptl.bar() cria um gráfico de barras

        #Desenha uma Linha horizontal, neste caso representa a média
        plt.axhline(media, linestyle="--", label=f"Média: {media:.1f}")

        #Títulos e nomes dos eixos
        plt.title("Vendas Mensais do Mini-Projeto")
        plt.xlabel("Meses")
        plt.ylabel("Número de Vendas")

        #Grelha horizontal
        plt.grid(axis="y", linestyle=":", alpha=0.6)

        #Valores em cima das barras
        plt.bar_label(barras,padding=3) #Escreve o valor por cima de cada barra

        #Legenda
        plt.legend()

        #Ajusta o layout
        plt.tight_layout()

        #Mostra o gráfico
        plt.show()

    #Dados principais do programa

    meses = ["Jan","Fev","Mar","Abr","Mai","Jun"]
    vendas = gerar_vendas(meses)
    media = calcular_media(vendas)

    #Mostrar resultados
    mostrar_resumo(meses, vendas, media)
    criar_grafico(meses, vendas, media)

if __name__ == "__main__":
    main()