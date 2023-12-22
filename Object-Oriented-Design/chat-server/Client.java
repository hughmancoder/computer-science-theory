public class Client {
    private User user;
    private Server server;

    public Client(User user, Server server) {
        this.user = user;
        this.server = server;
    }

    public void sendMessage(String chatRoomId, String content) {
        Message message = new Message(user.getUsername(), content);
        server.sendMessageToChatRoom(chatRoomId, message);
    }
}
