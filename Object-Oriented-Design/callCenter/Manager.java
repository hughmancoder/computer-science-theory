// Source code is decompiled from a .class file using FernFlower decompiler.
public class Manager extends Employee {
    public Manager(String var1) {
        super(var1);
    }

    public void handleCall(Call var1) {
        String var10001 = this.name;
        System.out.println("Manager " + var10001 + " handling call from " + var1.getCaller().getName());
    }
}
