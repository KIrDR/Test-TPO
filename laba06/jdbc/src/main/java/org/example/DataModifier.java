package org.example;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DataModifier {
    private Connection connection;

    public DataModifier() {
        try {
            connection = DBConnection.getConnection();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Пример метода для удаления фильмов, дата выхода которых была более заданного числа лет назад
    public void deleteOldMovies(int yearsAgo) {
        String query = "DELETE FROM movies WHERE YEAR(release_date) < YEAR(NOW()) - ?";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, yearsAgo);
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Другие методы для модификации данных
}
