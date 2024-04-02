import java.util.*;

public class Train {
    private String destination;
    private int trainNumber;
    private String departureTime;
    private int totalSeats;
    private int coupeSeats;
    private int reservedSeats;
    private int luxurySeats;

    public Train(String destination, int trainNumber, String departureTime, int totalSeats, int coupeSeats, int reservedSeats, int luxurySeats) {
        this.destination = destination;
        this.trainNumber = trainNumber;
        this.departureTime = departureTime;
        this.totalSeats = totalSeats;
        this.coupeSeats = coupeSeats;
        this.reservedSeats = reservedSeats;
        this.luxurySeats = luxurySeats;
    }

    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }

    public int getTrainNumber() {
        return trainNumber;
    }

    public void setTrainNumber(int trainNumber) {
        this.trainNumber = trainNumber;
    }

    public String getDepartureTime() {
        return departureTime;
    }

    public void setDepartureTime(String departureTime) {
        this.departureTime = departureTime;
    }

    public int getTotalSeats() {
        return totalSeats;
    }

    public void setTotalSeats(int totalSeats) {
        this.totalSeats = totalSeats;
    }

    public int getCoupeSeats() {
        return coupeSeats;
    }

    public void setCoupeSeats(int coupeSeats) {
        this.coupeSeats = coupeSeats;
    }

    public int getReservedSeats() {
        return reservedSeats;
    }

    public void setReservedSeats(int reservedSeats) {
        this.reservedSeats = reservedSeats;
    }

    public int getLuxurySeats() {
        return luxurySeats;
    }

    public void setLuxurySeats(int luxurySeats) {
        this.luxurySeats = luxurySeats;
    }

    @Override
    public String toString() {
        return "Train{" +
                "destination='" + destination + '\'' +
                ", trainNumber=" + trainNumber +
                ", departureTime='" + departureTime + '\'' +
                ", totalSeats=" + totalSeats +
                ", coupeSeats=" + coupeSeats +
                ", reservedSeats=" + reservedSeats +
                ", luxurySeats=" + luxurySeats +
                '}';
    }

    public static void main(String[] args) {
         Train[] trains = {
                new Train("Moscow", 123, "10:00", 200, 50, 100, 50),
                new Train("St. Petersburg", 456, "12:00", 150, 40, 80, 30),
                new Train("Novosibirsk", 789, "14:00", 180, 60, 70, 50)
        };

        String destination = "Moscow";
        System.out.println("Trains to " + destination + ":");
        for (Train train : trains) {
            if (train.getDestination().equals(destination)) {
                System.out.println(train);
            }
        }

        String destination2 = "St. Petersburg";
        String departureTime2 = "11:00";
        System.out.println("\nTrains to " + destination2 + " after " + departureTime2 + ":");
        for (Train train : trains) {
            if (train.getDestination().equals(destination2) && train.getDepartureTime().compareTo(departureTime2) > 0) {
                System.out.println(train);
            }
        }

        String destination3 = "Novosibirsk";
        System.out.println("\nTrains to " + destination3 + " with reserved seats:");
        for (Train train : trains) {
            if (train.getDestination().equals(destination3) && train.getReservedSeats() > 0) {
                System.out.println(train);
            }
        }
    }
}
