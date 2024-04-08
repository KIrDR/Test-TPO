package org.example;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

class Airport {
    private static final int RUNWAYS = 5;
    private static final int SIMULATION_TIME = 10; // 10 секунд
    private static final int REAL_TIME_FACTOR = 1; // 1 секунда реального времени = 1 секунда в симуляции

    public static void main(String[] args) {
        ExecutorService runwayExecutor = Executors.newFixedThreadPool(RUNWAYS);
        for (int i = 0; i < RUNWAYS; i++) {
            runwayExecutor.execute(new Runway());
        }

        try {
            TimeUnit.SECONDS.sleep(1); // Даем время для запуска потоков
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        for (int i = 1; i <= 3; i++) {
            int runwayId = (i % RUNWAYS) + 1; // Полосы нумеруются с 1 до RUNWAYS
            Runway runway = getRunwayById(runwayId);
            if (runway != null) {
                runway.landPlane(i);
                try {
                    TimeUnit.SECONDS.sleep(1 * REAL_TIME_FACTOR);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                runway.takeOffPlane(i);
            }
        }

        try {
            TimeUnit.SECONDS.sleep((SIMULATION_TIME - 5) * REAL_TIME_FACTOR);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        runwayExecutor.shutdownNow();
    }

    private static Runway getRunwayById(int id) {
        for (Thread t : Thread.getAllStackTraces().keySet()) {
            if (t instanceof Runway && ((Runway) t).id == id) {
                return (Runway) t;
            }
        }
        return null;
    }

    static class Runway extends Thread {
        private static int runwayCounter = 0;
        private int id;
        private boolean occupied = false;

        public Runway() {
            this.id = ++runwayCounter;
        }

        @Override
        public void run() {
            try {
                while (!Thread.currentThread().isInterrupted()) {
                    System.out.println("Полоса " + id + " свободна");

                    // Ожидание самолета на полосе
                    TimeUnit.SECONDS.sleep(1 * REAL_TIME_FACTOR);

                    System.out.println("Полоса " + id + " приняла самолет");
                    occupied = true;

                    // Ожидание взлета самолета
                    TimeUnit.SECONDS.sleep(1 * REAL_TIME_FACTOR);

                    System.out.println("Самолет взлетел с полосы " + id);
                    occupied = false;
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        public boolean isOccupied() {
            return occupied;
        }

        public void landPlane(int planeId) {
            System.out.println("Самолет " + planeId + " приземлился на полосу " + id);
        }

        public void takeOffPlane(int planeId) {
            System.out.println("Самолет " + planeId + " покинул полосу " + id);
        }
    }
}
