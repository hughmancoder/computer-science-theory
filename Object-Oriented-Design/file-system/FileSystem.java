import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

class FileSystem {
    private final Directory root;
    private Directory currentDirectory;

    public FileSystem() {
        root = new Directory("~", null);
        currentDirectory = root;
        System.out.println("Info: file system created");
    }

    public Directory getRoot() {
        return root;
    }

    Directory cd(String path) {
        Directory t = currentDirectory;
        if (!path.equals("/")) {
            String[] d = path.split("/");
            System.out.println("Info: changing directory to: " + path + " from " + currentDirectory.getDirectoryPath()
                    + " path sourcemap is " + Arrays.toString(d));
            for (int i = 1; i < d.length; i++) {
                if (d[i].length() == 0) {
                    continue;
                }
                if (!t.getSubDirectories().containsKey(d[i])) {
                    throw new IllegalArgumentException("Directory not found in path: " + path);
                }
                t = t.getSubDirectories().get(d[i]);
            }
        }
        this.currentDirectory = t;
        return t;
    }

    public void ls(String path) {
        Directory t = currentDirectory;
        List<String> contents = new ArrayList<>();
        if (path != null) {
            String[] directories = path.split("/");
            for (String directory : directories) {
                if (!t.getSubDirectories().containsKey(directory)) {
                    throw new IllegalArgumentException("Directory not found in path: " + path);
                }
                t = t.getSubDirectories().get(directory);
            }
        }
        contents = t.listContents();
        contents.sort(String::compareTo);
        for (String content : contents) {
            System.out.println(content);
        }
    }

    public void mkdir(String path) {
        Directory t = currentDirectory;
        String[] d = path.split("/");
        for (int i = 1; i < d.length; i++) {
            String pathStr = d[i];
            if (!t.getSubDirectories().containsKey(pathStr)) {
                t.putSubDirectory(pathStr);
                System.out.println("Info: directory created: " + pathStr);
            }
            t = t.getSubDirectories().get(d[i]);
        }
    }

    public void pwd() {
        System.out.println(currentDirectory.getDirectoryPath());
    }

    public String readContentFromFile(String fileName) {
        Map<String, File> files = currentDirectory.getFiles();
        if (!files.containsKey(fileName)) {
            throw new IllegalArgumentException("File not found in " + currentDirectory.getDirectoryPath());
        }
        File file = files.get(fileName);
        return file.getContent();
    }

    public void rm(String filePath) {
        String[] d = filePath.split("/");
        String Directories = String.join("/", Arrays.copyOfRange(d, 0, d.length - 1));
        String fileName = d[d.length - 1];
        Directory childDirectory = cd(Directories);
        Map<String, File> files = childDirectory.getFiles();
        if (!files.containsKey(fileName)) {
            throw new IllegalArgumentException("File not found: " + filePath);
        }
        files.remove(fileName);
        System.out.println("Info: file removed: " + filePath);
    }

    public void touch(String filePath) {
        String[] d = filePath.split("/");
        String Directories = String.join("/", Arrays.copyOfRange(d, 0, d.length - 1));
        String fileName = d[d.length - 1];
        Directory childDirectory = cd(Directories);
        Map<String, File> files = childDirectory.getFiles();
        if (files.containsKey(fileName)) {
            throw new IllegalArgumentException("File already exists: " + filePath);
        }
        files.put(fileName, new File(""));
        System.out.println("Info: file created: " + filePath);
    }

    public Directory getCurrentDirectory() {
        return currentDirectory;
    }
}