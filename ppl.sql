-- Заполнение таблицы Users
INSERT INTO Users (login, password, username, experience) VALUES 
('bob', 'password1', 'User One', 1000),
('dell', 'password2', 'User Two', 1500),
('froot', 'password3', 'User Three', 2000);

-- Заполнение таблицы Tasks
INSERT INTO Tasks (Name, Description, Difficulty) VALUES 
('0. История языка python', 'Description for Task 1', 1),
('1. Ввод и вывод', 'Description for Task 2', 2),
('Task 3', 'Description for Task 3', 3);

-- Заполнение таблицы Achievements
INSERT INTO Achievements (AchieveName, goal, reward) VALUES 
('Achievement 1', 'Complete 10 tasks', '500'),
('Achievement 2', 'Reach level 5', '700'),
('Achievement 3', 'Complete all tasks', '1000');

-- Заполнение таблицы AchievementsList
INSERT INTO AchievementsList (UserID, AchieveName) VALUES 
(1, 'Achievement 1'),
(2, 'Achievement 2'),
(3, 'Achievement 3');

-- Заполнение таблицы TaskCompletions
INSERT INTO TaskCompletions (UserID, TaskID) VALUES 
(1, 1),
(1, 2),
(2, 2),
(3, 3);
