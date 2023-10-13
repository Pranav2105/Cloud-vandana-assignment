#Java code to Check if the input is pangram or not. (A pangram is a sentence that contains all the alphabets from A to Z).
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class PangramChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String input = scanner.nextLine().toLowerCase(); // Convert to lowercase for case insensitivity
        scanner.close();

        boolean isPangram = isPangram(input);
        
        if (isPangram) {
            System.out.println("The input is a pangram.");
        } else {
            System.out.println("The input is not a pangram.");
        }
    }

    public static boolean isPangram(String input) {
        Set<Character> characterSet = new HashSet<>();

        for (char c : input.toCharArray()) {
            if (Character.isLetter(c)) {
                characterSet.add(c);
            }
        }

        // Check if the set contains all 26 letters (A to Z)
        return characterSet.size() == 26;
    }
}
