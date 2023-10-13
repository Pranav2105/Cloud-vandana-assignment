#Java code to Enter a Roman Number as input and convert it to an integer. (Example: IX = 9)
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class RomanToInteger {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a Roman numeral: ");
        String romanNumeral = scanner.nextLine().toUpperCase();
        scanner.close();

        int result = romanToInteger(romanNumeral);
        if (result == -1) {
            System.out.println("Invalid Roman numeral.");
        } else {
            System.out.println("Integer equivalent: " + result);
        }
    }

    public static int romanToInteger(String s) {
        Map<Character, Integer> romanToIntegerMap = new HashMap<>();
        romanToIntegerMap.put('I', 1);
        romanToIntegerMap.put('V', 5);
        romanToIntegerMap.put('X', 10);
        romanToIntegerMap.put('L', 50);
        romanToIntegerMap.put('C', 100);
        romanToIntegerMap.put('D', 500);
        romanToIntegerMap.put('M', 1000);

        int result = 0;
        int prevValue = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int currentValue = romanToIntegerMap.getOrDefault(s.charAt(i), 0);

            if (currentValue < prevValue) {
                result -= currentValue;
            } else {
                result += currentValue;
            }

            prevValue = currentValue;
        }

        // Check for invalid Roman numerals
        for (int i = 0; i < s.length() - 1; i++) {
            if (romanToIntegerMap.get(s.charAt(i)) < romanToIntegerMap.get(s.charAt(i + 1))) {
                return -1; // Invalid Roman numeral
            }
        }

        return result;
    }
}
