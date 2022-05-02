import java.util.ArrayList;
import java.lang.Math;

public class Questao4 {
  
  public static void main(String args[]) {

    int[][] img = ImagemDigital.carregarImagem("./static/imagens/Fig0309(a)(washed_out_aerial_image).png");
    double[] gamas = {3, 4, 5};
    for (int i = 0; i < gamas.length; i++) {
      int[][] result = transformGama(img, gamas[i]);
      result = Questao1.correcaoEscala(result);
      ImagemDigital.plotarImagem(result, "Transformação gama: " + gamas[i]);

    }
  }

  static int[][] transformGama(int[][] img, double gama) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    double c = getC(img, gama);
    int[][] result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        result[i][j] = (int) (c * Math.pow(img[i][j], gama));
      }
    }

    return result;
  }

  static double getC(int[][] img, double gama) {
    ArrayList<Integer> tonsCinza = Questao1.tonsCinza(img);

    return Math.pow((tonsCinza.size() - 1), (1 - gama));
  }
}