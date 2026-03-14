import cv2
import matplotlib.pyplot as plt
import numpy as np

def executar_checkpoint(image_path):
    # --- PASSO 1: Carregamento ---
    img = cv2.imread(image_path)
    if img is None:
        print("Erro: Imagem não encontrada.")
        return

    # --- PASSO 2: Escala de Cinza ---
    # Reduz a imagem de 3 canais (RGB) para 1 canal de intensidade
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # --- PASSO 3: Histograma ---
    # Mostra a distribuição de luz para validar a segmentação
    plt.figure(figsize=(8, 4))
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title("Passo 3: Histograma de Intensidade")
    plt.show()

    # --- PASSO 4: Segmentação (Otsu) ---
    # Transforma em preto e branco automaticamente
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # --- PASSO 5: Morfologia (Opening) ---
    # Limpa ruídos e suaviza as bordas
    kernel = np.ones((3,3), np.uint8)
    img_processed = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    # --- PASSO 6: Detecção de Contornos ---
    # Localiza as silhuetas dos objetos
    contornos, _ = cv2.findContours(img_processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # --- PASSO 7: Processamento e Filtro de Área ---
    img_final = img.copy()
    total_objetos = 0
    
    for cnt in contornos:
        area = cv2.contourArea(cnt)
        if area > 500: # Filtro para ignorar sujeiras
            x, y, w, h = cv2.boundingRect(cnt)
            # Desenha o retângulo verde
            cv2.rectangle(img_final, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Escreve a área individual em azul
            cv2.putText(img_final, f"Area: {int(area)}", (x, y-10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
            total_objetos += 1

    # --- PASSO 8: Resultado Final na Imagem ---
    # Adiciona o contador total no topo da imagem
    texto_total = f"Contagem Total: {total_objetos} objetos"
    cv2.putText(img_final, texto_total, (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Exibição das janelas
    print(f"Sucesso! {texto_total}")
    cv2.imshow("Etapa 5: Mascara Binaria (Morfologia)", img_processed)
    cv2.imshow("Etapa 8: Resultado Final", img_final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Para rodar, basta chamar a função com o nome do seu arquivo
executar_checkpoint('morcegos.jpg')