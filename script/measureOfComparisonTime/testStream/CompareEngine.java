import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.*;
import java.io.*;
import java.net.*;
import java.util.stream.Stream;
import java.util.stream.IntStream;
import java.util.stream.Collectors;

class CompareEngine{
    private String filename;
    private String birthmark;
    private String filenameOfSearchResult;
    private String simOfSearchResult;
    private String birthmarkOfSearchResult;

    public CompareEngine(String filename, String birthmark, String filenameOfSearchResult, String simOfSearchResult, String birthmarkOfSearchResult){
        this.filename = filename;
        this.birthmark = birthmark;
        this.filenameOfSearchResult = filenameOfSearchResult;
        this.simOfSearchResult = simOfSearchResult;
        this.birthmarkOfSearchResult = birthmarkOfSearchResult;
    }


    public File createFile(String filename) throws IOException{
        File file = new File("./" + filename + ".csv");
        file.createNewFile();
        return file;
    }

    public void deleteFile(String filename) throws IOException{
        File file = new File("./" + filename + ".csv");
        file.delete();
    }

    public FileWriter createFileWriter(File file) throws IOException{
        return new FileWriter(file);
    }

    public void writeFile() throws IOException{
        writeAndCloseFileWriter(createFileWriter(createFile(filename.concat("1"))), filename.concat("1"), birthmark);;
        writeAndCloseFileWriter(createFileWriter(createFile(filenameOfSearchResult.concat("2"))), filenameOfSearchResult.concat("2"), birthmarkOfSearchResult.replace("\"", ""));;
    }

    public void writeAndCloseFileWriter(FileWriter filewriter, String f, String b) throws IOException{
        PrintWriter pw = new PrintWriter(new BufferedWriter(filewriter));
        pw.write(f + ",,," + b);
        pw.close();
    }

    public List<String> runCompare() throws IOException{
        writeFile();
        return new BufferedReader(new InputStreamReader(Runtime.getRuntime().exec("java -jar -Xms12g -Xmx12g ./pochi/pochi-runner/target/pochi-runner-1.0-SNAPSHOT.jar ./compare_input_csv_test.js ./" + filename + "1.csv ./" + filenameOfSearchResult + "2.csv").getInputStream()))
            .lines()
            .collect(Collectors.toList());
    }

    public String performCompare(){
        try{
            List<String> list = runCompare();
            deleteFile(filename.concat("1"));
            deleteFile(filenameOfSearchResult.concat("2"));
            return list.get(0).split(",")[2] + "," + list.get(1);
        }catch(Exception e){
            System.out.println(e);
            return null;
        }
    }
}
