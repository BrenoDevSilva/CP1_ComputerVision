# Checkpoint 1 - Visão Computacional 🦇

## 📌 Descrição do Projeto
Este projeto consiste em um pipeline de processamento de imagem para detecção e contagem de objetos (neste caso, morcegos). O sistema utiliza técnicas de binarização, morfologia e análise de contornos para identificar elementos em um cenário bimodal.

## Autores - 4ESPW
- Breno Silva (RM99275)
- Gabriela Trevisan (RM99500)

## 🧠 Parte Conceitual

### 1. Por que a conversão para escala de cinza é importante?
A conversão reduz a complexidade da imagem, passando de três canais de cor (RGB) para apenas um (intensidade). Isso diminui o custo computacional e remove informações de cores que podem gerar ruído em algoritmos de segmentação que dependem apenas do contraste entre objeto e fundo.

### 2. O que o histograma revela sobre a imagem?
O histograma mostra a distribuição dos níveis de intensidade dos pixels. Ele revela se a imagem está subexposta ou superexposta e se possui um contraste adequado. No nosso caso, ele ajuda a confirmar se a imagem é bimodal, o que valida o uso do algoritmo de Otsu para segmentação.

### 3. Por que aplicar morfologia antes de detectar contornos?
A morfologia (como o **fechamento**) é essencial para limpar a imagem binária. Ela une partes fragmentadas de um mesmo objeto e preenche buracos internos. Sem isso, o algoritmo de contornos poderia identificar múltiplos objetos onde existe apenas um, gerando uma contagem errada.

### 4. Cenário Real de Aplicação
Este sistema pode ser aplicado no **Monitoramento Biológico Automatizado**. Pesquisadores podem instalar câmeras em cavernas para contar populações de morcegos de forma não invasiva, permitindo o acompanhamento de espécies sem interferência humana direta.

## 🚀 Como Executar
1. Instale as dependências: `pip install opencv-python matplotlib`
2. Garanta que a imagem `morcegos.jpg` esteja na raiz do projeto.
3. Execute o arquivo principal:
   ```bash
   python main.py

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- OpenCV (Processamento de Imagem)
- Matplotlib (Visualização de Histogramas)
