// Source code is decompiled from a .class file using FernFlower decompiler.
public class Respondent extends Employee {
    public Respondent(String var1) {
        super(var1);
    }

    public void handleCall(Call var1) {
        System.out.println("Respondent " + this.getName() + " handling call");
        var1.reply("Respondent reply");
    }
}
