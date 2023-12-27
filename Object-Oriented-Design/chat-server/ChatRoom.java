import java.util.ArrayList;
import java.util.List;

public class ChatRoom {
    private List<Message> messages = new ArrayList<>();

    public void addMessage(Message message) {
        messages.add(message);
        System.out.println("[" + message.getSender() + "]: " + message.getContent());
    }
}
