package org.example;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {
        try (Connection connection = DBConnection.getConnection()) {
            // Найти все фильмы, вышедшие на экран в текущем и прошлом году
            findRecentMovies(connection);

            // Вывести информацию об актерах, снимавшихся в заданном фильме
            int movieId = 1; // фильм с id = 1
            findActorsInMovie(connection, movieId);

            // Вывести информацию об актерах, снимавшихся как минимум в N фильмах
            int minMovieCount = 2;
            findActorsInMinimumMovies(connection, minMovieCount);

            // Вывести информацию об актерах, которые были режиссерами хотя бы одного из фильмов
            findActorDirectors(connection);

            // Удалить все фильмы, дата выхода которых была более заданного числа лет назад
            int yearsAgo = 5; // Предположим, что заданное количество лет - 5
            deleteOldMovies(connection, yearsAgo);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void findRecentMovies(Connection connection) throws SQLException {
        String query = "SELECT * FROM Movies WHERE YEAR(release_date) >= YEAR(NOW()) - 1";
        try (PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()) {
            System.out.println("Фильмы, вышедшие на экран в текущем и прошлом году:");
            while (resultSet.next()) {
                System.out.println(resultSet.getString("title"));
            }
            System.out.println();
        }
    }

    private static void findActorsInMovie(Connection connection, int movieId) throws SQLException {
        String query = "SELECT a.full_name FROM Actors a JOIN MovieActors ma ON a.actor_id = ma.actor_id WHERE ma.movie_id = ?";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, movieId);
            try (ResultSet resultSet = statement.executeQuery()) {
                System.out.println("Актеры, снимавшиеся в заданном фильме:");
                while (resultSet.next()) {
                    System.out.println(resultSet.getString("full_name"));
                }
                System.out.println();
            }
        }
    }

    private static void findActorsInMinimumMovies(Connection connection, int minMovieCount) throws SQLException {
        String query = "SELECT a.full_name FROM Actors a JOIN MovieActors ma ON a.actor_id = ma.actor_id GROUP BY a.actor_id HAVING COUNT(*) >= ?";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, minMovieCount);
            try (ResultSet resultSet = statement.executeQuery()) {
                System.out.println("Актеры, снимавшиеся как минимум в " + minMovieCount + " фильмах:");
                while (resultSet.next()) {
                    System.out.println(resultSet.getString("full_name"));
                }
                System.out.println();
            }
        }
    }

    private static void findActorDirectors(Connection connection) throws SQLException {
        String query = "SELECT DISTINCT a.full_name FROM Actors a JOIN Directors md ON a.actor_id = md.director_id";
        try (PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()) {
            System.out.println("Актеры, которые были режиссерами хотя бы одного из фильмов:");
            while (resultSet.next()) {
                System.out.println(resultSet.getString("full_name"));
            }
            System.out.println();
        }
    }

    private static void deleteOldMovies(Connection connection, int yearsAgo) throws SQLException {
        String query = "DELETE FROM Movies WHERE YEAR(release_date) < YEAR(NOW()) - ?";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, yearsAgo);
            int rowsAffected = statement.executeUpdate();
            System.out.println("Удалено " + rowsAffected + " фильмов, дата выхода которых была более " + yearsAgo + " лет назад");
        }
    }
}
