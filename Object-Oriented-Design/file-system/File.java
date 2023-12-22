import java.io.Serializable;

public class File implements Serializable {

    private String name;
    private byte[] content;
    private long creationTime;
    private long modificationTime;

    public File(String content) {
        this.creationTime = System.currentTimeMillis();
        this.content = content.getBytes();
    }

    public void setContent(byte[] content) {
        modificationTime = System.currentTimeMillis();
        ;
        this.content = content;
    }

    public String getName() {
        return name;
    }

    public String getContent() {
        return new String(content);
    }
}