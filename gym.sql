-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Mar 18, 2021 alle 11:59
-- Versione del server: 10.1.31-MariaDB
-- Versione PHP: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gym`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `admins`
--

CREATE TABLE `admins` (
  `admin_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `admins`
--

INSERT INTO `admins` (`admin_id`) VALUES
(36);

-- --------------------------------------------------------

--
-- Struttura della tabella `courses`
--

CREATE TABLE `courses` (
  `course_name` varchar(20) NOT NULL,
  `days` varchar(40) NOT NULL,
  `monthly_cost` double NOT NULL,
  `instructor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `courses`
--

INSERT INTO `courses` (`course_name`, `days`, `monthly_cost`, `instructor_id`) VALUES
('Ballo', 'lunedi', 50, 13),
('Nuoto', 'Martedi', 30, 13),
('Pilates', 'Lunedi,Mercoledi', 12, 18),
('Sala', 'Giovedi', 10, 16),
('Spinning', 'Sabato', 15, 18),
('Yoga', 'Lunedi', 15, 17),
('Zumba', 'Lunedi', 200, 16);

-- --------------------------------------------------------

--
-- Struttura della tabella `instructors`
--

CREATE TABLE `instructors` (
  `instructor_id` int(10) NOT NULL,
  `name` varchar(10) NOT NULL,
  `surname` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `instructors`
--

INSERT INTO `instructors` (`instructor_id`, `name`, `surname`) VALUES
(13, 'Giovanni', 'Pippo'),
(16, 'Mario', 'Rossi'),
(17, 'Fabrizio', 'Russo'),
(18, 'Mario', 'Draghi');

-- --------------------------------------------------------

--
-- Struttura della tabella `membership`
--

CREATE TABLE `membership` (
  `course_name` varchar(20) NOT NULL,
  `user_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `membership`
--

INSERT INTO `membership` (`course_name`, `user_id`) VALUES
('Yoga', 35),
('Spinning', 38),
('Yoga', 38),
('Zumba', 40),
('Ballo', 41),
('Yoga', 41),
('Zumba', 47);

-- --------------------------------------------------------

--
-- Struttura della tabella `users`
--

CREATE TABLE `users` (
  `user_id` int(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `surname` varchar(20) NOT NULL,
  `gender` char(1) NOT NULL,
  `address` varchar(20) NOT NULL,
  `birth_date` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `activation_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `users`
--

INSERT INTO `users` (`user_id`, `name`, `surname`, `gender`, `address`, `birth_date`, `email`, `username`, `password`, `activation_time`) VALUES
(35, 'Sara', 'Greco', 'F', 'Bergamo', '05/03/1997', '@gmail.it', 'q', 'q', '2021-03-05 09:47:21'),
(36, 'Diego', 'Calabretta', 'M', 'Via Roma', '05/03/1997', '@livre.it', 'a', 'a', '2021-03-05 09:50:07'),
(38, 'Giovanni', 'Verni', 'M', 'via Roma', '05/03/1997', '@live', 'w', 'w', '2021-07-05 12:34:33'),
(40, 'Franco', 'Romano', 'M', 'Via Rossi', '05/03/1997', 'rmial@gmail.com', 'asd', 'asd', '2021-03-05 12:39:06'),
(41, 'Fabio', 'Vecchio', 'M', 'via Perti', '05/03/1960', '@live.it', 't', 't', '2021-03-05 17:46:33'),
(42, 'Maria', 'Tari', 'F', 'Via giosa', '05/03/2012', '@GMAIL', 'd', 'd', '2021-03-05 18:02:05'),
(47, 'Gianfranco', 'Pitto', 'M', 'Via Etnea', '07/03/1970', 'f@gmai.com', 'zx', 'zx', '2021-03-07 11:59:07');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`admin_id`),
  ADD UNIQUE KEY `user_id` (`admin_id`);

--
-- Indici per le tabelle `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`course_name`),
  ADD KEY `instructor_id` (`instructor_id`);

--
-- Indici per le tabelle `instructors`
--
ALTER TABLE `instructors`
  ADD PRIMARY KEY (`instructor_id`);

--
-- Indici per le tabelle `membership`
--
ALTER TABLE `membership`
  ADD PRIMARY KEY (`user_id`,`course_name`),
  ADD UNIQUE KEY `user_id` (`user_id`,`course_name`),
  ADD KEY `course_name` (`course_name`);

--
-- Indici per le tabelle `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `admins`
--
ALTER TABLE `admins`
  MODIFY `admin_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT per la tabella `instructors`
--
ALTER TABLE `instructors`
  MODIFY `instructor_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT per la tabella `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `admins`
--
ALTER TABLE `admins`
  ADD CONSTRAINT `admins_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `courses`
--
ALTER TABLE `courses`
  ADD CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`instructor_id`) REFERENCES `instructors` (`instructor_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `membership`
--
ALTER TABLE `membership`
  ADD CONSTRAINT `membership_ibfk_2` FOREIGN KEY (`course_name`) REFERENCES `courses` (`course_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `membership_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
