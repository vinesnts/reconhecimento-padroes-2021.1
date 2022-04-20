/*
 * GUI.java
 *
 * Created on 26 de Junho de 2006, 21:45
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import java.awt.image.PixelGrabber;
import java.awt.image.WritableRaster;
import java.io.File;
import java.io.IOException;
import java.util.Iterator;

import javax.imageio.ImageIO;
import javax.imageio.ImageWriter;
import javax.imageio.stream.ImageOutputStream;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

/**
 * Universidade Federal Rural de Pernambuco
 * 
 * Unidade Acad�mica de Garanhuns
 * 
 * Bacharelado em Ci�ncias da Computa��o 
 * 
 * Disciplina obrigat�ria: Reconhecimento de Padr�es 2013.1
 * 
 * @author Tiago Buarque Assun��o de Carvalho <tbac@cin.ufpe.br>
 * 
 */
public class ImagemDigital {

	private BufferedImage buffer;

	private JFrame frm;

	private Graphics tela;

	/** Creates a new instance of GUI */
	private ImagemDigital(int altura, int largura) {
		buffer = new BufferedImage(largura, altura, BufferedImage.TYPE_INT_RGB);
		tela = buffer.createGraphics();
		tela.setColor(Color.WHITE);
		tela.fillRect(0, 0, largura, altura);
	}

	/**
	 * 
	 * @param x
	 *            posi��o X do ponto na tela
	 * @param y
	 *            posi��o Y do ponto na tela
	 * @param cor
	 *            cor a ser pintada
	 */
	private void pintar(int x, int y, Color cor) {
		tela.setColor(cor);
		tela.drawLine(x, y, x, y);
	}

	/**
	 * Abre a janela(Frame).
	 * 
	 */
	private void mostrar(String nome) {
		frm = new JFrame(nome);
		JPanel pan = new JPanel();
		JLabel lbl = new JLabel(new ImageIcon(buffer));
		pan.add(lbl);
		frm.getContentPane().add(pan);
		frm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frm.setResizable(false);
		frm.pack();
		Dimension dim = frm.getToolkit().getScreenSize();
		Rectangle abounds = frm.getBounds();
		frm.setLocation((dim.width - abounds.width) / 2,
				(dim.height - abounds.height) / 3);
		frm.requestFocus();
		frm.setVisible(true);
		frm.setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
	}

	/**
	 * Carrega um arquivo de imagem e o converte em um array bidimensional de
	 * uma imagem em tons de cinza. M�nimo 0 e m�ximo 255 em cada posi��o do
	 * array. Se uma imagem colorida for carregada, apenas o espectro vermelho �
	 * considerado.
	 * 
	 * @param nomeArquivo
	 *            endere�o da imagem.
	 * @return
	 */
	public static int[][] carregarImagem(String nomeArquivo) {
		int[][] imagem;
		Image bmp;
		int w = -1;
		int h = -1;
		int[] pixels = { -1 };

		ImageIcon arquivo = new ImageIcon(nomeArquivo);
		bmp = arquivo.getImage();

		w = bmp.getWidth(null);
		h = bmp.getHeight(null);
		PixelGrabber pixelGrabber = new PixelGrabber(bmp, 0, 0, w, h, true);
		try {
			pixelGrabber.grabPixels();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		pixels = (int[]) pixelGrabber.getPixels();

		imagem = new int[w][h];
		for (int y = 0; y < w; y++) {
			for (int x = 0; x < h; x++) {
				int i = y + x * w;
				imagem[y][x] = (new Color(pixels[i])).getRed();
			}
		}
		return imagem;

	}

	/**
	 * Carrega um arquivo de imagem e o converte em um array bidimensional de
	 * uma imagem em tons de cinza. M�nimo 0 e m�ximo 255 em cada posi��o do
	 * array. Se uma imagem colorida for carregada, apenas o espectro vermelho �
	 * considerado.
	 * 
	 * @param nomeArquivo
	 *            endere�o da imagem.
	 * @return
	 */
	public static int[][][] carregarImagemCor(String nomeArquivo) {
		int[][][] imagem;
		Image bmp;
		int w = -1;
		int h = -1;
		int[] pixels = { -1 };

		ImageIcon arquivo = new ImageIcon(nomeArquivo);
		bmp = arquivo.getImage();

		w = bmp.getWidth(null);
		h = bmp.getHeight(null);
		PixelGrabber pixelGrabber = new PixelGrabber(bmp, 0, 0, w, h, true);
		try {
			pixelGrabber.grabPixels();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		pixels = (int[]) pixelGrabber.getPixels();

		imagem = new int[w][h][3];
		for (int y = 0; y < w; y++) {
			for (int x = 0; x < h; x++) {
				int i = y + x * w;
				imagem[y][x][0] = (new Color(pixels[i])).getRed();
				imagem[y][x][1] = (new Color(pixels[i])).getGreen();
				imagem[y][x][2] = (new Color(pixels[i])).getBlue();
			}
		}
		return imagem;

	}

	/**
	 * Mostra uma imagem na tela
	 * 
	 * @param imagem
	 *            � importante lembrar que o limite dos inteiros � 0 e 255.
	 * @param nome
	 *            informa��o mostrada no t�tulo da janela.
	 * @return
	 */
	public static ImagemDigital plotarImagem(int[][] imagem, String nome) {
		int w = imagem[0].length;
		int h = imagem.length;
		ImagemDigital teste = new ImagemDigital(w, h);
		for (int y = 0; y < h; y++) {
			for (int x = 0; x < w; x++) {
				// int i = y * h + x;
				teste.pintar(y, x, new Color(imagem[y][x], imagem[y][x],
						imagem[y][x]));
			}
		}
		teste.mostrar(w + "x" + h + " - " + nome);
		return teste;
	}

	/**
	 * Mostra uma imagem na tela
	 * 
	 * @param imagem
	 *            � importante lembrar que o limite dos inteiros � 0 e 255.
	 * @param nome
	 *            informa��o mostrada no t�tulo da janela.
	 * @return
	 */
	public static ImagemDigital plotarImagemCor(int[][][] imagem, String nome) {
		int w = imagem[0].length;
		int h = imagem.length;
		ImagemDigital teste = new ImagemDigital(w, h);
		for (int y = 0; y < h; y++) {
			for (int x = 0; x < w; x++) {
				// int i = y * h + x;
				teste.pintar(y, x, new Color(imagem[y][x][0], imagem[y][x][1],
						imagem[y][x][2]));
			}
		}
		teste.mostrar(w + "x" + h + " - " + nome);
		return teste;
	}

	/**
	 * Salva uma matriz de inteiros como uma imagem em tons de cinza no formato
	 * PNG.
	 * 
	 * @param imagem
	 *            � importante lembrar que o limite dos inteiros � 0 e 255.
	 * @param enderecoImagem
	 *            deve constar .png no final do nome do arquivo.
	 */
	public static void salvarImagemPNG(int[][] imagem, String enderecoImagem) {
		try {
			Iterator<ImageWriter> writers = ImageIO
					.getImageWritersByFormatName("png");
			ImageWriter writer = writers.next();

			File f = new File(enderecoImagem);
			ImageOutputStream ios = ImageIO.createImageOutputStream(f);
			writer.setOutput(ios);

			BufferedImage bi = new BufferedImage(imagem.length,
					imagem[0].length, BufferedImage.TYPE_BYTE_GRAY);
			WritableRaster raster = bi.getRaster();

			for (int i = 0; i < imagem.length; i++) {
				for (int j = 0; j < imagem[i].length; j++) {
					raster.setPixel(i, j, new int[] { imagem[i][j] });
				}
			}
			writer.write(bi);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	/**
	 * Salva uma matriz de inteiros como uma imagem em tons de cinza no formato
	 * PNG.
	 * 
	 * @param imagem
	 *            � importante lembrar que o limite dos inteiros � 0 e 255.
	 * @param enderecoImagem
	 *            deve constar .png no final do nome do arquivo.
	 */
	public static void salvarImagemCorPNG(int[][][] imagem, String enderecoImagem) {
		try {
			Iterator<ImageWriter> writers = ImageIO
					.getImageWritersByFormatName("png");
			ImageWriter writer = writers.next();

			File f = new File(enderecoImagem);
			ImageOutputStream ios = ImageIO.createImageOutputStream(f);
			writer.setOutput(ios);

			BufferedImage bi = new BufferedImage(imagem.length,
					imagem[0].length, BufferedImage.TYPE_3BYTE_BGR);
			WritableRaster raster = bi.getRaster();

			for (int i = 0; i < imagem.length; i++) {
				for (int j = 0; j < imagem[i].length; j++) {
					raster.setPixel(i, j, new int[] { imagem[i][j][0], imagem[i][j][1], imagem[i][j][2] });
				}
			}
			writer.write(bi);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) throws Exception {
		int[][] imagem = carregarImagem("./cap02/Fig0222(a)(face).png");
		plotarImagem(imagem, "nome");
		// salvarImagemPNG(imagem, "teste.png");
	}

}