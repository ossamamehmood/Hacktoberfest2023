import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rand = new Random();

        int lowerBound = 1;
        int upperBound = 100;
        int secretNumber = rand.nextInt(upperBound - lowerBound + 1) + lowerBound;
        int guess;
        int attempts = 0;

        System.out.println("Welcome to the Guess the Number game!");
        System.out.println("I'm thinking of a number between " + lowerBound + " and " + upperBound + ".");

        do {
            System.out.print("Enter your guess: ");
            guess = input.nextInt();
            attempts++;

            if (guess < secretNumber) {
                System.out.println("Too low! Try again.");
            } else if (guess > secretNumber) {
                System.out.println("Too high! Try again.");
            } else {
                System.out.println("Congratulations! You guessed the number in " + attempts + " attempts!");
            }
        } while (guess != secretNumber);

        input.close();
    }
}
