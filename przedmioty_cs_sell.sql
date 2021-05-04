-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 04 Maj 2021, 20:20
-- Wersja serwera: 10.4.17-MariaDB
-- Wersja PHP: 7.3.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `przedmioty_cs_sell`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `marketplace_balance`
--

CREATE TABLE `marketplace_balance` (
  `waxpeer_balance` decimal(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `selling`
--

CREATE TABLE `selling` (
  `item_id` varchar(20) NOT NULL,
  `waxpeer_price` decimal(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `sold`
--

CREATE TABLE `sold` (
  `item_id` varchar(20) NOT NULL,
  `bought_for` decimal(15,2) NOT NULL,
  `sold_for` decimal(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `to_be_sold`
--

CREATE TABLE `to_be_sold` (
  `item_id` varchar(20) NOT NULL,
  `price` decimal(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `selling`
--
ALTER TABLE `selling`
  ADD PRIMARY KEY (`item_id`);

--
-- Indeksy dla tabeli `sold`
--
ALTER TABLE `sold`
  ADD PRIMARY KEY (`item_id`);

--
-- Indeksy dla tabeli `to_be_sold`
--
ALTER TABLE `to_be_sold`
  ADD PRIMARY KEY (`item_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
