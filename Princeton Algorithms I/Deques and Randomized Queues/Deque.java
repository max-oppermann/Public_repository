import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {

    private int numItems;
    private Node first, last;

    private class Node {
        Item item;
        Node next;
    }

    // construct an empty deque
    public Deque() {
        numItems = 0;
        first = null;
        last = null;
    }

    // is the deque empty?
    public boolean isEmpty() {
        return (first == null || last == null);
    }

    // return the number of items on the deque
    public int size() {
        return numItems;
    }

    // add the item to the front
    public void addFirst(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }

        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;
        if (isEmpty()) {
            last = first;
        }

        numItems++;
    }

    // add the item to the back
    public void addLast(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }

        Node oldlast = last;
        last = new Node();
        last.item = item;
        last.next = null;
        if (isEmpty()) {
            first = last;
        }
        else {
            oldlast.next = last;
        }

        numItems++;
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }

        Item item = first.item;
        first = first.next;
        if (isEmpty()) {
            last = null;
        }

        numItems--;
        return item;
    }

    // remove and return the item from the back
    // this is the complicated one
    public Item removeLast() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        Item item = last.item;
        if (first == last) {
            first = null;
            last = null;
        }
        else {
            Node current = first;
            while (current.next.next != null) {
                current = current.next;
            }
            current.next = null;
            last = current;
        }

        numItems--;
        return item;
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public Item next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }

            Item item = current.item;
            current = current.next;
            return item;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    // unit testing (required)
    public static void main(String[] args) {
        // Create an instance of the Deque class
        Deque<String> deque = new Deque<>();

        // Test addFirst and addLast methods
        deque.addFirst("Middle");
        deque.addFirst("First");
        deque.addLast("Last");
        for (String item : deque) {
            System.out.println(item);
        }

        System.out.println("Removed from front: " + deque.removeFirst());
        System.out.println("Removed from back: " + deque.removeLast());
        System.out.println(deque.isEmpty());

        deque.addFirst("New First");
        deque.addLast("New Last");

        // Iterate and print elements
        for (String item : deque) {
            System.out.println(item);
        }

        System.out.println(deque.size());
    }


}
