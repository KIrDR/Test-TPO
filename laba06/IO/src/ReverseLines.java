import java.io.*;

public class ReverseLines {
    public static void main(String[] args) {
        File inputFile = new File("input.java");
        File outputFile = new File("output.java");

        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile));
             PrintWriter writer = new PrintWriter(new FileWriter(outputFile))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Переворачиваем строку
                String reversedLine = new StringBuilder(line).reverse().toString();
                writer.println(reversedLine);
            }
            System.out.println("Файл успешно перевернут.");
        } catch (IOException e) {
            System.err.println("Ошибка при чтении или записи файла.");
            e.printStackTrace();
        }
    }
}
