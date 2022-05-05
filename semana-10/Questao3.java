import java.util.ArrayList;
import java.lang.Math;

public class Questao3 {
  
  public static void main(String args[]) {

    int[][] img = ImagemDigital.carregarImagem("./static/imagens/Fig0308(a)(fractured_spine).png");
    double[] gamas =  {0.6, 0.5, 0.4};
    for (int i = 0; i < gamas.length; i++) {
      int[][] result = transformLog(img, gamas[i]);
      ImagemDigital.plotarImagem(result, "Transformação log: " + gamas[i]);

    }
  }

  static int[][] transformLog(int[][] img, double logBase) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    double c = getC(img, logBase);
    int[][] result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        result[i][j] = (int) (c * (Math.log(1 + img[i][j]) / Math.log(logBase)));
      }
    }

    return result;
  }

  static double getC(int[][] img, double logBase) {
    ArrayList<Integer> tonsCinza = Questao1.tonsCinza(img);

    return (tonsCinza.size() - 1) / (Math.log(tonsCinza.size()) / Math.log(logBase));
  }

  static int[][][] transformLogCor(int[][][] img, double logBase) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    double c = Questao5.getC(img, logBase);
    int[][][] result = new int[img.length][img[0].length][3];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        for (int k = 0; k < 3; k++) {
          result[i][j][k] = (int) (c * (Math.log(1 + img[i][j][k]) / Math.log(logBase)));
        }
      }
    }

    return result;
  }
}