import java.util.ArrayList;
import java.util.List;

public class BruteCollinearPoints {
    private int numSegments = 0;
    private final List<LineSegment> segmentsList;

    // finds all line segments containing 4 points
    public BruteCollinearPoints(Point[] points) {
        if (points == null) {
            throw new IllegalArgumentException();
        }

        for (Point point : points) {
            if (point == null) {
                throw new IllegalArgumentException("One or more points are null");
            }
        }

        int n = points.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (points[i].compareTo(points[j]) == 0) {
                    throw new IllegalArgumentException("One or more points are repeated");
                }
            }
        }

        segmentsList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            Point p = points[i];
            for (int j = 0; j < n; j++) {
                Point q = points[j];
                for (int k = 0; k < n; k++) {
                    Point r = points[k];
                    for (int l = 0; l < n; l++) {
                        Point s = points[l];
                        if ((p.compareTo(q) < 0 && q.compareTo(r) < 0 && r.compareTo(s) < 0
                                && p.slopeTo(q) == p.slopeTo(r) && p.slopeTo(r) == p.slopeTo(s))) {
                            segmentsList.add(new LineSegment(p, s));
                            numSegments++;
                        }
                    }
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
        /* Point p1 = new Point(0, 0);
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

        Point[] points = { p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, };

        BruteCollinearPoints collinear = new BruteCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
        } */
    }
}
