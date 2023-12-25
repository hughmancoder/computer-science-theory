// Source code is decompiled from a .class file using FernFlower decompiler.
public class Director extends Employee {
    public Director(String var1) {
        super(var1);
    }

    public void handleCall(Call var1) {
        System.out.println("Director " + this.getName() + " handling call");
        var1.reply("Director reply");
    }
}
