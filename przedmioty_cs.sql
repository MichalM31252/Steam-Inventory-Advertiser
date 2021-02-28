-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 01 Mar 2021, 00:15
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
  `exterior` varchar(35) NOT NULL,
  `item_float` varchar(15) NOT NULL,
  `screenshot` varchar(100) NOT NULL,
  `tradeable` tinyint(1) NOT NULL,
  `tradeable_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `items`
--

INSERT INTO `items` (`item_id`, `market_hash_name`, `market_hash_name_short`, `market_hash_name_shorter`, `price`, `inspect_link`, `exterior`, `item_float`, `screenshot`, `tradeable`, `tradeable_date`) VALUES
('20816824720', 'AK-47 | The Empress (Minimal Wear)', 'AK-47 The Empress (Minimal Wear)', 'AK-47 The Empress MW', '56.77', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20816824720D7802526918315796823', 'Minimal Wear', '0.0998903', 'https://s.swap.gg/ay4_XdW5J.jpg', 1, '0000-00-00 00:00:00'),
('20858229894', 'Five-SeveN | Case Hardened (Minimal Wear)', 'Five-SeveN Case Hardened (Minimal Wear)', 'Five-SeveN Case Hardened MW', '6.74', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20858229894D587159149303972893', 'Minimal Wear', '0.1130244', 'https://s.swap.gg/Dw2rAlFbm.jpg', 0, '2021-03-02 08:00:00');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `items_with_stickers`
--

CREATE TABLE `items_with_stickers` (
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
-- Zrzut danych tabeli `items_with_stickers`
--

INSERT INTO `items_with_stickers` (`item_id`, `market_hash_name`, `market_hash_name_short`, `market_hash_name_shorter`, `price`, `inspect_link`, `has_expensive_stickers`, `exterior`, `item_float`, `screenshot`, `tradeable`, `tradeable_date`) VALUES
('20672834034', 'StatTrak™ PP-Bizon | Water Sigil (Minimal Wear)', 'StatTrak™ PP-Bizon Water Sigil (Minimal Wear)', 'ST PP-Bizon Water Sigil MW', '2.72', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20672834034D16187698617051477084', 1, 'Minimal Wear', '0.1438741', 'https://s.swap.gg/B3Iopj5Et.jpg', 1, '0000-00-00 00:00:00'),
('20783984557', 'StatTrak™ AK-47 | Redline (Field-Tested)', 'StatTrak™ AK-47 Redline (Field-Tested)', 'ST AK-47 Redline FT', '46.36', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20783984557D7108064413455918065', 1, 'Field-Tested', '0.2514981', 'https://s.swap.gg/-oCe58hZf.jpg', 1, '0000-00-00 00:00:00'),
('20792176167', 'AWP | Worm God (Minimal Wear)', 'AWP Worm God (Minimal Wear)', 'AWP Worm God MW', '1.64', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20792176167D1019654555271330313', 1, 'Minimal Wear', '0.0846460', 'https://s.swap.gg/8Jw2CRKg1.jpg', 1, '0000-00-00 00:00:00'),
('20802715827', 'M4A4 | Evil Daimyo (Minimal Wear)', 'M4A4 Evil Daimyo (Minimal Wear)', 'M4A4 Evil Daimyo MW', '5.30', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20802715827D11972512170319275010', 1, 'Minimal Wear', '0.1170929', 'https://s.swap.gg/FjvdGiMlS.jpg', 1, '0000-00-00 00:00:00'),
('20815120980', 'M4A4 | Desert-Strike (Field-Tested)', 'M4A4 Desert-Strike (Field-Tested)', 'M4A4 Desert-Strike FT', '7.27', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20815120980D2469742809530846346', 1, 'Field-Tested', '0.3365946', 'https://s.swap.gg/ip8QfDJcQ.jpg', 1, '0000-00-00 00:00:00'),
('20815123426', 'Glock-18 | Royal Legion (Battle-Scarred)', 'Glock-18 Royal Legion (Battle-Scarred)', 'Glock-18 Royal Legion BS', '1.10', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20815123426D16313172868091375554', 0, 'Battle-Scarred', '0.8695453', 'https://s.swap.gg/uxIFFr9yd.jpg', 1, '0000-00-00 00:00:00'),
('20850621579', 'AWP | Worm God (Minimal Wear)', 'AWP Worm God (Minimal Wear)', 'AWP Worm God MW', '1.64', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20850621579D17161123097547026533', 1, 'Minimal Wear', '0.1117436', 'https://s.swap.gg/vVqc27fhH.jpg', 0, '2021-03-01 08:00:00'),
('20943840002', 'Glock-18 | Candy Apple (Field-Tested)', 'Glock-18 Candy Apple (Field-Tested)', 'Glock-18 Candy Apple FT', '0.68', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20943840002D2621354943254906176', 0, 'Field-Tested', '0.1530000', 'https://s.swap.gg/Qg2x5kV0V.jpg', 1, '0000-00-00 00:00:00');

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
('Cloud9 (Holo) | Cologne 2014'),
('Cloud9 (Holo) | DreamHack 2014'),
('Cloud9 G2A (Holo) | Katowice 2015'),
('compLexity Gaming (Holo) | Katowice 2014'),
('compLexity Gaming | Katowice 2014'),
('Copenhagen Wolves (Holo) | Cologne 2014'),
('Counter Logic Gaming (Holo) | Katowice 2'),
('Crown (Foil)'),
('dAT team (Holo) | Cologne 2014'),
('device (Gold) | Boston 2018'),
('Epsilon eSports (Holo) | Cologne 2014'),
('ESL One Cologne 2014 (Red)'),
('ESL Skull (Foil) | Katowice 2014'),
('ESL Wolf (Foil) | Katowice 2014'),
('fer (Gold) | Boston 2018'),
('Flammable (Foil)'),
('Flipsid3 Tactics (Holo) | Katowice 2015'),
('Fnatic (Holo) | Cologne 2014'),
('Fnatic (Holo) | Katowice 2014'),
('Fnatic (Holo) | Katowice 2015'),
('Fnatic | Katowice 2014'),
('FURIA (Holo) | Katowice 2019'),
('Harp of War (Holo)'),
('Headhunter (Foil)'),
('HellRaisers (Holo) | Cologne 2014'),
('HellRaisers (Holo) | Katowice 2014'),
('HellRaisers (Holo) | Katowice 2015'),
('HellRaisers | Katowice 2014'),
('Howling Dawn'),
('iBUYPOWER (Holo) | Cologne 2014'),
('iBUYPOWER (Holo) | Katowice 2014'),
('iBUYPOWER | Cologne 2014'),
('iBUYPOWER | DreamHack 2014'),
('iBUYPOWER | Katowice 2014'),
('kennyS (Gold) | Krakow 2017'),
('Keyd Stars (Holo) | Katowice 2015'),
('LGB eSports (Holo) | Katowice 2014'),
('LGB eSports | Katowice 2014'),
('London Conspiracy (Holo) | Cologne 2014'),
('mousesports (Holo) | Katowice 2014'),
('mousesports | Katowice 2014'),
('MTS GameGod Wolf (Holo) | Cologne 2014'),
('NAF (Gold) | Boston 2018'),
('Natus Vincere (Foil) | Katowice 2015'),
('Natus Vincere (Holo) | Cologne 2014'),
('Natus Vincere (Holo) | Katowice 2014'),
('Natus Vincere (Holo) | Katowice 2015'),
('Natus Vincere | Katowice 2014'),
('NiKo (Gold) | Katowice 2019'),
('Ninjas in Pyjamas (Holo) | Cologne 2014'),
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
('Sticker | Team Dignitas (Holo) | Cologne'),
('Swag (Foil)'),
('Team Dignitas (Holo) | Cologne 2014'),
('Team Dignitas (Holo) | Katowice 2014'),
('Team Dignitas | Katowice 2014'),
('Team LDLC.com (Holo) | Cologne 2014'),
('Team LDLC.com (Holo) | Katowice 2014'),
('Team LDLC.com | Katowice 2014'),
('Titan (Foil) | Cologne 2015'),
('Titan (Holo) | Cologne 2014'),
('Titan (Holo) | Katowice 2014'),
('Titan (Holo) | Katowice 2015'),
('Titan | Cologne 2014'),
('Titan | Katowice 2014'),
('Tyloo (Foil) | Boston 2018'),
('Virtus.Pro (Holo) | Cologne 2014'),
('Virtus.Pro (Holo) | Katowice 2014'),
('Virtus.pro (Holo) | Katowice 2015'),
('Virtus.Pro | Katowice 2014'),
('Vox Eminor (Holo) | Cologne 2014'),
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
('20672834034', '3DMAX | Katowice 2014', '', '', '', ''),
('20783984557', 'fox (Foil) | Cologne 2016', 'FaZe Clan (Holo) | Boston 2018', 'The Guru', '3DMAX (Holo) | Katowice 2014', ''),
('20792176167', 'Natus Vincere (Holo) | Cologne 2014', '', '', '', ''),
('20802715827', 'shox | Boston 2018', 'suNny (Foil) | Boston 2018', 'dAT team (Holo) | Cologne 2014', 'shox | Boston 2018', ''),
('20815120980', 'Copenhagen Wolves (Holo) | Cologne 2014', 'Ninjas in Pyjamas (Holo) | Cologne 2014', '', '', ''),
('20815123426', 'OpTic Gaming (Holo) | Atlanta 2017', '', '', '', ''),
('20850621579', 'Copenhagen Wolves (Holo) | Cologne 2014', '', '', '', ''),
('20943840002', 'peet (Foil) | Cologne 2015', '', '', '', '');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`item_id`);

--
-- Indeksy dla tabeli `items_with_stickers`
--
ALTER TABLE `items_with_stickers`
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

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `stickers_applied`
--
ALTER TABLE `stickers_applied`
  ADD CONSTRAINT `aaa` FOREIGN KEY (`item_id`) REFERENCES `items_with_stickers` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
