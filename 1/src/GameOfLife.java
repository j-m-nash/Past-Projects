public class GameOfLife {

    private World world;

    public GameOfLife(World w) {
        world = w;
    }

    public void play() throws java.io.IOException {
        int userResponse = 0;
        while (userResponse != 'q') {
            print();
            userResponse = System.in.read();
            nextGeneration();
        }
    }

    public void print() {
        // TODO
    }

    public static void main(String args[]) throws IOException {

        World w=null;

        // TODO: initialise w as an ArrayWorld or a PackedWorld
        // based on the command line input

        GameOfLife gol = new GameOfLife(w);
        gol.play();
    }
}