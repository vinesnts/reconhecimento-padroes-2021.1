public class Questao1 {
  
  public static void main(String args[]) {

    int[][] lena = ImagemDigital.carregarImagem("./static/imagens/lena_gray_512.png");
    int[][] mandril = ImagemDigital.carregarImagem("./static/imagens/mandril_gray.png");

    float[] alphas = { 0.25F, 0.50F, 0.75F };
    for (float alpha : alphas) {
      ImagemDigital.plotarImagem(somaPonderada(lena, mandril, alpha), "Soma ("+alpha+")");
    }
  }

  static int[][] somaPonderada(int[][] img1, int[][] img2, float alpha) {
    int[][] result = null;
    if (img1.length <= 0 || img1.length != img2.length)
      return result;
    
    result = new int[img1.length][img1[0].length];
    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        result[i][j] = (int) (alpha * img1[i][j] + (1 - alpha) * img2[i][j]);
      }
    }
    return result;
  }
}