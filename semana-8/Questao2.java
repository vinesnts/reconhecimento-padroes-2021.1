public class Questao2 {
  
  public static void main(String args[]) {
    int[][] imagemGerada1 = new int[300][300];
    int[][] imagemGerada2 = new int[300][300];
    int[][] imagemGerada3 = new int[300][300];

    for (int i = 0; i < imagemGerada1.length; i++) {
      for (int j = 0; j < imagemGerada1[i].length; j++) {
        if (j < 100 || j > 200 || i < 100 || i > 200) {
          imagemGerada1[i][j] = 0;
          imagemGerada2[i][j] = 64;
          imagemGerada3[i][j] = 192;
        } else {
          imagemGerada1[i][j] = 128;
          imagemGerada2[i][j] = 128;
          imagemGerada3[i][j] = 128;
        }
      }
    }

    ImagemDigital.plotarImagem(imagemGerada1, "imagem1");
    ImagemDigital.plotarImagem(imagemGerada2, "imagem2");
    ImagemDigital.plotarImagem(imagemGerada3, "imagem3");
  }
}
