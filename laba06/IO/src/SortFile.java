import java.io.*;
import java.util.*;

public class SortFile {
    public static void main(String[] args) {
        File file = new File("numbers.txt");
        generateRandomNumbers(file, 10);

        List<Integer> numbers = readNumbersFromFile(file);
        Collections.sort(numbers);
        writeNumbersToFile(file, numbers);
    }

    private static void generateRandomNumbers(File file, int count) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(file))) {
            Random random = new Random();
            for (int i = 0; i < count; i++) {
                int randomNumber = random.nextInt(100);
                writer.println(randomNumber);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static List<Integer> readNumbersFromFile(File file) {
        List<Integer> numbers = new ArrayList<>();
        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNextInt()) {
                int number = scanner.nextInt();
                numbers.add(number);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return numbers;
    }
    private static void writeNumbersToFile(File file, List<Integer> numbers) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(file))) {
            for (int number : numbers) {
                writer.println(number);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
