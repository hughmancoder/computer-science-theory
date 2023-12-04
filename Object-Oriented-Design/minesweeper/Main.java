public class Main {
    public static void main(String[] args) {
        int X = 10;
        int Y = 15;
        MinesweeperGameRunner game = new MinesweeperGameRunner(X, Y, 10); // 10x15 grid with 10 mines
        game.startGame();
    }
}
