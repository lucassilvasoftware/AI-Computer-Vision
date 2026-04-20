# Visão computacional — processamento de imagens

Conjunto de scripts em Python para experimentos de visão computacional: conversão de espaços de cores, operações morfológicas, contornos e um fluxo principal (`main.py`) que aplica suavização e detecção de bordas com **Canny**, gera visualizações com Matplotlib e exporta imagens para análise (por exemplo, relatórios em LaTeX/Overleaf).

## Tecnologias

- Python 3
- OpenCV (`cv2`), NumPy, Matplotlib

## Como executar

1. Instale as dependências (ambiente virtual recomendado):

```bash
pip install opencv-python numpy matplotlib
```

2. As imagens de entrada em `main.py` referenciam a pasta `./imagens/` (por exemplo `GIRAFA.jpeg`, `SATELITE.jpeg`, `AVIAO.jpeg`). Ajuste os caminhos em `imagens` conforme seus arquivos.

3. Execute:

```bash
python main.py
```

Os arquivos de saída (PNG/JPG de etapas e comparações) são gravados no diretório de trabalho atual.

Os demais módulos (`espacoCores.py`, `operadorMorfologico.py`, `contorno.py`) podem ser executados individualmente, conforme o conteúdo de cada arquivo.
