public class Questao6a {
  
  public static void main(String args[]) {

    int[][] img = ImagemDigital.carregarImagem("./static/imagens/Fig0310(b)(washed_out_pollen_image).png");
    int[][] result = transformLinear(img);
    ImagemDigital.plotarImagem(result, "Transformação linear");
  }

  static int[][] transformLinear(int[][] img) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    int[][] result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (img[i][j] < 64) {
          result[i][j] = (int) (img[i][j] * 0.5);
        } else if (64 <= img[i][j] && img[i][j] <= 192) {
          result[i][j] = (int) (img[i][j] * 1.5 - 65);
        } else if (img[i][j] > 192) {
          result[i][j] = (int) (img[i][j] * 0.5 + 128);
        }
      }
    }

    return result;
  }
}