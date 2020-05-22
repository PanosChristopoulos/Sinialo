package selector;
import java.util.Scanner;
 class selectorscreen {
    int days;
    int people;
    int budget;
    int num_visit;
    int num_search;

    public selectorscreen(int days,int people, int budget,int num_visit,int num_search) {
        this.days = days;
        this.people = people;
        this.budget = budget;
        num_visit = num_visit+1;
        num_search = num_search+1;

    }

    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);

        System.out.println("Enter days,number of people,budget in euros:");
        int days=myObj.nextInt();
        int people=myObj.nextInt();
        int budget=myObj.nextInt();

        System.out.println("days: " +days );
        System.out.println("people: " +people );
        System.out.println("budget: " +budget );

    }
}
