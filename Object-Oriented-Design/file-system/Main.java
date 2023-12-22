public class Main {

    public static void main(String args[]) {
        // Create a FileSystem
        FileSystem fs = new FileSystem();

        // Create a ~ directory
        fs.mkdir("/~");

        // Create a file in the ~ directory
        File file1 = new File("This is the content of file1");
        fs.getRoot().addFile("file1.txt", file1);

        // Create a subdirectory
        fs.mkdir("/~/subdir");

        // Create a file in the subdirectory
        File file2 = new File("This is the content of file2");
        fs.traverseDirectories("/~/subdir").addFile("file2.txt", file2);

        // Read content from a file in the ~ directory
        String content1 = fs.readContentFromFile("/file1.txt");
        System.out.println(content1);

        // Read content from a file in the subdirectory
        String content2 = fs.readContentFromFile("/~/subdir/file2.txt");
        System.out.println(content2);

    }
}