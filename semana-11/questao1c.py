import numpy as np

from PIL import Image
import matplotlib.pyplot as plt

from questao1a import img_list, load_image_as_array, plot_hist, tons_cinza

def equalizar_hist(img):
  tons = tons_cinza(img)
  M = len(img)
  N = len(img[0])
  saida = {}

  tons_order = {}
  for i in range(0, 255):
    if i in tons:
      tons_order[i] = tons[i]
    else:
      tons_order[i] = 0

  for i, (tom, _) in enumerate(tons_order.items()):
    soma = 0
    n = list(tons_order.items())[0: i + 1]
    for tom1, qtd in n:
      soma += (len(tons_order) - 1) * (qtd / (M * N))
    if int(soma) in saida:
      saida[int(soma)] += qtd
    else:
      saida[int(soma)] = qtd
    
  saida_order = {}
  for i in range(0, 255):
    if i in saida:
      saida_order[i] = saida[i]
    else:
      saida_order[i] = 0

  return saida_order

def main():
  for img in img_list:
    img_array = load_image_as_array(f"./static/imagens/{img}.png")
    img_array = equalizar_hist(img_array)
    plot_hist(img_array, f"./static/questao1c_{img}.png")
    print(f'''- Imagem: {img}
![{img}](./static/questao1c_{img}.png)''')

if __name__ == '__main__':
  main()