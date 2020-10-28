public class PackedWorld extends World {

    private long world;

    public PackedWorld(String serial)  {
        super(serial);
        world = 0L;
        getPattern().initialise(this);

    }

    public boolean getCell(int col, int row){
        return (col>=0&col<=7&row>=0&row<=7&PackedLong.get(world, 8*row+col));
    }

    public void setCell(int col, int row, boolean newval){
        world = (col>=0&col<=7&row>=0&row<=7)?set(world,8*row+col,newval):world;
    }

    public static long set(long packed, int position, boolean value) {
        if (value) {
            packed = packed | (1L << position);
        } else {
            packed = packed & (~(1L << position));
        }
        return packed;
    }

    public void nextGeneration(){
        long newworld = world;
        for(int col=0;col<8;col++){
            for(int row=0;row<8;row++){
                newworld = (col>=0&col<=7&row>=0&row<=7)?set(newworld,8*row+col,computeCell(col,row)):newworld;
            }
        }
        world = newworld;
        incrementGenerationCount();
    }

    public static void main(String args[]) throws Exception {
        PackedWorld pl = new PackedWorld(args[0]);
        pl.play();
    }
}