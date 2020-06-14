package com.iLink.Hackathon;

import com.iLink.Hackathon.Utils.Cell;
import com.iLink.Hackathon.Utils.MapData;
import com.iLink.Hackathon.Utils.Path;

import java.util.*;

public class ShortestPath {

    private final int MAP_SIZE = 400;

    private List<List<Integer>> mapData = new ArrayList<List<Integer>>(MAP_SIZE);
    private List<List<Integer>> visited;
    private List<List<Cell>> predecessor;

    public Path findPath(Cell source, Cell destination) {

        Path pathToStart = findNearestPoint(source);
        Path pathToEnd = findNearestPoint(destination);

        Cell start = pathToStart.getDestination();
        Cell end = pathToEnd.getDestination();

        initializeVisitedMetrics();
        initializePredecessorMetrics();

        Queue<Cell> queue = new LinkedList<>();
        queue.add(start);

        while (!queue.isEmpty() && !isVisited(end.getRow(), end.getCol())) {
            Cell curr = queue.remove();
            visit(curr.getRow(), curr.getCol());

            int[][] steps = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

            for (int[] step : steps) {
                int row = curr.getRow() + step[0];
                int col = curr.getCol() + step[1];

                if (isValidMove(row, col)) {
                    queue.add(new Cell(row, col));
                    setPredecessor(row, col, curr);
                }
            }
        }

        Deque<Cell> path = new ArrayDeque<>();
        if (isVisited(end.getRow(), end.getCol())) {
            Cell curr = end;
            while (curr != start) {
                path.push(curr);
                curr = getPredecessor(curr);
            }
        }

        Path startEndPath = new Path(path.size(), path, start, end);

        return Path.finalPath(pathToStart, startEndPath, pathToEnd);
    }

    private boolean isValidMove(int row, int col) {
        return isValidCell(row, col) && mapData.get(row).get(col) == 1 && !isVisited(row, col);
    }

    private boolean isValidCell(int row, int col) {
        return row >= 0 && row < MAP_SIZE && col >= 0 && col < MAP_SIZE;
    }

    private boolean isVisited(int row, int col) {
        return visited.get(row).get(col) == 1;
    }

    private void visit(int row, int col) {
        visited.get(row).set(col, 1);
    }

    private void setPredecessor(int row, int col, Cell curr) {
        predecessor.get(row).set(col, curr);
    }

    private Cell getPredecessor(Cell curr) {
        return predecessor.get(curr.getRow()).get(curr.getCol());
    }

    private void initializeMapDataMetrics(List<List<Integer>> mapData) {
        this.mapData = mapData;
    }

    private void initializeVisitedMetrics() {
        visited = new ArrayList<List<Integer>>(MAP_SIZE);
        for (int i = 0; i < MAP_SIZE; i++) {
            visited.add(new ArrayList<Integer>(MAP_SIZE));
            for (int j = 0; j < MAP_SIZE; j++){
                visited.get(i).add(0);
            }
        }
    }

    private void initializePredecessorMetrics() {
        predecessor = new ArrayList<List<Cell>>(MAP_SIZE);
        for (int i = 0; i < MAP_SIZE; i++) {
            List<Cell> cells = new ArrayList<>();
            for (int j = 0; j < MAP_SIZE; j++) {
                cells.add(new Cell(-1, -1));
            }
            predecessor.add(cells);
        }
    }

    private Path findNearestPoint(Cell source) {
        if (mapData.get(source.getRow()).get(source.getCol()) == 1) {
            return new Path(0, new ArrayDeque<Cell>(), source, source);
        }
        initializeVisitedMetrics();
        initializePredecessorMetrics();
        Queue<Cell> queue = new LinkedList<>();
        queue.add(source);

        while (!queue.isEmpty()) {
            Cell curr = queue.remove();
            visit(curr.getRow(), curr.getCol());

            int[][] steps = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

            for (int[] step : steps) {
                int row = curr.getRow() + step[0];
                int col = curr.getCol() + step[1];

                if (isValidCell(row, col) && !isVisited(row, col)) {
                    if (mapData.get(row).get(col) == 1) {
                        Deque<Cell> path = new ArrayDeque<>();
                        path.push(new Cell(row, col));
                        while (curr != source) {
                            path.push(curr);
                            curr = getPredecessor(curr);
                        }
                        return new Path(path.size(), path, source, new Cell(row, col));
                    }
                    queue.add(new Cell(row, col));
                    setPredecessor(row, col, curr);
                }
            }
        }
        return null;
    }


    public static void main(String[] args) throws Exception {
        ShortestPath sp = new ShortestPath();

        sp.initializeMapDataMetrics(MapData.getMapData());

        Cell source = new Cell(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
        Cell destination = new Cell(Integer.parseInt(args[2]),Integer.parseInt(args[3]));

        Path path = sp.findPath(source, destination);

        System.out.println(path.toString());
    }
}
