#block 5 am (pre-transit)

mset = '15A-043.sb5am.spw2-33'

#field names
target = '3~562'
phscal = '2'
bcal= '1'
fcal = '0'

#-----------------------------
#configuration scan flagging -
#-----------------------------

if flag == 1:
	flagdata(vis = mset+'.ms', scan = '2,5,9,13,15,17,73,75,131,133,189,191,247,249,307,309,311,367,369,425,427,483,485,541,543')

#--------------------------
#post inspection flagging -
#--------------------------

if flag == 2:

#####################################
### group 1 spw2-9 (new spw's 0-7)###
#####################################

#spw 2 (0)

	flagdata(vis = mset+'.ms', spw = '0:0~3', scan = '40')	
	flagdata(vis = mset+'.ms', spw = '0', scan = '18~71', antenna = 'ea04&ea20;ea04&ea13;ea13&ea20')
	flagdata(vis = mset+'.ms', spw = '0:15~15;33~34;43~43', scan = '486~539')
	flagdata(vis = mset+'.ms', spw = '0:43~44', scan = '134~187', antenna = 'ea13&ea20')
	flagdata(vis = mset+'.ms', spw = '0:42~44', scan = '134~188', antenna = 'ea04&ea13')

	flagdata(vis = mset+'.ms', spw = '0:15~15', scan = '540', field = '2')
#	flagdata(vis = mset+'.ms', spw = '0:0~2')
	flagdata(vis = mset+'.ms', spw = '0:55~59', scan = '6,10')
	flagdata(vis = mset+'.ms', spw = '0:53~54', scan = '6', antenna = 'ea08&ea11')
	flagdata(vis = mset+'.ms', spw = '0:53~60', scan = '6,10', antenna = 'ea21&ea22')
	flagdata(vis = mset+'.ms', spw = '0', antenna = 'ea04&ea20')

	flagdata(vis = mset+'.ms', spw = '0:40~55', scan = '134~159', antenna = 'ea04&ea13')
	flagdata(vis = mset+'.ms', spw = '0:40~58', scan = '219~220', antenna = 'ea04&ea13')
	flagdata(vis = mset+'.ms', spw = '0:40~47', scan = '246', antenna = 'ea04&ea13')
#	flagdata(vis = mset+'.ms', spw = '0:', scan = '', antenna = 'ea04&ea13')

	flagdata(vis = mset+'.ms', spw = '0:5~23', scan ='18~71', antenna = 'ea04&ea14')
	flagdata(vis = mset+'.ms', spw = '0', scan = '312~365', antenna = 'ea01&ea27')
	flagdata(vis = mset+'.ms', spw = '0:43~43', scan = '18~71', antenna = 'ea04&ea13')
	flagdata(vis = mset+'.ms', spw = '0', antenna = 'ea20')
#	flagdata(vis = mset+'.ms', mode = 'tfcrop')

#spw 3 (1)

#spw 4 (2)
	flagdata(vis = mset+'.ms', spw = '2:47~55', scan = '33~37', antenna = 'ea03&ea16; ea03&ea24; ea04&ea09; ea04&ea13; ea04&ea14; ea04&ea20; ea04&ea27; ea09&ea11; ea09&ea13; ea09&ea19; ea09&ea20; ea09&ea25; ea09&ea27; ea11&ea13; ea11&ea19; ea11&ea20; ea13&ea20; ea13&ea27; ea14&ea26; ea16&ea25; ea19&ea25; ea19&ea27; ea20&ea27; ea25&ea27')
	flagdata(vis = mset+'.ms', spw = '2:46~47', scan = '33~37', antenna = 'ea09&ea13')
	flagdata(vis = mset+'.ms', spw = '2:42~57', scan = '33~37', antenna = 'ea09&ea20; ea13&ea20')
#spw 5 (3)

#spw 6 (4)

#spw 7 (5)
#	flagdata(vis = mset+'.ms', field = '197~201', scan = '216~220', spw = '5:8~63') #might be a source - create model column while imaging - use clean boxes to mark the bright sources - subtract model from target data in plotms to see which spikes remain
#spw 8 (6)

#spw 9 (7)
#	flagdata(vis = mset+'.ms', field = '2', scan = '130', spw = '7:63~63', antenna = 'ea01&ea27; ea04&ea20; ea13&ea20; ea14&ea20; ea20&ea27')

########################################
### group 2 spw10-17 (new spw's 8-15)###
########################################

#spw 10 (8)
	flagdata(vis = mset+'.ms', field = '0', spw = '8:8~10', antenna = 'ea02&ea16')
	flagdata(vis = mset+'.ms', field = '0~1', spw = '8:6~10', antenna = 'ea02&ea22')
	flagdata(vis = mset+'.ms', field = '2~562', spw = '8:25~26', antenna = '*&ea28')

#spw 11 (9)


	flagdata(vis = mset+'.ms', field = '0~1', spw = '9:4~22', antenna = 'ea02&*')
	flagdata(vis = mset+'.ms', field = '0~1', spw = '9:26~29', antenna = 'ea02&ea07')
	flagdata(vis = mset+'.ms', field = '1', spw = '9:29', antenna = 'ea03&ea07')

	flagdata(vis = mset+'.ms', field = '2', spw = '9:21~22', antenna = '*&ea19')	
	flagdata(vis = mset+'.ms', field = '2', scan = '72', spw = '9:18~19', antenna = '*&ea27')
	flagdata(vis = mset+'.ms', field = '2', scan = '130', spw = '9:18', antenna = '*&ea27')
	flagdata(vis = mset+'.ms', field = '2', scan = '188', spw = '9:17', antenna = '*&ea27')
	flagdata(vis = mset+'.ms', field = '2', scan = '246', spw = '9:16~18', antenna = '*&ea27')
	flagdata(vis = mset+'.ms', field = '2', scan = '304, 308', spw = '9:15~16', antenna = '*&ea27')
	flagdata(vis = mset+'.ms', field = '2', scan = '366', spw = '9:11~14', antenna = '*&ea27')
	flagdata(vis = mset+'.ms', field = '2', scan = '424', spw = '9:10~11', antenna = '*&ea27')
	flagdata(vis = mset+'.ms', field = '2', scan = '482', spw = '9:8~11', antenna = '*&ea27')
	flagdata(vis = mset+'.ms', field = '2', scan = '540', spw = '9:8~9', antenna = '*&ea27')
	flagdata(vis = mset+'.ms', field = '2', scan = '598', spw = '9:7~9', antenna = '*&ea27')

	flagdata(vis = mset+'.ms', field = '3~562', spw = '9', antenna = '*&ea27')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '9:20~22', antenna = 'ea19')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '9:38', antenna = 'ea12')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '9:60', antenna = 'ea18')
#spw 12 (10)
	flagdata(vis = mset+'.ms', field = '0~1', spw = '10:38', antenna = 'ea12&ea19')

	flagdata(vis = mset+'.ms', field = '2', spw = '10:0', antenna = '*&ea25')
	flagdata(vis = mset+'.ms', field = '2', spw = '10:3~4;16~18', antenna = 'ea13')
	flagdata(vis = mset+'.ms', field = '2', spw = '10:10~11', antenna = '*&ea20')
	flagdata(vis = mset+'.ms', field = '2', spw = '10:13~14', antenna = 'ea07')
	flagdata(vis = mset+'.ms', field = '2', spw = '10:17', antenna = '*&ea22')
	flagdata(vis = mset+'.ms', field = '2', spw = '10:23~25', antenna = 'ea06')
	flagdata(vis = mset+'.ms', field = '2', spw = '10:37~39', antenna = '*&ea19')
	flagdata(vis = mset+'.ms', field = '2', spw = '10:38~39', antenna = 'ea11; ea12')
	flagdata(vis = mset+'.ms', field = '2', spw = '10:46~47', antenna = '*&ea22')
	flagdata(vis = mset+'.ms', field = '2', spw = '10:47', antenna = 'ea23')
	flagdata(vis = mset+'.ms', field = '2', spw = '10:58', antenna = 'ea04')
	
	flagdata(vis = mset+'.ms', field = '3~562', spw = '10:38', antenna = 'ea12&ea19')
	
#spw 13 (11)
	flagdata(vis = mset+'.ms', field = '0', spw = '11:36', antenna = 'ea01&ea02; ea01&ea09')

	flagdata(vis = mset+'.ms', field = '1', spw = '11:35~36', antenna = 'ea01&ea14; ea01&ea27')
	flagdata(vis = mset+'.ms', field = '1', spw = '11:36', antenna = 'ea01&ea04; ea01&ea05; ea01&ea13; ea01&ea23; ea02&ea08')
	flagdata(vis = mset+'.ms', field = '1', spw = '11:52', antenna = 'ea16&ea25')


	flagdata(vis = mset+'.ms', field = '2', spw = '11:0', antenna = 'ea18')
	flagdata(vis = mset+'.ms', field = '2', spw = '11:26~50', antenna = 'ea01')# 'ea01&ea04; ea01&ea27')
	flagdata(vis = mset+'.ms', field = '2', spw = '11:36', antenna = 'ea20')
#	flagdata(vis = mset+'.ms', field = '2', spw = '11:35~37', antenna = 'ea01&ea02')
	flagdata(vis = mset+'.ms', field = '2', scan = '540', spw = '11:51', antenna = 'ea16&ea25')
	flagdata(vis = mset+'.ms', field = '2', spw = '11:52', antenna = 'ea16')
	flagdata(vis = mset+'.ms', field = '2', spw = '11:50~55', antenna = 'ea04&ea16; ea16&ea20; ea16&ea27')
	
	flagdata(vis = mset+'.ms', field = '541~562', spw = '11:32', antenna = 'ea01&ea27')
	flagdata(vis = mset+'.ms', field = '91~562', scan = '106~597', spw = '11:33', antenna = 'ea01&ea27')
	flagdata(vis = mset+'.ms', field = '120~562', spw = '11:34', antenna = 'ea01&ea27')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '11:35~36', antenna = 'ea01&*')
	flagdata(vis = mset+'.ms', field = '539~562', spw = '11:37', antenna = 'ea01&ea04')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '11:37~40', antenna = 'ea01&ea27')
	flagdata(vis = mset+'.ms', field = '550~562', spw = '11:41', antenna = 'ea01&ea27')
	flagdata(vis = mset+'.ms', field = '397~562', spw = '11:52', antenna = 'ea16&ea25')
	flagdata(vis = mset+'.ms', field = '285~334', spw = '11:52', antenna = 'ea16&ea27')


	
#spw 14 (12)
	flagdata(vis = mset+'.ms', field = '0', spw = '12:26', antenna = 'ea19')

	flagdata(vis = mset+'.ms', field = '1', spw = '12:25~26', antenna = 'ea09&ea19; ea11&ea19; ea13&ea19; ea19&ea22; ea19&ea25')
	flagdata(vis = mset+'.ms', field = '1', spw = '12:56', antenna = 'ea18')

	flagdata(vis = mset+'.ms', field = '2', spw = '12:25~26', antenna = 'ea19')
	flagdata(vis = mset+'.ms', field = '2', spw = '12:24~28', antenna = 'ea11&ea19')
	flagdata(vis = mset+'.ms', field = '2', spw = '12:56', antenna = 'ea18')
	flagdata(vis = mset+'.ms', field = '2', scan = '598', spw = '12:55;57', antenna = 'ea18&ea24')

	flagdata(vis = mset+'.ms', field = '3~562', spw = '12:25~26', antenna = 'ea19')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '12:56', antenna = 'ea18')
#spw 15 (13)
#spw 16 (14)
#	flagdata(vis = mset+'.ms', field = '0~2', spw = '14:
	flagdata(vis = mset+'.ms', field = '1', spw = '14:16~19', antenna = 'ea13&ea27')	
	flagdata(vis = mset+'.ms', field = '1', spw = '14:36', antenna = 'ea13&ea25')
	flagdata(vis = mset+'.ms', field = '2~562', spw = '14:12', antenna = 'ea19')
#spw 17 (15)
#	flagdata(vis = mset+'.ms', field = '3~562', spw = '15:59~63


#########################################
### group 3 spw18-25 (new spw's 16-23)###
#########################################

#spw 18 (16)

#spw 19 (17)
	

#spw 20 (18)
	flagdata(vis = mset+'.ms', field = '0~1', spw = '18:56~58', antenna = 'ea13&ea25')
	flagdata(vis = mset+'.ms', field = '0~1', spw = '18:10~13', antenna = 'ea13&ea22; ea11&ea22; ea11&ea23')
	flagdata(vis = mset+'.ms', field = '0~1', spw = '18:9~14', antenna = 'ea13&ea22; ea11&ea22')
	
#spw 21 (19)
	flagdata(vis = mset+'.ms', field = '0', spw = '19:29~32', antenna = 'ea11&ea23')
	flagdata(vis = mset+'.ms', field = '0~1', spw = '19:6~8', antenna = 'ea23')
	flagdata(vis = mset+'.ms', field = '341~506', spw = '19:56~58', antenna = 'ea27')
	flagdata(vis = mset+'.ms', field = '509~562', spw = '19:55~58', antenna = 'ea27')
	
#spw 22 (20)
	flagdata(vis = mset+'.ms', field = '0~1', spw = '20:47~51;55~60', antenna = 'ea22')
	flagdata(vis = mset+'.ms', field = '0~1', spw = '20:57~59', antenna = 'ea13&ea15')
#spw 23 (21)
	flagdata(vis = mset+'.ms', field = '0', spw = '21:56~58', antenna = 'ea05')
	flagdata(vis = mset+'.ms', field = '1', spw = '21:55~58', antenna = 'ea25')
	flagdata(vis = mset+'.ms', field = '2', spw = '21:32', antenna = 'ea11')
#spw 24 (22)

#spw 25 (23)
	flagdata(vis = mset+'.ms', field = '0', spw = '23:5~10', antenna = 'ea02&ea22')
	flagdata(vis = mset+'.ms', field = '1', spw = '23:6~8', antenna = 'ea22')
	flagdata(vis = mset+'.ms', field = '1', spw = '23:41~44', antenna = 'ea22&ea25')
	flagdata(vis = mset+'.ms', field = '1~2', spw = '23:25~26', antenna = 'ea27')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '23:24~27', antenna = 'ea27')
#########################################
### group 4 spw26-33 (new spw's 24-31)###
#########################################

#spw 26 (24)
	flagdata(vis = mset+'.ms', field = '2', spw = '24:40~42', antenna = 'ea28')

	flagdata(vis = mset+'.ms', field = '453~506', scan = '486~539', spw = '24:39', antenna = 'ea28')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '24:40~43', antenna = 'ea28')
#spw 27 (25)
	flagdata(vis = mset+'.ms', field = '2', spw = '25:36~37', antenna = 'ea26')
	flagdata(vis = mset+'.ms', field = '2', spw = '25:49~51', antenna = 'ea20')
	flagdata(vis = mset+'.ms', field = '2', spw = '25:59', antenna = 'ea07&ea08')

	flagdata(vis = mset+'.ms', field = '3~562', spw = '25:36~37', antenna = 'ea26')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '25:49~51', antenna = 'ea20')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '25:54', antenna = 'ea02;ea14')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '25:59', antenna = 'ea08')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '25:59~60', antenna = 'ea07')

	flagdata(vis = mset+'.ms', field = '3~562', spw = '25:59', antenna = 'ea08')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '25:59~60', antenna = 'ea07')

#spw 28 (26)
	flagdata(vis = mset+'.ms', field = '0~1', scan = '6,10', spw = '26:30', antenna = 'ea19&ea22')
	flagdata(vis = mset+'.ms', field = '0', scan = '6', spw = '26:48~49', antenna = 'ea16')
	flagdata(vis = mset+'.ms', field = '1', scan = '10', spw = '26:48', antenna = 'ea02&ea16')
	flagdata(vis = mset+'.ms', field = '1', scan = '10', spw = '26:49', antenna = 'ea02&ea16; ea15&ea16; ea16&ea23')
	flagdata(vis = mset+'.ms', field = '1', scan = '10', spw = '26:59~60', antenna = 'ea19&ea25')
	flagdata(vis = mset+'.ms', field = '1', scan = '10', spw = '26:62', antenna = 'ea09&ea19;ea14&ea19')

	flagdata(vis = mset+'.ms', field = '2', spw = '26:31', antenna = 'ea05')	
	flagdata(vis = mset+'.ms', field = '2', spw = '26:24~25', antenna = 'ea10')
	flagdata(vis = mset+'.ms', field = '2', spw = '26:29~30', antenna = 'ea19')
	flagdata(vis = mset+'.ms', field = '2', spw = '26:30~31', antenna = 'ea22')
	flagdata(vis = mset+'.ms', field = '2', spw = '26:40', antenna = 'ea03&ea27')
	flagdata(vis = mset+'.ms', field = '2', spw = '26:42', antenna = 'ea26')
	flagdata(vis = mset+'.ms', field = '2', spw = '26:48~49', antenna = 'ea16')
	flagdata(vis = mset+'.ms', field = '2', spw = '26:59', antenna = 'ea01')
	flagdata(vis = mset+'.ms', field = '2', spw = '26:60', antenna = 'ea25')

	flagdata(vis = mset+'.ms', field = '3~562', spw = '26:39~40', antenna = 'ea27')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '26:29~31', antenna = 'ea19;ea22')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '26:40~41', antenna = 'ea03')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '26:42~43', antenna = 'ea26')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '26:48~49', antenna = 'ea16')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '26:54', antenna = 'ea18')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '26:58~59', antenna = 'ea01')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '26:60', antenna = 'ea25')
#spw 29 (27)
	flagdata(vis = mset+'.ms', field = '0', scan = '6', spw = '27:16~17', antenna = 'ea11&ea26')
	flagdata(vis = mset+'.ms', field = '0', scan = '6', spw = '27:19~20', antenna = 'ea14&ea26')

	flagdata(vis = mset+'.ms', field = '1', scan = '10', spw = '27:47', antenna = 'ea04&ea19')
	flagdata(vis = mset+'.ms', field = '1', scan = '10', spw = '27:62', antenna = 'ea01&ea19; ea04&ea19; ea06&ea19; ea09&ea19')

	flagdata(vis = mset+'.ms', field = '2', spw = '27:9~10', antenna = 'ea24')
	flagdata(vis = mset+'.ms', field = '2', spw = '27:13~14', antenna = 'ea22')
	flagdata(vis = mset+'.ms', field = '2', spw = '27:16~17', antenna = 'ea11')
	flagdata(vis = mset+'.ms', field = '2', spw = '27:20~21', antenna = 'ea14')
	flagdata(vis = mset+'.ms', field = '2', spw = '27:46~47', antenna = 'ea04')

	flagdata(vis = mset+'.ms', field = '3~562', spw = '27:13~14', antenna = 'ea22')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '27:46~47', antenna = 'ea04')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '27:16~18', antenna = 'ea11')
	flagdata(vis = mset+'.ms', field = '5~57', scan = '18~70', spw = '27:19', antenna = 'ea14')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '27:20~21', antenna = 'ea14')
#spw 30 (28)
	flagdata(vis = mset+'.ms', field = '2', spw = '28:9~10', antenna = 'ea01')
	flagdata(vis = mset+'.ms', field = '2', spw = '28:19~20', antenna = 'ea04')

	flagdata(vis = mset+'.ms', field = '3~562', spw = '28:8~10', antenna = 'ea01')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '28:20', antenna = 'ea04')
#spw 31 (29)
	flagdata(vis = mset+'.ms', field = '0', scan = '6', spw = '29:11~13', antenna = 'ea11&ea26')

	flagdata(vis = mset+'.ms', field = '2', spw = '29:12~13', antenna = 'ea11')
	flagdata(vis = mset+'.ms', field = '2', spw = '29:39~40', antenna = 'ea08')

	flagdata(vis = mset+'.ms', field = '3~562', spw = '29:12~13', antenna = 'ea11')
	flagdata(vis = mset+'.ms', field = '3~562', spw = '29:40', antenna = 'ea08')
#spw 32 (30)

#spw 33 (31)
	flagdata(vis = mset+'.ms', field = '3~562', spw = '31:4~11;59~63')


