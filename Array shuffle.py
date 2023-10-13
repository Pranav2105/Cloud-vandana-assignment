#Create an array with the values (1, 2, 3, 4, 5, 6, 7) and shuffle it.
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ShuffleArray {
    public static void main(String[] args) {
        // Create an ArrayList with the values (1, 2, 3, 4, 5, 6, 7)
        List<Integer> arrayList = new ArrayList<>();
        arrayList.add(1);
        arrayList.add(2);
        arrayList.add(3);
        arrayList.add(4);
        arrayList.add(5);
        arrayList.add(6);
        arrayList.add(7);

        // Shuffle the ArrayList
        Collections.shuffle(arrayList);

        // Convert the shuffled ArrayList back to an array if needed
        Integer[] shuffledArray = arrayList.toArray(new Integer[0]);

        // Print the shuffled array
        for (int i = 0; i < shuffledArray.length; i++) {
            System.out.print(shuffledArray[i]);
            if (i < shuffledArray.length - 1) {
                System.out.print(", ");
            }
        }
    }
}
