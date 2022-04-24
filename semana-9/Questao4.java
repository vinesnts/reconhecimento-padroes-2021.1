public class Questao4 {
  
  public static void main(String args[]) {

    int[][] img1 = ImagemDigital.carregarImagem("./static/imagens/Fig0230(a)(dental_xray).png");
    int[][] img2 = ImagemDigital.carregarImagem("./static/imagens/Fig0230(b)(dental_xray_mask).png");
    int[][] img3 = ImagemDigital.carregarImagem("./static/imagens/Fig0230(b)(dental_xray_mask)_1.png");
    int[][] img4 = ImagemDigital.carregarImagem("./static/imagens/Fig0230(b)(dental_xray_mask)_2.png");

    ImagemDigital.plotarImagem(produto(img1, img2), "Produto");
    ImagemDigital.plotarImagem(produto(img1, img3), "Produto");
    ImagemDigital.plotarImagem(produto(img1, img4), "Produto");
  }

  static int[][] produto(int[][] img1, int[][] img2) {
    int[][] result = null;
    if (img1.length <= 0 || img1.length != img2.length)
      return result;
    
    result = new int[img1.length][img1[0].length];
    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        result[i][j] = (img1[i][j] * img2[i][j]) / 255;
      }
    }
    return result;
  }
}