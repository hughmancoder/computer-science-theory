import java.util.Random;

public class Grid {
    private Cell[][] grid;
    private int width;
    private int height;

    public Grid(int width, int height, int numMines) {
        this.width = width;
        this.height = height;
        this.grid = new Cell[height][width];
        initializeCells();
        placeMines(numMines);
        calculateAdjacentMines();
    }

    private void initializeCells() {
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                grid[row][col] = new Cell();
            }
        }
    }

    private void placeMines(int numMines) {
        Random random = new Random();
        int minesPlaced = 0;
        while (minesPlaced < numMines) {
            int row = random.nextInt(height);
            int col = random.nextInt(width);
            if (!grid[row][col].isMine()) {
                grid[row][col].setMine(true);
                minesPlaced++;
            }
        }
    }

    private void calculateAdjacentMines() {
        int[][] offsets = { { -1, -1 }, { -1, 0 }, { -1, 1 }, { 0, -1 }, { 0, 1 }, { 1, -1 }, { 1, 0 }, { 1, 1 } };
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                int neighboringMines = 0;
                for (int[] offset : offsets) {
                    int adjacentRow = row + offset[0];
                    int adjacentCol = col + offset[1];
                    if (adjacentRow >= 0 && adjacentRow < height && adjacentCol >= 0 && adjacentCol < width) {
                        if (grid[adjacentRow][adjacentCol].isMine()) {
                            neighboringMines++;
                        }
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
                System.out.print(" " + getCellDisplaySymbol(cell) + " "); // Padding added around cell symbol
            }
            System.out.println();
        }
    }

    private void printColumnHeaders() {
        System.out.print("  "); // Spacing for row headers
        for (int col = 0; col < width; col++) {
            System.out.printf(" %2d", col); // Adjusted format for column headers
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

    public void flagCell(int row, int col) {
        grid[row][col].toggleFlag();
    }

    public void openCell(int row, int col) {
        Cell cell = grid[row][col];
        if (!cell.isFlagged() && !cell.isOpen()) {
            cell.setOpen(true);
            if (cell.getAdjacentMines() == 0 && !cell.isMine()) {
                // Open all adjacent cells
                openAdjacentCells(row, col);
            }
        }
    }

    private void openAdjacentCells(int row, int col) {
        int[][] offsets = { { -1, -1 }, { -1, 0 }, { -1, 1 }, { 0, -1 }, { 0, 1 }, { 1, -1 }, { 1, 0 }, { 1, 1 } };
        for (int[] offset : offsets) {
            int adjacentRow = row + offset[0];
            int adjacentCol = col + offset[1];
            if (adjacentRow >= 0 && adjacentRow < height && adjacentCol >= 0 && adjacentCol < width) {
                Cell adjacentCell = grid[adjacentRow][adjacentCol];
                if (!adjacentCell.isOpen() && !adjacentCell.isMine()) {
                    adjacentCell.setOpen(true);
                    if (adjacentCell.getAdjacentMines() == 0) {
                        openAdjacentCells(adjacentRow, adjacentCol);
                    }
                }
            }
        }
    }

    public boolean isMineHit() {
        for (Cell[] row : grid) {
            for (Cell cell : row) {
                if (cell.isOpen() && cell.isMine()) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean isAllNonMinesOpened() {
        for (Cell[] row : grid) {
            for (Cell cell : row) {
                if (!cell.isMine() && !cell.isOpen()) {
                    return false;
                }
            }
        }
        return true;
    }

    public boolean isAllMinesFlagged() {
        for (Cell[] row : grid) {
            for (Cell cell : row) {
                if (cell.isMine() && !cell.isFlagged()) {
                    return false;
                }
            }
        }
        return true;
    }

    public void revealAll() {
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                grid[row][col].setOpen(true);
            }
        }
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

}