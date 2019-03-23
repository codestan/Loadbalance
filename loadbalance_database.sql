-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 12, 2018 at 09:55 AM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 7.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `loadbalance_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `accesspoint_ip`
--

CREATE TABLE `accesspoint_ip` (
  `ap_ip` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ap_username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ap_password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ap_group` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ap_model` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ap_hostname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ap_ssid` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ap_channel` int(10) NOT NULL,
  `ap_status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ap_authen` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ap_numclient` int(99) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `accesspoint_ip`
--

INSERT INTO `accesspoint_ip` (`ap_ip`, `ap_username`, `ap_password`, `ap_group`, `ap_model`, `ap_hostname`, `ap_ssid`, `ap_channel`, `ap_status`, `ap_authen`, `ap_numclient`) VALUES
('192.168.1.23', 'root', '1234', 'group A', 'TP-Link N900', 'OpenWRT23', 'OpenWRT', 11, 'Online', 'Online', 4),
('192.168.1.24', 'root', '1234', 'group A', 'TP-Link N900', 'OpenWRT24', 'OpenWRT', 11, 'Offline', 'Offline', 5);

-- --------------------------------------------------------

--
-- Table structure for table `client_data`
--

CREATE TABLE `client_data` (
  `client_ip` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_station` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_inactivetime` int(10) NOT NULL,
  `client_rx` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_tx` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_signal` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `client_data`
--

INSERT INTO `client_data` (`client_ip`, `client_station`, `client_inactivetime`, `client_rx`, `client_tx`, `client_signal`) VALUES
('192.168.1.23', 'Online', 15000, '3000', '6000', '-40'),
('192.168.1.24', 'Offline', 15000, '3000', '6000', '-50');

-- --------------------------------------------------------

--
-- Table structure for table `group_data`
--

CREATE TABLE `group_data` (
  `group_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `group_data`
--

INSERT INTO `group_data` (`group_name`) VALUES
('group A');

-- --------------------------------------------------------

--
-- Table structure for table `login_data`
--

CREATE TABLE `login_data` (
  `login_username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `login_password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `login_data`
--

INSERT INTO `login_data` (`login_username`, `login_password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `log_data`
--

CREATE TABLE `log_data` (
  `day` int(2) NOT NULL,
  `month` int(2) NOT NULL,
  `year` int(4) NOT NULL,
  `time_h` int(2) NOT NULL,
  `time_m` int(2) NOT NULL,
  `group_n` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `inac_time` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `rx_byte` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `tx_byte` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `sig_avg` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `ip` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `mac` varchar(17) COLLATE utf8_unicode_ci NOT NULL,
  `id` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `log_data`
--

INSERT INTO `log_data` (`day`, `month`, `year`, `time_h`, `time_m`, `group_n`, `inac_time`, `rx_byte`, `tx_byte`, `sig_avg`, `ip`, `mac`, `id`) VALUES
(2, 3, 2018, 6, 5, 'group A', '730', '57119129', '1643416010', '-60', '192.168.1.22', '84:9f:b5:c1:b5:96', 703),
(2, 3, 2018, 6, 10, 'group A', '250', '57144869', '1643430476', '-61', '192.168.1.22', '84:9f:b5:c1:b5:96', 704),
(2, 3, 2018, 6, 15, 'group A', '900', '57172148', '1643483248', '-57', '192.168.1.22', '84:9f:b5:c1:b5:96', 705),
(2, 3, 2018, 6, 20, 'group A', '2610', '57203436', '1643555990', '-55', '192.168.1.22', '84:9f:b5:c1:b5:96', 706),
(2, 3, 2018, 6, 25, 'group A', '1910', '57300246', '1643629025', '-56', '192.168.1.22', '84:9f:b5:c1:b5:96', 707),
(2, 3, 2018, 6, 30, 'group A', '90', '57339778', '1643668391', '-55', '192.168.1.22', '84:9f:b5:c1:b5:96', 708),
(2, 3, 2018, 6, 35, 'group A', '20', '57412782', '1643833303', '-55', '192.168.1.22', '84:9f:b5:c1:b5:96', 709),
(2, 3, 2018, 6, 40, 'group A', '1110', '57457318', '1643974124', '-56', '192.168.1.22', '84:9f:b5:c1:b5:96', 710),
(2, 3, 2018, 6, 45, 'group A', '60', '57488812', '1644083760', '-55', '192.168.1.22', '84:9f:b5:c1:b5:96', 711),
(2, 3, 2018, 6, 50, 'group A', '20', '57565307', '1644284040', '-55', '192.168.1.22', '84:9f:b5:c1:b5:96', 712),
(2, 3, 2018, 6, 55, 'group A', '1540', '57622346', '1644570946', '-54', '192.168.1.22', '84:9f:b5:c1:b5:96', 713),
(2, 3, 2018, 7, 0, 'group A', '540', '57652842', '1644594529', '-55', '192.168.1.22', '84:9f:b5:c1:b5:96', 714),
(2, 3, 2018, 7, 5, 'group A', '100', '57729302', '1644922860', '-57', '192.168.1.22', '84:9f:b5:c1:b5:96', 715);

-- --------------------------------------------------------

--
-- Table structure for table `reserve_ip`
--

CREATE TABLE `reserve_ip` (
  `reserve_ip` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `reserve_ip`
--

INSERT INTO `reserve_ip` (`reserve_ip`) VALUES
('192.168.1.2');

-- --------------------------------------------------------

--
-- Table structure for table `server_data`
--

CREATE TABLE `server_data` (
  `server_ip` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `server_different` int(10) NOT NULL,
  `server_presetlevel` int(10) NOT NULL,
  `server_inactivetime` int(10) NOT NULL,
  `server_refreshtime` int(10) NOT NULL,
  `server_mask` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `server_gateway` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `server_dns` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `server_mac` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `server_hostname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `server_data`
--

INSERT INTO `server_data` (`server_ip`, `server_different`, `server_presetlevel`, `server_inactivetime`, `server_refreshtime`, `server_mask`, `server_gateway`, `server_dns`, `server_mac`, `server_hostname`) VALUES
('192.168.1.21', 11, 5, 99, 55, '255.255.255.0', '192.168.1.1', '8.8.8.8', 'b8:27:eb:49:d9:88', 'raspberrypi');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accesspoint_ip`
--
ALTER TABLE `accesspoint_ip`
  ADD PRIMARY KEY (`ap_ip`);

--
-- Indexes for table `client_data`
--
ALTER TABLE `client_data`
  ADD PRIMARY KEY (`client_ip`);

--
-- Indexes for table `group_data`
--
ALTER TABLE `group_data`
  ADD PRIMARY KEY (`group_name`);

--
-- Indexes for table `login_data`
--
ALTER TABLE `login_data`
  ADD PRIMARY KEY (`login_username`);

--
-- Indexes for table `log_data`
--
ALTER TABLE `log_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reserve_ip`
--
ALTER TABLE `reserve_ip`
  ADD PRIMARY KEY (`reserve_ip`);

--
-- Indexes for table `server_data`
--
ALTER TABLE `server_data`
  ADD PRIMARY KEY (`server_ip`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `log_data`
--
ALTER TABLE `log_data`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=716;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
