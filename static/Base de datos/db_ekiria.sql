-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-10-2021 a las 22:07:03
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_ekiria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas`
--

CREATE TABLE `citas` (
  `id_cita` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  `fecha_registro` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `id_compra` int(11) NOT NULL,
  `descripcion` varchar(200) COLLATE utf8_nopad_bin NOT NULL,
  `cantidad` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `proveedor_id` int(11) NOT NULL,
  `precio` double NOT NULL,
  `estado` bit(1) NOT NULL DEFAULT b'1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_nopad_bin;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `front_end`
--

CREATE TABLE `front_end` (
  `id_front_end` int(11) NOT NULL,
  `titulo` varchar(20) NOT NULL,
  `camp1` varchar(1000) NOT NULL,
  `camp2` varchar(1000) DEFAULT NULL,
  `camp3` varchar(1000) DEFAULT NULL,
  `camp4` varchar(1000) DEFAULT NULL,
  `camp5` varchar(1000) DEFAULT NULL,
  `camp6` varchar(1000) DEFAULT NULL,
  `img1` varchar(1000) DEFAULT NULL,
  `img2` varchar(1000) DEFAULT NULL,
  `color_titulo` varchar(11) DEFAULT NULL,
  `color_txt` varchar(11) DEFAULT NULL,
  `negrita_titulo` bit(1) DEFAULT NULL,
  `boton_tex_compra` varchar(11) DEFAULT NULL,
  `negrita_producto` bit(1) DEFAULT NULL,
  `tamano_texto` int(3) DEFAULT NULL,
  `tamano_titulo` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `municipios`
--

CREATE TABLE `municipios` (
  `id_municipio` int(11) UNSIGNED NOT NULL,
  `municipio` varchar(255) NOT NULL DEFAULT '',
  `estado` int(1) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `municipios`
--

INSERT INTO `municipios` (`id_municipio`, `municipio`, `estado`) VALUES
(1, 'Abriaquí', 1),
(2, 'Acacías', 1),
(3, 'Acandí', 1),
(4, 'Acevedo', 1),
(5, 'Achí', 1),
(6, 'Agrado', 1),
(7, 'Agua de Dios', 1),
(8, 'Aguachica', 1),
(9, 'Aguada', 1),
(10, 'Aguadas', 1),
(11, 'Aguazul', 1),
(12, 'Agustín Codazzi', 1),
(13, 'Aipe', 1),
(14, 'Albania', 1),
(15, 'Albania', 1),
(16, 'Albania', 1),
(17, 'Albán', 1),
(18, 'Albán (San José)', 1),
(19, 'Alcalá', 1),
(20, 'Alejandria', 1),
(21, 'Algarrobo', 1),
(22, 'Algeciras', 1),
(23, 'Almaguer', 1),
(24, 'Almeida', 1),
(25, 'Alpujarra', 1),
(26, 'Altamira', 1),
(27, 'Alto Baudó (Pie de Pato)', 1),
(28, 'Altos del Rosario', 1),
(29, 'Alvarado', 1),
(30, 'Amagá', 1),
(31, 'Amalfi', 1),
(32, 'Ambalema', 1),
(33, 'Anapoima', 1),
(34, 'Ancuya', 1),
(35, 'Andalucía', 1),
(36, 'Andes', 1),
(37, 'Angelópolis', 1),
(38, 'Angostura', 1),
(39, 'Anolaima', 1),
(40, 'Anorí', 1),
(41, 'Anserma', 1),
(42, 'Ansermanuevo', 1),
(43, 'Anzoátegui', 1),
(44, 'Anzá', 1),
(45, 'Apartadó', 1),
(46, 'Apulo', 1),
(47, 'Apía', 1),
(48, 'Aquitania', 1),
(49, 'Aracataca', 1),
(50, 'Aranzazu', 1),
(51, 'Aratoca', 1),
(52, 'Arauca', 1),
(53, 'Arauquita', 1),
(54, 'Arbeláez', 1),
(55, 'Arboleda (Berruecos)', 1),
(56, 'Arboledas', 1),
(57, 'Arboletes', 1),
(58, 'Arcabuco', 1),
(59, 'Arenal', 1),
(60, 'Argelia', 1),
(61, 'Argelia', 1),
(62, 'Argelia', 1),
(63, 'Ariguaní (El Difícil)', 1),
(64, 'Arjona', 1),
(65, 'Armenia', 1),
(66, 'Armenia', 1),
(67, 'Armero (Guayabal)', 1),
(68, 'Arroyohondo', 1),
(69, 'Astrea', 1),
(70, 'Ataco', 1),
(71, 'Atrato (Yuto)', 1),
(72, 'Ayapel', 1),
(73, 'Bagadó', 1),
(74, 'Bahía Solano (Mútis)', 1),
(75, 'Bajo Baudó (Pizarro)', 1),
(76, 'Balboa', 1),
(77, 'Balboa', 1),
(78, 'Baranoa', 1),
(79, 'Baraya', 1),
(80, 'Barbacoas', 1),
(81, 'Barbosa', 1),
(82, 'Barbosa', 1),
(83, 'Barichara', 1),
(84, 'Barranca de Upía', 1),
(85, 'Barrancabermeja', 1),
(86, 'Barrancas', 1),
(87, 'Barranco de Loba', 1),
(88, 'Barranquilla', 1),
(89, 'Becerríl', 1),
(90, 'Belalcázar', 1),
(91, 'Bello', 1),
(92, 'Belmira', 1),
(93, 'Beltrán', 1),
(94, 'Belén', 1),
(95, 'Belén', 1),
(96, 'Belén de Bajirá', 1),
(97, 'Belén de Umbría', 1),
(98, 'Belén de los Andaquíes', 1),
(99, 'Berbeo', 1),
(100, 'Betania', 1),
(101, 'Beteitiva', 1),
(102, 'Betulia', 1),
(103, 'Betulia', 1),
(104, 'Bituima', 1),
(105, 'Boavita', 1),
(106, 'Bochalema', 1),
(107, 'Bogotá D.C.', 1),
(108, 'Bojacá', 1),
(109, 'Bojayá (Bellavista)', 1),
(110, 'Bolívar', 1),
(111, 'Bolívar', 1),
(112, 'Bolívar', 1),
(113, 'Bolívar', 1),
(114, 'Bosconia', 1),
(115, 'Boyacá', 1),
(116, 'Briceño', 1),
(117, 'Briceño', 1),
(118, 'Bucaramanga', 1),
(119, 'Bucarasica', 1),
(120, 'Buenaventura', 1),
(121, 'Buenavista', 1),
(122, 'Buenavista', 1),
(123, 'Buenavista', 1),
(124, 'Buenavista', 1),
(125, 'Buenos Aires', 1),
(126, 'Buesaco', 1),
(127, 'Buga', 1),
(128, 'Bugalagrande', 1),
(129, 'Burítica', 1),
(130, 'Busbanza', 1),
(131, 'Cabrera', 1),
(132, 'Cabrera', 1),
(133, 'Cabuyaro', 1),
(134, 'Cachipay', 1),
(135, 'Caicedo', 1),
(136, 'Caicedonia', 1),
(137, 'Caimito', 1),
(138, 'Cajamarca', 1),
(139, 'Cajibío', 1),
(140, 'Cajicá', 1),
(141, 'Calamar', 1),
(142, 'Calamar', 1),
(143, 'Calarcá', 1),
(144, 'Caldas', 1),
(145, 'Caldas', 1),
(146, 'Caldono', 1),
(147, 'California', 1),
(148, 'Calima (Darién)', 1),
(149, 'Caloto', 1),
(150, 'Calí', 1),
(151, 'Campamento', 1),
(152, 'Campo de la Cruz', 1),
(153, 'Campoalegre', 1),
(154, 'Campohermoso', 1),
(155, 'Canalete', 1),
(156, 'Candelaria', 1),
(157, 'Candelaria', 1),
(158, 'Cantagallo', 1),
(159, 'Cantón de San Pablo', 1),
(160, 'Caparrapí', 1),
(161, 'Capitanejo', 1),
(162, 'Caracolí', 1),
(163, 'Caramanta', 1),
(164, 'Carcasí', 1),
(165, 'Carepa', 1),
(166, 'Carmen de Apicalá', 1),
(167, 'Carmen de Carupa', 1),
(168, 'Carmen de Viboral', 1),
(169, 'Carmen del Darién (CURBARADÓ)', 1),
(170, 'Carolina', 1),
(171, 'Cartagena', 1),
(172, 'Cartagena del Chairá', 1),
(173, 'Cartago', 1),
(174, 'Carurú', 1),
(175, 'Casabianca', 1),
(176, 'Castilla la Nueva', 1),
(177, 'Caucasia', 1),
(178, 'Cañasgordas', 1),
(179, 'Cepita', 1),
(180, 'Cereté', 1),
(181, 'Cerinza', 1),
(182, 'Cerrito', 1),
(183, 'Cerro San Antonio', 1),
(184, 'Chachaguí', 1),
(185, 'Chaguaní', 1),
(186, 'Chalán', 1),
(187, 'Chaparral', 1),
(188, 'Charalá', 1),
(189, 'Charta', 1),
(190, 'Chigorodó', 1),
(191, 'Chima', 1),
(192, 'Chimichagua', 1),
(193, 'Chimá', 1),
(194, 'Chinavita', 1),
(195, 'Chinchiná', 1),
(196, 'Chinácota', 1),
(197, 'Chinú', 1),
(198, 'Chipaque', 1),
(199, 'Chipatá', 1),
(200, 'Chiquinquirá', 1),
(201, 'Chiriguaná', 1),
(202, 'Chiscas', 1),
(203, 'Chita', 1),
(204, 'Chitagá', 1),
(205, 'Chitaraque', 1),
(206, 'Chivatá', 1),
(207, 'Chivolo', 1),
(208, 'Choachí', 1),
(209, 'Chocontá', 1),
(210, 'Chámeza', 1),
(211, 'Chía', 1),
(212, 'Chíquiza', 1),
(213, 'Chívor', 1),
(214, 'Cicuco', 1),
(215, 'Cimitarra', 1),
(216, 'Circasia', 1),
(217, 'Cisneros', 1),
(218, 'Ciénaga', 1),
(219, 'Ciénaga', 1),
(220, 'Ciénaga de Oro', 1),
(221, 'Clemencia', 1),
(222, 'Cocorná', 1),
(223, 'Coello', 1),
(224, 'Cogua', 1),
(225, 'Colombia', 1),
(226, 'Colosó (Ricaurte)', 1),
(227, 'Colón', 1),
(228, 'Colón (Génova)', 1),
(229, 'Concepción', 1),
(230, 'Concepción', 1),
(231, 'Concordia', 1),
(232, 'Concordia', 1),
(233, 'Condoto', 1),
(234, 'Confines', 1),
(235, 'Consaca', 1),
(236, 'Contadero', 1),
(237, 'Contratación', 1),
(238, 'Convención', 1),
(239, 'Copacabana', 1),
(240, 'Coper', 1),
(241, 'Cordobá', 1),
(242, 'Corinto', 1),
(243, 'Coromoro', 1),
(244, 'Corozal', 1),
(245, 'Corrales', 1),
(246, 'Cota', 1),
(247, 'Cotorra', 1),
(248, 'Covarachía', 1),
(249, 'Coveñas', 1),
(250, 'Coyaima', 1),
(251, 'Cravo Norte', 1),
(252, 'Cuaspud (Carlosama)', 1),
(253, 'Cubarral', 1),
(254, 'Cubará', 1),
(255, 'Cucaita', 1),
(256, 'Cucunubá', 1),
(257, 'Cucutilla', 1),
(258, 'Cuitiva', 1),
(259, 'Cumaral', 1),
(260, 'Cumaribo', 1),
(261, 'Cumbal', 1),
(262, 'Cumbitara', 1),
(263, 'Cunday', 1),
(264, 'Curillo', 1),
(265, 'Curití', 1),
(266, 'Curumaní', 1),
(267, 'Cáceres', 1),
(268, 'Cáchira', 1),
(269, 'Cácota', 1),
(270, 'Cáqueza', 1),
(271, 'Cértegui', 1),
(272, 'Cómbita', 1),
(273, 'Córdoba', 1),
(274, 'Córdoba', 1),
(275, 'Cúcuta', 1),
(276, 'Dabeiba', 1),
(277, 'Dagua', 1),
(278, 'Dibulla', 1),
(279, 'Distracción', 1),
(280, 'Dolores', 1),
(281, 'Don Matías', 1),
(282, 'Dos Quebradas', 1),
(283, 'Duitama', 1),
(284, 'Durania', 1),
(285, 'Ebéjico', 1),
(286, 'El Bagre', 1),
(287, 'El Banco', 1),
(288, 'El Cairo', 1),
(289, 'El Calvario', 1),
(290, 'El Carmen', 1),
(291, 'El Carmen', 1),
(292, 'El Carmen de Atrato', 1),
(293, 'El Carmen de Bolívar', 1),
(294, 'El Castillo', 1),
(295, 'El Cerrito', 1),
(296, 'El Charco', 1),
(297, 'El Cocuy', 1),
(298, 'El Colegio', 1),
(299, 'El Copey', 1),
(300, 'El Doncello', 1),
(301, 'El Dorado', 1),
(302, 'El Dovio', 1),
(303, 'El Espino', 1),
(304, 'El Guacamayo', 1),
(305, 'El Guamo', 1),
(306, 'El Molino', 1),
(307, 'El Paso', 1),
(308, 'El Paujil', 1),
(309, 'El Peñol', 1),
(310, 'El Peñon', 1),
(311, 'El Peñon', 1),
(312, 'El Peñón', 1),
(313, 'El Piñon', 1),
(314, 'El Playón', 1),
(315, 'El Retorno', 1),
(316, 'El Retén', 1),
(317, 'El Roble', 1),
(318, 'El Rosal', 1),
(319, 'El Rosario', 1),
(320, 'El Tablón de Gómez', 1),
(321, 'El Tambo', 1),
(322, 'El Tambo', 1),
(323, 'El Tarra', 1),
(324, 'El Zulia', 1),
(325, 'El Águila', 1),
(326, 'Elías', 1),
(327, 'Encino', 1),
(328, 'Enciso', 1),
(329, 'Entrerríos', 1),
(330, 'Envigado', 1),
(331, 'Espinal', 1),
(332, 'Facatativá', 1),
(333, 'Falan', 1),
(334, 'Filadelfia', 1),
(335, 'Filandia', 1),
(336, 'Firavitoba', 1),
(337, 'Flandes', 1),
(338, 'Florencia', 1),
(339, 'Florencia', 1),
(340, 'Floresta', 1),
(341, 'Florida', 1),
(342, 'Floridablanca', 1),
(343, 'Florián', 1),
(344, 'Fonseca', 1),
(345, 'Fortúl', 1),
(346, 'Fosca', 1),
(347, 'Francisco Pizarro', 1),
(348, 'Fredonia', 1),
(349, 'Fresno', 1),
(350, 'Frontino', 1),
(351, 'Fuente de Oro', 1),
(352, 'Fundación', 1),
(353, 'Funes', 1),
(354, 'Funza', 1),
(355, 'Fusagasugá', 1),
(356, 'Fómeque', 1),
(357, 'Fúquene', 1),
(358, 'Gachalá', 1),
(359, 'Gachancipá', 1),
(360, 'Gachantivá', 1),
(361, 'Gachetá', 1),
(362, 'Galapa', 1),
(363, 'Galeras (Nueva Granada)', 1),
(364, 'Galán', 1),
(365, 'Gama', 1),
(366, 'Gamarra', 1),
(367, 'Garagoa', 1),
(368, 'Garzón', 1),
(369, 'Gigante', 1),
(370, 'Ginebra', 1),
(371, 'Giraldo', 1),
(372, 'Girardot', 1),
(373, 'Girardota', 1),
(374, 'Girón', 1),
(375, 'Gonzalez', 1),
(376, 'Gramalote', 1),
(377, 'Granada', 1),
(378, 'Granada', 1),
(379, 'Granada', 1),
(380, 'Guaca', 1),
(381, 'Guacamayas', 1),
(382, 'Guacarí', 1),
(383, 'Guachavés', 1),
(384, 'Guachené', 1),
(385, 'Guachetá', 1),
(386, 'Guachucal', 1),
(387, 'Guadalupe', 1),
(388, 'Guadalupe', 1),
(389, 'Guadalupe', 1),
(390, 'Guaduas', 1),
(391, 'Guaitarilla', 1),
(392, 'Gualmatán', 1),
(393, 'Guamal', 1),
(394, 'Guamal', 1),
(395, 'Guamo', 1),
(396, 'Guapota', 1),
(397, 'Guapí', 1),
(398, 'Guaranda', 1),
(399, 'Guarne', 1),
(400, 'Guasca', 1),
(401, 'Guatapé', 1),
(402, 'Guataquí', 1),
(403, 'Guatavita', 1),
(404, 'Guateque', 1),
(405, 'Guavatá', 1),
(406, 'Guayabal de Siquima', 1),
(407, 'Guayabetal', 1),
(408, 'Guayatá', 1),
(409, 'Guepsa', 1),
(410, 'Guicán', 1),
(411, 'Gutiérrez', 1),
(412, 'Guática', 1),
(413, 'Gámbita', 1),
(414, 'Gámeza', 1),
(415, 'Génova', 1),
(416, 'Gómez Plata', 1),
(417, 'Hacarí', 1),
(418, 'Hatillo de Loba', 1),
(419, 'Hato', 1),
(420, 'Hato Corozal', 1),
(421, 'Hatonuevo', 1),
(422, 'Heliconia', 1),
(423, 'Herrán', 1),
(424, 'Herveo', 1),
(425, 'Hispania', 1),
(426, 'Hobo', 1),
(427, 'Honda', 1),
(428, 'Ibagué', 1),
(429, 'Icononzo', 1),
(430, 'Iles', 1),
(431, 'Imúes', 1),
(432, 'Inzá', 1),
(433, 'Inírida', 1),
(434, 'Ipiales', 1),
(435, 'Isnos', 1),
(436, 'Istmina', 1),
(437, 'Itagüí', 1),
(438, 'Ituango', 1),
(439, 'Izá', 1),
(440, 'Jambaló', 1),
(441, 'Jamundí', 1),
(442, 'Jardín', 1),
(443, 'Jenesano', 1),
(444, 'Jericó', 1),
(445, 'Jericó', 1),
(446, 'Jerusalén', 1),
(447, 'Jesús María', 1),
(448, 'Jordán', 1),
(449, 'Juan de Acosta', 1),
(450, 'Junín', 1),
(451, 'Juradó', 1),
(452, 'La Apartada y La Frontera', 1),
(453, 'La Argentina', 1),
(454, 'La Belleza', 1),
(455, 'La Calera', 1),
(456, 'La Capilla', 1),
(457, 'La Ceja', 1),
(458, 'La Celia', 1),
(459, 'La Cruz', 1),
(460, 'La Cumbre', 1),
(461, 'La Dorada', 1),
(462, 'La Esperanza', 1),
(463, 'La Estrella', 1),
(464, 'La Florida', 1),
(465, 'La Gloria', 1),
(466, 'La Jagua de Ibirico', 1),
(467, 'La Jagua del Pilar', 1),
(468, 'La Llanada', 1),
(469, 'La Macarena', 1),
(470, 'La Merced', 1),
(471, 'La Mesa', 1),
(472, 'La Montañita', 1),
(473, 'La Palma', 1),
(474, 'La Paz', 1),
(475, 'La Paz (Robles)', 1),
(476, 'La Peña', 1),
(477, 'La Pintada', 1),
(478, 'La Plata', 1),
(479, 'La Playa', 1),
(480, 'La Primavera', 1),
(481, 'La Salina', 1),
(482, 'La Sierra', 1),
(483, 'La Tebaida', 1),
(484, 'La Tola', 1),
(485, 'La Unión', 1),
(486, 'La Unión', 1),
(487, 'La Unión', 1),
(488, 'La Unión', 1),
(489, 'La Uvita', 1),
(490, 'La Vega', 1),
(491, 'La Vega', 1),
(492, 'La Victoria', 1),
(493, 'La Victoria', 1),
(494, 'La Victoria', 1),
(495, 'La Virginia', 1),
(496, 'Labateca', 1),
(497, 'Labranzagrande', 1),
(498, 'Landázuri', 1),
(499, 'Lebrija', 1),
(500, 'Leiva', 1),
(501, 'Lejanías', 1),
(502, 'Lenguazaque', 1),
(503, 'Leticia', 1),
(504, 'Liborina', 1),
(505, 'Linares', 1),
(506, 'Lloró', 1),
(507, 'Lorica', 1),
(508, 'Los Córdobas', 1),
(509, 'Los Palmitos', 1),
(510, 'Los Patios', 1),
(511, 'Los Santos', 1),
(512, 'Lourdes', 1),
(513, 'Luruaco', 1),
(514, 'Lérida', 1),
(515, 'Líbano', 1),
(516, 'López (Micay)', 1),
(517, 'Macanal', 1),
(518, 'Macaravita', 1),
(519, 'Maceo', 1),
(520, 'Machetá', 1),
(521, 'Madrid', 1),
(522, 'Magangué', 1),
(523, 'Magüi (Payán)', 1),
(524, 'Mahates', 1),
(525, 'Maicao', 1),
(526, 'Majagual', 1),
(527, 'Malambo', 1),
(528, 'Mallama (Piedrancha)', 1),
(529, 'Manatí', 1),
(530, 'Manaure', 1),
(531, 'Manaure Balcón del Cesar', 1),
(532, 'Manizales', 1),
(533, 'Manta', 1),
(534, 'Manzanares', 1),
(535, 'Maní', 1),
(536, 'Mapiripan', 1),
(537, 'Margarita', 1),
(538, 'Marinilla', 1),
(539, 'Maripí', 1),
(540, 'Mariquita', 1),
(541, 'Marmato', 1),
(542, 'Marquetalia', 1),
(543, 'Marsella', 1),
(544, 'Marulanda', 1),
(545, 'María la Baja', 1),
(546, 'Matanza', 1),
(547, 'Medellín', 1),
(548, 'Medina', 1),
(549, 'Medio Atrato', 1),
(550, 'Medio Baudó', 1),
(551, 'Medio San Juan (ANDAGOYA)', 1),
(552, 'Melgar', 1),
(553, 'Mercaderes', 1),
(554, 'Mesetas', 1),
(555, 'Milán', 1),
(556, 'Miraflores', 1),
(557, 'Miraflores', 1),
(558, 'Miranda', 1),
(559, 'Mistrató', 1),
(560, 'Mitú', 1),
(561, 'Mocoa', 1),
(562, 'Mogotes', 1),
(563, 'Molagavita', 1),
(564, 'Momil', 1),
(565, 'Mompós', 1),
(566, 'Mongua', 1),
(567, 'Monguí', 1),
(568, 'Moniquirá', 1),
(569, 'Montebello', 1),
(570, 'Montecristo', 1),
(571, 'Montelíbano', 1),
(572, 'Montenegro', 1),
(573, 'Monteria', 1),
(574, 'Monterrey', 1),
(575, 'Morales', 1),
(576, 'Morales', 1),
(577, 'Morelia', 1),
(578, 'Morroa', 1),
(579, 'Mosquera', 1),
(580, 'Mosquera', 1),
(581, 'Motavita', 1),
(582, 'Moñitos', 1),
(583, 'Murillo', 1),
(584, 'Murindó', 1),
(585, 'Mutatá', 1),
(586, 'Mutiscua', 1),
(587, 'Muzo', 1),
(588, 'Málaga', 1),
(589, 'Nariño', 1),
(590, 'Nariño', 1),
(591, 'Nariño', 1),
(592, 'Natagaima', 1),
(593, 'Nechí', 1),
(594, 'Necoclí', 1),
(595, 'Neira', 1),
(596, 'Neiva', 1),
(597, 'Nemocón', 1),
(598, 'Nilo', 1),
(599, 'Nimaima', 1),
(600, 'Nobsa', 1),
(601, 'Nocaima', 1),
(602, 'Norcasia', 1),
(603, 'Norosí', 1),
(604, 'Novita', 1),
(605, 'Nueva Granada', 1),
(606, 'Nuevo Colón', 1),
(607, 'Nunchía', 1),
(608, 'Nuquí', 1),
(609, 'Nátaga', 1),
(610, 'Obando', 1),
(611, 'Ocamonte', 1),
(612, 'Ocaña', 1),
(613, 'Oiba', 1),
(614, 'Oicatá', 1),
(615, 'Olaya', 1),
(616, 'Olaya Herrera', 1),
(617, 'Onzaga', 1),
(618, 'Oporapa', 1),
(619, 'Orito', 1),
(620, 'Orocué', 1),
(621, 'Ortega', 1),
(622, 'Ospina', 1),
(623, 'Otanche', 1),
(624, 'Ovejas', 1),
(625, 'Pachavita', 1),
(626, 'Pacho', 1),
(627, 'Padilla', 1),
(628, 'Paicol', 1),
(629, 'Pailitas', 1),
(630, 'Paime', 1),
(631, 'Paipa', 1),
(632, 'Pajarito', 1),
(633, 'Palermo', 1),
(634, 'Palestina', 1),
(635, 'Palestina', 1),
(636, 'Palmar', 1),
(637, 'Palmar de Varela', 1),
(638, 'Palmas del Socorro', 1),
(639, 'Palmira', 1),
(640, 'Palmito', 1),
(641, 'Palocabildo', 1),
(642, 'Pamplona', 1),
(643, 'Pamplonita', 1),
(644, 'Pandi', 1),
(645, 'Panqueba', 1),
(646, 'Paratebueno', 1),
(647, 'Pasca', 1),
(648, 'Patía (El Bordo)', 1),
(649, 'Pauna', 1),
(650, 'Paya', 1),
(651, 'Paz de Ariporo', 1),
(652, 'Paz de Río', 1),
(653, 'Pedraza', 1),
(654, 'Pelaya', 1),
(655, 'Pensilvania', 1),
(656, 'Peque', 1),
(657, 'Pereira', 1),
(658, 'Pesca', 1),
(659, 'Peñol', 1),
(660, 'Piamonte', 1),
(661, 'Pie de Cuesta', 1),
(662, 'Piedras', 1),
(663, 'Piendamó', 1),
(664, 'Pijao', 1),
(665, 'Pijiño', 1),
(666, 'Pinchote', 1),
(667, 'Pinillos', 1),
(668, 'Piojo', 1),
(669, 'Pisva', 1),
(670, 'Pital', 1),
(671, 'Pitalito', 1),
(672, 'Pivijay', 1),
(673, 'Planadas', 1),
(674, 'Planeta Rica', 1),
(675, 'Plato', 1),
(676, 'Policarpa', 1),
(677, 'Polonuevo', 1),
(678, 'Ponedera', 1),
(679, 'Popayán', 1),
(680, 'Pore', 1),
(681, 'Potosí', 1),
(682, 'Pradera', 1),
(683, 'Prado', 1),
(684, 'Providencia', 1),
(685, 'Providencia', 1),
(686, 'Pueblo Bello', 1),
(687, 'Pueblo Nuevo', 1),
(688, 'Pueblo Rico', 1),
(689, 'Pueblorrico', 1),
(690, 'Puebloviejo', 1),
(691, 'Puente Nacional', 1),
(692, 'Puerres', 1),
(693, 'Puerto Asís', 1),
(694, 'Puerto Berrío', 1),
(695, 'Puerto Boyacá', 1),
(696, 'Puerto Caicedo', 1),
(697, 'Puerto Carreño', 1),
(698, 'Puerto Colombia', 1),
(699, 'Puerto Concordia', 1),
(700, 'Puerto Escondido', 1),
(701, 'Puerto Gaitán', 1),
(702, 'Puerto Guzmán', 1),
(703, 'Puerto Leguízamo', 1),
(704, 'Puerto Libertador', 1),
(705, 'Puerto Lleras', 1),
(706, 'Puerto López', 1),
(707, 'Puerto Nare', 1),
(708, 'Puerto Nariño', 1),
(709, 'Puerto Parra', 1),
(710, 'Puerto Rico', 1),
(711, 'Puerto Rico', 1),
(712, 'Puerto Rondón', 1),
(713, 'Puerto Salgar', 1),
(714, 'Puerto Santander', 1),
(715, 'Puerto Tejada', 1),
(716, 'Puerto Triunfo', 1),
(717, 'Puerto Wilches', 1),
(718, 'Pulí', 1),
(719, 'Pupiales', 1),
(720, 'Puracé (Coconuco)', 1),
(721, 'Purificación', 1),
(722, 'Purísima', 1),
(723, 'Pácora', 1),
(724, 'Páez', 1),
(725, 'Páez (Belalcazar)', 1),
(726, 'Páramo', 1),
(727, 'Quebradanegra', 1),
(728, 'Quetame', 1),
(729, 'Quibdó', 1),
(730, 'Quimbaya', 1),
(731, 'Quinchía', 1),
(732, 'Quipama', 1),
(733, 'Quipile', 1),
(734, 'Ragonvalia', 1),
(735, 'Ramiriquí', 1),
(736, 'Recetor', 1),
(737, 'Regidor', 1),
(738, 'Remedios', 1),
(739, 'Remolino', 1),
(740, 'Repelón', 1),
(741, 'Restrepo', 1),
(742, 'Restrepo', 1),
(743, 'Retiro', 1),
(744, 'Ricaurte', 1),
(745, 'Ricaurte', 1),
(746, 'Rio Negro', 1),
(747, 'Rioblanco', 1),
(748, 'Riofrío', 1),
(749, 'Riohacha', 1),
(750, 'Risaralda', 1),
(751, 'Rivera', 1),
(752, 'Roberto Payán (San José)', 1),
(753, 'Roldanillo', 1),
(754, 'Roncesvalles', 1),
(755, 'Rondón', 1),
(756, 'Rosas', 1),
(757, 'Rovira', 1),
(758, 'Ráquira', 1),
(759, 'Río Iró', 1),
(760, 'Río Quito', 1),
(761, 'Río Sucio', 1),
(762, 'Río Viejo', 1),
(763, 'Río de oro', 1),
(764, 'Ríonegro', 1),
(765, 'Ríosucio', 1),
(766, 'Sabana de Torres', 1),
(767, 'Sabanagrande', 1),
(768, 'Sabanalarga', 1),
(769, 'Sabanalarga', 1),
(770, 'Sabanalarga', 1),
(771, 'Sabanas de San Angel (SAN ANGEL)', 1),
(772, 'Sabaneta', 1),
(773, 'Saboyá', 1),
(774, 'Sahagún', 1),
(775, 'Saladoblanco', 1),
(776, 'Salamina', 1),
(777, 'Salamina', 1),
(778, 'Salazar', 1),
(779, 'Saldaña', 1),
(780, 'Salento', 1),
(781, 'Salgar', 1),
(782, 'Samacá', 1),
(783, 'Samaniego', 1),
(784, 'Samaná', 1),
(785, 'Sampués', 1),
(786, 'San Agustín', 1),
(787, 'San Alberto', 1),
(788, 'San Andrés', 1),
(789, 'San Andrés Sotavento', 1),
(790, 'San Andrés de Cuerquía', 1),
(791, 'San Antero', 1),
(792, 'San Antonio', 1),
(793, 'San Antonio de Tequendama', 1),
(794, 'San Benito', 1),
(795, 'San Benito Abad', 1),
(796, 'San Bernardo', 1),
(797, 'San Bernardo', 1),
(798, 'San Bernardo del Viento', 1),
(799, 'San Calixto', 1),
(800, 'San Carlos', 1),
(801, 'San Carlos', 1),
(802, 'San Carlos de Guaroa', 1),
(803, 'San Cayetano', 1),
(804, 'San Cayetano', 1),
(805, 'San Cristobal', 1),
(806, 'San Diego', 1),
(807, 'San Eduardo', 1),
(808, 'San Estanislao', 1),
(809, 'San Fernando', 1),
(810, 'San Francisco', 1),
(811, 'San Francisco', 1),
(812, 'San Francisco', 1),
(813, 'San Gíl', 1),
(814, 'San Jacinto', 1),
(815, 'San Jacinto del Cauca', 1),
(816, 'San Jerónimo', 1),
(817, 'San Joaquín', 1),
(818, 'San José', 1),
(819, 'San José de Miranda', 1),
(820, 'San José de Montaña', 1),
(821, 'San José de Pare', 1),
(822, 'San José de Uré', 1),
(823, 'San José del Fragua', 1),
(824, 'San José del Guaviare', 1),
(825, 'San José del Palmar', 1),
(826, 'San Juan de Arama', 1),
(827, 'San Juan de Betulia', 1),
(828, 'San Juan de Nepomuceno', 1),
(829, 'San Juan de Pasto', 1),
(830, 'San Juan de Río Seco', 1),
(831, 'San Juan de Urabá', 1),
(832, 'San Juan del Cesar', 1),
(833, 'San Juanito', 1),
(834, 'San Lorenzo', 1),
(835, 'San Luis', 1),
(836, 'San Luís', 1),
(837, 'San Luís de Gaceno', 1),
(838, 'San Luís de Palenque', 1),
(839, 'San Marcos', 1),
(840, 'San Martín', 1),
(841, 'San Martín', 1),
(842, 'San Martín de Loba', 1),
(843, 'San Mateo', 1),
(844, 'San Miguel', 1),
(845, 'San Miguel', 1),
(846, 'San Miguel de Sema', 1),
(847, 'San Onofre', 1),
(848, 'San Pablo', 1),
(849, 'San Pablo', 1),
(850, 'San Pablo de Borbur', 1),
(851, 'San Pedro', 1),
(852, 'San Pedro', 1),
(853, 'San Pedro', 1),
(854, 'San Pedro de Cartago', 1),
(855, 'San Pedro de Urabá', 1),
(856, 'San Pelayo', 1),
(857, 'San Rafael', 1),
(858, 'San Roque', 1),
(859, 'San Sebastián', 1),
(860, 'San Sebastián de Buenavista', 1),
(861, 'San Vicente', 1),
(862, 'San Vicente del Caguán', 1),
(863, 'San Vicente del Chucurí', 1),
(864, 'San Zenón', 1),
(865, 'Sandoná', 1),
(866, 'Santa Ana', 1),
(867, 'Santa Bárbara', 1),
(868, 'Santa Bárbara', 1),
(869, 'Santa Bárbara (Iscuandé)', 1),
(870, 'Santa Bárbara de Pinto', 1),
(871, 'Santa Catalina', 1),
(872, 'Santa Fé de Antioquia', 1),
(873, 'Santa Genoveva de Docorodó', 1),
(874, 'Santa Helena del Opón', 1),
(875, 'Santa Isabel', 1),
(876, 'Santa Lucía', 1),
(877, 'Santa Marta', 1),
(878, 'Santa María', 1),
(879, 'Santa María', 1),
(880, 'Santa Rosa', 1),
(881, 'Santa Rosa', 1),
(882, 'Santa Rosa de Cabal', 1),
(883, 'Santa Rosa de Osos', 1),
(884, 'Santa Rosa de Viterbo', 1),
(885, 'Santa Rosa del Sur', 1),
(886, 'Santa Rosalía', 1),
(887, 'Santa Sofía', 1),
(888, 'Santana', 1),
(889, 'Santander de Quilichao', 1),
(890, 'Santiago', 1),
(891, 'Santiago', 1),
(892, 'Santo Domingo', 1),
(893, 'Santo Tomás', 1),
(894, 'Santuario', 1),
(895, 'Santuario', 1),
(896, 'Sapuyes', 1),
(897, 'Saravena', 1),
(898, 'Sardinata', 1),
(899, 'Sasaima', 1),
(900, 'Sativanorte', 1),
(901, 'Sativasur', 1),
(902, 'Segovia', 1),
(903, 'Sesquilé', 1),
(904, 'Sevilla', 1),
(905, 'Siachoque', 1),
(906, 'Sibaté', 1),
(907, 'Sibundoy', 1),
(908, 'Silos', 1),
(909, 'Silvania', 1),
(910, 'Silvia', 1),
(911, 'Simacota', 1),
(912, 'Simijaca', 1),
(913, 'Simití', 1),
(914, 'Sincelejo', 1),
(915, 'Sincé', 1),
(916, 'Sipí', 1),
(917, 'Sitionuevo', 1),
(918, 'Soacha', 1),
(919, 'Soatá', 1),
(920, 'Socha', 1),
(921, 'Socorro', 1),
(922, 'Socotá', 1),
(923, 'Sogamoso', 1),
(924, 'Solano', 1),
(925, 'Soledad', 1),
(926, 'Solita', 1),
(927, 'Somondoco', 1),
(928, 'Sonsón', 1),
(929, 'Sopetrán', 1),
(930, 'Soplaviento', 1),
(931, 'Sopó', 1),
(932, 'Sora', 1),
(933, 'Soracá', 1),
(934, 'Sotaquirá', 1),
(935, 'Sotara (Paispamba)', 1),
(936, 'Sotomayor (Los Andes)', 1),
(937, 'Suaita', 1),
(938, 'Suan', 1),
(939, 'Suaza', 1),
(940, 'Subachoque', 1),
(941, 'Sucre', 1),
(942, 'Sucre', 1),
(943, 'Sucre', 1),
(944, 'Suesca', 1),
(945, 'Supatá', 1),
(946, 'Supía', 1),
(947, 'Suratá', 1),
(948, 'Susa', 1),
(949, 'Susacón', 1),
(950, 'Sutamarchán', 1),
(951, 'Sutatausa', 1),
(952, 'Sutatenza', 1),
(953, 'Suárez', 1),
(954, 'Suárez', 1),
(955, 'Sácama', 1),
(956, 'Sáchica', 1),
(957, 'Tabio', 1),
(958, 'Tadó', 1),
(959, 'Talaigua Nuevo', 1),
(960, 'Tamalameque', 1),
(961, 'Tame', 1),
(962, 'Taminango', 1),
(963, 'Tangua', 1),
(964, 'Taraira', 1),
(965, 'Tarazá', 1),
(966, 'Tarqui', 1),
(967, 'Tarso', 1),
(968, 'Tasco', 1),
(969, 'Tauramena', 1),
(970, 'Tausa', 1),
(971, 'Tello', 1),
(972, 'Tena', 1),
(973, 'Tenerife', 1),
(974, 'Tenjo', 1),
(975, 'Tenza', 1),
(976, 'Teorama', 1),
(977, 'Teruel', 1),
(978, 'Tesalia', 1),
(979, 'Tibacuy', 1),
(980, 'Tibaná', 1),
(981, 'Tibasosa', 1),
(982, 'Tibirita', 1),
(983, 'Tibú', 1),
(984, 'Tierralta', 1),
(985, 'Timaná', 1),
(986, 'Timbiquí', 1),
(987, 'Timbío', 1),
(988, 'Tinjacá', 1),
(989, 'Tipacoque', 1),
(990, 'Tiquisio (Puerto Rico)', 1),
(991, 'Titiribí', 1),
(992, 'Toca', 1),
(993, 'Tocaima', 1),
(994, 'Tocancipá', 1),
(995, 'Toguí', 1),
(996, 'Toledo', 1),
(997, 'Toledo', 1),
(998, 'Tolú', 1),
(999, 'Tolú Viejo', 1),
(1000, 'Tona', 1),
(1001, 'Topagá', 1),
(1002, 'Topaipí', 1),
(1003, 'Toribío', 1),
(1004, 'Toro', 1),
(1005, 'Tota', 1),
(1006, 'Totoró', 1),
(1007, 'Trinidad', 1),
(1008, 'Trujillo', 1),
(1009, 'Tubará', 1),
(1010, 'Tuchín', 1),
(1011, 'Tulúa', 1),
(1012, 'Tumaco', 1),
(1013, 'Tunja', 1),
(1014, 'Tunungua', 1),
(1015, 'Turbaco', 1),
(1016, 'Turbaná', 1),
(1017, 'Turbo', 1),
(1018, 'Turmequé', 1),
(1019, 'Tuta', 1),
(1020, 'Tutasá', 1),
(1021, 'Támara', 1),
(1022, 'Támesis', 1),
(1023, 'Túquerres', 1),
(1024, 'Ubalá', 1),
(1025, 'Ubaque', 1),
(1026, 'Ubaté', 1),
(1027, 'Ulloa', 1),
(1028, 'Une', 1),
(1029, 'Unguía', 1),
(1030, 'Unión Panamericana (ÁNIMAS)', 1),
(1031, 'Uramita', 1),
(1032, 'Uribe', 1),
(1033, 'Uribia', 1),
(1034, 'Urrao', 1),
(1035, 'Urumita', 1),
(1036, 'Usiacuri', 1),
(1037, 'Valdivia', 1),
(1038, 'Valencia', 1),
(1039, 'Valle de San José', 1),
(1040, 'Valle de San Juan', 1),
(1041, 'Valle del Guamuez', 1),
(1042, 'Valledupar', 1),
(1043, 'Valparaiso', 1),
(1044, 'Valparaiso', 1),
(1045, 'Vegachí', 1),
(1046, 'Venadillo', 1),
(1047, 'Venecia', 1),
(1048, 'Venecia (Ospina Pérez)', 1),
(1049, 'Ventaquemada', 1),
(1050, 'Vergara', 1),
(1051, 'Versalles', 1),
(1052, 'Vetas', 1),
(1053, 'Viani', 1),
(1054, 'Vigía del Fuerte', 1),
(1055, 'Vijes', 1),
(1056, 'Villa Caro', 1),
(1057, 'Villa Rica', 1),
(1058, 'Villa de Leiva', 1),
(1059, 'Villa del Rosario', 1),
(1060, 'Villagarzón', 1),
(1061, 'Villagómez', 1),
(1062, 'Villahermosa', 1),
(1063, 'Villamaría', 1),
(1064, 'Villanueva', 1),
(1065, 'Villanueva', 1),
(1066, 'Villanueva', 1),
(1067, 'Villanueva', 1),
(1068, 'Villapinzón', 1),
(1069, 'Villarrica', 1),
(1070, 'Villavicencio', 1),
(1071, 'Villavieja', 1),
(1072, 'Villeta', 1),
(1073, 'Viotá', 1),
(1074, 'Viracachá', 1),
(1075, 'Vista Hermosa', 1),
(1076, 'Viterbo', 1),
(1077, 'Vélez', 1),
(1078, 'Yacopí', 1),
(1079, 'Yacuanquer', 1),
(1080, 'Yaguará', 1),
(1081, 'Yalí', 1),
(1082, 'Yarumal', 1),
(1083, 'Yolombó', 1),
(1084, 'Yondó (Casabe)', 1),
(1085, 'Yopal', 1),
(1086, 'Yotoco', 1),
(1087, 'Yumbo', 1),
(1088, 'Zambrano', 1),
(1089, 'Zapatoca', 1),
(1090, 'Zapayán (PUNTA DE PIEDRAS)', 1),
(1091, 'Zaragoza', 1),
(1092, 'Zarzal', 1),
(1093, 'Zetaquirá', 1),
(1094, 'Zipacón', 1),
(1095, 'Zipaquirá', 1),
(1096, 'Zona Bananera (PRADO - SEVILLA)', 1),
(1097, 'Ábrego', 1),
(1098, 'Íquira', 1),
(1099, 'Úmbita', 1),
(1100, 'Útica', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id_pedido` int(11) NOT NULL,
  `cita_id` int(11) NOT NULL,
  `total_pagar` double NOT NULL,
  `fecha_cita` datetime NOT NULL,
  `descripcion` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos_personalizados`
--

CREATE TABLE `pedidos_personalizados` (
  `id_pedido_pesonalizado` int(11) NOT NULL,
  `cita_id` int(11) NOT NULL,
  `total_pagar` double NOT NULL,
  `fecha_cita` datetime NOT NULL,
  `descripcion` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `id_permiso` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `estado` bit(1) NOT NULL DEFAULT b'1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `producto_id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `precio` double NOT NULL,
  `proveedor_id` int(11) NOT NULL,
  `tipo_producto_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `estado` bit(1) NOT NULL DEFAULT b'1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `id_proveedores` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `celular` varchar(10) DEFAULT NULL,
  `encargado` varchar(20) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `estado` bit(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `permiso_id` int(11) NOT NULL,
  `estado` bit(1) NOT NULL DEFAULT b'1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE `servicios` (
  `id_servicio` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `img_servicio` varchar(1000) NOT NULL,
  `precio` int(11) NOT NULL,
  `tipo_servicio_id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `estado` bit(1) NOT NULL DEFAULT b'1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_documentos`
--

CREATE TABLE `tipo_documentos` (
  `id_tipo_documento` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_productos`
--

CREATE TABLE `tipo_productos` (
  `id_tipo_producto` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_servicios`
--

CREATE TABLE `tipo_servicios` (
  `id_tipo_servicio` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(15) NOT NULL,
  `nombres` varchar(60) NOT NULL,
  `apellidos` varchar(60) NOT NULL,
  `apodo` varchar(16) NOT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `celular` varchar(10) NOT NULL,
  `email` varchar(60) NOT NULL,
  `fech_nac` date NOT NULL,
  `tipo_documuento_id` int(11) NOT NULL,
  `num_documento` varchar(15) NOT NULL,
  `img_usuario` text DEFAULT NULL,
  `contrasena` varchar(40) NOT NULL,
  `municipio_id` int(11) NOT NULL,
  `direccion` varchar(80) DEFAULT NULL,
  `cod_postal_id` int(11) DEFAULT NULL,
  `rol_id` int(11) NOT NULL DEFAULT 1,
  `estado` bit(1) NOT NULL DEFAULT b'1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `citas`
--
ALTER TABLE `citas`
  ADD PRIMARY KEY (`id_cita`);

--
-- Indices de la tabla `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`id_compra`);

--
-- Indices de la tabla `front_end`
--
ALTER TABLE `front_end`
  ADD PRIMARY KEY (`id_front_end`);

--
-- Indices de la tabla `municipios`
--
ALTER TABLE `municipios`
  ADD PRIMARY KEY (`id_municipio`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id_pedido`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`id_permiso`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`producto_id`);

--
-- Indices de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`id_proveedores`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`id_servicio`);

--
-- Indices de la tabla `tipo_documentos`
--
ALTER TABLE `tipo_documentos`
  ADD PRIMARY KEY (`id_tipo_documento`);

--
-- Indices de la tabla `tipo_productos`
--
ALTER TABLE `tipo_productos`
  ADD PRIMARY KEY (`id_tipo_producto`);

--
-- Indices de la tabla `tipo_servicios`
--
ALTER TABLE `tipo_servicios`
  ADD PRIMARY KEY (`id_tipo_servicio`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `citas`
--
ALTER TABLE `citas`
  MODIFY `id_cita` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `compras`
--
ALTER TABLE `compras`
  MODIFY `id_compra` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `front_end`
--
ALTER TABLE `front_end`
  MODIFY `id_front_end` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `municipios`
--
ALTER TABLE `municipios`
  MODIFY `id_municipio` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1101;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id_permiso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `producto_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  MODIFY `id_proveedores` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `id_servicio` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_documentos`
--
ALTER TABLE `tipo_documentos`
  MODIFY `id_tipo_documento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_productos`
--
ALTER TABLE `tipo_productos`
  MODIFY `id_tipo_producto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_servicios`
--
ALTER TABLE `tipo_servicios`
  MODIFY `id_tipo_servicio` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(15) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
