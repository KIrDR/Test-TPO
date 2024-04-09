package org.example;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class QueryExecutor {
    private Connection connection;

    public QueryExecutor() {
        try {
            connection = DBConnection.getConnection();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Пример метода для поиска фильмов, вышедших на экран в текущем и прошлом году
    public void findRecentMovies() {
        String query = "SELECT * FROM movies WHERE YEAR(release_date) >= YEAR(NOW()) - 1";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                // Обработка результата
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Другие методы для выполнения запросов
}
