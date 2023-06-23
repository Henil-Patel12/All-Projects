import java.util.Scanner;
import java.util.Random;

public class tictoc {
  static char[][] board = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
  static Scanner scan = new Scanner(System.in);
  static Random rand = new Random();
  
  public static void main(String[] args) {
    char currentPlayer = 'X';
    boolean gameOver = false;
    int row, col;
    while (!gameOver) {
      displayBoard();
      if (currentPlayer == 'X') {
        System.out.println("Player X turn. Enter row and column (1-3):");
        row = scan.nextInt() - 1;
        col = scan.nextInt() - 1;
        board[row][col] = 'X';
      } else {
        System.out.println("Player O (AI) turn.");
        row = rand.nextInt(3);
        col = rand.nextInt(3);
        if (board[row][col] == ' ') {
          board[row][col] = 'O';
        } else {
          continue;
        }
      }
      if (checkWin('X')) {
        displayBoard();
        System.out.println("Player X wins!");
        gameOver = true;
      } else if (checkWin('O')) {
        displayBoard();
        System.out.println("Player O wins!");
        gameOver = true;
      } else if (isDraw()) {
        displayBoard();
        System.out.println("Draw!");
        gameOver = true;
      }
      currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }
  }
  
  public static void displayBoard() {
    System.out.println("-------------");
    for (int i = 0; i < 3; i++) {
      System.out.print("| ");
      for (int j = 0; j < 3; j++) {
        System.out.print(board[i][j] + " | ");
      }
      System.out.println();
      System.out.println("-------------");
    }
  }
  
  public static boolean checkWin(char player) {
    // Check rows
    for (int i = 0; i < 3; i++) {
      if (board[i][0] == player && board[i][1] == player && board[i][2] == player) {
        return true;
      }
    }
    // Check columns
    for (int j = 0; j < 3; j++) {
      if (board[0][j] == player && board[1][j] == player && board[2][j] == player) {
        return true;
      }
    }
    // Check diagonals
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player) {
      return true;
    }
    if (board[0][2] == player && board[1
