public abstract class World {

    private int generation;
    private Pattern pattern;

    public abstract boolean getCell(int col, int row);

    public abstract void setCell(int col, int row, boolean val);

    public abstract void nextGeneration();

    private int countNeighbours(int col, int row){
        int neighbours = 0;
        for(int i=-1;i<2;i++){
            for(int j=-1;j<2;j++){
                if (col+i<0||row+j<0||col+i>=getWidth()||row+j>=getHeight()) {
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


    private void print() {
        System.out.println("-");
        for (int row = 0; row < getHeight(); row++) {
            for (int col = 0; col < getWidth(); col++) {
                System.out.print(getCell(col, row) ? "#" : "_");
            }
            System.out.println();
        }
        System.out.println(getGenerationCount());
    }

    public int getWidth(){
        return pattern.getWidth();
    }

    public int getHeight(){
        return pattern.getHeight();
    }

    protected void incrementGenerationCount(){
        generation += 1;
    }

    public World(String format){
        pattern = new Pattern(format);
    }

    public int getGenerationCount(){
        return generation;
    }

    public Pattern getPattern(){
        return pattern;
    }




}