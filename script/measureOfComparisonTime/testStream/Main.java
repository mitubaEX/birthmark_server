import java.io.FileReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.*;
import java.io.*;
import java.net.*;
import java.util.stream.Stream;
import java.util.stream.IntStream;
import java.util.stream.Collectors;

class Main{
    private List<Double> thresholdList = new ArrayList<>();
    private List<Long> comparisonTimeList = new ArrayList<>();
    private long allTime = 0;
    public Main(String[] args){
        try{
            TextReader textReader = new TextReader(args);
            textReader.readFile()
                .stream()
                .forEach(n -> parseStream2(n.collectSearcher()));
            // System.out.println(thresholdList.stream()
            //         .filter(n -> n >= 0.75)
            //         .count() + "," + comparisonTimeList.stream().mapToLong(n -> n).sum());
        }catch(Exception e){
            // System.out.println(e + ":main");
        }
    }

    public void parseStream(Stream<SearchEngine> stream){
        stream.forEach(n -> parseString(n.run().filter(i -> i != null)));
    }
    public void parseStream2(Stream<SearchEngine> stream){
        stream.forEach(n -> allTime += n.run2());
        System.out.println(allTime);
    }

    public void parseString(Stream<String[]> stream){
        stream.forEach(m -> listAdd(m[0],m[1]));
    }

    public void listAdd(String a, String b){
        thresholdList.add(Double.parseDouble(a));
        comparisonTimeList.add(Long.parseLong(b));
    }

    public static void main(String[] args){
        new Main(args);
        System.out.println("exit!");
    }
}
