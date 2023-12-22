import java.util.HashMap;
import java.util.Map;

public class Server {
    private Map<String, ChatRoom> chatRooms = new HashMap<>();

    public void sendMessageToChatRoom(String chatRoomId, Message message) {
        if (!chatRooms.containsKey(chatRoomId)) {
            chatRooms.put(chatRoomId, new ChatRoom());
        }
        chatRooms.get(chatRoomId).addMessage(message);
    }
}
