import numpy as np
import cv2
import matplotlib.pyplot as plt

def processar_imagem(caminho_imagem, nome_saida):
    """
    Processa uma imagem e gera a versão final com bordas em vermelho
    """
    # Carregar a imagem
    img = cv2.imread(caminho_imagem)
    if img is None:
        print(f"ERRO: Não foi possível carregar {caminho_imagem}")
        return None
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Converter para escala de cinza
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    
    # Aplicar filtro de suavização
    kernel_size = 5
    img_blur = cv2.blur(img_gray, ksize=(kernel_size, kernel_size))
    
    # Obter valor máximo para calcular thresholds
    a = img_blur.max()
    
    # Detecção de bordas com Canny
    threshold1 = a / 2
    threshold2 = a / 2
    edges = cv2.Canny(image=img_blur, threshold1=threshold1, threshold2=threshold2)
    
    # Criar imagem de saída com bordas em vermelho
    img_output = img_rgb.copy()
    img_output[edges == 255] = [255, 0, 0]
    
    # Estatísticas
    num_pixels_borda = np.sum(edges == 255)
    percentual = 100 * num_pixels_borda / edges.size
    
    # Criar figura com 4 etapas do processamento (2x2)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Imagem original
    axes[0, 0].imshow(img_rgb)
    axes[0, 0].set_title('Imagem Original', fontsize=12, fontweight='bold')
    axes[0, 0].axis('off')
    
    # Escala de cinza
    axes[0, 1].imshow(img_gray, cmap='gray')
    axes[0, 1].set_title('Escala de Cinza', fontsize=12, fontweight='bold')
    axes[0, 1].axis('off')
    
    # Bordas detectadas
    axes[1, 0].imshow(edges, cmap='gray')
    axes[1, 0].set_title('Bordas Detectadas (Canny)', fontsize=12, fontweight='bold')
    axes[1, 0].axis('off')
    
    # Resultado final
    axes[1, 1].imshow(img_output)
    axes[1, 1].set_title('Bordas em Vermelho', fontsize=12, fontweight='bold')
    axes[1, 1].axis('off')
    
    plt.tight_layout()
    plt.savefig(f'{nome_saida}_processamento.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Criar figura comparativa (Original vs Resultado)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Imagem original
    axes[0].imshow(img_rgb)
    axes[0].set_title('Imagem Original', fontsize=14, fontweight='bold')
    axes[0].axis('off')
    
    # Resultado final
    axes[1].imshow(img_output)
    axes[1].set_title('Bordas em Vermelho', fontsize=14, fontweight='bold')
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.savefig(f'{nome_saida}_comparacao.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Salvar apenas a imagem final
    plt.figure(figsize=(10, 8))
    plt.imshow(img_output)
    plt.title(f'{nome_saida.upper()} - Detecção de Bordas (Canny)', 
              fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f'{nome_saida}_final.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Salvar também em formato JPG
    cv2.imwrite(f'{nome_saida}_final.jpg', 
                cv2.cvtColor(img_output, cv2.COLOR_RGB2BGR))
    
    print(f"\n{'='*60}")
    print(f"Processamento de {nome_saida.upper()} concluído!")
    print(f"{'='*60}")
    print(f"Número de pixels de borda detectados: {num_pixels_borda:,}")
    print(f"Percentual de bordas na imagem: {percentual:.2f}%")
    print(f"Total de pixels: {edges.size:,}")
    print(f"Dimensões da imagem: {img_rgb.shape[1]} x {img_rgb.shape[0]} pixels")
    print(f"\nArquivos gerados:")
    print(f"  - {nome_saida}_processamento.png (4 etapas do processo)")
    print(f"  - {nome_saida}_comparacao.png (Original vs Resultado)")
    print(f"  - {nome_saida}_final.png (Apenas resultado)")
    print(f"  - {nome_saida}_final.jpg (Apenas resultado em JPG)")
    
    return {
        'nome': nome_saida,
        'pixels_borda': num_pixels_borda,
        'percentual': percentual,
        'total_pixels': edges.size,
        'dimensoes': (img_rgb.shape[1], img_rgb.shape[0])
    }

# Lista de imagens para processar
imagens = [
    ('./imagens/GIRAFA.jpeg', 'girafa'),
    ('./imagens/SATELITE.jpeg', 'satelite'),
    ('./imagens/AVIAO.jpeg', 'aviao')
]

# Processar todas as imagens
resultados = []
for caminho, nome in imagens:
    print(f"\nProcessando {nome.upper()}...")
    resultado = processar_imagem(caminho, nome)
    if resultado:
        resultados.append(resultado)

# Criar tabela comparativa
if len(resultados) > 0:
    print("\n" + "="*80)
    print("RESUMO COMPARATIVO - TODAS AS IMAGENS")
    print("="*80)
    print(f"\n{'Métrica':<35} {'GIRAFA':>14} {'SATELITE':>14} {'AVIAO':>14}")
    print("-"*80)
    
    if len(resultados) == 3:
        print(f"{'Pixels de borda detectados':<35} {resultados[0]['pixels_borda']:>14,} {resultados[1]['pixels_borda']:>14,} {resultados[2]['pixels_borda']:>14,}")
        print(f"{'Percentual de bordas (%)':<35} {resultados[0]['percentual']:>14.2f} {resultados[1]['percentual']:>14.2f} {resultados[2]['percentual']:>14.2f}")
        print(f"{'Total de pixels':<35} {resultados[0]['total_pixels']:>14,} {resultados[1]['total_pixels']:>14,} {resultados[2]['total_pixels']:>14,}")
        dim0 = f"{resultados[0]['dimensoes'][0]}x{resultados[0]['dimensoes'][1]}"
        dim1 = f"{resultados[1]['dimensoes'][0]}x{resultados[1]['dimensoes'][1]}"
        dim2 = f"{resultados[2]['dimensoes'][0]}x{resultados[2]['dimensoes'][1]}"
        print(f"{'Dimensões (largura x altura)':<35} {dim0:>14} {dim1:>14} {dim2:>14}")
    
    print("="*80)

# Criar figura com as três imagens processadas lado a lado
if len(resultados) == 3:
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    for idx, (caminho, nome) in enumerate(imagens):
        img = cv2.imread(caminho)
        if img is not None:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
            img_blur = cv2.blur(img_gray, ksize=(5, 5))
            a = img_blur.max()
            edges = cv2.Canny(image=img_blur, threshold1=a/2, threshold2=a/2)
            img_output = img_rgb.copy()
            img_output[edges == 255] = [255, 0, 0]
            
            axes[idx].imshow(img_output)
            axes[idx].set_title(f'{nome.upper()}\n({resultados[idx]["percentual"]:.2f}% bordas)', 
                              fontsize=12, fontweight='bold')
            axes[idx].axis('off')
    
    plt.tight_layout()
    plt.savefig('todas_imagens_comparacao.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("\n✅ Arquivo adicional gerado:")
    print("  - todas_imagens_comparacao.png (GIRAFA, SATELITE e AVIAO lado a lado)")

print("\n🎉 Todos os arquivos foram gerados com sucesso!")
print("\n📁 Organize os arquivos na seguinte estrutura para o Overleaf:")
print("   images/")
print("   └── Results/")
print("       ├── girafa_processamento.png")
print("       ├── girafa_comparacao.png")
print("       ├── satelite_processamento.png")
print("       ├── satelite_comparacao.png")
print("       ├── aviao_processamento.png")
print("       ├── aviao_comparacao.png")
print("       └── todas_imagens_comparacao.png")