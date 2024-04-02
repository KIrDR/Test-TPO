import java.io.*;

public class ModifyJavaFile {
    public static void main(String[] args) {
        File inputFile = new File("Example.java");
        File outputFile = new File("ModifyExample.java");

        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile));
             PrintWriter writer = new PrintWriter(new FileWriter(outputFile))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Заменяем слово "public" на "private" в каждой строке
                String modifiedLine = line.replaceAll("\\bpublic\\b", "private");
                writer.println(modifiedLine);
            }
            System.out.println("Файл успешно изменен.");
        } catch (IOException e) {
            System.err.println("Ошибка при чтении или записи файла.");
            e.printStackTrace();
        }
    }
}
