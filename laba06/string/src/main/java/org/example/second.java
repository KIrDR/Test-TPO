package org.example;
import java.io.*;
import java.util.*;
import java.util.regex.*;

public class second {
    public static void main(String[] args) throws IOException {
        String filename = "C:\\MyStudy\\32\\Testing\\git-demo\\laba06\\string\\src\\main\\java\\org\\example\\input.txt"; // Имя файла для чтения текста

        File file = new File(filename);
        BufferedReader reader = new BufferedReader(new FileReader(file));

        List<String> vowelWords = new ArrayList<>();
        String line;
        while ((line = reader.readLine()) != null) {
            for (String word : line.split("\\s+")) {
                if (word.matches("^[аеёиоуыэюяАЕЁИОУЫЭЮЯ].*")) {
                    vowelWords.add(word);
                }
            }
        }
        reader.close();

        Collections.sort(vowelWords, new Comparator<String>() {
            @Override
            public int compare(String word1, String word2) {
                char firstConsonant1 = findFirstConsonant(word1);
                char firstConsonant2 = findFirstConsonant(word2);
                return Character.compare(firstConsonant1, firstConsonant2);
            }

            private char findFirstConsonant(String word) {
                for (char c : word.toCharArray()) {
                    if (!"аеёиоуыэюяАЕЁИОУЫЭЮЯ".contains(String.valueOf(c))) {
                        return c;
                    }
                }
                return 'а'; // Возвращаем 'а', если согласная не найдена
            }
        });

        for (String word : vowelWords) {
            System.out.println(word);
        }
    }
}
