package org.example;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        String filename = "C:\\MyStudy\\32\\Testing\\git-demo\\laba06\\string\\src\\main\\java\\org\\example\\input.txt"; // Имя файла для чтения текста
        List<String> words = readWordsFromFile(filename);

        if (words != null) {
            sortWordsByVowelRatio(words);
            for (String word : words) {
                System.out.println(word);
            }
        } else {
            System.out.println("Не удалось прочитать слова из файла.");
        }
    }

    private static List<String> readWordsFromFile(String filename) {
        List<String> words = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] lineWords = line.split("\\s+"); // Разбиваем строку на слова
                words.addAll(Arrays.asList(lineWords));
            }
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
        return words;
    }

    private static void sortWordsByVowelRatio(List<String> words) {
        Collections.sort(words, new Comparator<String>() {
            @Override
            public int compare(String word1, String word2) {
                double ratio1 = getVowelRatio(word1);
                double ratio2 = getVowelRatio(word2);
                return Double.compare(ratio1, ratio2);
            }
        });
    }

    private static double getVowelRatio(String word) {
        int vowelCount = 0;
        int totalCount = word.length();
        for (int i = 0; i < word.length(); i++) {
            char ch = Character.toLowerCase(word.charAt(i)); // Приводим символ к нижнему регистру
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'y' || ch == 'а' || ch == 'е' || ch == 'ё' || ch == 'и' || ch == 'о' || ch == 'у' || ch == 'ы' || ch == 'э' || ch == 'ю' || ch == 'я') {
                vowelCount++;
            }
        }
        return (double) vowelCount / totalCount;
    }

}
