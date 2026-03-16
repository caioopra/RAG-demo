import matplotlib.pyplot as plt


def gerar_grafico_interativo():
    # Cria a figura em um tamanho excelente para apresentação
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection="3d")

    # Palavras do nosso exemplo
    words = ["Deploy", "Pipeline", "Homologação", "Férias", "Holerite", "Abacaxi"]

    # Cluster Tech (Engenharia) - Azul (Afastados, mas na mesma região "vetorial")
    x_tech = [10, 20, 5]
    y_tech = [10, 5, 20]
    z_tech = [10, 15, 5]

    # Cluster RH - Verde (Em outra região distante do gráfico)
    x_hr = [70, 80]
    y_hr = [70, 60]
    z_hr = [70, 80]

    # Outlier (Aleatório) - Vermelho (Completamente isolado no espaço)
    x_rand = [90]
    y_rand = [10]
    z_rand = [90]

    # Unindo as coordenadas
    xs = x_tech + x_hr + x_rand
    ys = y_tech + y_hr + y_rand
    zs = z_tech + z_hr + z_rand

    # Definindo as cores
    colors = ["blue", "blue", "blue", "green", "green", "red"]

    # Plotando as esferas/pontos
    ax.scatter(xs, ys, zs, c=colors, s=150, alpha=0.8, edgecolors="k")

    # Adicionando os textos (labels) com espaçamento e fundo translúcido para leitura
    for i, word in enumerate(words):
        # A tag bbox cria aquele fundo branco translúcido pra não misturar o texto com as linhas
        ax.text(
            xs[i] + 2,
            ys[i] + 2,
            zs[i] + 2,
            word,
            fontsize=12,
            fontweight="bold",
            bbox=dict(facecolor="white", alpha=0.7, edgecolor="none", pad=2),
        )

    # Configurações de Título e Eixos
    ax.set_title(
        "Representação Visual de Embeddings\n(Semântica no Espaço Vetorial)",
        fontsize=16,
        pad=30,
    )
    ax.set_xlabel("Dim X (Contexto de Engenharia)", labelpad=10)
    ax.set_ylabel("Dim Y (Contexto Administrativo/RH)", labelpad=10)
    ax.set_zlabel("Dim Z (Contexto Alimentar)", labelpad=10)

    # Ajustando o ângulo de visão inicial
    ax.view_init(elev=25, azim=45)

    print("Salvando a imagem estática para os slides...")
    plt.savefig("embeddings_3d_interativo.png", bbox_inches="tight")

    print("Abrindo janela interativa. Use o mouse para rotacionar e dar zoom!")
    # O comando abaixo é o que "trava" o script e abre a janela interativa onde você
    # pode brincar com o 3D na frente da sua banca.
    plt.show()


if __name__ == "__main__":
    gerar_grafico_interativo()
