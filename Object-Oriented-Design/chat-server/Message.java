public class Message {
    private String content;
    private String sender;

    public Message(String sender, String content) {
        this.sender = sender;
        this.content = content;
    }

    public String getContent() {
        return content;
    }

    public String getSender() {
        return sender;
    }
}
