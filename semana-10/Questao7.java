public class Questao7 {
  
  public static void main(String args[]) {

    int[][] img = ImagemDigital.carregarImagem("./static/imagens/Fig0312(a)(kidney).png");
    int[][] resultA = questao7a(img);
    ImagemDigital.plotarImagem(resultA, "Questão 7 a");
    int[][] resultB = questao7b(img);
    ImagemDigital.plotarImagem(resultB, "Questão 7 b");
  }

  static int[][] questao7a(int[][] img) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    int[][] result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (150 <= img[i][j] && img[i][j] <= 255) {
          result[i][j] = 153;
        } else {
          result[i][j] = 25;
        }
      }
    }

    return result;
  }

  static int[][] questao7b(int[][] img) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    int[][] result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (150 <= img[i][j] && img[i][j] <= 200) {
          result[i][j] = 204;
        } else {
          result[i][j] = img[i][j];
        }
      }
    }

    return result;
  }
}