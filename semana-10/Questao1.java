import java.util.ArrayList;

public class Questao1 {
  
  public static void main(String args[]) {

    int[][] img = ImagemDigital.carregarImagem("./static/imagens/Fig0304(a)(breast_digital_Xray).png");
    int[][] result = imagemNegativa(img);
    result = correcaoEscala(result);

    ImagemDigital.plotarImagem(result, "Imagem negativa");
  }

  static int[][] imagemNegativa(int[][] img) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    ArrayList<Integer> tonsCinza = tonsCinza(img);
    int[][] result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        result[i][j] = tonsCinza.size() - 1 - img[i][j];
      }
    }

    return result;
  }

  static ArrayList<Integer> tonsCinza(int[][] img) {
    ArrayList<Integer> tonsCinza = new ArrayList<Integer>();

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (!tonsCinza.contains(img[i][j])) tonsCinza.add(img[i][j]);
      }
    }

    return tonsCinza;
  }

  static int max(int[][] img) {
    ArrayList<Integer> tonsCinza = tonsCinza(img);
    int max = 0;

    for (int i = 0; i < tonsCinza.size(); i++) {
      if (tonsCinza.get(i) > max) max = tonsCinza.get(i);
    }

    return max;
  }

  static int min(int[][] img) {
    ArrayList<Integer> tonsCinza = tonsCinza(img);
    int min = 255;

    for (int i = 0; i < tonsCinza.size(); i++) {
      if (tonsCinza.get(i) < min) min = tonsCinza.get(i);
    }

    return min;
  }

  static int[][] correcaoEscala(int[][] img) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    int max = max(img);
    int min = min(img);
    int[][] result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        result[i][j] = 255 * (img[i][j] - min) / (max - min);
      }
    }

    return result;
  }
}