import java.lang.Integer;

public class Questao8 {
  
  public static void main(String args[]) {

    int[][] img = ImagemDigital.carregarImagem("./static/imagens/Fig0314(a)(100-dollars).png");
    int[] bits = {7,6,5,4,3,2,1,0};
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
        String binary = String.format("%8s", Integer.toBinaryString(img[i][j])).replaceAll(" ", "0");
        for (int k = 0; k < binary.toCharArray().length; k++) {
          if (k == bit && binary.charAt(bit) == '1') {
            result[i][j] = img[i][j];
          }
        }
      }
    }

    return result;
  }
}