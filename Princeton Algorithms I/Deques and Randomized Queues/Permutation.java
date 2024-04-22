import edu.princeton.cs.algs4.StdIn;

public class Permutation {
    public static void main(String[] args) {
        int k = Integer.parseInt(args[0]);
        RandomizedQueue<String> rq = new RandomizedQueue<>();

        while (!StdIn.isEmpty()) {
            String value = StdIn.readString();
            rq.enqueue(value);
        }
        int count = 0;
        for (String item : rq) {
            if (count < k) {
                System.out.println(item);
                count++;
            }
            else {
                break;
            }
        }
    }
}
