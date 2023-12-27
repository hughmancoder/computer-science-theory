public class Cell {
    private boolean isMine;
    private boolean isOpen;
    private boolean isFlagged;
    private int adjacentMines;

    public Cell() {
        this.isMine = false;
        this.isOpen = false;
        this.isFlagged = false;
        this.adjacentMines = 0;
    }

    public boolean isMine() {
        return isMine;
    }

    public void setMine(boolean isMine) {
        this.isMine = isMine;
    }

    public boolean isOpen() {
        return isOpen;
    }

    public void setOpen(boolean isOpen) {
        this.isOpen = isOpen;
    }

    public boolean isFlagged() {
        return isFlagged;
    }

    public void setFlagged(boolean isFlagged) {
        this.isFlagged = isFlagged;
    }

    public int getAdjacentMines() {
        return adjacentMines;
    }

    public void setAdjacentMines(int adjacentMines) {
        this.adjacentMines = adjacentMines;
    }

    // Additional functionality
    public void toggleFlag() {
        if (!isOpen) {
            isFlagged = !isFlagged;
        }
    }

    public void open() {
        if (!isFlagged) {
            isOpen = true;
        }
    }
}