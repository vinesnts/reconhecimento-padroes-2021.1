public class Questao3 {
  
  public static void main(String args[]) {

    int[][] img1 = ImagemDigital.carregarImagem("./static/imagens/Fig0229(a)(tungsten_filament_shaded).png");
    int[][] img2 = ImagemDigital.carregarImagem("./static/imagens/Fig0229(b)(tungsten_sensor_shading).png");

    ImagemDigital.plotarImagem(divisao(img1, img2), "Divisão");
  }

  static int[][] divisao(int[][] img1, int[][] img2) {
    int[][] result = null;
    if (img1.length <= 0 || img1.length != img2.length)
      return result;
    
    result = new int[img1.length][img1[0].length];
    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        result[i][j] = (int) (((float) img1[i][j] / (float) img2[i][j]) * 255F);
      }
    }
    return result;
  }
}