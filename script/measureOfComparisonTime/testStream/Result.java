import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.*;
import java.io.*;
import java.net.*;
import java.util.stream.Stream;
import java.util.stream.IntStream;
import java.util.stream.Collectors;

class Result{
    List<String[]> list = new ArrayList<>();

    public Result(List<String[]> list){
        this.list = list;
    }

    // public void resultPrint(){
    //     System.out.println(thresholdList.stream()
    //             .filter(n -> n >= 0.75)
    //             .count() + "," + comparisonTimeList.stream().mapToLong(n -> n).sum());
    // }

}
