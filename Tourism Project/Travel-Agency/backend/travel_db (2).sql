-- phpMyAdmin SQL Dump
-- version 4.1.6
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 21, 2026 at 08:59 AM
-- Server version: 5.6.16
-- PHP Version: 5.5.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `travel_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=73 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add package', 7, 'add_package'),
(26, 'Can change package', 7, 'change_package'),
(27, 'Can delete package', 7, 'delete_package'),
(28, 'Can view package', 7, 'view_package'),
(29, 'Can add credit card payment', 8, 'add_creditcardpayment'),
(30, 'Can change credit card payment', 8, 'change_creditcardpayment'),
(31, 'Can delete credit card payment', 8, 'delete_creditcardpayment'),
(32, 'Can view credit card payment', 8, 'view_creditcardpayment'),
(33, 'Can add bookings', 9, 'add_bookings'),
(34, 'Can change bookings', 9, 'change_bookings'),
(35, 'Can delete bookings', 9, 'delete_bookings'),
(36, 'Can view bookings', 9, 'view_bookings'),
(37, 'Can add chat message', 10, 'add_chatmessage'),
(38, 'Can change chat message', 10, 'change_chatmessage'),
(39, 'Can delete chat message', 10, 'delete_chatmessage'),
(40, 'Can view chat message', 10, 'view_chatmessage'),
(41, 'Can add feedback', 11, 'add_feedback'),
(42, 'Can change feedback', 11, 'change_feedback'),
(43, 'Can delete feedback', 11, 'delete_feedback'),
(44, 'Can view feedback', 11, 'view_feedback'),
(45, 'Can add chatbot qa', 12, 'add_chatbotqa'),
(46, 'Can change chatbot qa', 12, 'change_chatbotqa'),
(47, 'Can delete chatbot qa', 12, 'delete_chatbotqa'),
(48, 'Can view chatbot qa', 12, 'view_chatbotqa'),
(49, 'Can add search history', 13, 'add_searchhistory'),
(50, 'Can change search history', 13, 'change_searchhistory'),
(51, 'Can delete search history', 13, 'delete_searchhistory'),
(52, 'Can view search history', 13, 'view_searchhistory'),
(53, 'Can add accommodation', 14, 'add_accommodation'),
(54, 'Can change accommodation', 14, 'change_accommodation'),
(55, 'Can delete accommodation', 14, 'delete_accommodation'),
(56, 'Can view accommodation', 14, 'view_accommodation'),
(57, 'Can add hotel booking', 15, 'add_hotelbooking'),
(58, 'Can change hotel booking', 15, 'change_hotelbooking'),
(59, 'Can delete hotel booking', 15, 'delete_hotelbooking'),
(60, 'Can view hotel booking', 15, 'view_hotelbooking'),
(61, 'Can add hotel review', 16, 'add_hotelreview'),
(62, 'Can change hotel review', 16, 'change_hotelreview'),
(63, 'Can delete hotel review', 16, 'delete_hotelreview'),
(64, 'Can view hotel review', 16, 'view_hotelreview'),
(65, 'Can add hotel complaint', 17, 'add_hotelcomplaint'),
(66, 'Can change hotel complaint', 17, 'change_hotelcomplaint'),
(67, 'Can delete hotel complaint', 17, 'delete_hotelcomplaint'),
(68, 'Can view hotel complaint', 17, 'view_hotelcomplaint'),
(69, 'Can add destination', 18, 'add_destination'),
(70, 'Can change destination', 18, 'change_destination'),
(71, 'Can delete destination', 18, 'delete_destination'),
(72, 'Can view destination', 18, 'view_destination');

-- --------------------------------------------------------

--
-- Table structure for table `chat_message`
--

CREATE TABLE IF NOT EXISTS `chat_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `receiver_id` bigint(20) NOT NULL,
  `sender_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chat_message_receiver_id_0eceddde_fk_user_id` (`receiver_id`),
  KEY `chat_message_sender_id_991c686c_fk_user_id` (`sender_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `chat_message`
--

INSERT INTO `chat_message` (`id`, `message`, `timestamp`, `receiver_id`, `sender_id`) VALUES
(7, 'hi riya', '2026-02-17 08:10:30.926587', 8, 9),
(8, 'hi\r\n', '2026-02-18 04:13:52.801269', 8, 9),
(9, 'spots', '2026-02-18 06:00:21.375548', 9, 8),
(10, 'favourite spots', '2026-02-18 06:00:34.911388', 9, 8),
(11, 'thailad', '2026-02-18 06:08:38.910186', 8, 9),
(12, 'yo\r\n', '2026-03-12 06:32:23.428348', 14, 15);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(14, 'login', 'accommodation'),
(9, 'login', 'bookings'),
(12, 'login', 'chatbotqa'),
(10, 'login', 'chatmessage'),
(8, 'login', 'creditcardpayment'),
(18, 'login', 'destination'),
(11, 'login', 'feedback'),
(15, 'login', 'hotelbooking'),
(17, 'login', 'hotelcomplaint'),
(16, 'login', 'hotelreview'),
(7, 'login', 'package'),
(13, 'login', 'searchhistory'),
(6, 'login', 'user'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=44 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-02-07 06:31:40.260994'),
(2, 'contenttypes', '0002_remove_content_type_name', '2026-02-07 06:31:40.531787'),
(3, 'auth', '0001_initial', '2026-02-07 06:31:41.459681'),
(4, 'auth', '0002_alter_permission_name_max_length', '2026-02-07 06:31:41.595449'),
(5, 'auth', '0003_alter_user_email_max_length', '2026-02-07 06:31:41.612771'),
(6, 'auth', '0004_alter_user_username_opts', '2026-02-07 06:31:41.629622'),
(7, 'auth', '0005_alter_user_last_login_null', '2026-02-07 06:31:41.646048'),
(8, 'auth', '0006_require_contenttypes_0002', '2026-02-07 06:31:41.654291'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2026-02-07 06:31:41.664847'),
(10, 'auth', '0008_alter_user_username_max_length', '2026-02-07 06:31:41.676797'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2026-02-07 06:31:41.690623'),
(12, 'auth', '0010_alter_group_name_max_length', '2026-02-07 06:31:41.809726'),
(13, 'auth', '0011_update_proxy_permissions', '2026-02-07 06:31:41.829414'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2026-02-07 06:31:41.846510'),
(15, 'login', '0001_initial', '2026-02-07 06:31:43.413980'),
(16, 'admin', '0001_initial', '2026-02-07 06:31:43.967114'),
(17, 'admin', '0002_logentry_remove_auto_add', '2026-02-07 06:31:43.985000'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2026-02-07 06:31:44.005366'),
(19, 'login', '0002_package_packageimage', '2026-02-07 06:31:44.725407'),
(20, 'login', '0003_auto_20250301_0951', '2026-02-07 06:31:44.933489'),
(21, 'login', '0004_auto_20250301_1130', '2026-02-07 06:31:45.146517'),
(22, 'login', '0005_creditcardpayment', '2026-02-07 06:31:45.453428'),
(23, 'login', '0006_bookings', '2026-02-07 06:31:45.921192'),
(24, 'login', '0007_bookings_payment', '2026-02-07 06:31:46.130493'),
(25, 'login', '0008_auto_20250305_1003', '2026-02-07 06:31:46.508918'),
(26, 'login', '0009_chatmessage', '2026-02-07 06:31:46.957622'),
(27, 'login', '0010_feedback', '2026-02-07 06:31:47.213623'),
(28, 'login', '0011_user_status', '2026-02-07 06:31:47.353538'),
(29, 'sessions', '0001_initial', '2026-02-07 06:31:47.560030'),
(30, 'login', '0012_chatbotqa_searchhistory', '2026-02-17 04:38:24.240342'),
(31, 'login', '0012_bookings_num_persons', '2026-02-18 04:24:47.967206'),
(32, 'login', '0013_bookings_num_persons', '2026-03-12 06:55:23.954962'),
(33, 'login', '0014_accommodation', '2026-03-20 14:02:55.050867'),
(34, 'login', '0015_auto_20260320_1942', '2026-03-20 14:12:09.262108'),
(35, 'login', '0016_auto_20260320_1959', '2026-03-20 14:29:04.791276'),
(36, 'login', '0017_accommodation_room_type', '2026-03-20 14:48:58.043844'),
(37, 'login', '0018_hotelreview', '2026-03-20 14:53:48.491461'),
(38, 'login', '0019_hotelcomplaint', '2026-03-20 14:58:13.820447'),
(39, 'login', '0020_destination', '2026-03-20 15:09:59.948955'),
(40, 'login', '0021_auto_20260320_2052', '2026-03-20 15:22:27.823179'),
(41, 'login', '0022_auto_20260320_2103', '2026-03-20 15:33:44.441581'),
(42, 'login', '0023_accommodation_password', '2026-03-20 15:41:05.168254'),
(43, 'login', '0024_auto_20260320_2206', '2026-03-20 16:36:31.307940');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('l1ogobpegxldugapao6ivvlezmf8xe81', '.eJxVjMsOwiAQRf-FtSEgz3Hpvt9AgGGkaiAp7cr479qkC93ec859sRC3tYZtlCXMyC7Ms9PvlmJ-lLYDvMd26zz3ti5z4rvCDzr41LE8r4f7d1DjqN_aoidlNEkFlJwXWQutgcDITAqzROMEgiKSMamE3p8BIYItSVupjWPvD-MpN8Y:1vsD7J:XvQ_HzfjFXMG00jnQedLOCvLsmm4AwtWWK8oL0hnEDY', '2026-03-03 04:55:21.261158'),
('nlk057ixrjprtfce64p9a6qjr9s1jp5c', '.eJxVjMsOwiAQRf-FtSEgz3Hpvt9AgGGkaiAp7cr479qkC93ec859sRC3tYZtlCXMyC7Ms9PvlmJ-lLYDvMd26zz3ti5z4rvCDzr41LE8r4f7d1DjqN_aoidlNEkFlJwXWQutgcDITAqzROMEgiKSMamE3p8BIYItSVupjWPvD-MpN8Y:1vsf2D:nkzBc4c7xeZ2HkjWVK2fEg_Kb95pnU3qa2z2eykmL_o', '2026-03-04 10:43:57.600212'),
('stgdd08bp5m6lx9odf9a7u2lgkdfhxdg', '.eJxVjMsOwiAQRf-FtSEgz3Hpvt9AgGGkaiAp7cr479qkC93ec859sRC3tYZtlCXMyC7Ms9PvlmJ-lLYDvMd26zz3ti5z4rvCDzr41LE8r4f7d1DjqN_aoidlNEkFlJwXWQutgcDITAqzROMEgiKSMamE3p8BIYItSVupjWPvD-MpN8Y:1w3cmJ:SRVvpk7cp2bhyPgkefOnXi4f4Udua_64l8033RJzods', '2026-04-03 16:32:51.131083'),
('z66x1jt5mjm4nwsepv6gn50vaj0rp890', '.eJxVjMsOwiAQRf-FtSEgz3Hpvt9AgGGkaiAp7cr479qkC93ec859sRC3tYZtlCXMyC7Ms9PvlmJ-lLYDvMd26zz3ti5z4rvCDzr41LE8r4f7d1DjqN_aoidlNEkFlJwXWQutgcDITAqzROMEgiKSMamE3p8BIYItSVupjWPvD-MpN8Y:1vtJ8P:8eu1H2F_uPKbcMdv2gbXKnPmJ1iZLplOr7-yS6ppnTc', '2026-03-06 05:33:01.571129');

-- --------------------------------------------------------

--
-- Table structure for table `login_accommodation`
--

CREATE TABLE IF NOT EXISTS `login_accommodation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `type` varchar(100) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` longtext NOT NULL,
  `total_rooms` int(10) unsigned NOT NULL,
  `checkin` time(6) NOT NULL,
  `checkout` time(6) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `price_per_night` int(10) unsigned NOT NULL,
  `room_type` varchar(20) NOT NULL,
  `password` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `login_accommodation`
--

INSERT INTO `login_accommodation` (`id`, `name`, `type`, `phone_number`, `email`, `address`, `total_rooms`, `checkin`, `checkout`, `image`, `status`, `price_per_night`, `room_type`, `password`) VALUES
(1, 'hill casa', 'offers', '09446608631', 'amaswathy259@gmail.com', 'achu house', 2, '20:50:00.000000', '23:50:00.000000', 'accommodation_images/OIP_1.jpg', 'Accepted', 1000, 'Non-AC', '1234'),
(3, 'Amrutha', 'bueatyful', '9876543210', 'a@gmail.com', 'ammi house', 5, '12:30:00.000000', '13:30:00.000000', 'accommodation_images/OIP_XGnPuOA.jpg', 'Accepted', 10000, 'AC', '2468');

-- --------------------------------------------------------

--
-- Table structure for table `login_bookings`
--

CREATE TABLE IF NOT EXISTS `login_bookings` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `status` varchar(100) DEFAULT NULL,
  `package_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `payment_id` bigint(20) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `vacation_date` date DEFAULT NULL,
  `num_persons` int(10) unsigned NOT NULL,
  `guide_id` bigint(20) DEFAULT NULL,
  `hotel_id` bigint(20) DEFAULT NULL,
  `advance_paid` decimal(10,2) NOT NULL,
  `balance_amount` decimal(10,2) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `login_bookings_package_id_559278f0_fk_login_package_id` (`package_id`),
  KEY `login_bookings_user_id_2b7bf68b_fk_user_id` (`user_id`),
  KEY `login_bookings_payment_id_d30369bb_fk_login_creditcardpayment_id` (`payment_id`),
  KEY `login_bookings_guide_id_d64deff5_fk_user_id` (`guide_id`),
  KEY `login_bookings_hotel_id_07aaa80b_fk_login_accommodation_id` (`hotel_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `login_bookings`
--

INSERT INTO `login_bookings` (`id`, `status`, `package_id`, `user_id`, `payment_id`, `created_at`, `vacation_date`, `num_persons`, `guide_id`, `hotel_id`, `advance_paid`, `balance_amount`, `total_price`) VALUES
(9, 'Booked', 3, 14, NULL, '2026-03-20 16:12:59.004272', '2026-06-20', 2, 16, 1, '0.00', '0.00', '0.00'),
(10, 'Booked', 4, 5, NULL, '2026-03-20 16:12:59.016670', '2026-07-15', 3, 16, 1, '0.00', '0.00', '0.00'),
(11, 'Booked', 3, 8, 18, '2026-03-20 16:41:43.567165', '2026-03-21', 2, 16, 1, '25000.00', '0.00', '25000.00');

-- --------------------------------------------------------

--
-- Table structure for table `login_chatbotqa`
--

CREATE TABLE IF NOT EXISTS `login_chatbotqa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) NOT NULL,
  `answer` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=48 ;

--
-- Dumping data for table `login_chatbotqa`
--

INSERT INTO `login_chatbotqa` (`id`, `question`, `answer`) VALUES
(19, 'Tell me about Thailand', 'Thailand - Land of Smiles!\n\nThailand is a Southeast Asian gem famous for its ornate temples, turquoise beaches, lush jungles, and vibrant street food scene. Top attractions include:\n- Bangkok: Grand Palace, Wat Pho, floating markets\n- Chiang Mai: ancient temples, elephant sanctuaries, night bazaar\n- Phuket & Krabi: stunning beaches and island hopping\n- Pattaya: nightlife and water sports\n\nBest time to visit: November to April (cool & dry season).\nCurrency: Thai Baht (THB). Language: Thai.\nKnown for: Pad Thai, Tom Yum soup, and world-class hospitality.'),
(20, 'Thailand package', 'Our Thailand packages start from Rs. 35,000 per person and cover:\n- Hotel accommodation (3 to 7 nights)\n- Bangkok + Phuket itinerary\n- Temple tours, beach excursions & street food walks\n- Airport transfers included\n\nVisit the Packages page to see current prices and book your Thailand trip!'),
(21, 'Tell me about Maldives', 'Maldives - Paradise on Earth!\n\nThe Maldives is an Indian Ocean archipelago of 26 coral atolls known for its crystal-clear lagoons, overwater bungalows, and spectacular marine life. Highlights include:\n- Overwater villas with direct ocean access\n- Snorkelling & scuba diving with manta rays and whale sharks\n- Sandbank picnics and sunset cruises\n- Bioluminescent beach at Vaadhoo Island\n\nBest time to visit: November to April (dry season).\nCurrency: Maldivian Rufiyaa (MVR). Language: Dhivehi / English.\nPerfect for: Honeymoons, anniversaries & luxury escapes.'),
(22, 'Maldives package', 'Our Maldives packages include:\n- Overwater or beach villa stay (4 to 7 nights)\n- All-inclusive meals at the resort\n- Snorkelling, diving & water sports\n- Speedboat or seaplane transfers\n\nPrices start from Rs. 65,000 per person. Check the Packages page for details!'),
(23, 'Tell me about Paris', 'Paris - The City of Light!\n\nParis is the capital of France and one of the world''s most visited cities, celebrated for its art, fashion, gastronomy, and culture. Must-sees:\n- Eiffel Tower: iconic iron lattice tower\n- Louvre Museum: home of the Mona Lisa\n- Notre-Dame Cathedral & Sacre-Coeur\n- Champs-Elysees & Arc de Triomphe\n- Seine River cruises & Versailles day trip\n\nBest time to visit: April to June or September to November.\nCurrency: Euro (EUR). Language: French.\nFamous for: Croissants, wine, high fashion & romance.'),
(24, 'Paris package', 'Our Paris packages start from Rs. 80,000 per person and include:\n- 5 to 7 nights in a centrally located hotel\n- Eiffel Tower skip-the-line tickets\n- Louvre Museum guided tour\n- Seine River dinner cruise\n- Versailles day excursion\n\nBrowse the Packages page to find the right Paris package for you!'),
(25, 'Tell me about Bali', 'Bali - Island of the Gods!\n\nBali is an Indonesian island renowned for its forested volcanic mountains, iconic rice paddies, beaches, and coral reefs. Top spots:\n- Ubud: cultural heart, rice terraces & monkey forest\n- Seminyak & Kuta: beach clubs and nightlife\n- Tanah Lot & Uluwatu temples (stunning cliff-top views)\n- Mount Batur: sunrise trekking\n- Nusa Penida: cliffside views & manta ray diving\n\nBest time to visit: April to October (dry season).\nCurrency: Indonesian Rupiah (IDR). Language: Bahasa Indonesia / Balinese.\nFamous for: Yoga retreats, spa culture & traditional dance.'),
(26, 'Bali package', 'Our Bali packages start from Rs. 30,000 per person and cover:\n- 5 to 7 nights in a villa or resort\n- Ubud cultural tour & rice terrace visit\n- Temple visits (Tanah Lot, Uluwatu)\n- Mount Batur sunrise trek\n- Airport transfers included\n\nVisit the Packages page to see current Bali deals!'),
(27, 'Tell me about Dubai', 'Dubai - City of the Future!\n\nDubai is a glittering metropolis in the UAE famous for record-breaking architecture, luxury shopping, and desert adventures. Highlights:\n- Burj Khalifa: world''s tallest building (observation deck)\n- Dubai Mall & Dubai Fountain show\n- Palm Jumeirah & Atlantis resort\n- Desert safari with dune bashing, camel rides & BBQ dinner\n- Dubai Creek & old gold/spice souks\n- Burj Al Arab: iconic luxury hotel\n\nBest time to visit: November to March (pleasant weather).\nCurrency: UAE Dirham (AED). Language: Arabic / English.\nFamous for: Luxury, shopping, and modern marvels.'),
(28, 'Dubai package', 'Our Dubai packages start from Rs. 45,000 per person and include:\n- 4 to 6 nights in a 4/5-star hotel\n- Burj Khalifa At the Top ticket\n- Desert safari with BBQ dinner\n- Dhow cruise dinner\n- City tour & Dubai Mall visit\n\nCheck the Packages page to book your Dubai adventure!'),
(29, 'Tell me about Switzerland', 'Switzerland - Land of Alps & Chocolate!\n\nSwitzerland is a landlocked Central European country celebrated for its snow-capped mountains, pristine lakes, and precision craftsmanship. Top sights:\n- Interlaken: adventure capital (skydiving, paragliding)\n- Jungfraujoch: ''Top of Europe'' at 3,454 m altitude\n- Lucerne: Chapel Bridge & Lake Lucerne cruise\n- Zurich: vibrant city, art museums & nightlife\n- Zermatt & the Matterhorn: skiing & scenic trains\n- Montreux: Chillon Castle on Lake Geneva\n\nBest time to visit: June to September (summer) or December to February (skiing).\nCurrency: Swiss Franc (CHF). Languages: German, French, Italian.\nFamous for: Swiss chocolate, cheese, watches & Alpine beauty.'),
(30, 'Switzerland package', 'Our Switzerland packages start from Rs. 1,10,000 per person and include:\n- 6 to 8 nights in 3/4-star hotels\n- Jungfraujoch excursion (Top of Europe)\n- Swiss Travel Pass for trains & buses\n- Lucerne & Interlaken guided tours\n- Rhine Falls visit\n\nBrowse the Packages page for Switzerland itineraries!'),
(31, 'Tell me about Sydney', 'Sydney - Australia''s Harbour City!\n\nSydney is Australia''s largest city, known for its stunning harbour, golden beaches, and iconic landmarks. Must-visit spots:\n- Sydney Opera House: UNESCO World Heritage Site\n- Harbour Bridge climb & BridgeClimb experience\n- Bondi Beach: surfing & coastal walks\n- Darling Harbour: dining & entertainment\n- Taronga Zoo with harbour views\n- Blue Mountains: Three Sisters rock formation\n\nBest time to visit: September to November or March to May.\nCurrency: Australian Dollar (AUD). Language: English.\nFamous for: Surf culture, cafe scene & outdoor lifestyle.'),
(32, 'Sydney package', 'Our Sydney packages start from Rs. 95,000 per person and cover:\n- 6 to 8 nights hotel accommodation\n- Sydney Opera House & Harbour Bridge tour\n- Blue Mountains day trip\n- Bondi Beach guided walk\n- Airport transfers included\n\nVisit the Packages page to explore Sydney itineraries!'),
(33, 'Tell me about Tokyo', 'Tokyo - Where Tradition Meets Technology!\n\nTokyo, Japan''s capital, is a neon-lit metropolis blending ultramodern and traditional elements. Key highlights:\n- Shibuya Crossing: world''s busiest pedestrian scramble\n- Senso-ji Temple in Asakusa: Tokyo''s oldest temple\n- Shinjuku: skyscrapers, Kabukicho & Golden Gai\n- Akihabara: electronics & anime culture\n- teamLab Borderless: immersive digital art museum\n- Day trip to Mount Fuji & Hakone\n\nBest time to visit: March to April (cherry blossoms) or October to November (autumn).\nCurrency: Japanese Yen (JPY). Language: Japanese.\nFamous for: Sushi, ramen, anime, Bullet Train & cherry blossoms.'),
(34, 'Tokyo package', 'Our Tokyo packages start from Rs. 85,000 per person and include:\n- 6 to 8 nights in a central hotel\n- Senso-ji & Meiji Shrine guided tour\n- Shibuya, Shinjuku & Akihabara exploration\n- Mount Fuji day trip\n- JR Pass for bullet train rides\n\nCheck the Packages page for full Tokyo itineraries!'),
(35, 'Tell me about Indonesia', 'Indonesia - The Emerald of the Equator!\n\nIndonesia is the world''s largest archipelago with over 17,000 islands, featuring volcanoes, rainforests, and diverse cultures. Top destinations:\n- Bali: rice terraces, temples & beaches\n- Yogyakarta: Borobudur & Prambanan temples\n- Lombok: Rinjani volcano & pristine beaches\n- Komodo Island: Komodo dragons in the wild\n- Raja Ampat: world-class diving & marine life\n\nBest time to visit: May to September (dry season).\nCurrency: Indonesian Rupiah (IDR). Language: Bahasa Indonesia.\nFamous for: Tropical beauty, batik textiles & rich spice heritage.'),
(36, 'Indonesia package', 'Our Indonesia packages start from Rs. 28,000 per person and include:\n- 5 to 7 nights accommodation\n- Bali & Yogyakarta combined itinerary\n- Borobudur temple sunrise tour\n- Beach & diving excursions\n- Domestic flights between islands\n\nVisit the Packages page to book your Indonesian adventure!'),
(37, 'Tell me about Malaysia', 'Malaysia - Truly Asia!\n\nMalaysia is a multicultural Southeast Asian nation offering rainforests, modern cities, and pristine islands. Key highlights:\n- Kuala Lumpur: Petronas Twin Towers, Batu Caves\n- Penang: UNESCO heritage town & famous street food\n- Langkawi: duty-free island with cable cars & beaches\n- Cameron Highlands: tea plantations & cool mountain air\n- Borneo: orangutans, rainforests & diving at Sipadan\n\nBest time to visit: December to February (west coast) or May to September (east coast).\nCurrency: Malaysian Ringgit (MYR). Languages: Malay, English, Chinese, Tamil.\nFamous for: Nasi Lemak, Roti Canai & multicultural harmony.'),
(38, 'Malaysia package', 'Our Malaysia packages start from Rs. 25,000 per person and cover:\n- 5 to 7 nights in Kuala Lumpur & Langkawi\n- Petronas Twin Towers observation deck\n- Batu Caves & Penang heritage walk\n- Langkawi cable car & island hopping\n- Airport transfers included\n\nCheck the Packages page to explore Malaysia deals!'),
(39, 'How do I book a package', 'Booking a package is simple!\n\n1. Browse our Packages page and find your dream destination.\n2. Click ''View More'' to see full details.\n3. Click ''Book Now'' and fill in your travel date.\n4. Enter your payment details to confirm the booking.\n5. You will receive a booking confirmation instantly!'),
(40, 'What packages are available', 'We offer amazing travel packages to:\nThailand, Maldives, Paris, Bali, Dubai, Switzerland, Sydney, Tokyo, Indonesia, Malaysia & more!\n\nEach package includes accommodation, guided tours, and transfers.\nVisit the Packages page or ask me about any specific destination for details!'),
(41, 'Visa requirements', 'Visa requirements vary by destination and your passport:\n\n- Thailand: Visa on arrival for Indian passport holders (30 days).\n- Maldives: Visa on arrival (30 days, free).\n- Bali / Indonesia: Visa on arrival for Indians (30 days).\n- Malaysia: Visa on arrival for Indians (30 days) in most cases.\n- Dubai: Visa required; we assist with the process.\n- Paris & Switzerland: Schengen visa required for Indian citizens.\n- Sydney: Australian Tourist Visa (ETA) required.\n- Tokyo: Japanese Tourist Visa required for Indians.\n\nContact our team for visa assistance and documentation support!'),
(42, 'Best time to travel', 'Best travel seasons by destination:\n\n- Thailand: November to April\n- Maldives: November to April\n- Paris: April to June, September to November\n- Bali: April to October\n- Dubai: November to March\n- Switzerland: June to September (summer) or December to February (skiing)\n- Sydney: September to November and March to May\n- Tokyo: March to April (cherry blossoms) and October to November\n- Indonesia: May to September\n- Malaysia: December to February (west coast)\n\nAsk me about any specific spot for personalised travel advice!'),
(43, 'Cancel booking', 'Cancellation Policy:\n\n- Cancellations made 7 or more days before the travel date: Full refund.\n- Cancellations within 3 to 7 days: 50% refund.\n- Cancellations within 48 hours: No refund.\n\nTo cancel, go to My Bookings and click ''Cancel Booking'', or contact our support team at support@smarttravel.com.'),
(44, 'Payment methods', 'We accept the following payment methods:\n\n- Credit / Debit Card (Visa, MasterCard, RuPay)\n- Net Banking\n- UPI (Google Pay, PhonePe, Paytm)\n- EMI options available on select packages\n\nAll payments are secured with 256-bit SSL encryption.'),
(45, 'Contact support', 'You can reach our support team via:\n\n- Phone: 1800-123-4567 (Toll-free, Monday to Saturday, 9 AM to 6 PM)\n- Email: support@smarttravel.com\n- Live Chat: Available on this page via our Travel Assistant\n\nWe are happy to help with bookings, visa queries, itinerary planning & more!'),
(46, 'What is included in the package', 'Most of our packages include:\n\n- Hotel / resort accommodation\n- Airport transfers (pick-up & drop-off)\n- Guided sightseeing tours\n- Entrance fees to major attractions\n\nSome packages also include meals and domestic flights.\nCheck the individual package details for a full breakdown!'),
(47, 'Travel insurance', 'We strongly recommend travel insurance for all international trips.\n\nOur packages offer optional travel insurance covering:\n- Trip cancellation & interruption\n- Medical emergencies abroad\n- Lost or delayed baggage\n- Flight delays\n\nAdd travel insurance at checkout for peace of mind on your journey!');

-- --------------------------------------------------------

--
-- Table structure for table `login_creditcardpayment`
--

CREATE TABLE IF NOT EXISTS `login_creditcardpayment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `card_holder_name` varchar(255) NOT NULL,
  `card_number_last4` varchar(4) NOT NULL,
  `amount_paid` decimal(10,2) NOT NULL,
  `status` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `login_creditcardpayment_user_id_51df44e9_fk_user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=20 ;

--
-- Dumping data for table `login_creditcardpayment`
--

INSERT INTO `login_creditcardpayment` (`id`, `card_holder_name`, `card_number_last4`, `amount_paid`, `status`, `created_at`, `user_id`) VALUES
(1, 'sbi', '3456', '3456.00', 'Success', '2026-02-17 04:59:54.817644', 8),
(2, 'federal', '3456', '2500.00', 'Success', '2026-02-17 05:13:36.906481', 8),
(3, 'federal bank', '3456', '2500.00', 'Success', '2026-02-17 08:01:40.272620', 8),
(4, 'federal', '4567', '25000.00', 'Success', '2026-02-17 08:09:20.883626', 8),
(5, 'federal', '1234', '25000.00', 'Success', '2026-02-18 06:23:49.137267', 8),
(6, 'sbi', '7890', '1100.00', 'Success', '2026-03-12 06:26:48.603988', 14),
(7, 'federal', '5678', '2500.00', 'Success', '2026-03-12 06:36:13.172158', 14),
(8, 'federal', '7898', '2500.00', 'Success', '2026-03-12 06:44:31.716354', 8),
(9, 'federal', '7898', '2500.00', 'Success', '2026-03-12 06:56:01.746473', 8),
(10, 'federal', '5678', '500.00', 'Success', '2026-03-12 06:56:36.938485', 8),
(11, 'federal', '6789', '24500.00', 'Success', '2026-03-12 06:59:52.788549', 14),
(12, 'federal', '9876', '2500.00', 'Success', '2026-03-12 07:01:10.040401', 14),
(13, 'aswathy', '0000', '6000.00', 'Success', '2026-03-20 14:58:50.248634', 8),
(14, 'aswathy', '0000', '1000.00', 'Success', '2026-03-20 15:01:51.109090', 8),
(15, 'aswathy', '0000', '1000.00', 'Success', '2026-03-20 15:02:04.829304', 8),
(16, 'aswathy', '0000', '16000.00', 'Success', '2026-03-20 15:04:24.799696', 8),
(17, 'ashi', '8760', '90000.00', 'Success', '2026-03-20 16:19:11.116794', 8),
(18, 'ashi', '8760', '25000.00', 'Success', '2026-03-20 16:41:43.556734', 8),
(19, 'febin', '24e', '1220000.00', 'Success', '2026-03-21 07:13:38.193924', 8);

-- --------------------------------------------------------

--
-- Table structure for table `login_destination`
--

CREATE TABLE IF NOT EXISTS `login_destination` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `best_season` varchar(100) NOT NULL,
  `entry_fees` int(10) unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `login_destination`
--

INSERT INTO `login_destination` (`id`, `name`, `description`, `image`, `state`, `city`, `best_season`, `entry_fees`, `created_at`) VALUES
(1, 'New delhi', 'New Delhi, the capital of India, is a city that seamlessly blends ancient and modern. It is home to a plethora of attractions that cater to various interests. Here are some of the top destinations to explore in New Delhi:\r\nSwaminarayan Akshardham: A futuristic architectural wonder with impressive architecture and a mesmerizing theme show.', 'destinations/download_1.webp', 'india', 'new delhi', 'dec-jan', 500, '2026-03-20 15:18:40.625466');

-- --------------------------------------------------------

--
-- Table structure for table `login_feedback`
--

CREATE TABLE IF NOT EXISTS `login_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(150) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `login_feedback_user_id_4ed0efde_fk_user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `login_feedback`
--

INSERT INTO `login_feedback` (`id`, `feedback`, `created_at`, `user_id`) VALUES
(1, 'great', '2026-02-17 04:14:13.778395', 6),
(2, 'nice trip', '2026-02-17 07:39:01.420192', 8),
(3, 'good one', '2026-02-17 08:03:14.459994', 8),
(4, 'good', '2026-02-18 06:26:53.451354', 8);

-- --------------------------------------------------------

--
-- Table structure for table `login_hotelbooking`
--

CREATE TABLE IF NOT EXISTS `login_hotelbooking` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `check_in_date` date NOT NULL,
  `check_out_date` date NOT NULL,
  `num_rooms` int(10) unsigned NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `hotel_id` bigint(20) NOT NULL,
  `payment_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `login_hotelbooking_hotel_id_79abfd2b_fk_login_accommodation_id` (`hotel_id`),
  KEY `login_hotelbooking_payment_id_d6074ac0_fk_login_cre` (`payment_id`),
  KEY `login_hotelbooking_user_id_8e86f3c6_fk_user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `login_hotelbooking`
--

INSERT INTO `login_hotelbooking` (`id`, `check_in_date`, `check_out_date`, `num_rooms`, `total_amount`, `status`, `created_at`, `hotel_id`, `payment_id`, `user_id`) VALUES
(1, '2026-03-28', '2026-04-03', 1, '6000.00', 'Booked', '2026-03-20 14:58:50.258827', 1, 13, 8),
(2, '2026-03-20', '2026-03-21', 1, '1000.00', 'Booked', '2026-03-20 15:01:51.112353', 1, 14, 8),
(3, '2026-03-20', '2026-03-21', 1, '1000.00', 'Booked', '2026-03-20 15:02:04.832911', 1, 15, 8),
(4, '2026-03-25', '2026-04-02', 2, '16000.00', 'Booked', '2026-03-20 15:04:24.805892', 1, 16, 8),
(5, '2026-04-10', '2026-04-15', 2, '15000.00', 'Booked', '2026-03-20 16:12:58.983358', 1, NULL, 5),
(6, '2026-05-01', '2026-05-03', 1, '5000.00', 'Booked', '2026-03-20 16:12:58.989844', 1, NULL, 6),
(7, '2026-03-21', '2026-03-24', 3, '90000.00', 'Booked', '2026-03-20 16:19:11.119935', 3, 17, 8),
(8, '2026-10-11', '2026-12-11', 2, '1220000.00', 'Booked', '2026-03-21 07:13:38.212635', 3, 19, 8);

-- --------------------------------------------------------

--
-- Table structure for table `login_hotelcomplaint`
--

CREATE TABLE IF NOT EXISTS `login_hotelcomplaint` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `subject` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `hotel_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `login_hotelcomplaint_hotel_id_b090df07_fk_login_accommodation_id` (`hotel_id`),
  KEY `login_hotelcomplaint_user_id_ad21dcc5_fk_user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `login_hotelcomplaint`
--

INSERT INTO `login_hotelcomplaint` (`id`, `subject`, `description`, `status`, `created_at`, `hotel_id`, `user_id`) VALUES
(1, 'Ac not working', 'plz helping', 'Pending', '2026-03-20 15:06:29.712244', 1, 8),
(2, 'AC Leakage', 'Water is leaking from the AC in room 204. Please fix it soon.', 'Pending', '2026-03-20 16:12:59.068031', 1, 5),
(3, 'WiFi Issue', 'Internet signal is very weak in the lobby area.', 'Investigating', '2026-03-20 16:12:59.075851', 1, 6),
(4, 'water leaking', 'damage', 'Pending', '2026-03-20 16:21:01.831977', 3, 8);

-- --------------------------------------------------------

--
-- Table structure for table `login_hotelreview`
--

CREATE TABLE IF NOT EXISTS `login_hotelreview` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rating` int(10) unsigned NOT NULL,
  `comment` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `hotel_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `login_hotelreview_hotel_id_9d5abc75_fk_login_accommodation_id` (`hotel_id`),
  KEY `login_hotelreview_user_id_31cdaa7e_fk_user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `login_hotelreview`
--

INSERT INTO `login_hotelreview` (`id`, `rating`, `comment`, `created_at`, `hotel_id`, `user_id`) VALUES
(1, 4, 'nice', '2026-03-20 15:05:53.488948', 1, 8),
(2, 5, 'Wonderful stay! The hill view is breathtaking.', '2026-03-20 16:12:59.044282', 1, 6),
(3, 4, 'Great food and service. Highly recommend the AC rooms.', '2026-03-20 16:12:59.048815', 1, 14),
(4, 3, 'nice', '2026-03-20 16:19:33.930860', 3, 8);

-- --------------------------------------------------------

--
-- Table structure for table `login_package`
--

CREATE TABLE IF NOT EXISTS `login_package` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `place` varchar(100) DEFAULT NULL,
  `person` int(10) unsigned NOT NULL,
  `days` int(10) unsigned NOT NULL,
  `price` int(10) unsigned NOT NULL,
  `coordinator_id` bigint(20) NOT NULL,
  `guide_id` bigint(20) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `login_package_coordinator_id_84bdf1df_fk_user_id` (`coordinator_id`),
  KEY `login_package_guide_id_b5643894_fk_user_id` (`guide_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `login_package`
--

INSERT INTO `login_package` (`id`, `place`, `person`, `days`, `price`, `coordinator_id`, `guide_id`, `image`) VALUES
(3, 'Thailand', 1, 5, 25000, 1, 1, 'package_images/package-3.jpg'),
(4, 'Bali Beaches', 2, 7, 45000, 1, 1, 'package_images/destination-1.jpg'),
(5, 'Paris city tour', 1, 4, 85000, 1, 1, 'package_images/destination-2.jpg'),
(6, 'Sydney Opera House', 2, 6, 120000, 1, 1, 'package_images/destination-3.jpg'),
(7, 'Tokyo Adventure', 1, 8, 95000, 1, 1, 'package_images/destination-4.jpg'),
(8, 'Swiss Alps', 2, 10, 150000, 1, 1, 'package_images/bg-hero.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `login_searchhistory`
--

CREATE TABLE IF NOT EXISTS `login_searchhistory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `query` varchar(255) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `login_searchhistory_user_id_ae7c1adc_fk_user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `login_searchhistory`
--

INSERT INTO `login_searchhistory` (`id`, `query`, `timestamp`, `user_id`) VALUES
(1, 'Kochi', '2026-02-17 04:43:55.735965', 1),
(2, 'thailand', '2026-02-17 05:12:48.233427', 8);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `fullname` varchar(100) DEFAULT NULL,
  `address` longtext NOT NULL,
  `profile` varchar(100) NOT NULL,
  `role` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `languages` varchar(255) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `years_of_experience` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `password`, `last_login`, `is_superuser`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `email`, `phone`, `fullname`, `address`, `profile`, `role`, `status`, `languages`, `location`, `years_of_experience`) VALUES
(1, 'pbkdf2_sha256$260000$zfKEXAWMfCHKM8OJ2CS3tx$DCTTCT4d8iYEz3BZLQaYJny9V3dKaCXmX94dlpj4Wvk=', '2026-03-21 07:52:42.036389', 1, '', '', 1, 1, '2026-02-07 06:32:20.194738', 'admin@gmail.com', NULL, NULL, '', '', NULL, NULL, NULL, NULL, 0),
(5, 'pbkdf2_sha256$260000$1zrAymez3Jy7m3VlsVlKOk$bTLEiVI/QgtsTUYU7ulaT35S/nE7wMr9qmlEG9M9htA=', '2026-02-07 07:09:35.197455', 0, '', '', 0, 1, '2026-02-07 07:09:14.720630', 'sanjaips2004@gmail.com', '9656044967', 'sanjai ps', 'Pullampallil thadathil nellickamon p.o ranni\r\nPathanamthitta,kerala', 'profile/ER_LMS_Diagram_7WtKGiM.png', 'user', 'pending', NULL, NULL, 0),
(6, 'pbkdf2_sha256$260000$83cDfqEnOMGEFiH6WzVanN$gg0BG8QvLZ4rXx2Zk38LxYQwBzeTLdcPi+OLrlOplcg=', '2026-02-17 04:46:54.359076', 0, '', '', 0, 1, '2026-02-17 04:12:04.413422', 'diya@gmail.com', '7654321234', 'diya', 'mjkiuteis', 'profile/oto1.png', 'user', 'pending', NULL, NULL, 0),
(8, 'pbkdf2_sha256$260000$v25oISGq9Qj5l4PCZ7aIw9$Io4k6nW0uXTdU2HcBy+bO/vY+5TPHaF09h3yOM9xHv8=', '2026-03-21 07:52:01.986303', 0, '', '', 0, 1, '2026-02-17 04:49:07.831673', 'riya@gmail.com', '6543212345', 'riya', 'jmhfdg', 'profile/m1.jpg', 'user', 'pending', NULL, NULL, 0),
(9, 'pbkdf2_sha256$260000$wzSKWrGPg0X9w6kRpTG2D0$UK+fPaA9k963Eyu2a0wEktN8q0V6kUAwDvkkgfY2aC8=', '2026-03-21 07:33:43.750356', 0, '', '', 0, 1, '2026-02-17 05:01:40.065119', 'akku@gmail.com', '9213456789', 'akku', 'mjbhjkk', 'profile/Gemini_Generated_Image_u0ikmsu0ikmsu0ik.png', 'coordinator', 'accepted', NULL, NULL, 0),
(13, 'pbkdf2_sha256$260000$uX0LJZYhyxT6peZ7iFRUKa$E7tWU3Quy2FLErSc6z7FCY4Z4x8xpMhPwI5feLNrJe4=', '2026-02-18 10:42:29.969210', 0, '', '', 0, 1, '2026-02-18 10:41:32.932906', 'kevin@gmail.com', '8765432123', 'kevin', 'hkjlkjh', 'profile/133927903068310691.jpg', 'coordinator', 'accepted', NULL, NULL, 0),
(14, 'pbkdf2_sha256$260000$1XENX0oNWWxZEEfjXbBtgx$gizwq8YK/F9e7SYpPp2X6KHGSqYfR3IxOoUU7aRCeE4=', '2026-03-12 06:59:19.051774', 0, '', '', 0, 1, '2026-03-12 06:22:45.108573', 'afia@gmail.com', '0876123444', 'Afia', 'hull', 'profile/WhatsApp_Image_2026-03-08_at_10.16.39_AM.jpeg', 'user', 'pending', NULL, NULL, 0),
(15, 'pbkdf2_sha256$260000$QYHFMRYwPWl7TliljDjXeF$v1UTgFVcBIEH8ld60ACIMIxQKVWirqNKCcpj2YQs+Sw=', '2026-03-12 07:01:38.443063', 0, '', '', 0, 1, '2026-03-12 06:29:04.271376', 'gowri@gmail.com', '1234567890', 'gowri', 'fhhk', 'profile/WhatsApp_Image_2026-03-08_at_10.16.39_AM_ZfvSRN0.jpeg', 'coordinator', 'accepted', NULL, NULL, 0),
(16, 'pbkdf2_sha256$260000$1OSe6Z0gqwk6LETPlGBWlH$rONq6JlY/eOkFSgqPj5v+4cR4mqhghDn+hbXnHPed0E=', NULL, 0, '', '', 0, 1, '2026-03-20 15:37:09.122199', 'akhila@gmail.com', '09087654332', 'akhila', 'achu house', 'profile/download.webp', 'guide', 'Pending', 'english', 'Goa', 3);

-- --------------------------------------------------------

--
-- Table structure for table `user_groups`
--

CREATE TABLE IF NOT EXISTS `user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_groups_user_id_group_id_40beef00_uniq` (`user_id`,`group_id`),
  KEY `user_groups_group_id_b76f8aba_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_user_permissions_user_id_permission_id_7dc6e2e0_uniq` (`user_id`,`permission_id`),
  KEY `user_user_permission_permission_id_9deb68a3_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `chat_message`
--
ALTER TABLE `chat_message`
  ADD CONSTRAINT `chat_message_receiver_id_0eceddde_fk_user_id` FOREIGN KEY (`receiver_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `chat_message_sender_id_991c686c_fk_user_id` FOREIGN KEY (`sender_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `login_bookings`
--
ALTER TABLE `login_bookings`
  ADD CONSTRAINT `login_bookings_guide_id_d64deff5_fk_user_id` FOREIGN KEY (`guide_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `login_bookings_hotel_id_07aaa80b_fk_login_accommodation_id` FOREIGN KEY (`hotel_id`) REFERENCES `login_accommodation` (`id`),
  ADD CONSTRAINT `login_bookings_package_id_559278f0_fk_login_package_id` FOREIGN KEY (`package_id`) REFERENCES `login_package` (`id`),
  ADD CONSTRAINT `login_bookings_payment_id_d30369bb_fk_login_creditcardpayment_id` FOREIGN KEY (`payment_id`) REFERENCES `login_creditcardpayment` (`id`),
  ADD CONSTRAINT `login_bookings_user_id_2b7bf68b_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `login_creditcardpayment`
--
ALTER TABLE `login_creditcardpayment`
  ADD CONSTRAINT `login_creditcardpayment_user_id_51df44e9_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `login_feedback`
--
ALTER TABLE `login_feedback`
  ADD CONSTRAINT `login_feedback_user_id_4ed0efde_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `login_hotelbooking`
--
ALTER TABLE `login_hotelbooking`
  ADD CONSTRAINT `login_hotelbooking_hotel_id_79abfd2b_fk_login_accommodation_id` FOREIGN KEY (`hotel_id`) REFERENCES `login_accommodation` (`id`),
  ADD CONSTRAINT `login_hotelbooking_payment_id_d6074ac0_fk_login_cre` FOREIGN KEY (`payment_id`) REFERENCES `login_creditcardpayment` (`id`),
  ADD CONSTRAINT `login_hotelbooking_user_id_8e86f3c6_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `login_hotelcomplaint`
--
ALTER TABLE `login_hotelcomplaint`
  ADD CONSTRAINT `login_hotelcomplaint_hotel_id_b090df07_fk_login_accommodation_id` FOREIGN KEY (`hotel_id`) REFERENCES `login_accommodation` (`id`),
  ADD CONSTRAINT `login_hotelcomplaint_user_id_ad21dcc5_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `login_hotelreview`
--
ALTER TABLE `login_hotelreview`
  ADD CONSTRAINT `login_hotelreview_hotel_id_9d5abc75_fk_login_accommodation_id` FOREIGN KEY (`hotel_id`) REFERENCES `login_accommodation` (`id`),
  ADD CONSTRAINT `login_hotelreview_user_id_31cdaa7e_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `login_package`
--
ALTER TABLE `login_package`
  ADD CONSTRAINT `login_package_coordinator_id_84bdf1df_fk_user_id` FOREIGN KEY (`coordinator_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `login_package_guide_id_b5643894_fk_user_id` FOREIGN KEY (`guide_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `login_searchhistory`
--
ALTER TABLE `login_searchhistory`
  ADD CONSTRAINT `login_searchhistory_user_id_ae7c1adc_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `user_groups`
--
ALTER TABLE `user_groups`
  ADD CONSTRAINT `user_groups_group_id_b76f8aba_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_groups_user_id_abaea130_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `user_user_permissions`
--
ALTER TABLE `user_user_permissions`
  ADD CONSTRAINT `user_user_permissions_user_id_ed4a47ea_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `user_user_permission_permission_id_9deb68a3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
