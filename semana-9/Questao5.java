public class Questao5 {
  
  public static void main(String args[]) {
    int n = 10;
    int[][] result = ImagemDigital.carregarImagem("./static/ruido/lena1.png");
    for (int i = 2; i <= n; i++) {
      int[][] lena = ImagemDigital.carregarImagem("./static/ruido/lena" + i + ".png");
      result = soma(result, lena);
    }
    result = media(result, n);
    ImagemDigital.plotarImagem(result, "Média de 10");
  }

  static int[][] soma(int[][] img1, int[][] img2) {
    int[][] result = null;
    if (img1.length <= 0 || img1.length != img2.length)
      return result;
    
    result = new int[img1.length][img1[0].length];
    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        result[i][j] = img1[i][j] + img2[i][j];
      }
    }
    return result;
  }

  static int[][] media(int[][] img, int n) {
    int[][] result = null;
    if (img.length <= 0)
      return result;
    
    result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        result[i][j] = img[i][j] / n;
      }
    }
    return result;
  }
}