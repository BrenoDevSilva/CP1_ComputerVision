import cv2
import matplotlib.pyplot as plt

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise ValueError(f"Erro: Imagem '{path}' não encontrada.")
    return image

def plot_histogram(gray_image):
    plt.figure(figsize=(8, 4))
    plt.hist(gray_image.ravel(), bins=256, range=[0, 256], color='gray')
    plt.title("Histograma de Intensidade (Gray)")
    plt.xlabel("Intensidade")
    plt.ylabel("Quantidade de Pixels")
    plt.show()

def apply_segmentation(gray_image):
    # INV porque morcegos são escuros e queremos que o objeto vire BRANCO
    _, binary = cv2.threshold(
        gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )
    return binary

def apply_morphology(binary_image):
    # Kernel 5x5 para fechar buracos nos corpos dos morcegos
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    cleaned = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    return cleaned

def draw_results(original_img, contours, area_minima=500):
    img_copy = original_img.copy()
    count = 0
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        # --- LÓGICA DO BÔNUS: Filtro de área mínima ---
        if area > area_minima:
            count += 1
            x, y, w, h = cv2.boundingRect(cnt)
            
            # Desenha o retângulo
            cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Escreve a área acima do retângulo (Parte do Bônus)
            cv2.putText(img_copy, f"Area: {int(area)}", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            
    return img_copy, count