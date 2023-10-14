import java.util.*;

class Node {

    String task;
    String date;
    Node next;

    public Node(String task, String date) {

        this.task = task;
        this.date = date;
        next = null;

    }

}

class Node2 {

    String event;
    String date;
    Node2 next;

    public Node2(String event, String date) {

        this.event = event;
        this.date = date;
        next = null;

    }

}

class clan {

    class calendar {
        String info;
        calendar next;

        public calendar(String info) {
            this.info = info;
            next = null;
        }
    }

    calendar head3 = null;

    void add(String info) {
        calendar newNode = new calendar(info);
        if (head3 == null) {
            head3 = newNode;
        } else {
            calendar current = head3;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    void print() {

        calendar current = head3;

        int dayOfWeekCounter = 0;

        while (current != null) {

            System.out.print(current.info);

            current = current.next;
            dayOfWeekCounter++;

            if (dayOfWeekCounter == 7) {
                System.out.println();
                dayOfWeekCounter = 0;
            }
        }

        System.out.println();
    }

}

class Calendar {

    Node head;
    Node2 head2;
    // calendar head3;
    String dates[];

    public Calendar() {
        head = null;
        head2 = null;
    }

    static int getNumberOfDaysInMonth(int year, int month) {

        if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12)
            return 31;
        if (month == 4 || month == 6 || month == 9 || month == 11)
            return 30;
        if (month == 2)
            return isLeapYear(year) ? 29 : 28;
        return 0;
    }

    static boolean isLeapYear(int year) {

        return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);

    }

    public void insertTask(String event, String date) {
        Node newNode = new Node(event, date);
        newNode.next = head;
        head = newNode;
    }

    public void setMonth(int date, int month, int year) {
        dates = new String[getNumberOfDaysInMonth(year, month)];

        for (int i = 0; i < dates.length; i++) {
            if (month < 10)
                dates[i] = Integer.toString(i + 1) + "-0" + Integer.toString(month) + "-" + Integer.toString(year);
            else
                dates[i] = Integer.toString(i + 1) + "-" + Integer.toString(month) + "-" + Integer.toString(year);
        }

    }

    public void insertEvent(String event, String date) {
        Node2 newNode = new Node2(event, date);
        newNode.next = head2;
        head2 = newNode;
    }

    public void printTask() {
        Node current = head;
        while (current != null) {
            System.out.println("  " + current.date + " :  " + current.task);
            current = current.next;
        }
    }

    public void printEvent() {
        Node2 current = head2;
        while (current != null) {
            System.out.println("  " + current.date + " :  " + current.event);
            current = current.next;
        }
    }

    void printMonth(int year, int month) {
        printMonthTitle(year, month);
        printMonthBody(year, month);
    }

    void printMonthTitle(int year, int month) {
        System.out.println("         " + getMonthName(month) + " " + year);
        System.out.println(" Sun Mon Tue Wed Thu Fri Sat");
    }

    static String getMonthName(int month) {

        String monthName = null;
        switch (month) {
            case 1:
                monthName = "January";
                break;
            case 2:
                monthName = "February";
                break;
            case 3:
                monthName = "March";
                break;
            case 4:
                monthName = "April";
                break;
            case 5:
                monthName = "May";
                break;
            case 6:
                monthName = "June";
                break;
            case 7:
                monthName = "July";
                break;
            case 8:
                monthName = "August";
                break;
            case 9:
                monthName = "September";
                break;
            case 10:
                monthName = "October";
                break;
            case 11:
                monthName = "November";
                break;
            case 12:
                monthName = "December";
        }
        return monthName;
    }

    void printMonthBody(int year, int month) {

        int startDay = getStartDay(year, month);
        int numberOfDaysInMonth = getNumberOfDaysInMonth(year, month);
        clan cl = new clan();
        // cl.clear();

        for (int i = 0; i < startDay; i++)
            cl.add("    ");
        for (int i = 1; i <= numberOfDaysInMonth; i++) {
            if (i < 10)
                cl.add("   " + i);
            else
                cl.add("  " + i);
        }
        cl.print();

    }

    static int getStartDay(int year, int month) {
        int startDay1800 = 3;
        int totalNumberOfDays = getTotalNumberOfDays(year, month);
        return (totalNumberOfDays + startDay1800) % 7;
    }

    static int getTotalNumberOfDays(int year, int month) {

        int total = 0;
        for (int i = 1800; i < year; i++)
            if (isLeapYear(i))
                total = total + 366;
            else
                total = total + 365;
        for (int i = 1; i < month; i++)
            total = total + getNumberOfDaysInMonth(year, i);
        return total;
    }
}

class New {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        Calendar calan = new Calendar();

        System.out.println("Enter todays date");
        int dat = sc.nextInt();
        System.out.println("Enter todays Month");
        int month = sc.nextInt();
        System.out.println("Enter todays Year");
        int year = sc.nextInt();

        System.out.println("              [Calender]              ");
        System.out.println("1. Print Calendar");
        System.out.println("2. Print Today's Tasks");
        System.out.println("3. Print Today's Events");
        System.out.println("4. Add Task for Today");
        System.out.println("5. Add Event for Today");
        System.out.println("6. Exit");

        int x = sc.nextInt();
        switch (x) {
            case 1:
                calan.printMonth(year, month);
                break;
            case 2:
                calan.printTask();
                break;
            case 3:
                calan.printEvent();
                break;
            case 4:
                String temp;
                if (month < 10)
                    temp = Integer.toString(dat) + "-0" + Integer.toString(month) + "-" + Integer.toString(year);
                else
                    temp = Integer.toString(dat) + "-" + Integer.toString(month) + "-" + Integer.toString(year);

                System.out.println("Type your ToDo task");
                String tas = sc.next();
                calan.insertTask(tas, temp);

                break;
            case 5:
                String temp2;
                if (month < 10)
                    temp2 = Integer.toString(dat) + "-0" + Integer.toString(month) + "-" + Integer.toString(year);
                else
                    temp2 = Integer.toString(dat) + "-" + Integer.toString(month) + "-" + Integer.toString(year);

                System.out.println("Type your Event");
                String eve = sc.next();
                calan.insertEvent(eve, temp2);

                break;
            case 6:
                System.exit(0);
                break;
            default:
                System.out.println("Invalid Choice");
                break;
        }
    }
}
