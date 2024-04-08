package org.example;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

abstract class Sweet {
    private String name;
    private double weight;
    private double sugarContent;

    public Sweet(String name, double weight, double sugarContent) {
        this.name = name;
        this.weight = weight;
        this.sugarContent = sugarContent;
    }

    public String getName() {
        return name;
    }

    public double getWeight() {
        return weight;
    }

    public double getSugarContent() {
        return sugarContent;
    }
}

// Расширение класса Sweet для конкретных типов конфет
class Candy extends Sweet {
    public Candy(String name, double weight, double sugarContent) {
        super(name, weight, sugarContent);
    }
}

class Gift {
    private List<Sweet> sweets = new ArrayList<>();

    public void addSweet(Sweet sweet) {
        sweets.add(sweet);
    }

    public double calculateTotalWeight() {
        return sweets.stream().mapToDouble(Sweet::getWeight).sum();
    }

    public void sortBySugarContent() {
        sweets.sort(Comparator.comparingDouble(Sweet::getSugarContent));
    }

    public List<Sweet> findSweetsBySugarRange(double min, double max) {
        return sweets.stream()
                .filter(s -> s.getSugarContent() >= min && s.getSugarContent() <= max)
                .collect(Collectors.toList());
    }

    public void printSweets() {
        sweets.forEach(s -> System.out.println(s.getName() + ": " + s.getWeight() + "g, Sugar: " + s.getSugarContent() + "%"));
    }
}

// Демонстрация использования классов
public class NewYearGiftApp {
    public static void main(String[] args) {
        Gift gift = new Gift();

        gift.addSweet(new Candy("Конфета А", 10, 5.5));
        gift.addSweet(new Candy("Конфета Б", 15, 7.2));
        gift.addSweet(new Candy("Конфета В", 8, 4.8));

        System.out.println("Общий вес подарка: " + gift.calculateTotalWeight() + "g");

        gift.sortBySugarContent();

        double minSugar = 4.0;
        double maxSugar = 6.0;
        List<Sweet> sweetsInRange = gift.findSweetsBySugarRange(minSugar, maxSugar);
        System.out.println("Конфеты в диапазоне сахара от " + minSugar + "% до " + maxSugar + "%:");
        sweetsInRange.forEach(s -> System.out.println(s.getName()));

        System.out.println("Все конфеты в подарке:");
        gift.printSweets();
    }
}
