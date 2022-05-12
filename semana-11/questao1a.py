import numpy as np

from PIL import Image
import matplotlib.pyplot as plt

img_list = [
  'Fig0320(1)(top_left)',
  'Fig0320(2)(2nd_from_top)',
  'Fig0320(3)(third_from_top)',
  'Fig0320(4)(bottom_left)',
  'Fig0323(a)(mars_moon_phobos)',
  'Fig0309(a)(washed_out_aerial_image)',
  'Fig0308(a)(fractured_spine)',
]

def load_image_as_array(path: str):
  img = Image.open(path, 'r')
  img_array = np.asarray(img)
  return img_array

def tons_cinza(img_array) -> dict:
  tons_cinza = {}
  for row in img_array:
    for tom in row:
      if tom not in tons_cinza:
        tons_cinza[tom] = 1
      else:
        tons_cinza[tom] += 1
  return tons_cinza

def hist_data(img_array) -> dict:
  tons = tons_cinza(img_array)
  M = len(img_array)
  N = len(img_array[0])
  hist_data = {}
  for i in range(0, 255):
    if i in tons:
      hist_data[i] = tons[i] / (M * N)
    else:
      hist_data[i] = 0
  return hist_data

def plot_hist(hist_data, filename: str):
  plt.clf()
  plt.bar(hist_data.keys(), hist_data.values())
  plt.savefig(filename)

def main():
  for img in img_list:
    img_array = load_image_as_array(f'./static/imagens/{img}.png')
    img_array = hist_data(img_array)
    plot_hist(img_array, f'./static/questao1a_{img}.png')
    print(f'''- Imagem: {img}
![{img}](./static/questao1a_{img}.png)''')

if __name__ == '__main__':
  main()