public class Grid {
    private Cell[][] grid;
    private int width;
    private int height;

    public Grid(int width, int height) {
        this.width = width;
        this.height = height;
        this.grid = new Cell[height][width];
        initializeCells();
    }

    private void initializeCells() {
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                grid[row][col] = new Cell();
            }
        }

        // check for adjacent mines
        int[][] offsets = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                int neighboringMines = 0;
                for (int[] offset : offsets) {
                    int adjacentRow = row + offset[0];
                    int adjacentCol = col + offset[1];
                    if (adjacentRow < 0 || adjacentCol >= height || adjacentCol < 0 || adjacentCol >= width) {
                        continue;
                    }
                    if (grid[adjacentRow][adjacentCol].isMine()) {
                        neighboringMines++;
                    }
                }
                grid[row][col].setAdjacentMines(neighboringMines);
            }
        }
    }

    public void display() {
        System.out.println("Minesweeper Grid:");
        printColumnHeaders();
        for (int row = 0; row < height; row++) {
            System.out.printf("%2d ", row); // Row header
            for (int col = 0; col < width; col++) {
                Cell cell = grid[row][col];
                System.out.print(getCellDisplaySymbol(cell) + " ");
            }
            System.out.println();
        }
    }

    private void printColumnHeaders() {
        System.out.print("   "); // Spacing for row headers
        for (int col = 0; col < width; col++) {
            System.out.printf("%2d ", col); // Column headers
        }
        System.out.println();
    }

    private String getCellDisplaySymbol(Cell cell) {
        if (cell.isFlagged()) {
            return "F";
        } else if (!cell.isOpen()) {
            return "-";
        } else if (cell.isMine()) {
            return "*";
        } else {
            int adjacentMines = cell.getAdjacentMines();
            return adjacentMines > 0 ? String.valueOf(adjacentMines) : " ";
        }
    }
}
