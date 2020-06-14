package com.iLink.Hackathon.Utils;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class MapData {

    public static List<List<Integer>> getMapData() throws FileNotFoundException {
        File file = new File("/Users/gopabhin/IdeaProjects/iLinkHackathon/src/com/iLink/Hackathon/Utils/mapInput.txt");
        Scanner sc = new Scanner(file);
        List<List<Integer>> mapData = new ArrayList<List<Integer>>();

        while (sc.hasNextLine()) {
            String numbers = sc.nextLine();
            List<Integer> list = Stream.of(numbers.split(","))
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());

            mapData.add(list);
        }
        return mapData;
    }

}
