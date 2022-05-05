import java.lang.Integer;

public class Questao8 {
  
  public static void main(String args[]) {

    int[][] img = ImagemDigital.carregarImagem("./static/imagens/Fig0314(a)(100-dollars).png");
    int[] bits = {0,1,2,3,4,5,6,7};
    for (int i = 0; i < bits.length; i++) {
      int[][] result = fatiar(img, bits[i]);
      ImagemDigital.plotarImagem(result, "Questão 8, " + (i + 1) + "º bit menos significativo");
    }
  }

  static int[][] fatiar(int[][] img, int bit) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    int[][] result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        result[i][j] = 255 * ((img[i][j] / (int) Math.pow(2, bit)) % 2);
      }
    }

    return result;
  }
}