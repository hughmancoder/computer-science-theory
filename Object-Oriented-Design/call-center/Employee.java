// Source code is decompiled from a .class file using FernFlower decompiler.
public abstract class Employee {
    private boolean available = true;
    protected String name;

    Employee(String var1) {
        this.name = var1;
    }

    public String getName() {
        return this.name;
    }

    public boolean isAvailable() {
        return this.available;
    }

    public void setAvailable(boolean var1) {
        this.available = var1;
    }

    public abstract void handleCall(Call var1);
}
