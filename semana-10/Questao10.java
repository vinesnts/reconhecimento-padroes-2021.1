public class Questao10 {
  
  public static void main(String args[]) {

    double gama = .6;
    int[][][] img = ImagemDigital.carregarImagemCor("./static/imagens/Floresta.png");
    int[][][] floresta = Questao5.transformGama(img, gama);
    ImagemDigital.plotarImagemCor(floresta, "Floresta, gama: " + gama);
    
    int[][] img2 = ImagemDigital.carregarImagem("./static/imagens/Celula.png");
    int[][] celula = Questao1.imagemNegativa(img2);
    celula = Questao1.correcaoEscala(celula);
    ImagemDigital.plotarImagem(celula, "Celula, negativa");

    gama = 4;
    int[][][] img3 = ImagemDigital.carregarImagemCor("./static/imagens/GorisRaioni.jpg");
    img3 = Questao5.transformGama(img3, gama);
    ImagemDigital.plotarImagemCor(img3, "GorisRaioni, gama: " + gama);

    int[][] img4 = ImagemDigital.carregarImagem("./static/imagens/CВrebro.png");
    img4 = intervalo(img4);
    img4 = Questao1.correcaoEscala(img4);
    ImagemDigital.plotarImagem(img4, "Cérebro, gama: " + gama);
  }

  static int[][] intervalo(int[][] img) {
    if (img.length <= 0 || img[0].length <= 0) return null;

    int[][] result = new int[img.length][img[0].length];
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (150 <= img[i][j] && img[i][j] <= 255) {
          result[i][j] = 153;
        } else if (img[i][j] < 150) {
          result[i][j] = 25;
        }
      }
    }

    return result;
  }
}