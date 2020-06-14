package com.iLink.Hackathon.Utils;

import java.util.Deque;
import java.util.StringJoiner;

public class Path {
    private int dist;
    private Deque<Cell> path;
    private Cell source;
    private Cell destination;

    public Path(int dist, Deque<Cell> path, Cell source, Cell destination) {
        this.dist = dist;
        this.path = path;
        this.source = source;
        this.destination = destination;
    }

    public int getDist() {
        return dist;
    }

    public Deque<Cell> getPath() {
        return path;
    }

    public Cell getSource() {
        return source;
    }

    public Cell getDestination() {
        return destination;
    }

    @Override
    public String toString() {

        String pathArray = new String();
        StringJoiner stringJoiner = new StringJoiner(", ");
        for (Cell cell : this.path) {
            stringJoiner.add("[" + cell.getRow() + ", " + cell.getCol() + "]");
            pathArray = "[" + stringJoiner.toString() + "]";
        }

        return "{ " +
                "\"dist\" : " + dist +
                ", \"path\" : " + pathArray +
                " }";
    }

    public void setDist(int dist) {
        this.dist = dist;
    }

    public void setPath(Deque<Cell> path) {
        this.path = path;
    }

    public void setSource(Cell source) {
        this.source = source;
    }

    public void setDestination(Cell destination) {
        this.destination = destination;
    }

    public static Path finalPath(Path pathToStart, Path startEndPath, Path pathToEnd) {
        int totalDist = pathToStart.getDist() + startEndPath.getDist() + pathToEnd.getDist();

        Deque<Cell> finalPath = pathToStart.getPath();

        finalPath.addAll(startEndPath.getPath());
        finalPath.addAll(pathToEnd.getPath());

        return new Path(totalDist, finalPath, null, null);

    }
}
