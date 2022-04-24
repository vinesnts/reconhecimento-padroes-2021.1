public class Questao2 {
  
  public static void main(String args[]) {

    int[][] img1 = ImagemDigital.carregarImagem("./static/imagens/Fig0228(a)(angiography_mask_image).png");
    int[][] img2 = ImagemDigital.carregarImagem("./static/imagens/Fig0228(b)(angiography_live_ image).png");

    ImagemDigital.plotarImagem(diferenca(img2, img1), "Diferença");
  }

  static int[][] diferenca(int[][] img1, int[][] img2) {
    int[][] result = null;
    if (img1.length <= 0 || img1.length != img2.length)
      return result;
    
    result = new int[img1.length][img1[0].length];
    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        result[i][j] = img1[i][j] - img2[i][j];
        if (result[i][j] < 0) result[i][j] = 0;
      }
    }
    return result;
  }
}