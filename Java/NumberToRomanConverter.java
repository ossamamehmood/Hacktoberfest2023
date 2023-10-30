//Add Number to Roman convertor in java

import java.util.Scanner;

public class NumberToRomanConverter {

    public static String intToRoman(int num) {
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] romanSymbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder result = new StringBuilder();
        int i = 0;

        while (num > 0) {
            int quotient = num / values[i];
            num %= values[i];
            for (int j = 0; j < quotient; j++) {
                result.append(romanSymbols[i]);
            }
            i++;
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        scanner.close();

        if (number < 1 || number > 3999) {
            System.out.println("Please enter a number between 1 and 3999.");
        } else {
            String romanNumeral = intToRoman(number);
            System.out.println("Roman numeral: " + romanNumeral);
        }
    }
}

