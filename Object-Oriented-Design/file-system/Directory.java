import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

/*
 * Serializable indicates that an object can be converted into a stream of bytes
 * and reconstructed later back into its original state. This process is called
 * serialization and deserialization respectively.
 */

public class Directory implements Serializable {

    private String name;
    private Map<String, Directory> subDirectories = new HashMap<>();
    private Map<String, File> files = new HashMap<>();
    private static long creationTime;
    private long modificationTime;

    public Directory(String name, Map<String, Directory> subDirectories) {
        this.subDirectories = (subDirectories != null) ? subDirectories : new HashMap<>();
        this.modificationTime = System.currentTimeMillis();
        this.files = new HashMap<>();
        this.name = name;
    }

    public void addDirectory(String name, Directory directory) {
        if (subDirectories.containsKey(name)) {
            throw new IllegalArgumentException("Directory already exists: " + name);
        }
        subDirectories.put(name, directory);
        modificationTime = System.currentTimeMillis();
    }

    public void addFile(String name, File file) {
        if (files.containsKey(name)) {
            throw new IllegalArgumentException("File already exists: " + name);
        }
        files.put(name, file);
        modificationTime = System.currentTimeMillis();
    }

    public List<String> listContents() {
        List<String> contents = new ArrayList<>();
        for (String fileName : files.keySet()) {
            contents.add(fileName);
        }
        for (String subDirectoryName : subDirectories.keySet()) {
            contents.add(subDirectoryName + "/");
        }
        return contents;
    }

    public String getName() {
        return name;
    }

    public Map<String, Directory> getSubDirectories() {
        return subDirectories;
    }

    public void putSubDirectory(String name) {
        subDirectories.put(name, new Directory(name, null));
    }

    public Map<String, File> getFiles() {
        return files;
    }
}