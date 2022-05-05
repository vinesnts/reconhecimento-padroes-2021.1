import java.util.ArrayList;
import java.lang.Math;

public class Questao5 {
  
  public static void main(String args[]) {

    int[][][] img = ImagemDigital.carregarImagemCor("./static/imagens/a4d88a27b6e6f33558a8e675b742-1458995.jpg");
    double[] gamas = {0.5, 2, 5};
    for (int i = 0; i < gamas.length; i++) {
      int[][][] result = transformGama(img, gamas[i]);
      ImagemDigital.plotarImagemCor(result, "Transformação gama: " + gamas[i]);

    }
  }

  static int[][][] transformGama(int[][][] img, double gama) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    double c = getC(img, gama);
    int[][][] result = new int[img.length][img[0].length][3];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        for (int k = 0; k < img[i][j].length; k++) {
          result[i][j][k] = (int) Math.min(255, (c * Math.pow(img[i][j][k], gama)));
        }
      }
    }

    return result;
  }

  static double getC(int[][][] img, double gama) {
    ArrayList<Integer> tons = tons(img);

    return Math.pow((tons.size() - 1), (1 - gama));
  }

  static ArrayList<Integer> tons(int[][][] img) {
    ArrayList<Integer> tons = new ArrayList<Integer>();

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        for (int k = 0; k < img[i][j].length; k++) {
          if (!tons.contains(img[i][j][k])) tons.add(img[i][j][k]);

        }
      }
    }

    return tons;
  }
}