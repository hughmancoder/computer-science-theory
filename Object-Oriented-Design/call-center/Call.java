// Source code is decompiled from a .class file using FernFlower decompiler.
public class Call {
    private Employee caller;
    private int rank;

    public Call(Employee var1) {
        this.caller = var1;
        this.rank = 0;
    }

    public Employee getCaller() {
        return this.caller;
    }

    public void reply(String var1) {
        System.out.println("Replying to caller: " + var1);
    }

    public int getRank() {
        return this.rank;
    }

    public void disconnect() {
        this.reply("Thank you for calling");
    }
}
