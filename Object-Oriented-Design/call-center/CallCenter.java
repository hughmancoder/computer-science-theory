
// Source code is decompiled from a .class file using FernFlower decompiler.
import java.util.Iterator;
import java.util.List;

public class CallCenter {
    private List<Respondent> respondents;
    private List<Manager> managers;
    private List<Director> directors;

    public CallCenter(List<Respondent> var1, List<Manager> var2, List<Director> var3) {
        this.respondents = var1;
        this.managers = var2;
        this.directors = var3;
    }

    public void dispatchCall(Call var1) {
        Employee var2 = this.findAvailableEmployee();
        if (var2 != null) {
            var2.handleCall(var1);
        }

    }

    private Employee findAvailableEmployee() {
        Iterator var1 = this.respondents.iterator();

        Respondent var2;
        do {
            if (!var1.hasNext()) {
                var1 = this.managers.iterator();

                Manager var3;
                do {
                    if (!var1.hasNext()) {
                        var1 = this.directors.iterator();

                        Director var4;
                        do {
                            if (!var1.hasNext()) {
                                return null;
                            }

                            var4 = (Director) var1.next();
                        } while (!var4.isAvailable());

                        return var4;
                    }

                    var3 = (Manager) var1.next();
                } while (!var3.isAvailable());

                return var3;
            }

            var2 = (Respondent) var1.next();
        } while (!var2.isAvailable());

        return var2;
    }
}
