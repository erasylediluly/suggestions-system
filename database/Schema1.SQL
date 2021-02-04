CREATE TABLE Country ( 
	country_id int NOT NULL,
	country_name varchar(50) NOT NULL,
	CONSTRAINT PK_Country PRIMARY KEY (country_id)
)
;

CREATE TABLE City ( 
	city_id int NOT NULL,
	city_name varchar(50) NOT NULL,
	country_id int NOT NULL,
	CONSTRAINT PK_City PRIMARY KEY (city_id),
	CONSTRAINT FK_City_Country FOREIGN KEY (country_id) REFERENCES Country (country_id)
)
;

CREATE TABLE Product ( 
	product_id int NOT NULL,
	product_name varchar(50) NOT NULL,
	CONSTRAINT PK_Product PRIMARY KEY (product_id)
)
;

CREATE TABLE Customer ( 
	customer_id int NOT NULL,
	name varchar(50) NOT NULL,
	surname varchar(50) NOT NULL,
	password varchar(50) NOT NULL,
	CONSTRAINT PK_Customer PRIMARY KEY (customer_id)
)
;

CREATE TABLE Employee ( 
	employee_id int NOT NULL,
	name varchar(50) NOT NULL,
	surname varchar(50) NOT NULL,
	password varchar(50),
	CONSTRAINT PK_Employee PRIMARY KEY (employee_id)
)
;

CREATE TABLE Office ( 
	office_id int NOT NULL,
	city_id int NOT NULL,
	address varchar(50),
	CONSTRAINT PK_Office PRIMARY KEY (office_id),
	CONSTRAINT FK_Office_City FOREIGN KEY (city_id) REFERENCES City (city_id)
)
;

CREATE TABLE Order ( 
	order_id int NOT NULL,
	customer_id int NOT NULL,
	employee_id int,
	source_office_id int NOT NULL,
	destination_office_id int NOT NULL,
	product_id int NOT NULL,
	amount int NOT NULL,
	taken_time datetime,
	delivered_time datetime,
	CONSTRAINT PK_Order PRIMARY KEY (order_id),
	CONSTRAINT FK_Order_Customer FOREIGN KEY (customer_id) REFERENCES Customer (customer_id),
	CONSTRAINT FK_Order_Office1 FOREIGN KEY (source_office_id) REFERENCES Office (office_id),
	CONSTRAINT FK_Order_Office2 FOREIGN KEY (destination_office_id) REFERENCES Office (office_id),
	CONSTRAINT FK_Order_Product FOREIGN KEY (product_id) REFERENCES Product (product_id),
	CONSTRAINT FK_Order_Employee FOREIGN KEY (employee_id) REFERENCES Employee (employee_id)
)
;
sqlite> INSERT INTO Country VALUES(1,'Afghanistan');
sqlite> INSERT INTO Country VALUES(2,'Albania');
sqlite> INSERT INTO Country VALUES(3,'Algeria');
sqlite> INSERT INTO Country VALUES(4,'American Samoa');
sqlite> INSERT INTO Country VALUES(5,'Andorra');
sqlite> INSERT INTO Country VALUES(6,'Angola');
sqlite> INSERT INTO Country VALUES(7,'Anguilla');
sqlite> INSERT INTO Country VALUES(8,'Antarcti');
sqlite> INSERT INTO Country VALUES(9,'Antigua and Barbuda');
sqlite> INSERT INTO Country VALUES(10, 'Argentina');
sqlite> INSERT INTO Country VALUES(11, 'Armenia');
sqlite> INSERT INTO Country VALUES(12, 'Aruba');
sqlite> INSERT INTO Country VALUES(13, 'Australia');
sqlite> INSERT INTO Country VALUES(14, 'Austria');
sqlite> INSERT INTO Country VALUES(15, 'Azerbaijan');
sqlite> INSERT INTO Country VALUES(16, 'Bahamas');
sqlite> INSERT INTO Country VALUES(17, 'Bahrain');
sqlite> INSERT INTO Country VALUES(18, 'Bangladesh');
sqlite> INSERT INTO Country VALUES(19, 'Barbados');
sqlite> INSERT INTO Country VALUES(20, 'Belarus');
sqlite> INSERT INTO Country VALUES(21, 'Belgium');
sqlite> INSERT INTO Country VALUES(22, 'Belize');
sqlite> INSERT INTO Country VALUES(23, 'Benin');
sqlite> INSERT INTO Country VALUES(24, 'Bermuda');
sqlite> INSERT INTO Country VALUES(25, 'Bhutan');
sqlite> INSERT INTO Country VALUES(26, 'Bolivia');
sqlite> INSERT INTO Country VALUES(27, 'Bosnia and Herzegovina');
sqlite> INSERT INTO Country VALUES(28, 'Botswana');
sqlite> INSERT INTO Country VALUES(29, 'Bouvet Islands');
sqlite> INSERT INTO Country VALUES(30, 'Brazil');
sqlite> INSERT INTO Country VALUES(31, 'British Indian Ocean Territories');
sqlite> INSERT INTO Country VALUES(32, 'Brunei Darussalam');
sqlite> INSERT INTO Country VALUES(33, 'Bulgaria');
sqlite> INSERT INTO Country VALUES(34, 'Burkina Faso');
sqlite> INSERT INTO Country VALUES(35, 'Burundi');
sqlite> INSERT INTO Country VALUES(36, 'Cambodia');
sqlite> INSERT INTO Country VALUES(37, 'Cameroon');
sqlite> INSERT INTO Country VALUES(38, 'Canada');
sqlite> INSERT INTO Country VALUES(39, 'Cape Verde');
sqlite> INSERT INTO Country VALUES(40, 'Cayman Islands');
sqlite> INSERT INTO Country VALUES(41, 'Central African Republic');
sqlite> INSERT INTO Country VALUES(42, 'Chad');
sqlite> INSERT INTO Country VALUES(43, 'Chile');
sqlite> INSERT INTO Country VALUES(44, 'China');
sqlite> INSERT INTO Country VALUES(45, 'Christmas Islands');
sqlite> INSERT INTO Country VALUES(46, 'Cocos (Keeling) Islands');
sqlite> INSERT INTO Country VALUES(47, 'Colombia');
sqlite> INSERT INTO Country VALUES(48, 'Comoros');
sqlite> INSERT INTO Country VALUES(49, 'Congo');
sqlite> INSERT INTO Country VALUES(50, 'Congo, the Democratic Republic of the');
sqlite> INSERT INTO Country VALUES(51, 'Cook Islands');
sqlite> INSERT INTO Country VALUES(52, 'Costa Rica');
sqlite> INSERT INTO Country VALUES(53, 'Cote D''Ivoire');
sqlite> INSERT INTO Country VALUES(54, 'Croatia');
sqlite> INSERT INTO Country VALUES(55, 'Cuba');
sqlite> INSERT INTO Country VALUES(56, 'Cyprus');
sqlite> INSERT INTO Country VALUES(57, 'Czech Republic');
sqlite> INSERT INTO Country VALUES(58, 'Denmark');
sqlite> INSERT INTO Country VALUES(59, 'Djibouti');
sqlite> INSERT INTO Country VALUES(60, 'Dominica');
sqlite> INSERT INTO Country VALUES(61, 'Dominican Republic');
sqlite> INSERT INTO Country VALUES(62, 'Ecuador');
sqlite> INSERT INTO Country VALUES(63, 'Egypt');
sqlite> INSERT INTO Country VALUES(64, 'El Salvador');
sqlite> INSERT INTO Country VALUES(65, 'Equatorial Guinea');
sqlite> INSERT INTO Country VALUES(66, 'Eritrea');
sqlite> INSERT INTO Country VALUES(67, 'Estonia');
sqlite> INSERT INTO Country VALUES(68, 'Ethiopia');
sqlite> INSERT INTO Country VALUES(69, 'Falkland Islands (Malvinas)');
sqlite> INSERT INTO Country VALUES(70, 'Faroe Islands');
sqlite> INSERT INTO Country VALUES(71, 'Fiji');
sqlite> INSERT INTO Country VALUES(72, 'Finland');
sqlite> INSERT INTO Country VALUES(73, 'France');
sqlite> INSERT INTO Country VALUES(74, 'French Guiana');
sqlite> INSERT INTO Country VALUES(75, 'French Polynesia');
sqlite> INSERT INTO Country VALUES(76, 'French Southern Territories');
sqlite> INSERT INTO Country VALUES(77, 'Gabon');
sqlite> INSERT INTO Country VALUES(78, 'Gambia');
sqlite> INSERT INTO Country VALUES(79, 'Georgia');
sqlite> INSERT INTO Country VALUES(80, 'Germany');
sqlite> INSERT INTO Country VALUES(81, 'Ghana');
sqlite> INSERT INTO Country VALUES(82, 'Gibraltar');
sqlite> INSERT INTO Country VALUES(83, 'Greece');
sqlite> INSERT INTO Country VALUES(84, 'Greenland');
sqlite> INSERT INTO Country VALUES(85, 'Grenada');
sqlite> INSERT INTO Country VALUES(86, 'Guadeloupe');
sqlite> INSERT INTO Country VALUES(87, 'Guam');
sqlite> INSERT INTO Country VALUES(88, 'Guatemala');
sqlite> INSERT INTO Country VALUES(89, 'Guinea');
sqlite> INSERT INTO Country VALUES(90, 'Guinea-Bissau');
sqlite> INSERT INTO Country VALUES(91, 'Guyana');
sqlite> INSERT INTO Country VALUES(92, 'Haiti');
sqlite> INSERT INTO Country VALUES(93, 'Heard Island and Mcdonald Islands');
sqlite> INSERT INTO Country VALUES(94, 'Holy See (Vatican City State)');
sqlite> INSERT INTO Country VALUES(95, 'Honduras');
sqlite> INSERT INTO Country VALUES(96, 'Hong Kong');
sqlite> INSERT INTO Country VALUES(97, 'Hungary');
sqlite> INSERT INTO Country VALUES(98, 'Iceland');
sqlite> INSERT INTO Country VALUES(99, 'India');
sqlite> INSERT INTO Country VALUES(100, 'Indonesia');
sqlite> INSERT INTO Country VALUES(101, 'Iran, Islamic Republic of');
sqlite> INSERT INTO Country VALUES(102, 'Iraq');
sqlite> INSERT INTO Country VALUES(103, 'Ireland');
sqlite> INSERT INTO Country VALUES(104, 'Israel');
sqlite> INSERT INTO Country VALUES(105, 'Italy');
sqlite> INSERT INTO Country VALUES(106, 'Jamaica');
sqlite> INSERT INTO Country VALUES(107, 'Japan');
sqlite> INSERT INTO Country VALUES(108, 'Jordan');
sqlite> INSERT INTO Country VALUES(109, 'Kazakhstan');
sqlite> INSERT INTO Country VALUES(110, 'Kenya');
sqlite> INSERT INTO Country VALUES(111, 'Kiribati');
sqlite> INSERT INTO Country VALUES(112, 'Korea, Democratic People''s Republic of');
sqlite> INSERT INTO Country VALUES(113, 'Korea, Republic of');
sqlite> INSERT INTO Country VALUES(114, 'Kuwait');
sqlite> INSERT INTO Country VALUES(115, 'Kyrgyzstan');
sqlite> INSERT INTO Country VALUES(116, 'Lao People''s Democratic Republic');
sqlite> INSERT INTO Country VALUES(117, 'Latvia');
sqlite> INSERT INTO Country VALUES(118, 'Lebanon');
sqlite> INSERT INTO Country VALUES(119, 'Lesotho');
sqlite> INSERT INTO Country VALUES(120, 'Liberia');
sqlite> INSERT INTO Country VALUES(121, 'Libyan Arab Jamahiriya');
sqlite> INSERT INTO Country VALUES(122, 'Liechtenstein');
sqlite> INSERT INTO Country VALUES(123, 'Lithuania');
sqlite> INSERT INTO Country VALUES(124, 'Luxembourg');
sqlite> INSERT INTO Country VALUES(125, 'Macao');
sqlite> INSERT INTO Country VALUES(126, 'Macedonia, the Former Yugoslav Republic of');
sqlite> INSERT INTO Country VALUES(127, 'Madagascar');
sqlite> INSERT INTO Country VALUES(128, 'Malawi');
sqlite> INSERT INTO Country VALUES(129, 'Malaysia');
sqlite> INSERT INTO Country VALUES(130, 'Maldives');
sqlite> INSERT INTO Country VALUES(131, 'Mali');
sqlite> INSERT INTO Country VALUES(132, 'Malta');
sqlite> INSERT INTO Country VALUES(133, 'Marshall Islands');
sqlite> INSERT INTO Country VALUES(134, 'Martinique');
sqlite> INSERT INTO Country VALUES(135, 'Mauritania');
sqlite> INSERT INTO Country VALUES(136, 'Mauritius');
sqlite> INSERT INTO Country VALUES(137, 'Mayotte');
sqlite> INSERT INTO Country VALUES(138, 'Mexico');
sqlite> INSERT INTO Country VALUES(139, 'Micronesia, Federated States of');
sqlite> INSERT INTO Country VALUES(140, 'Moldova, Republic of');
sqlite> INSERT INTO Country VALUES(141, 'Monaco');
sqlite> INSERT INTO Country VALUES(142, 'Mongolia');
sqlite> INSERT INTO Country VALUES(143, 'Montserrat');
sqlite> INSERT INTO Country VALUES(144, 'Morocco');
sqlite> INSERT INTO Country VALUES(145, 'Mozambique');
sqlite> INSERT INTO Country VALUES(146, 'Myanmar');
sqlite> INSERT INTO Country VALUES(147, 'Namibia');
sqlite> INSERT INTO Country VALUES(148, 'Nauru');
sqlite> INSERT INTO Country VALUES(149, 'Nepal');
sqlite> INSERT INTO Country VALUES(150, 'Netherlands');
sqlite> INSERT INTO Country VALUES(151, 'Netherlands Antilles');
sqlite> INSERT INTO Country VALUES(152, 'New Caledonia');
sqlite> INSERT INTO Country VALUES(153, 'New Zealand');
sqlite> INSERT INTO Country VALUES(154, 'Nicaragua');
sqlite> INSERT INTO Country VALUES(155, 'Niger');
sqlite> INSERT INTO Country VALUES(156, 'Nigeria');
sqlite> INSERT INTO Country VALUES(157, 'Niue');
sqlite> INSERT INTO Country VALUES(158, 'Norfolk Island');
sqlite> INSERT INTO Country VALUES(159, 'Northern Mariana Islands');
sqlite> INSERT INTO Country VALUES(160, 'Norway');
sqlite> INSERT INTO Country VALUES(161, 'Oman');
sqlite> INSERT INTO Country VALUES(162, 'Pakistan');
sqlite> INSERT INTO Country VALUES(163, 'Palau');
sqlite> INSERT INTO Country VALUES(164, 'Palestinian Territory, Occupies');
sqlite> INSERT INTO Country VALUES(165, 'Panama');
sqlite> INSERT INTO Country VALUES(166, 'Papua New Guinea');
sqlite> INSERT INTO Country VALUES(167, 'Paraguay');
sqlite> INSERT INTO Country VALUES(168, 'Peru');
sqlite> INSERT INTO Country VALUES(169, 'Philippines');
sqlite> INSERT INTO Country VALUES(170, 'Pitcairn');
sqlite> INSERT INTO Country VALUES(171, 'Poland');
sqlite> INSERT INTO Country VALUES(172, 'Portugal');
sqlite> INSERT INTO Country VALUES(173, 'Puerto Rico');
sqlite> INSERT INTO Country VALUES(174, 'Qatar');
sqlite> INSERT INTO Country VALUES(175, 'Reunion');
sqlite> INSERT INTO Country VALUES(176, 'Romania');
sqlite> INSERT INTO Country VALUES(177, 'Russian Federation');
sqlite> INSERT INTO Country VALUES(178, 'Rwanda');
sqlite> INSERT INTO Country VALUES(179, 'Saint Helena');
sqlite> INSERT INTO Country VALUES(180, 'Saint Kitts and Nevis');
sqlite> INSERT INTO Country VALUES(181, 'Saint Lucia');
sqlite> INSERT INTO Country VALUES(182, 'Saint Pierre and Miquelon');
sqlite> INSERT INTO Country VALUES(183, 'Saint Vincent and the Grenadines');
sqlite> INSERT INTO Country VALUES(184, 'Samoa');
sqlite> INSERT INTO Country VALUES(185, 'San Marino');
sqlite> INSERT INTO Country VALUES(186, 'Sao Tome and Principe');
sqlite> INSERT INTO Country VALUES(187, 'Saudi Arabia');
sqlite> INSERT INTO Country VALUES(188, 'Senegal');
sqlite> INSERT INTO Country VALUES(189, 'Serbia and Montenegro');
sqlite> INSERT INTO Country VALUES(190, 'Seychelles');
sqlite> INSERT INTO Country VALUES(191, 'Sierra Leone');
sqlite> INSERT INTO Country VALUES(192, 'Singapore');
sqlite> INSERT INTO Country VALUES(193, 'Slovakia');
sqlite> INSERT INTO Country VALUES(194, 'Slovenia');
sqlite> INSERT INTO Country VALUES(195, 'Solomon Islands');
sqlite> INSERT INTO Country VALUES(196, 'Somalia');
sqlite> INSERT INTO Country VALUES(197, 'South Africa');
sqlite> INSERT INTO Country VALUES(198, 'South Georgia and the South Sandwich Islands');
sqlite> INSERT INTO Country VALUES(199, 'Spain');
sqlite> INSERT INTO Country VALUES(200, 'Sri Lanka');
sqlite> INSERT INTO Country VALUES(201, 'Sudan');
sqlite> INSERT INTO Country VALUES(202, 'Suriname');
sqlite> INSERT INTO Country VALUES(203, 'Svalbard and Jan Mayen');
sqlite> INSERT INTO Country VALUES(204, 'Swaziland');
sqlite> INSERT INTO Country VALUES(205, 'Sweden');
sqlite> INSERT INTO Country VALUES(206, 'Switzerland');
sqlite> INSERT INTO Country VALUES(207, 'Syrian Arab Republic');
sqlite> INSERT INTO Country VALUES(208, 'Taiwan, Province of China');
sqlite> INSERT INTO Country VALUES(209, 'Tajikistan');
sqlite> INSERT INTO Country VALUES(210, 'Tanzania, United Republic of');
sqlite> INSERT INTO Country VALUES(211, 'Thailand');
sqlite> INSERT INTO Country VALUES(212, 'Timor-Leste');
sqlite> INSERT INTO Country VALUES(213, 'Togo');
sqlite> INSERT INTO Country VALUES(214, 'Tokelau');
sqlite> INSERT INTO Country VALUES(215, 'Tonga');
sqlite> INSERT INTO Country VALUES(216, 'Trinidad and Tobago');
sqlite> INSERT INTO Country VALUES(217, 'Tunisia');
sqlite> INSERT INTO Country VALUES(218, 'Turkey');
sqlite> INSERT INTO Country VALUES(219, 'Turkmenistan');
sqlite> INSERT INTO Country VALUES(220, 'Turks and Caicos Islands');
sqlite> INSERT INTO Country VALUES(221, 'Tuvalu');
sqlite> INSERT INTO Country VALUES(222, 'Uganda');
sqlite> INSERT INTO Country VALUES(223, 'Ukraine');
sqlite> INSERT INTO Country VALUES(224, 'United Arab Emirates');
sqlite> INSERT INTO Country VALUES(225, 'United Kingdom');
sqlite> INSERT INTO Country VALUES(226, 'United States');
sqlite> INSERT INTO Country VALUES(227, 'United States Minor Outlying Islands');
sqlite> INSERT INTO Country VALUES(228, 'Uruguay');
sqlite> INSERT INTO Country VALUES(229, 'Uzbekistan');
sqlite> INSERT INTO Country VALUES(230, 'Vanuatu');
sqlite> INSERT INTO Country VALUES(231, 'Venezuela');
sqlite> INSERT INTO Country VALUES(232, 'Viet Nam');
sqlite> INSERT INTO Country VALUES(233, 'Virgin Islands, British');
sqlite> INSERT INTO Country VALUES(234, 'Virgin Islands, U.s.');
sqlite> INSERT INTO Country VALUES(235, 'Wallis and Futuna');
sqlite> INSERT INTO Country VALUES(236, 'Western Sahara');
sqlite> INSERT INTO Country VALUES(237, 'Yemen');
sqlite> INSERT INTO Country VALUES(238, 'Zambia');
sqlite> INSERT INTO Country VALUES(239, 'Zimbabwe');
sqlite> INSERT INTO City VALUES(1,'Aktau',1);
sqlite> INSERT INTO City VALUES(2,'Aktobe',1);
sqlite> INSERT INTO City VALUES(3,'Almaty',1);
sqlite> INSERT INTO City VALUES(4,'Arkalyk',1);
sqlite> INSERT INTO City VALUES(5,'Atyrau',1);
sqlite> INSERT INTO City VALUES(6,'Baikonur',1);
sqlite> INSERT INTO City VALUES(7,'Balqash',1);
sqlite> INSERT INTO City VALUES(8,'Zhezkazgan',1);
sqlite> INSERT INTO City VALUES(9,'Karagandy',1);
sqlite> INSERT INTO City VALUES(10, 'Kentau',1);
sqlite> INSERT INTO City VALUES(11, 'Kyzylorda',1);
sqlite> INSERT INTO City VALUES(12, 'Kokshetau',1);
sqlite> INSERT INTO City VALUES(13, 'Zhanaozen',1);
sqlite> INSERT INTO City VALUES(14, 'Pavlodar',1);
sqlite> INSERT INTO City VALUES(15, 'Petropavl',1);
sqlite> INSERT INTO City VALUES(16, 'Ridder',1);
sqlite> INSERT INTO City VALUES(17, 'Saran',1);
sqlite> INSERT INTO City VALUES(18, 'Satbayev',1);
sqlite> INSERT INTO City VALUES(19, 'Semey',1);
sqlite> INSERT INTO City VALUES(20, 'Stepnogorsk',1);
sqlite> INSERT INTO City VALUES(21, 'Taldykorgan',1);
sqlite> INSERT INTO City VALUES(22, 'Taraz',1);
sqlite> INSERT INTO City VALUES(23, 'Temirtau',1);
sqlite> INSERT INTO City VALUES(24, 'Turkistan',1);
sqlite> INSERT INTO City VALUES(25, 'Oral',1);
sqlite> INSERT INTO City VALUES(26, 'Oskemen',1);
sqlite> INSERT INTO City VALUES(27, 'Shymkent',1);
sqlite> INSERT INTO City VALUES(28, 'Shakhtinsk',1);
sqlite> INSERT INTO City VALUES(29, 'Schuchinsk',1);
sqlite> INSERT INTO City VALUES(30, 'Ekibastuz',1);
sqlite> INSERT INTO City VALUES(31, 'Nur-Sultan',1);
sqlite> INSERT INTO City VALUES(32, 'Kostanay',1);
sqlite> INSERT INTO Office VALUES(1,31,'Mangilik el 40a');
sqlite> INSERT INTO Office VALUES(2,3,'Baitursynov 59');
sqlite> INSERT INTO Office VALUES(3,27,'Kozhanova 57');
sqlite> INSERT INTO Office VALUES(4,22,'Zhambyl 184');
sqlite> INSERT INTO Office VALUES(5,24,'Sattarkhnaov 24');
sqlite> INSERT INTO Office VALUES(6,11,'Korkyt ata 7');
sqlite> INSERT INTO Office VALUES(7,21,'Zhansugirov 116');
sqlite> INSERT INTO Office VALUES(8,26,'Abay 13');
sqlite> INSERT INTO Office VALUES(9,14,'Mashkhur Jusip 30');
sqlite> INSERT INTO Office VALUES(10,15,'Nazarbayev 111');
sqlite> INSERT INTO Office VALUES(11,32,'Baymagambetov 202');
sqlite> INSERT INTO Office VALUES(12,12,'Ashimov 76');
sqlite> INSERT INTO Office VALUES(13,9,'Satbayev 42');
sqlite> INSERT INTO Office VALUES(14,2,'Abilkhaiyr khan 78');
sqlite> INSERT INTO Office VALUES(15,25,'Isayev 51');
sqlite> INSERT INTO Office VALUES(16,5,'Taimanov 37');
sqlite> INSERT INTO Office VALUES(17,1,'Nazarbayev 21');