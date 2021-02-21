-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 12 Sty 2021, 11:33
-- Wersja serwera: 10.4.17-MariaDB
-- Wersja PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `przedmioty_cs`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `items`
--

CREATE TABLE `items` (
  `item_id` varchar(20) NOT NULL,
  `market_hash_name` varchar(60) NOT NULL,
  `market_hash_name_short` varchar(50) NOT NULL,
  `market_hash_name_shorter` varchar(40) NOT NULL,
  `price` decimal(15,2) NOT NULL,
  `inspect_link` varchar(500) NOT NULL,
  `has_expensive_stickers` tinyint(4) NOT NULL,
  `exterior` varchar(35) NOT NULL,
  `item_float` varchar(15) NOT NULL,
  `screenshot` varchar(100) NOT NULL,
  `tradeable` tinyint(1) NOT NULL,
  `tradeable_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `items`
--

INSERT INTO `items` (`item_id`, `market_hash_name`, `market_hash_name_short`, `market_hash_name_shorter`, `price`, `inspect_link`, `has_expensive_stickers`, `exterior`, `item_float`, `screenshot`, `tradeable`, `tradeable_date`) VALUES
('19962691815', 'SCAR-20 | Crimson Web (Field-Tested)', 'SCAR-20 Crimson Web (Field-Tested)', 'SCAR-20 Crimson Web FT', '1.16', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A19962691815D11593963225935546680', 1, 'Field-Tested', '0.1573464', 'https://s.swap.gg/Sfjw9HByr.jpg', 1, '0000-00-00 00:00:00'),
('20276189360', 'AWP | Redline (Field-Tested)', 'AWP Redline (Field-Tested)', 'AWP Redline FT', '25.53', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20276189360D1038722543479058475', 1, 'Field-Tested', '0.2245583', 'https://s.swap.gg/Fi5l61ckG.jpg', 1, '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `stickers`
--

CREATE TABLE `stickers` (
  `name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `stickers`
--

INSERT INTO `stickers` (`name`) VALUES
('3DMAX (Holo) | Katowice 2014'),
('3DMAX (Holo) | Katowice 2015'),
('3DMAX | Katowice 2014'),
('Clan-Mystik (Holo) | Katowice 2014'),
('Clan-Mystik | Katowice 2014'),
('Cloud9 (Holo) | DreamHack 2014'),
('Cloud9 G2A (Holo) | Katowice 2015'),
('compLexity Gaming (Holo) | Katowice 2014'),
('compLexity Gaming | Katowice 2014'),
('Counter Logic Gaming (Holo) | Katowice 2'),
('Crown (Foil)'),
('device (Gold) | Boston 2018'),
('ESL Skull (Foil) | Katowice 2014'),
('ESL Wolf (Foil) | Katowice 2014'),
('fer (Gold) | Boston 2018'),
('Flammable (Foil)'),
('Flipsid3 Tactics (Holo) | Katowice 2015'),
('Fnatic (Holo) | Katowice 2014'),
('Fnatic (Holo) | Katowice 2015'),
('Fnatic | Katowice 2014'),
('FURIA (Holo) | Katowice 2019'),
('Harp of War (Holo)'),
('Headhunter (Foil)'),
('HellRaisers (Holo) | Katowice 2014'),
('HellRaisers (Holo) | Katowice 2015'),
('HellRaisers | Katowice 2014'),
('Howling Dawn'),
('iBUYPOWER (Holo) | Cologne 2014'),
('iBUYPOWER (Holo) | Katowice 2014'),
('iBUYPOWER | DreamHack 2014'),
('iBUYPOWER | Katowice 2014'),
('kennyS (Gold) | Krakow 2017'),
('Keyd Stars (Holo) | Katowice 2015'),
('LGB eSports (Holo) | Katowice 2014'),
('LGB eSports | Katowice 2014'),
('mousesports (Holo) | Katowice 2014'),
('mousesports | Katowice 2014'),
('NAF (Gold) | Boston 2018'),
('Natus Vincere (Foil) | Katowice 2015'),
('Natus Vincere (Holo) | Katowice 2014'),
('Natus Vincere (Holo) | Katowice 2015'),
('Natus Vincere | Katowice 2014'),
('NiKo (Gold) | Katowice 2019'),
('Ninjas in Pyjamas (Holo) | Katowice 2014'),
('Ninjas in Pyjamas (Holo) | Katowice 2015'),
('Ninjas in Pyjamas | Katowice 2014'),
('Reason Gaming (Holo) | Katowice 2014'),
('Reason Gaming | Katowice 2014'),
('s1mple (Foil) | Atlanta 2017'),
('s1mple (Gold) | Boston 2018'),
('s1mple (Gold) | Katowice 2019'),
('ScreaM (Gold) | Boston 2018'),
('Sticker | kennyS (Gold) | London 2018'),
('Swag (Foil)'),
('Team Dignitas (Holo) | Cologne 2014'),
('Team Dignitas (Holo) | Katowice 2014'),
('Team Dignitas | Katowice 2014'),
('Team LDLC.com (Holo) | Katowice 2014'),
('Team LDLC.com | Katowice 2014'),
('Titan (Foil) | Cologne 2015'),
('Titan (Holo) | Cologne 2014'),
('Titan (Holo) | Katowice 2014'),
('Titan (Holo) | Katowice 2015'),
('Titan | Katowice 2014'),
('Tyloo (Foil) | Boston 2018'),
('Virtus.Pro (Holo) | Katowice 2014'),
('Virtus.pro (Holo) | Katowice 2015'),
('Virtus.Pro | Katowice 2014'),
('Vox Eminor (Holo) | Katowice 2014'),
('Vox Eminor | Katowice 2014'),
('Winged Defuser'),
('ZywOo (Gold) | Katowice 2019');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `stickers_applied`
--

CREATE TABLE `stickers_applied` (
  `item_id` varchar(20) NOT NULL,
  `sticker_1` varchar(60) NOT NULL,
  `sticker_2` varchar(60) NOT NULL,
  `sticker_3` varchar(60) NOT NULL,
  `sticker_4` varchar(60) NOT NULL,
  `sticker_5` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `stickers_applied`
--

INSERT INTO `stickers_applied` (`item_id`, `sticker_1`, `sticker_2`, `sticker_3`, `sticker_4`, `sticker_5`) VALUES
('19962691815', 'iBUYPOWER | Katowice 2014', '', '', '', ''),
('20276189360', 'LGB eSports (Holo) | Katowice 2014', 'Cloud9 | Cologne 2014', 'HellRaisers | Cologne 2014', '', '');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`item_id`);

--
-- Indeksy dla tabeli `stickers`
--
ALTER TABLE `stickers`
  ADD PRIMARY KEY (`name`);

--
-- Indeksy dla tabeli `stickers_applied`
--
ALTER TABLE `stickers_applied`
  ADD PRIMARY KEY (`item_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
