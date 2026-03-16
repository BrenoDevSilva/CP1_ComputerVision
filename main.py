from checkpoint1 import *
import cv2

if __name__ == "__main__":
    # 1. carregar
    img_color = load_image("morcegos.jpg")
    
    # 2. cinza
    gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    # 3. histograma
    plot_histogram(gray)
    
    # 4. segmentação (otsu)
    binary = apply_segmentation(gray)
    cv2.imshow("Passo 4 - Binaria (Otsu)", binary)
    cv2.waitKey(0)
    
    # 5. morfologia
    cleaned = apply_morphology(binary)
    cv2.imshow("Passo 5 - Morfologia", cleaned)
    cv2.waitKey(0)
    
    # 6. detecção de Contornos
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 7 e 8. desenhar bounding boxes e filtrar área
    resultado, total = draw_results(img_color, contours, area_minima=100)
    
    # exibir resultado final e contagem
    print(f"Quantidade total de objetos detectados: {total}")
    cv2.putText(resultado, f"Total: {total}", (20, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow("Resultado Final - Checkpoint 1", resultado)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
================================================================
RESPOSTAS CONCEITUAIS (CHECKPOINT 1)
================================================================
1. IMPORTÂNCIA DA ESCALA DE CINZA:
   A conversão reduz a complexidade da imagem de 3 canais (RGB) para 1. 
   Isso elimina informações de cor que podem ser irrelevantes para 
   detectar formas, reduz o custo computacional e facilita a binarização.

2. O QUE O HISTOGRAMA REVELA:
   Revela a distribuição de brilho. Se houver dois picos claros 
   (bimodal), indica que há um bom contraste entre objeto e fundo, 
   o que torna o algoritmo de Otsu muito eficiente.

3. MORFOLOGIA ANTES DOS CONTORNOS:
   A morfologia (como o fechamento) serve para unir partes 
   fragmentadas do objeto e tapar buracos internos. Sem isso, um 
   único morcego poderia ser contado como vários pedaços pequenos.

4. CENÁRIO REAL:
   Monitoramento biológico automatizado. Um sistema que conta 
   animais em cavernas ou florestas através de câmeras fixas, 
   ajudando pesquisadores a estimar populações sem contato humano.
================================================================
'''