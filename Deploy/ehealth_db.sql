-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 21, 2023 at 07:57 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ehealth_db`
--

--
-- Dumping data for table `ehealth_record_ailment`
--

INSERT INTO `ehealth_record_ailment` (`id`, `name`, `description`) VALUES
(1, 'Malaria Fever', 'A common tropical ailment that disturbs black-skinned humans.'),
(2, 'Ebola', 'Ebola is a bad disease'),
(3, 'Lassa Fever', 'Lassa Fever originates from Lassa village in Nigeria.');
(4, 'Dengue Fever', 'A tropical ailment.');
(5, 'Rheumatism', '');
(6, 'Higb BP', '');

--
-- Dumping data for table `ehealth_record_state`
--

INSERT INTO `ehealth_record_state` (`id`, `name`, `description`) VALUES
(1, 'Abia', ''),
(2, 'Adamawa', '');
(3, 'Akwa Ibom', '');
(4, 'Anambra', '');
(5, 'Bauchi', '');
(6, 'Bayelsa', '');
(7, 'Benue', '');
(8, 'Borno', '');
(9, 'Cross River', '');
(10, 'Delta', '');
(11, 'Ebonyi', '');
(12, 'Edo', '');
(13, 'Ekiti', '');
(14, 'Enugu', '');
(15, 'FCT, Abuja', '');
(16, 'Gombe', '');
(17, 'imo', '');
(18, 'Jigawa', '');
(19, 'Kaduna', '');
(20, 'Kano', '');
(21, 'Katsina', '');
(22, 'Kebbi', '');
(23, 'Kogi', '');
(24, 'Kwara', '');
(25, 'Lagos', '');
(26, 'Nasarawa', '');
(27, 'Niger', '');
(28, 'Ogun', '');
(29, 'Ondo', '');
(30, 'Osun', '');
(31, 'Oyo', '');
(32, 'Plateau', '');
(33, 'Rivers', '');
(34, 'Sokoto', '');
(35, 'Taraba', '');
(36, 'Yobe', '');
(37, 'Zamfara', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
