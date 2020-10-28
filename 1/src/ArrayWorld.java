public class ArrayWorld extends World {

    private boolean[][] world;

    public ArrayWorld(String serial)  {
        super(serial);
        world = new boolean[getHeight()][getWidth()];
        getPattern().initialise(this);

    }

    // TODO: fill in the inherited formerly-abstract methods
    public boolean getCell(int col, int row){
        return (col>=0&col<getWidth()&row>=0&row<getHeight()&world[row][col]);
    }

    public void setCell(int col, int row, boolean newval) {
        if (col >= 0 & col < getWidth() & row >= 0 & row < getHeight()) {
            world[row][col] = newval;
        }
    }

    public void nextGeneration() {
        boolean[][] nextGeneration = new boolean[getHeight()][];
        for (int y = 0; y < getHeight(); ++y) {
            nextGeneration[y] = new boolean[getWidth()];
            for (int x = 0; x < getWidth(); ++x) {
                boolean nextCell = computeCell(x, y);
                nextGeneration[y][x]=nextCell;
            }
        }
        world = nextGeneration;
        incrementGenerationCount();
    }

    public static void main(String args[]) throws Exception {
        ArrayWorld pl = new ArrayWorld(args[0]);
        pl.play();
    }
}
