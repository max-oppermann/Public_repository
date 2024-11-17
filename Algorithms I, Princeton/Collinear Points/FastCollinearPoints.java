import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FastCollinearPoints {
    private int numSegments = 0;
    private final List<LineSegment> segmentsList;

    // finds all line segments containing 4 or more points
    public FastCollinearPoints(Point[] points) {
        if (points == null) {
            throw new IllegalArgumentException();
        }

        for (Point point : points) {
            if (point == null) {
                throw new IllegalArgumentException("Some points are null");
            }
        }

        int n = points.length;
        Arrays.sort(points);
        for (int i = 1; i < n; i++) {
            if (points[i].compareTo(points[i - 1]) == 0) {
                throw new IllegalArgumentException("Some points are repeated");
            }
        }

        Point[] pointsCopySlopeOrder = Arrays.copyOf(points, n);
        Point[] pointsCopy = Arrays.copyOf(points, n);
        segmentsList = new ArrayList<>();
        Arrays.sort(pointsCopy);

        for (int i = 0; i < n; i++) {
            Point p = pointsCopy[i];
            Arrays.sort(pointsCopySlopeOrder);
            Arrays.sort(pointsCopySlopeOrder, p.slopeOrder());

            int counter = 1;
            Point firstColl = null;
            for (int s = 1; s < n - 1; s++) {
                if (pointsCopySlopeOrder[s].slopeTo(p) == pointsCopySlopeOrder[s + 1].slopeTo(p)) {
                    counter++;
                    if (counter == 2) {
                        firstColl = pointsCopySlopeOrder[s];
                        counter++;
                    }
                    else if (counter >= 4 && s + 1 == n - 1) {
                        if (firstColl.compareTo(p) > 0) {
                            segmentsList.add(new LineSegment(p, pointsCopySlopeOrder[s + 1]));
                            numSegments++;
                        }
                        counter = 1;
                    }
                }
                else if (counter >= 4) {
                    if (firstColl.compareTo(p) > 0) {
                        segmentsList.add(new LineSegment(p, pointsCopySlopeOrder[s]));
                        numSegments++;
                    }
                    counter = 1;
                }
                else {
                    counter = 1;
                }
            }

        }
    }


    // the number of line segments
    public int numberOfSegments() {
        return numSegments;
    }

    // the line segments
    public LineSegment[] segments() {
        LineSegment[] segmentsArray = new LineSegment[segmentsList.size()];
        segmentsList.toArray(segmentsArray);
        return segmentsArray;
    }


    public static void main(String[] args) {

        // read the n points from a file
        In in = new In(args[0]);
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
        }

        // draw the points
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        for (Point p : points) {
            p.draw();
        }
        StdDraw.show();

        // print and draw the line segments
        FastCollinearPoints collinear = new FastCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
        }
        StdDraw.show();
        /*
        Point p1 = new Point(0, 0);
        Point p2 = new Point(0, 1);
        Point p3 = new Point(0, 3);

        Point p4 = new Point(1, 1);
        Point p5 = new Point(1, 2);

        Point p6 = new Point(2, 0);
        Point p7 = new Point(2, 1);
        Point p8 = new Point(2, 2);
        Point p9 = new Point(2, 3);

        Point p10 = new Point(3, 0);
        Point p11 = new Point(3, 1);
        Point p12 = new Point(3, 3);

        Point p13 = new Point(4, 4);

        Point[] points = { p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, };

        FastCollinearPoints collinear = new FastCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
        }
        StdOut.println(collinear.numberOfSegments());*/
    }
}
