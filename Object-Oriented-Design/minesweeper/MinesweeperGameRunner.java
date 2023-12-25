import java.util.Scanner;

public class MinesweeperGameRunner {
    private Grid grid;
    private boolean gameOver;
    private Scanner scanner;

    public MinesweeperGameRunner(int width, int height, int numMines) {
        grid = new Grid(width, height, numMines);
        scanner = new Scanner(System.in);
        gameOver = false;
    }

    public void startGame() {
        printInstructions();
        while (!gameOver) {
            grid.display();
            System.out.println("Enter row and column to open, or 'f' to flag (e.g., '4 5', 'f 4 5'): ");
            String input = scanner.nextLine();
            processInput(input);
            checkGameOver();
        }
        scanner.close();
        if (grid.isAllMinesFlagged()) {
            System.out.println("Congratulations! You have won the game.");
            gameOver = true;
        } else {
            System.out.println("Game Over! You hit a mine.");
            grid.revealAll();
            grid.display();
            gameOver = true;
        }
    }

    private void processInput(String input) {
        String[] parts = input.split(" ");
        try {
            // Flagging a cell
            if (parts.length == 3 && parts[0].equals("f")) {
                int row = Integer.parseInt(parts[1]);
                int col = Integer.parseInt(parts[2]);
                if (isValidCell(row, col)) {
                    grid.flagCell(row, col);
                } else {
                    System.out.println("Invalid row or column. Please enter a valid row and column within the grid.");
                }
            } else if (parts.length == 2) {
                // Opening a cell
                int row = Integer.parseInt(parts[0]);
                int col = Integer.parseInt(parts[1]);
                if (isValidCell(row, col)) {
                    grid.openCell(row, col);
                } else {
                    System.out.println("Invalid row or column. Please enter a valid row and column within the grid.");
                }
            } else {
                System.out.println(
                        "Invalid input format. Please enter row and column to open, or 'f' to flag (e.g., '4 5', 'f 4 5').");
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter numeric values for row and column.");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Input out of grid bounds. Please enter a valid row and column within the grid.");
        }
    }

    private boolean isValidCell(int row, int col) {
        return row >= 0 && row < grid.getHeight() && col >= 0 && col < grid.getWidth();
    }

    private void checkGameOver() {
        if (grid.isMineHit() || grid.isAllNonMinesOpened()) {
            gameOver = true;
        }
    }

    private void printInstructions() {
        System.out.println("Welcome to Minesweeper!");
        System.out.println("The game is played on a grid. Some cells contain mines, while others don't.");
        System.out.println("The objective is to open all cells without mines.");
        System.out.println("\nInstructions:");
        System.out.println("1. To open a cell, enter the row and column numbers (e.g., '4 5').");
        System.out.println(
                "2. To flag a cell you suspect contains a mine, enter 'f' followed by the row and column numbers (e.g., 'f 4 5').");
        System.out.println("3. Flagged cells cannot be opened unless they are unflagged.");
        System.out.println("4. The numbers on the grid show how many mines are adjacent to a cell.");
        System.out.println("5. The game ends when you open all non-mine cells or when you open a cell with a mine.");
        System.out.println("\nLet's start the game! Here's the initial grid:\n");
    }
}
