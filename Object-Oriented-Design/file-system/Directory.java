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
    private String directoryPath;
    private Map<String, Directory> subDirectories = new HashMap<>();
    private Map<String, File> files = new HashMap<>();
    private static long creationTime;
    private long modificationTime;
    private Directory parentDirectory;

    public Directory(String directoryPath, Map<String, Directory> subDirectories, Directory parentDirectory) {
        this.subDirectories = (subDirectories != null) ? subDirectories : new HashMap<>();
        this.modificationTime = System.currentTimeMillis();
        this.files = new HashMap<>();
        this.directoryPath = directoryPath;
        this.parentDirectory = parentDirectory;
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
        for (Directory subDirectory : subDirectories.values()) {
            contents.add(subDirectory.getName());
        }
        return contents;
    }

    public String getName() {
        String[] pathArray = directoryPath.split("/");
        return pathArray[pathArray.length - 1];
    }

    public String getDirectoryPath() {
        return this.directoryPath;
    }

    public Map<String, Directory> getSubDirectories() {
        return subDirectories;
    }

    public void putSubDirectory(String name) {
        subDirectories.put(name, new Directory(name, null, this));
    }

    public Directory getParentDirectory() {
        return parentDirectory;
    }

    public Map<String, File> getFiles() {
        return files;
    }
}