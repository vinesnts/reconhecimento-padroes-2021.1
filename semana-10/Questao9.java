import java.lang.Integer;

public class Questao9 {
  
  public static void main(String args[]) {

    int[][] img = ImagemDigital.carregarImagem("./static/imagens/Fig0314(a)(100-dollars).png");
    int[][] bit7 = fatiar(img, 1);
    int[][] bit8 = fatiar(img, 0);
    int[][] result = combinar(bit7, bit8);
    ImagemDigital.plotarImagem(result, "Questão 9");
  }

  static int[][] fatiar(int[][] img, int bit) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    int[][] result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        String binary = String.format("%8s", Integer.toBinaryString(img[i][j])).replaceAll(" ", "0");
        if (binary.charAt(bit) == '1') {
          result[i][j] = img[i][j];
        }
      }
    }

    return result;
  }

  static int[][] combinar(int[][] img1, int[][] img2) {
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
}