import numpy as np

from PIL import Image
import matplotlib.pyplot as plt

from questao1a import img_list, load_image_as_array, plot_hist, tons_cinza

def equalizar_img(img):
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

  new_image = img.copy()
  for i, _ in enumerate(img):
    for j, _ in enumerate(img[i]):
      soma = 0
      n = list(tons_order.items())[0: img[i][j] + 1]
      for _, qtd in n:
        soma += (len(tons_order) - 1) * (qtd / (M * N))
      new_image[i][j] = soma

  return new_image

def main():
  for img in img_list:
    img_array = load_image_as_array(f"./static/imagens/{img}.png")
    img_array = equalizar_img(img_array)
    Image.fromarray(img_array).save(f"./static/questao1b_{img}.png")
    print(f'''- Imagem: {img}
![{img}](./static/questao1b_{img}.png)''')

if __name__ == '__main__':
  main()