-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 01 Kwi 2021, 23:30
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
('10101010', ' AWP | Medusa', ' AWP | Medusa', ' AWP | Medusa', '10003211.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M3448040456155372049A21047251618D7550476093732434659', 'Field-Tested', '0.2514981', 'ddd', 1, '0000-00-00 00:00:00'),
('1111111111111111', 'StatTrak™ Butterfly Knife | Marble Fade', 'StatTrak™ Butterfly Knife | Marble Fade', 'StatTrak™ Butterfly Knife | Marble Fade', '200.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M3449167159007296729A21079393255D11836766248529061435', 'Field-Tested', '0.2514981', 'asd', 1, '0000-00-00 00:00:00'),
('111211111', 'Sport Gloves | Vice', 'Sport Gloves | Vice', 'Sport Gloves | Vice', '1000111.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M4325117224759660444A21078724339D10117880646094170516', 'Field-Tested', '0.2514981', 'ass', 1, '0000-00-00 00:00:00'),
('12121212', 'Skeleton Knife | Crimson Web', 'Skeleton Knife | Crimson Web', 'Skeleton Knife | Crimson Web', '309.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M4166365337046871341A20842997707D642431949340548043', 'Field-Tested', '0.2514981', 'aaa', 1, '0000-00-00 00:00:00'),
('1231231415', 'Glock-18 | Fade', 'Glock-18 | Fade', 'Glock-18 | Fade', '312.00', 'd', 'Field-Tested', '0.2514981', 'd', 1, '0000-00-00 00:00:00'),
('131313131', 'AK-47 | Fire Serpent', 'AK-47 | Fire Serpent', 'AK-47 | Fire Serpent', '1000177.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M3458173555314430278A21041179124D12405416025525881749', 'Field-Tested', '0.2514981', 'ggg', 1, '0000-00-00 00:00:00'),
('14141414', 'AWP | Fade', 'AWP | Fade', 'AWP | Fade', '307.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M3449167159008142849A21088617412D12414218967949400653', 'Field-Tested', '0.2514981', 'asddsa', 1, '0000-00-00 00:00:00'),
('15151515', 'Butterfly Knife | Marble Fade', 'Butterfly Knife | Marble Fade', 'Butterfly Knife | Marble Fade', '10100001.00', 'asd', 'Field-Tested', '0.2514981', 'dsaasd', 1, '0000-00-00 00:00:00'),
('16161616', 'Driver Gloves | Overtake', 'Driver Gloves | Overtake', 'Driver Gloves | Overtake', '300.00', 'dfgdfgdg', 'Field-Tested', '0.2514981', 'dfgdfgdfgdg', 1, '0000-00-00 00:00:00'),
('1616167', 'Moto Gloves | Finish Line', 'Moto Gloves | Finish Line', 'Moto Gloves | Finish Line', '311.00', 'qwe', 'Field-Tested', '0.2514981', 'ewq', 1, '0000-00-00 00:00:00'),
('16616116', 'StatTrak™ Bayonet | Autotronic', 'StatTrak™ Bayonet | Autotronic', 'StatTrak™ Bayonet | Autotronic', '305.00', 'qweewq', 'Field-Tested', '0.2514981', 'ewqqwe', 1, '0000-00-00 00:00:00'),
('20783999999999', 'StatTrak™ Karambit | Fade', 'StatTrak™ Karambit | Fade', 'StatTrak™ Karambit | Fade', '100.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M3450292891583342510A21007189200D5233436124203954751', 'Field-Tested', '0.2514981', 'dsa', 1, '0000-00-00 00:00:00'),
('20816824720', 'AK-47 | The Empress (Minimal Wear)', 'AK-47 The Empress (Minimal Wear)', 'AK-47 The Empress MW', '59.14', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20816824720D480417040651003699', 'Minimal Wear', '0.0998903', 'https://s.swap.gg/1nzGi-DI2.jpg', 1, '0000-00-00 00:00:00'),
('22222222222222', 'Bowie Knife | Forest DDPAT', 'Bowie Knife | Forest DDPAT', 'Bowie Knife | Forest DDPAT', '313.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M3458172285067067674A20632431383D5111214013107463792', 'Field-Tested', '0.2514981', 'asd', 1, '0000-00-00 00:00:00'),
('3123', 'StatTrak™ Classic Knife | Fade', 'StatTrak™ Classic Knife | Fade', 'StatTrak™ Classic Knife | Fade', '1000231.00', 'ffff', 'Field-Tested', '0.2514981', 'ffff', 1, '0000-00-00 00:00:00'),
('33333333333333333', 'Souvenir AUG | Contractor', 'Souvenir AUG | Contractor', 'Souvenir AUG | Contractor', '302.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M2071031521346877951A17911021090D344666154765549068', 'Field-Tested', '0.2514981', 'asd', 1, '0000-00-00 00:00:00'),
('44444444444', 'AWP | The Prince', 'AWP | The Prince', 'AWP | The Prince', '304.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M3452542153386830769A19235613337D902453041419557607', 'Field-Tested', '0.2514981', 'dsa', 1, '0000-00-00 00:00:00'),
('473547346', 'Moto Gloves | Spearmint', 'Moto Gloves | Spearmint', 'Moto Gloves | Spearmint', '10004124.00', 'a', 'Field-Tested', '0.2514981', 'a', 1, '0000-00-00 00:00:00'),
('512123484557131231', 'Stiletto Knife | Crimson Web', 'Stiletto Knife | Crimson Web', 'Stiletto Knife | Crimson Web', '1000000000.00', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M3451417522108945069A20901493587D14000016344578456222', 'Field-Tested', '0.2514981', 'dfgsdh', 1, '0000-00-00 00:00:00'),
('51326723', 'Sport Gloves | Big Game', 'Sport Gloves | Big Game', 'Sport Gloves | Big Game', '10004124.00', 'a', 'Field-Tested', '0.2514981', 'a', 1, '0000-00-00 00:00:00'),
('55555555555', 'Specialist Gloves | Crimson Kimono', 'Specialist Gloves | Crimson Kimono', 'Specialist Gloves | Crimson Kimono', '301.00', 'ewqweasd', 'Field-Tested', '0.2514981', 'zdvzdb', 1, '0000-00-00 00:00:00'),
('65547', 'Driver Gloves | Snow Leopard', 'Driver Gloves | Snow Leopard', 'Driver Gloves | Snow Leopard', '1000238.00', 'q', 'Field-Tested', '0.2514981', 'q', 1, '0000-00-00 00:00:00'),
('666666666666', 'Specialist Gloves | Field Agent', 'Specialist Gloves | Field Agent', 'Specialist Gloves | Field Agent', '20031231.00', 'qwe', 'Field-Tested', '0.2514981', 'qwe', 1, '0000-00-00 00:00:00'),
('7457234', 'Driver Gloves | Convoy', 'Driver Gloves | Convoy', 'Driver Gloves | Convoy', '303.00', '41245125', 'Field-Tested', '0.2514981', 'f', 1, '0000-00-00 00:00:00'),
('777457', 'M4A1-S | Knight', 'M4A1-S | Knight', 'M4A1-S | Knight', '306.00', 'asd', 'Field-Tested', '0.2514981', 'asd', 1, '0000-00-00 00:00:00'),
('888888888', 'StatTrak™ Butterfly Knife | Fade', 'StatTrak™ Butterfly Knife | Fade', 'StatTrak™ Butterfly Knife | Fade', '1000686.00', 'qweqwe', 'Field-Tested', '0.2514981', 'qwe', 1, '0000-00-00 00:00:00'),
('938237', 'Negev | Mjölnir', 'Negev | Mjölnir', 'Negev | Mjölnir', '308.00', 'a', 'Field-Tested', '0.2514981', 'a', 1, '0000-00-00 00:00:00'),
('95756278', 'Hydra Gloves | Case Hardened', 'Hydra Gloves | Case Hardened', 'Hydra Gloves | Case Hardened', '10001525.00', 'a', 'Field-Tested', '0.2514981', 'a', 1, '0000-00-00 00:00:00'),
('999999999', 'StatTrak™ Flip Knife | Bright Water', 'StatTrak™ Flip Knife | Bright Water', 'StatTrak™ Flip Knife | Bright Water', '310.00', 'ad', 'Field-Tested', '0.2514981', 'asd', 1, '0000-00-00 00:00:00');

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
  `has_expensive_stickers` int(1) NOT NULL,
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
('20783984557', 'StatTrak™ AK-47 | Redline (Field-Tested)', 'StatTrak™ AK-47 Redline (Field-Tested)', 'ST AK-47 Redline FT', '49.31', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20783984557D7108064413455918065', 1, 'Field-Tested', '0.2514981', 'https://s.swap.gg/-oCe58hZf.jpg', 1, '0000-00-00 00:00:00'),
('20792176167', 'AWP | Worm God (Minimal Wear)', 'AWP Worm God (Minimal Wear)', 'AWP Worm God MW', '1.70', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20792176167D1019654555271330313', 1, 'Minimal Wear', '0.0846460', 'https://s.swap.gg/8Jw2CRKg1.jpg', 1, '0000-00-00 00:00:00'),
('20815120980', 'M4A4 | Desert-Strike (Field-Tested)', 'M4A4 Desert-Strike (Field-Tested)', 'M4A4 Desert-Strike FT', '7.55', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20815120980D2469742809530846346', 1, 'Field-Tested', '0.3365946', 'https://s.swap.gg/ip8QfDJcQ.jpg', 1, '0000-00-00 00:00:00'),
('20815123426', 'Glock-18 | Royal Legion (Battle-Scarred)', 'Glock-18 Royal Legion (Battle-Scarred)', 'Glock-18 Royal Legion BS', '0.92', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20815123426D16313172868091375554', 0, 'Battle-Scarred', '0.8695453', 'https://s.swap.gg/uxIFFr9yd.jpg', 1, '0000-00-00 00:00:00'),
('20850621579', 'AWP | Worm God (Minimal Wear)', 'AWP Worm God (Minimal Wear)', 'AWP Worm God MW', '1.69', 'steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198231636540A20850621579D11549130233962058831', 1, 'Minimal Wear', '0.1117436', 'https://s.swap.gg/JdL-KzVGp.jpg', 1, '0000-00-00 00:00:00');

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
('20783984557', 'fox (Foil) | Cologne 2016', 'FaZe Clan (Holo) | Boston 2018', 'The Guru', '3DMAX (Holo) | Katowice 2014', ''),
('20792176167', 'Natus Vincere (Holo) | Cologne 2014', '', '', '', ''),
('20815120980', 'Copenhagen Wolves (Holo) | Cologne 2014', 'Ninjas in Pyjamas (Holo) | Cologne 2014', '', '', ''),
('20815123426', 'OpTic Gaming (Holo) | Atlanta 2017', '', '', '', ''),
('20850621579', 'Copenhagen Wolves (Holo) | Cologne 2014', '', '', '', '');

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
  ADD CONSTRAINT `aaa` FOREIGN KEY (`item_id`) REFERENCES `items_with_stickers` (`item_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
