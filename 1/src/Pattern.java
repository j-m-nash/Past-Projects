public class Pattern {

    private String name;
    private String author;
    private int width;
    private int height;
    private int startCol;
    private int startRow;
    private String cells;

    public static void main(String[] args) throws Exception {
        Pattern p = new Pattern(args[0]);
        System.out.println(p.getName());
        System.out.println(p.getAuthor());
        System.out.println(p.getWidth());
        System.out.println(p.getHeight());
        System.out.println(p.getStartCol());
        System.out.println(p.getStartRow());
        System.out.println(p.getCells());
    }

    public String getName() {
        return name;
    }

    public String getAuthor() {
        return author;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public int getStartCol() {
        return startCol;
    }

    public int getStartRow() {
        return startRow;
    }

    public String getCells() {
        return cells;
    }

    public Pattern(String format) {
        name = format.split(":")[0];
        author = format.split(":")[1];
        width = Integer.parseInt(format.split(":")[2]);
        height = Integer.parseInt(format.split(":")[3]);
        startCol = Integer.parseInt(format.split(":")[4]);
        startRow = Integer.parseInt(format.split(":")[5]);
        cells = format.split(":")[6];
    }

    public void initialise(World world) {
        for(int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                world.setCell(i,j,Integer.parseInt(cells.split(" ")[i].split("")[j]) == 1);

                }
            }
        }
    }
