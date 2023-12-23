public class Main {

    public static void main(String args[]) {
        // Create a FileSystem
        FileSystem fs = new FileSystem();

        // Create a directory
        fs.mkdir("user/subdir");

        // Create a file in the root directory
        File file1 = new File("This is the content of file1");
        fs.getCurrentDirectory().addFile("file1.txt", file1);

        // Create a file in the subdirectory
        File file2 = new File("This is the content of file2");
        fs.cd("user/subdir").addFile("file2.txt", file2);

        // Print current directory
        fs.pwd();

        // List contents of current directory
        fs.ls(null);

        // Create a new file in the current directory
        fs.touch("newfile.txt");

        // Remove a file from the current directory
        fs.rm("file2.txt");

        // List contents of current directory after removing a file
        fs.ls(null);
    }
}