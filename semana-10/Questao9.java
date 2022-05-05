import java.lang.Integer;

public class Questao9 {
  
  public static void main(String args[]) {

    int[][] img = ImagemDigital.carregarImagem("./static/imagens/Fig0314(a)(100-dollars).png");
    int[][] bit7 = fatiar(img, 6);
    int[][] bit8 = fatiar(img, 7);
    int[][] result = combinar(bit7, bit8);
    ImagemDigital.plotarImagem(result, "Questão 9");
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

  static int[][] combinar(int[][] img1, int[][] img2) {
    int[][] result = null;
    if (img1.length <= 0 || img1.length != img2.length)
      return result;
    
    result = new int[img1.length][img1[0].length];
    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        char binary1 = String.format("%8s", Integer.toBinaryString(img1[i][j])).replaceAll(" ", "0").charAt(1);
        char binary2 = String.format("%8s", Integer.toBinaryString(img2[i][j])).replaceAll(" ", "0").charAt(0);
        result[i][j] = (binary1=='1' ? (int) Math.pow(2, 6) : 0) + (binary2=='1' ? (int) Math.pow(2,7) : 0);
      }
    }
    return result;
  }
}