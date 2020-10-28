public class TinyLife {
    public static void main(String[] args) throws java.io.IOException {
        play(Long.decode(args[1]));
    }

    public static long setCell(long world, int col, int row, boolean newval){
        return (col>=0&col<=7&row>=0&row<=7)?PackedLong.set(world,8*row+col,newval):world;
    }

    public static boolean getCell(long world, int col, int row){
        return (col>=0&col<=7&row>=0&row<=7&PackedLong.get(world, 8*row+col));
    }

    public static int countNeighbours(long world, int col, int row){
        int neighbours = 0;
        for(int i=-1;i<2;i++){
            for(int j=-1;j<2;j++){
                if(getCell(world,col+i,row+j)){
                    neighbours+=1;
                }
            }
        }
        if(getCell(world,col,row)){
            return neighbours-1;
        }
        else{
            return neighbours;
        }
    }

    public static boolean computeCell(long world,int col, int row){
        return (getCell(world,col,row)&&countNeighbours(world,col,row)==2)||(countNeighbours(world,col,row)==3);
    }

    public static long nextGeneration(long world){
        long newworld = world;
        for(int col=0;col<8;col++){
            for(int row=0;row<8;row++){
                newworld = setCell(newworld,col,row,computeCell(world,col,row));
            }
        }
        return newworld;
    }

    public static void play(long world) throws java.io.IOException {
        int userResponse = 0;
        while (userResponse != 'q') {
            print(world);
            userResponse = System.in.read();
            world = nextGeneration(world);
        }
    }

    public static void print(long world) {
        System.out.println("-");
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                System.out.print(getCell(world, col, row) ? "#" : "_");
            }
            System.out.println();
        }
    }
}
