public class FibonacciCache {

    public static long[] fib = null;

    public static void store() {
        try {
            fib[0] = 1;
            if (fib.length > 1) {
                fib[1] = 1;
                for (int i = 2; i < fib.length; i++) {
                    fib[i] = fib[i - 1] + fib[i - 2];
                }
            }
        }
        catch(NullPointerException e){
            System.out.println("fib is type null");
        }
    }

    public static void reset(int cachesize) {
        fib = new long[cachesize];
        for(int i=0;i<cachesize;i++){fib[i]=0;}
    }
    public static long get(int i) throws Exception {
        if (fib == null) throw new Exception("fib is type null");
        try {return fib[i];}
        catch (ArrayIndexOutOfBoundsException e) {
            throw new Exception("Value requested is out of bounds");
        }
    }

    public static void main(String[] args) {
        try {
            reset(20);
            store();
            int i = Integer.decode(args[0]);
            System.out.println(get(i));
        }
        catch (Exception e){System.out.print(e.getMessage());}
    }

}
