/*import java.io.IOException;

public class ArrayLife {

    private World world;
    private int width;
    private int height;
    private Pattern pattern;

    public ArrayLife(String format)  {
        pattern = new Pattern(format);
        width = pattern.getWidth();
        height = pattern.getHeight();
        world = new World(format);
        pattern.initialise(world);
    }

    public static void main(String[] args) throws Exception {
        ArrayLife al = new ArrayLife(args[0]);
        al.play();
    }

    public void setCell(int col, int row, boolean newval){
        if (col>=0&col<width&row>=0&row<height){
            world[row][col] = newval;
        }
    }

    public boolean getCell(int col, int row){
        return (col>=0&col<width&row>=0&row<height&world[row][col]);
    }

    public int countNeighbours(int col, int row){
        int neighbours = 0;
        for(int i=-1;i<2;i++){
            for(int j=-1;j<2;j++){
                if (col+i<0||row+j<0||col+i>=width||row+j>=height) {
                }
                else{
                    if(getCell(col+i,row+j)) {
                        neighbours += 1;
                    }
                }
            }
        }
        if(getCell(col,row)){
            return neighbours-1;
        }
        else{
            return neighbours;
        }
    }

    public boolean computeCell(int col, int row){
        return (getCell(col,row)&&countNeighbours(col,row)==2)||(countNeighbours(col,row)==3);
    }

    public void nextGeneration() {
        boolean[][] nextGeneration = new boolean[world.length][];
        for (int y = 0; y < world.length; ++y) {
            nextGeneration[y] = new boolean[world[y].length];
            for (int x = 0; x < world[y].length; ++x) {
                boolean nextCell = computeCell(x, y);
                nextGeneration[y][x]=nextCell;
            }
        }
        world = nextGeneration;
    }

    private void play() throws java.io.IOException {
        int userResponse = 0;
        while (userResponse != 'q') {
            print();
            userResponse = System.in.read();
            nextGeneration();
        }
    }

    public void print() {
        System.out.println("-");
        for (int row = 0; row < height; row++) {
            for (int col = 0; col < width; col++) {
                System.out.print(getCell(col, row) ? "#" : "_");
            }
            System.out.println();
        }
    }
}
*/