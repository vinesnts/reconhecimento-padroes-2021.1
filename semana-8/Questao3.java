import java.math.*;

public class Questao3 {

  public static void main(String args[]) {
    int[][][] imagem = ImagemDigital.carregarImagemCor("./static/eu.png");
    int[][][] face = new int[320][380][3];
    int[][][] imagemB = new int[825][824][3];
    int[][][] imagemC = new int[825][824][3];
    int[][][] imagemD = new int[825][824][3];
    int[][][] imagemE = new int[825][824][3];
    int[][][] imagemF = new int[825][824][3];

    for (int i = 0; i < imagem.length; i++) {
      for (int j = 0; j < imagem[i].length; j++) {
        if (
          (imagem[i][j][0] > imagem[i][j][1] && imagem[i][j][0] > imagem[i][j][2])
          && (imagem[i][j][0] > 20 && imagem[i][j][1] > 20 && imagem[i][j][2] > 20)) {
          face[Math.max(0, i/2-90)][Math.max(0, j/2-30)] = imagem[i][j];
        }
        imagemB[i][j][0] = imagem[i][j][0];
        imagemB[i][j][1] = imagem[i][j][1];
        imagemB[i][j][2] = Math.min(255, imagem[i][j][2] + 40);
        imagemC[i][j][0] = Math.min(255, imagem[i][j][0] + 40);
        imagemC[i][j][1] = Math.min(255, imagem[i][j][1] + 40);
        imagemC[i][j][2] = Math.min(255, imagem[i][j][2] + 40);
        imagemD[i][j][0] = Math.max(0, imagem[i][j][0] + (-40));
        imagemD[i][j][1] = Math.max(0, imagem[i][j][1] + (-40));
        imagemD[i][j][2] = Math.max(0, imagem[i][j][2] + (-40));
        imagemE[i][j][0] = Math.min(255, (int) (imagem[i][j][0] * 1.3));
        imagemE[i][j][1] = Math.min(255, (int) (imagem[i][j][1] * 1.3));
        imagemE[i][j][2] = Math.min(255, (int) (imagem[i][j][2] * 1.3));
        imagemF[i][j][0] = Math.min(255, (int) (imagem[i][j][0] * 0.7));
        imagemF[i][j][1] = Math.min(255, (int) (imagem[i][j][1] * 0.7));
        imagemF[i][j][2] = Math.min(255, (int) (imagem[i][j][2] * 0.7));
      }
    }

    // ImagemDigital.plotarImagemCor(imagem, "Eu");
    // ImagemDigital.plotarImagemCor(face, "Face");
    // ImagemDigital.plotarImagemCor(imagemB, "imagemB");
    // ImagemDigital.plotarImagemCor(imagemC, "imagemC");
    // ImagemDigital.plotarImagemCor(imagemD, "imagemD");
    // ImagemDigital.plotarImagemCor(imagemE, "imagemE");
    ImagemDigital.plotarImagemCor(imagemF, "imagemF");

  }
}