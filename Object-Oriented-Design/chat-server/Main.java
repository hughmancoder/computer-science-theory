public class Main {
    public static void main(String[] args) {
        Server server = new Server();

        User alice = new User("Alice");
        User bob = new User("Bob");

        Client clientAlice = new Client(alice, server);
        Client clientBob = new Client(bob, server);

        String chatRoomId = "room1";

        clientAlice.sendMessage(chatRoomId, "Hi Bob!");
        clientBob.sendMessage(chatRoomId, "Hello Alice!");
    }
}
