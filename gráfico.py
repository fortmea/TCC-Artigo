import numpy as np
import matplotlib.pyplot as plt

# Dados
tamanhos_pacote = [50000, 5000, 1000]
protocolos = ['TCP', 'UDP']
tempos_tcp = [14, 4, 3]
tempos_udp = [6, 2, 2]

# Configurar largura da barra
largura_barra = 0.35

# Calcular a posição das barras
posicoes_tcp = np.arange(len(tamanhos_pacote))
posicoes_udp = posicoes_tcp + largura_barra

# Criar barras para TCP e UDP
barra_tcp = plt.bar(posicoes_tcp, tempos_tcp, largura_barra, label='TCP')
barra_udp = plt.bar(posicoes_udp, tempos_udp, largura_barra, label='UDP')

# Adicionar linhas de conexão entre TCP e UDP com rótulos de diferença
for i in range(len(tamanhos_pacote)):
    plt.plot([posicoes_tcp[i] + largura_barra / 2, posicoes_udp[i] + largura_barra / 2],
             [tempos_tcp[i], tempos_udp[i]], color='gray', linestyle='--', linewidth=1)
    diferenca = tempos_udp[i] - tempos_tcp[i]
    plt.text(posicoes_tcp[i] + largura_barra / 2, (tempos_tcp[i] + tempos_udp[i]) / 2, f'{diferenca} ms',
             ha='center', va='center', bbox=dict(facecolor='white', edgecolor='white', boxstyle='round'),
             fontsize=14)  # Ajuste o tamanho da fonte aqui

# Ajustar tamanho das fontes
plt.xlabel('Tamanho do Pacote (Bytes)', fontsize=10)
plt.ylabel('Tempo de Resposta (ms)', fontsize=10)
plt.title('Tempo de Resposta por Protocolo e Tamanho do Pacote', fontsize=12)
plt.xticks(posicoes_tcp + largura_barra / 2, tamanhos_pacote, fontsize=8)  # Ajuste o tamanho da fonte aqui
plt.yticks(fontsize=14)  # Ajuste o tamanho da fonte aqui
plt.legend(fontsize=14)  # Ajuste o tamanho da fonte aqui

# Exibir o gráfico
plt.show()
