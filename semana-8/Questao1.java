import java.util.ArrayList;

public class Questao1 {
  
  public static void main(String args[]) {
    int[][] imagem = ImagemDigital.carregarImagem("./static/figura1.png");

    ArrayList<Integer> novosPixeis = new ArrayList<Integer>();
    for (int i = 0; i < imagem.length; i++) {
      for (int j = 0; j < imagem[i].length; j++) {
        if (!novosPixeis.contains(imagem[i][j])) {
          novosPixeis.add(imagem[i][j]);
          System.out.println(imagem[i][j]);
        }
      }
    }
  }
}
