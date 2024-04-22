import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.StdDraw;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class KdTree {
    private int size;
    private Node root;
    private Comparator<Point2D> xComp = Point2D.X_ORDER;
    private Comparator<Point2D> yComp = Point2D.Y_ORDER;

    private static class Node {
        Point2D point;
        Node left;
        Node right;
        boolean vertical;

        Node(Point2D point, boolean vertical) {
            this.point = point;
            this.left = null;
            this.right = null;
            this.vertical = vertical;
        }
    }

    public KdTree() {
        root = null;
    }

    // is the set empty?
    public boolean isEmpty() {
        return root == null;
    }

    // number of points in the set
    public int size() {
        if (root == null) {
            return 0;
        }
        return size;
    }

    // add the point to the set (if it is not already in the set)
    public void insert(Point2D point) {
        if (!contains(point)) {
            root = insert(root, point, true);
        }
    }

    private Node insert(Node node, Point2D point, boolean vertical) {
        // once we reach the end
        if (node == null) {
            size++;
            // if we compared by x *last*, vertical will be false
            return new Node(point, vertical);
        }
        if (node.point.equals(point)) {
            return node; // duplicates
        }

        // compare by x-coordinate iff vertical is true
        Comparator<Point2D> comparator = vertical ? xComp : yComp;

        // the ! flips the boolean everytime we go down one level
        if (comparator.compare(point, node.point) < 0) {
            node.left = insert(node.left, point, !vertical);
        }
        else {
            node.right = insert(node.right, point, !vertical);
        }

        return node;
    }

    // does the set contain point p?
    public boolean contains(Point2D p) {
        if (p == null) {
            throw new IllegalArgumentException();
        }
        return contains(root, p);
    }

    private boolean contains(Node node, Point2D p) {
        if (node == null) {
            return false;
        }
        if (node.point.equals(p)) {
            return true;
        }
        if (node.vertical) {
            if (p.x() < node.point.x()) {
                return contains(node.left, p);
            }
            else {
                return contains(node.right, p);
            }
        }
        else {
            if (p.y() < node.point.y()) {
                return contains(node.left, p);
            }
            else {
                return contains(node.right, p);
            }
        }
    }

    // draw all of the points to standard draw in black
    // the subdivisions in red (for vertical splits) and blue (for horizontal splits).
    public void draw() {
        StdDraw.setCanvasSize(800, 800);
        StdDraw.setXscale(0, 1);
        StdDraw.setYscale(0, 1);
        StdDraw.setPenColor(StdDraw.BLACK);

        draw(root, new RectHV(0, 0, 1, 1), true);
    }

    private void draw(Node node, RectHV rect, boolean vertical) {
        if (node == null) return;

        StdDraw.setPenColor(StdDraw.BLACK);
        StdDraw.setPenRadius(0.01);
        node.point.draw();

        StdDraw.setPenRadius();
        if (vertical) {
            StdDraw.setPenColor(StdDraw.RED);
            StdDraw.line(node.point.x(), rect.ymin(), node.point.x(), rect.ymax());
            draw(node.left, new RectHV(rect.xmin(), rect.ymin(), node.point.x(), rect.ymax()),
                 false);
            draw(node.right, new RectHV(node.point.x(), rect.ymin(), rect.xmax(), rect.ymax()),
                 false);
        }
        else {
            StdDraw.setPenColor(StdDraw.BLUE);
            StdDraw.line(rect.xmin(), node.point.y(), rect.xmax(), node.point.y());
            draw(node.left, new RectHV(rect.xmin(), rect.ymin(), rect.xmax(), node.point.y()),
                 true);
            draw(node.right, new RectHV(rect.xmin(), node.point.y(), rect.xmax(), rect.ymax()),
                 true);
        }
    }


    // all points that are inside the rectangle (or on the boundary)
    public Iterable<Point2D> range(RectHV rect) {
        if (rect == null) {
            throw new IllegalArgumentException();
        }
        List<Point2D> pointsInRange = new ArrayList<>();
        range(root, new RectHV(0, 0, 1, 1), rect, pointsInRange);
        return pointsInRange;
    }

    private void range(Node node, RectHV nodeRect, RectHV queryRect, List<Point2D> pointsInRange) {
        if (node == null) return;

        RectHV leftRect = null;
        RectHV rightRect = null;

        if (node.vertical) {
            leftRect = new RectHV(nodeRect.xmin(), nodeRect.ymin(), node.point.x(),
                                  nodeRect.ymax());
            rightRect = new RectHV(node.point.x(), nodeRect.ymin(), nodeRect.xmax(),
                                   nodeRect.ymax());
        }
        else {
            leftRect = new RectHV(nodeRect.xmin(), nodeRect.ymin(), nodeRect.xmax(),
                                  node.point.y());
            rightRect = new RectHV(nodeRect.xmin(), node.point.y(), nodeRect.xmax(),
                                   nodeRect.ymax());
        }


        if (queryRect.contains(node.point)) {
            pointsInRange.add(node.point);
        }

        // the leftRect/rightRect get updated recursively, don't worry
        if (leftRect.intersects(queryRect)) {
            range(node.left, leftRect, queryRect, pointsInRange);
        }

        if (rightRect.intersects(queryRect)) {
            range(node.right, rightRect, queryRect, pointsInRange);
        }
    }


    // a nearest neighbor in the set to point p; null if the set is empty

    // gets close, but does not actually find the nearest neighbor!!!
    public Point2D nearest(Point2D p) {
        if (p == null) {
            throw new IllegalArgumentException();
        }
        if (root == null) {
            return null;
        }
        if (isEmpty()) {
            return null;
        }
        // Create the initial rectangle corresponding to the unit square
        RectHV unitSquare = new RectHV(0, 0, 1, 1);
        return nearest(root, unitSquare, p, root.point, Double.POSITIVE_INFINITY);
    }


    private Point2D nearest(Node node, RectHV rect, Point2D queryPoint, Point2D champion,
                            double closestDistance) {
        if (node == null) {
            return champion;
        }

        double nodeDist = node.point.distanceSquaredTo(queryPoint);
        if (nodeDist < closestDistance) {
            champion = node.point;
            closestDistance = nodeDist;
        }

        RectHV leftRect, rightRect;
        if (node.vertical) {
            leftRect = new RectHV(rect.xmin(), rect.ymin(), node.point.x(), rect.ymax());
            rightRect = new RectHV(node.point.x(), rect.ymin(), rect.xmax(), rect.ymax());
        }
        else {
            leftRect = new RectHV(rect.xmin(), rect.ymin(), rect.xmax(), node.point.y()); // lower
            rightRect = new RectHV(rect.xmin(), node.point.y(), rect.xmax(), rect.ymax()); // upper
        }

        if (node.left != null
                && leftRect.distanceSquaredTo(queryPoint) < rightRect.distanceSquaredTo(
                queryPoint)) {
            champion = nearest(node.left, leftRect, queryPoint, champion, closestDistance);
        }
        else if (node.right != null && rightRect.distanceSquaredTo(queryPoint) < closestDistance) {
            champion = nearest(node.right, rightRect, queryPoint, champion, closestDistance);
        }

        return champion;
    }


    // unit testing of the methods (optional)
    public static void main(String[] args) {
        KdTree kdTree = new KdTree();

        // Insert some points into the KdTree
        kdTree.insert(new Point2D(0.2, 0.3));
        kdTree.insert(new Point2D(0.4, 0.5));
        kdTree.insert(new Point2D(0.8, 0.9));
        kdTree.draw();

        // Define a query point
        Point2D queryPoint = new Point2D(0.5, 0.6);

        // Find the nearest neighbor to the query point
        Point2D nearestNeighbor = kdTree.nearest(queryPoint);

        // Print the nearest neighbor
        if (nearestNeighbor != null) {
            System.out.println("Nearest neighbor to " + queryPoint + " is " + nearestNeighbor);
        }
        else {
            System.out.println("No nearest neighbor found.");
        }
    }

}
