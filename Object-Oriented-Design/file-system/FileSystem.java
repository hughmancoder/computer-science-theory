import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;

class FileSystem {
    private final Directory root;
    private Directory currentDirectory;

    public FileSystem() {
        root = new Directory("/", null);
        currentDirectory = root;
        System.out.println("Info: file system created");
    }

    public Directory getRoot() {
        return root;
    }

    Directory traverseDirectories(String path) {
        Directory t = currentDirectory;
        if (!path.equals("/")) {
            String[] d = path.split("/");
            for (int i = 1; i < d.length; i++) {
                if (!t.getSubDirectories().containsKey(d[i])) {
                    throw new IllegalArgumentException("Directory not found in path: " + path);
                }
                t = t.getSubDirectories().get(d[i]);
            }
        }
        return t;
    }

    public List<String> ls(String path) throws IllegalArgumentException {
        Directory t = root;
        List<String> contents = new ArrayList<>();
        if (!path.equals("/")) {
            String[] d = path.split("/");
            for (int i = 1; i < d.length; i++) {
                if (!t.getSubDirectories().containsKey(d[i])) {
                    throw new IllegalArgumentException("Directory not found in path: " + path);
                }
                t = t.getSubDirectories().get(d[i]);
            }
            contents = t.listContents();
        }
        Collections.sort(contents);
        return contents;
    }

    public void mkdir(String path) {
        Directory t = root;
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

    public String readContentFromFile(String filePath) {
        String[] d = filePath.split("/");
        String Directories = String.join("/", Arrays.copyOfRange(d, 0, d.length - 1));
        String fileName = d[d.length - 1];
        Directory childDirectory = traverseDirectories(Directories);
        Map<String, File> files = childDirectory.getFiles();
        if (!files.containsKey(fileName)) {
            throw new IllegalArgumentException("File not found: " + filePath);
        }
        File file = files.get(fileName);
        return file.getContent();
    }
}
