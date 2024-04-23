import edu.princeton.cs.algs4.StdRandom;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] s;
    private int N = 0;

    // construct an empty randomized queue
    public RandomizedQueue() {
        s = (Item[]) new Object[1];
    }

    private void resize(int capacity) {
        Item[] copy = (Item[]) new Object[capacity];
        for (int i = 0; i < N; i++) {
            copy[i] = s[i];
        }
        s = copy;
    }

    // is the randomized queue empty?
    public boolean isEmpty() {
        return N == 0;
    }

    // return the number of items on the randomized queue
    public int size() {
        return N;
    }

    // add the item
    public void enqueue(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        if (N == s.length) {
            resize(s.length * 2);
        }
        s[N++] = item;
    }

    // remove and return a random item
    // shuffle(Object[]) before dequeueing, then pop last element
    public Item dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        if (N == s.length / 4) {
            resize(s.length / 2);
        }

        int randomIndex = StdRandom.uniformInt(N);
        Item item = s[randomIndex];
        s[randomIndex] = s[N - 1];
        s[N - 1] = null;
        N--;

        return item;
    }

    // return a random item (but do not remove it)
    public Item sample() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        int randomIndex = StdRandom.uniformInt(N);
        Item item = s[randomIndex];

        return item;
    }

    // return an independent iterator over items in random order
    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item> {
        private int[] indices;
        private int position;

        public ListIterator() {
            indices = new int[N];
            for (int i = 0; i < N; i++) {
                indices[i] = i;
            }
            StdRandom.shuffle(indices);
            position = 0;
        }

        public boolean hasNext() {
            return position < N;
        }

        public Item next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            Item item = s[indices[position]];
            position++;
            return item;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    // unit testing (required)
    public static void main(String[] args) {
        // new randomized queue
        RandomizedQueue<Integer> rq = new RandomizedQueue<>();

        // enqueue
        rq.enqueue(1);
        rq.enqueue(2);
        rq.enqueue(3);
        rq.enqueue(4);

        // size
        System.out.println("Size: " + rq.size());

        // isEmpty
        System.out.println("Empty? " + rq.isEmpty());

        // iterate
        System.out.println("Randomized Iterator:");
        for (int item : rq) {
            System.out.println(item);
        }

        // sample
        System.out.println("Sample: " + rq.sample());

        // dequeue
        System.out.println("Dequeue: " + rq.dequeue());
        System.out.println("Dequeue: " + rq.dequeue());

        // check after dequeuing
        System.out.println("Size after dequeuing: " + rq.size());
        for (int item : rq) {
            System.out.println(item);
        }
    }

}
