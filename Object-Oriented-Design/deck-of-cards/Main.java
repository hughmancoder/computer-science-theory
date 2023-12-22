public class Main {
    public static void main(String[] args) {
        Deck deck = new Deck();
        deck.dealCard().display();
        deck.dealCard().display();
        deck.shuffle();
        deck.dealCard().display();
        deck.shuffle();
    }
}