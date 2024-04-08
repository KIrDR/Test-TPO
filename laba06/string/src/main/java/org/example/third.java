package org.example;
import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.*;

public class third {
    public static void main(String[] args) throws IOException {
        String filePath = "C:\\MyStudy\\32\\Testing\\git-demo\\laba06\\string\\src\\main\\java\\org\\example\\input.txt"; // Имя файла для чтения текста
        char letter = 'а'; // Замените на букву, по которой нужно сортировать
        List<String> words = Files.lines(Paths.get(filePath))
                .flatMap(line -> Arrays.stream(line.split("\\s+")))
                .collect(Collectors.toList());

        Comparator<String> byLetterCount = Comparator.comparingInt(
                word -> (int) word.chars().filter(ch -> ch == letter).count()
        );

        Comparator<String> alphabetical = Comparator.naturalOrder();

        words.stream()
                .sorted(byLetterCount.thenComparing(alphabetical))
                .forEach(System.out::println);
    }
}
