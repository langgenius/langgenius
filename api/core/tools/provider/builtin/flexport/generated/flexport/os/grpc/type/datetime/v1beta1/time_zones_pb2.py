# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flexport/os/grpc/type/datetime/v1beta1/time_zones.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n7flexport/os/grpc/type/datetime/v1beta1/time_zones.proto\x12&flexport.os.grpc.type.datetime.v1beta1"\x8e\x01\n\x08TimeZone\x12>\n\x04iana\x18\x01 \x01(\x0e\x32..flexport.os.grpc.type.datetime.v1beta1.TzIanaH\x00\x12<\n\x03utc\x18\x02 \x01(\x0e\x32-.flexport.os.grpc.type.datetime.v1beta1.TzUtcH\x00\x42\x04\n\x02\x62y*\x8a\x92\x01\n\x06TzIana\x12\x13\n\x0fTZ_IANA_INVALID\x10\x00\x12\x10\n\x0bTZ_IANA_UTC\x10\xe7\x07\x12\x1c\n\x18TZ_IANA_AFRICA_0_ABIDJAN\x10\x01\x12\x1a\n\x16TZ_IANA_AFRICA_0_ACCRA\x10\x02\x12 \n\x1cTZ_IANA_AFRICA_0_ADDIS_ABABA\x10\x03\x12\x1c\n\x18TZ_IANA_AFRICA_0_ALGIERS\x10\x04\x12\x1b\n\x17TZ_IANA_AFRICA_0_ASMARA\x10\x05\x12\x1b\n\x17TZ_IANA_AFRICA_0_ASMERA\x10\x06\x12\x1b\n\x17TZ_IANA_AFRICA_0_BAMAKO\x10\x07\x12\x1b\n\x17TZ_IANA_AFRICA_0_BANGUI\x10\x08\x12\x1b\n\x17TZ_IANA_AFRICA_0_BANJUL\x10\t\x12\x1b\n\x17TZ_IANA_AFRICA_0_BISSAU\x10\n\x12\x1c\n\x18TZ_IANA_AFRICA_0_BLATYRE\x10\x0b\x12 \n\x1cTZ_IANA_AFRICA_0_BRAZZAVILLE\x10\x0c\x12\x1e\n\x1aTZ_IANA_AFRICA_0_BUJUMBURA\x10\r\x12\x1a\n\x16TZ_IANA_AFRICA_0_CAIRO\x10\x0e\x12\x1f\n\x1bTZ_IANA_AFRICA_0_CASABLANCA\x10\x0f\x12\x1a\n\x16TZ_IANA_AFRICA_0_CEUTA\x10\x10\x12\x1c\n\x18TZ_IANA_AFRICA_0_CONAKRY\x10\x11\x12\x1a\n\x16TZ_IANA_AFRICA_0_DAKAR\x10\x12\x12"\n\x1eTZ_IANA_AFRICA_0_DAR_ES_SALAAM\x10\x13\x12\x1d\n\x19TZ_IANA_AFRICA_0_DJIBOUTI\x10\x14\x12\x1b\n\x17TZ_IANA_AFRICA_0_DOUALA\x10\x15\x12\x1d\n\x19TZ_IANA_AFRICA_0_EL_AAIUN\x10\x16\x12\x1d\n\x19TZ_IANA_AFRICA_0_FREETOWN\x10\x17\x12\x1d\n\x19TZ_IANA_AFRICA_0_GABORONE\x10\x18\x12\x1b\n\x17TZ_IANA_AFRICA_0_HARARE\x10\x19\x12!\n\x1dTZ_IANA_AFRICA_0_JOHANNESBURG\x10\x1a\x12\x19\n\x15TZ_IANA_AFRICA_0_JUBA\x10\x1b\x12\x1c\n\x18TZ_IANA_AFRICA_0_KAMPALA\x10\x1c\x12\x1d\n\x19TZ_IANA_AFRICA_0_KHARTOUM\x10\x1d\x12\x1b\n\x17TZ_IANA_AFRICA_0_KIGALI\x10\x1e\x12\x1d\n\x19TZ_IANA_AFRICA_0_KINSHASA\x10\x1f\x12\x1a\n\x16TZ_IANA_AFRICA_0_LAGOS\x10 \x12\x1f\n\x1bTZ_IANA_AFRICA_0_LIBERVILLE\x10!\x12\x19\n\x15TZ_IANA_AFRICA_0_LOME\x10"\x12\x1b\n\x17TZ_IANA_AFRICA_0_LUANDA\x10#\x12\x1f\n\x1bTZ_IANA_AFRICA_0_LUBUMBASHI\x10$\x12\x1b\n\x17TZ_IANA_AFRICA_0_LUSAKA\x10%\x12\x1b\n\x17TZ_IANA_AFRICA_0_MALABO\x10&\x12\x1b\n\x17TZ_IANA_AFRICA_0_MAPUTO\x10\'\x12\x1b\n\x17TZ_IANA_AFRICA_0_MASERU\x10(\x12\x1c\n\x18TZ_IANA_AFRICA_0_MBABANE\x10)\x12\x1e\n\x1aTZ_IANA_AFRICA_0_MOGADISHU\x10*\x12\x1d\n\x19TZ_IANA_AFRICA_0_MONROVIA\x10+\x12\x1c\n\x18TZ_IANA_AFRICA_0_NAIROBI\x10,\x12\x1d\n\x19TZ_IANA_AFRICA_0_NDJAMENA\x10-\x12\x1b\n\x17TZ_IANA_AFRICA_0_NIAMEY\x10.\x12\x1f\n\x1bTZ_IANA_AFRICA_0_NOUAKCHOTT\x10/\x12 \n\x1cTZ_IANA_AFRICA_0_OUAGADOUGOU\x10\x30\x12\x1f\n\x1bTZ_IANA_AFRICA_0_PORTO_NOVO\x10\x31\x12\x1d\n\x19TZ_IANA_AFRICA_0_SAO_TOME\x10\x32\x12\x1d\n\x19TZ_IANA_AFRICA_0_TIMBUKTU\x10\x33\x12\x1c\n\x18TZ_IANA_AFRICA_0_TRIPOLI\x10\x34\x12\x1a\n\x16TZ_IANA_AFRICA_0_TUNIS\x10\x35\x12\x1d\n\x19TZ_IANA_AFRICA_0_WINDHOEK\x10\x36\x12\x1a\n\x16TZ_IANA_AMERICA_0_ADAK\x10\x37\x12\x1f\n\x1bTZ_IANA_AMERICA_0_ANCHORAGE\x10\x38\x12\x1e\n\x1aTZ_IANA_AMERICA_0_ANGUILLA\x10\x39\x12\x1d\n\x19TZ_IANA_AMERICA_0_ANTIGUA\x10:\x12\x1f\n\x1bTZ_IANA_AMERICA_0_ARAGUAINA\x10;\x12.\n*TZ_IANA_AMERICA_0_ARGENTINA_0_BUENOS_AIRES\x10<\x12+\n\'TZ_IANA_AMERICA_0_ARGENTINA_0_CATAMARCA\x10=\x12\x30\n,TZ_IANA_AMERICA_0_ARGENTINA_0_COMODRIVADAVIA\x10>\x12)\n%TZ_IANA_AMERICA_0_ARGENTINA_0_CORDOBA\x10?\x12\'\n#TZ_IANA_AMERICA_0_ARGENTINA_0_JUJUY\x10@\x12*\n&TZ_IANA_AMERICA_0_ARGENTINA_0_LA_RIOJA\x10\x41\x12)\n%TZ_IANA_AMERICA_0_ARGENTINA_0_MENDOZA\x10\x42\x12.\n*TZ_IANA_AMERICA_0_ARGENTINA_0_RIO_GALLEGOS\x10\x43\x12\'\n#TZ_IANA_AMERICA_0_ARGENTINA_0_SALTA\x10\x44\x12*\n&TZ_IANA_AMERICA_0_ARGENTINA_0_SAN_JUAN\x10\x45\x12*\n&TZ_IANA_AMERICA_0_ARGENTINA_0_SAN_LUIS\x10\x46\x12)\n%TZ_IANA_AMERICA_0_ARGENTINA_0_TUCUMAN\x10G\x12)\n%TZ_IANA_AMERICA_0_ARGENTINA_0_USHUAIA\x10H\x12\x1b\n\x17TZ_IANA_AMERICA_0_ARUBA\x10I\x12\x1e\n\x1aTZ_IANA_AMERICA_0_ASUNCION\x10J\x12\x1e\n\x1aTZ_IANA_AMERICA_0_ATIKOKAN\x10K\x12\x1a\n\x16TZ_IANA_AMERICA_0_ATKA\x10L\x12\x1b\n\x17TZ_IANA_AMERICA_0_BAHIA\x10M\x12$\n TZ_IANA_AMERICA_0_BAHIA_BANDERAS\x10N\x12\x1e\n\x1aTZ_IANA_AMERICA_0_BARBADOS\x10O\x12\x1b\n\x17TZ_IANA_AMERICA_0_BELEM\x10P\x12\x1c\n\x18TZ_IANA_AMERICA_0_BELIZE\x10Q\x12"\n\x1eTZ_IANA_AMERICA_0_BLANC_SABLON\x10R\x12\x1f\n\x1bTZ_IANA_AMERICA_0_BOA_VISTA\x10S\x12\x1c\n\x18TZ_IANA_AMERICA_0_BOGOTA\x10T\x12\x1b\n\x17TZ_IANA_AMERICA_0_BOISE\x10U\x12"\n\x1eTZ_IANA_AMERICA_0_BUENOS_AIRES\x10V\x12#\n\x1fTZ_IANA_AMERICA_0_CAMBRIDGE_BAY\x10W\x12"\n\x1eTZ_IANA_AMERICA_0_CAMPO_GRANDE\x10X\x12\x1c\n\x18TZ_IANA_AMERICA_0_CANCUN\x10Y\x12\x1d\n\x19TZ_IANA_AMERICA_0_CARACAS\x10Z\x12\x1f\n\x1bTZ_IANA_AMERICA_0_CATAMARCA\x10[\x12\x1d\n\x19TZ_IANA_AMERICA_0_CAYENNE\x10\\\x12\x1c\n\x18TZ_IANA_AMERICA_0_CAYMAN\x10]\x12\x1d\n\x19TZ_IANA_AMERICA_0_CHICAGO\x10^\x12\x1f\n\x1bTZ_IANA_AMERICA_0_CHIHUAHUA\x10_\x12#\n\x1fTZ_IANA_AMERICA_0_CORAL_HARBOUR\x10`\x12\x1d\n\x19TZ_IANA_AMERICA_0_CORDOBA\x10\x61\x12 \n\x1cTZ_IANA_AMERICA_0_COSTA_RICA\x10\x62\x12\x1d\n\x19TZ_IANA_AMERICA_0_CRESTON\x10\x63\x12\x1c\n\x18TZ_IANA_AMERICA_0_CUIABA\x10\x64\x12\x1d\n\x19TZ_IANA_AMERICA_0_CURACAO\x10\x65\x12"\n\x1eTZ_IANA_AMERICA_0_DANMARKSHAVN\x10\x66\x12\x1c\n\x18TZ_IANA_AMERICA_0_DAWSON\x10g\x12"\n\x1eTZ_IANA_AMERICA_0_DAWSON_CREEK\x10h\x12\x1c\n\x18TZ_IANA_AMERICA_0_DENVER\x10i\x12\x1d\n\x19TZ_IANA_AMERICA_0_DETROIT\x10j\x12\x1e\n\x1aTZ_IANA_AMERICA_0_DOMINICA\x10k\x12\x1e\n\x1aTZ_IANA_AMERICA_0_EDMONTON\x10l\x12\x1e\n\x1aTZ_IANA_AMERICA_0_EIRUNEPE\x10m\x12!\n\x1dTZ_IANA_AMERICA_0_EL_SALVADOR\x10n\x12\x1e\n\x1aTZ_IANA_AMERICA_0_ENSENADA\x10o\x12!\n\x1dTZ_IANA_AMERICA_0_FORT_NELSON\x10p\x12 \n\x1cTZ_IANA_AMERICA_0_FORT_WAYNE\x10q\x12\x1f\n\x1bTZ_IANA_AMERICA_0_FORTALEZA\x10r\x12\x1f\n\x1bTZ_IANA_AMERICA_0_GLACE_BAY\x10s\x12\x1d\n\x19TZ_IANA_AMERICA_0_GODTHAB\x10t\x12\x1f\n\x1bTZ_IANA_AMERICA_0_GOOSE_BAY\x10u\x12 \n\x1cTZ_IANA_AMERICA_0_GRAND_TURK\x10v\x12\x1d\n\x19TZ_IANA_AMERICA_0_GRENADA\x10w\x12 \n\x1cTZ_IANA_AMERICA_0_GUADELOUPE\x10x\x12\x1f\n\x1bTZ_IANA_AMERICA_0_GUATEMALA\x10y\x12\x1f\n\x1bTZ_IANA_AMERICA_0_GUAYAQUIL\x10z\x12\x1c\n\x18TZ_IANA_AMERICA_0_GUYANA\x10{\x12\x1d\n\x19TZ_IANA_AMERICA_0_HALIFAX\x10|\x12\x1c\n\x18TZ_IANA_AMERICA_0_HAVANA\x10}\x12 \n\x1cTZ_IANA_AMERICA_0_HERMOSILLO\x10~\x12,\n(TZ_IANA_AMERICA_0_INDIANA_0_INDIANAPOLIS\x10\x7f\x12%\n TZ_IANA_AMERICA_0_INDIANA_0_KNOX\x10\x80\x01\x12(\n#TZ_IANA_AMERICA_0_INDIANA_0_MARENGO\x10\x81\x01\x12+\n&TZ_IANA_AMERICA_0_INDIANA_0_PETERSBURG\x10\x82\x01\x12*\n%TZ_IANA_AMERICA_0_INDIANA_0_TELL_CITY\x10\x83\x01\x12&\n!TZ_IANA_AMERICA_0_INDIANA_0_VEVAY\x10\x84\x01\x12*\n%TZ_IANA_AMERICA_0_INDIANA_0_VINCENNES\x10\x85\x01\x12(\n#TZ_IANA_AMERICA_0_INDIANA_0_WINAMAC\x10\x86\x01\x12#\n\x1eTZ_IANA_AMERICA_0_INDIANAPOLIS\x10\x87\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_INUVIK\x10\x88\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_IQALUIT\x10\x89\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_JAMAICA\x10\x8a\x01\x12\x1c\n\x17TZ_IANA_AMERICA_0_JUJUY\x10\x8b\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_JUNEAU\x10\x8c\x01\x12,\n\'TZ_IANA_AMERICA_0_KENTUCKY_0_LOUISVILLE\x10\x8d\x01\x12,\n\'TZ_IANA_AMERICA_0_KENTUCKY_0_MONTICELLO\x10\x8e\x01\x12#\n\x1eTZ_IANA_AMERICA_0_INDIANA_KNOX\x10\x8f\x01\x12"\n\x1dTZ_IANA_AMERICA_0_KRALENDIIJK\x10\x90\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_LA_PAZ\x10\x91\x01\x12\x1b\n\x16TZ_IANA_AMERICA_0_LIMA\x10\x92\x01\x12"\n\x1dTZ_IANA_AMERICA_0_LOS_ANGELES\x10\x93\x01\x12!\n\x1cTZ_IANA_AMERICA_0_LOUISVILLE\x10\x94\x01\x12%\n TZ_IANA_AMERICA_0_LOWER_PRINCESS\x10\x95\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_MACEIO\x10\x96\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_MANAGUA\x10\x97\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_MANAUS\x10\x98\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_MARIGOT\x10\x99\x01\x12!\n\x1cTZ_IANA_AMERICA_0_MARTINIQUE\x10\x9a\x01\x12 \n\x1bTZ_IANA_AMERICA_0_MATAMOROS\x10\x9b\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_MAZATLAN\x10\x9c\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_MENDOZA\x10\x9d\x01\x12 \n\x1bTZ_IANA_AMERICA_0_MENOMINEE\x10\x9e\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_MERIDA\x10\x9f\x01\x12!\n\x1cTZ_IANA_AMERICA_0_METLAKATLA\x10\xa0\x01\x12"\n\x1dTZ_IANA_AMERICA_0_MEXICO_CITY\x10\xa1\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_MIQUELON\x10\xa2\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_MONCTON\x10\xa3\x01\x12 \n\x1bTZ_IANA_AMERICA_0_MONTERREY\x10\xa4\x01\x12!\n\x1cTZ_IANA_AMERICA_0_MONTEVIDEO\x10\xa5\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_MONTREAL\x10\xa6\x01\x12!\n\x1cTZ_IANA_AMERICA_0_MONTSERRAT\x10\xa7\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_NASSAU\x10\xa8\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_NEW_YORK\x10\xa9\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_NIPIGON\x10\xaa\x01\x12\x1b\n\x16TZ_IANA_AMERICA_0_NOME\x10\xab\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_NORONHA\x10\xac\x01\x12,\n\'TZ_IANA_AMERICA_0_NORTH_DAKOTA_0_BEULAH\x10\xad\x01\x12,\n\'TZ_IANA_AMERICA_0_NORTH_DAKOTA_0_CENTER\x10\xae\x01\x12/\n*TZ_IANA_AMERICA_0_NORTH_DAKOTA_0_NEW_SALEM\x10\xaf\x01\x12\x1b\n\x16TZ_IANA_AMERICA_0_NUUK\x10\xb0\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_OJINAGA\x10\xb1\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_PANAMA\x10\xb2\x01\x12"\n\x1dTZ_IANA_AMERICA_0_PANGNIRTUNG\x10\xb3\x01\x12!\n\x1cTZ_IANA_AMERICA_0_PARAMARIBO\x10\xb4\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_PHOENIX\x10\xb5\x01\x12%\n TZ_IANA_AMERICA_0_PORT_AU_PRINCE\x10\xb6\x01\x12$\n\x1fTZ_IANA_AMERICA_0_PORT_OF_SPAIN\x10\xb7\x01\x12!\n\x1cTZ_IANA_AMERICA_0_PORTO_ACRE\x10\xb8\x01\x12"\n\x1dTZ_IANA_AMERICA_0_PORTO_VELHO\x10\xb9\x01\x12"\n\x1dTZ_IANA_AMERICA_0_PUERTO_RICO\x10\xba\x01\x12#\n\x1eTZ_IANA_AMERICA_0_PUNTA_ARENAS\x10\xbb\x01\x12"\n\x1dTZ_IANA_AMERICA_0_RAINY_RIVER\x10\xbc\x01\x12#\n\x1eTZ_IANA_AMERICA_0_RANKIN_INLET\x10\xbd\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_RECIFE\x10\xbe\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_REGINA\x10\xbf\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_RESOLUTE\x10\xc0\x01\x12!\n\x1cTZ_IANA_AMERICA_0_RIO_BRANCO\x10\xc1\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_ROSARIO\x10\xc2\x01\x12#\n\x1eTZ_IANA_AMERICA_0_SANTA_ISABEL\x10\xc3\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_SANTAREM\x10\xc4\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_SANTIAGO\x10\xc5\x01\x12$\n\x1fTZ_IANA_AMERICA_0_SANTO_DOMINGO\x10\xc6\x01\x12 \n\x1bTZ_IANA_AMERICA_0_SAO_PAULO\x10\xc7\x01\x12#\n\x1eTZ_IANA_AMERICA_0_SCORESBYSUND\x10\xc8\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_SHIPROCK\x10\xc9\x01\x12\x1c\n\x17TZ_IANA_AMERICA_0_SITKA\x10\xca\x01\x12#\n\x1eTZ_IANA_AMERICA_0_ST_BARHELEMY\x10\xcb\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_ST_JOHNS\x10\xcc\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_ST_KITTS\x10\xcd\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_ST_LUCIA\x10\xce\x01\x12 \n\x1bTZ_IANA_AMERICA_0_ST_THOMAS\x10\xcf\x01\x12!\n\x1cTZ_IANA_AMERICA_0_ST_VINCENT\x10\xd0\x01\x12$\n\x1fTZ_IANA_AMERICA_0_SWIFT_CURRENT\x10\xd1\x01\x12"\n\x1dTZ_IANA_AMERICA_0_TEGUCIGALPA\x10\xd2\x01\x12\x1c\n\x17TZ_IANA_AMERICA_0_THULE\x10\xd3\x01\x12"\n\x1dTZ_IANA_AMERICA_0_THUNDER_BAY\x10\xd4\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_TIJUANA\x10\xd5\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_TORONTO\x10\xd6\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_TORTOLA\x10\xd7\x01\x12 \n\x1bTZ_IANA_AMERICA_0_VANCOUVER\x10\xd8\x01\x12\x1d\n\x18TZ_IANA_AMERICA_0_VIRGIN\x10\xd9\x01\x12!\n\x1cTZ_IANA_AMERICA_0_WHITEHORSE\x10\xda\x01\x12\x1f\n\x1aTZ_IANA_AMERICA_0_WINNIPEG\x10\xdb\x01\x12\x1e\n\x19TZ_IANA_AMERICA_0_YAKUTAT\x10\xdc\x01\x12"\n\x1dTZ_IANA_AMERICA_0_YELLOWKNIFE\x10\xdd\x01\x12\x1f\n\x1aTZ_IANA_ANTARCTICA_0_CASEY\x10\xde\x01\x12\x1f\n\x1aTZ_IANA_ANTARCTICA_0_DAVIS\x10\xdf\x01\x12(\n#TZ_IANA_ANTARCTICA_0_DUMONTDURVILLE\x10\xe0\x01\x12#\n\x1eTZ_IANA_ANTARCTICA_0_MACQUARIE\x10\xe1\x01\x12 \n\x1bTZ_IANA_ANTARCTICA_0_MAWSON\x10\xe2\x01\x12\x1e\n\x19TZ_IANA_PACIFIC_0_MCMURDO\x10\xe3\x01\x12 \n\x1bTZ_IANA_ANTARCTICA_0_PALMER\x10\xe4\x01\x12!\n\x1cTZ_IANA_ANTARCTICA_0_ROTHERA\x10\xe5\x01\x12!\n\x1cTZ_IANA_PACIFIC_0_SOUTH_POLE\x10\xe6\x01\x12\x1f\n\x1aTZ_IANA_ANTARCTICA_0_SYOWA\x10\xe7\x01\x12\x1f\n\x1aTZ_IANA_ANTARCTICA_0_TROLL\x10\xe8\x01\x12 \n\x1bTZ_IANA_ANTARCTICA_0_VOSTOK\x10\xe9\x01\x12"\n\x1dTZ_IANA_ARCTIC_0_LONGYEARBYEN\x10\xea\x01\x12\x18\n\x13TZ_IANA_ASIA_0_ADEN\x10\xeb\x01\x12\x1a\n\x15TZ_IANA_ASIA_0_ALMATY\x10\xec\x01\x12\x19\n\x14TZ_IANA_ASIA_0_AMMAN\x10\xed\x01\x12\x1a\n\x15TZ_IANA_ASIA_0_ANADYR\x10\xee\x01\x12\x19\n\x14TZ_IANA_ASIA_0_AQTAU\x10\xef\x01\x12\x1a\n\x15TZ_IANA_ASIA_0_AQTOBE\x10\xf0\x01\x12\x1c\n\x17TZ_IANA_ASIA_0_ASHGABAT\x10\xf1\x01\x12\x1d\n\x18TZ_IANA_ASIA_0_ASHKHABAD\x10\xf2\x01\x12\x1a\n\x15TZ_IANA_ASIA_0_ATYRAU\x10\xf3\x01\x12\x1b\n\x16TZ_IANA_ASIA_0_BAGHDAD\x10\xf4\x01\x12\x1b\n\x16TZ_IANA_ASIA_0_BAHRAIN\x10\xf5\x01\x12\x18\n\x13TZ_IANA_ASIA_0_BAKU\x10\xf6\x01\x12\x1b\n\x16TZ_IANA_ASIA_0_BANGKOK\x10\xf7\x01\x12\x1b\n\x16TZ_IANA_ASIA_0_BARNAUL\x10\xf8\x01\x12\x1a\n\x15TZ_IANA_ASIA_0_BEIRUT\x10\xf9\x01\x12\x1b\n\x16TZ_IANA_ASIA_0_BISHKEK\x10\xfa\x01\x12\x1a\n\x15TZ_IANA_ASIA_0_BRUNEI\x10\xfb\x01\x12\x1c\n\x17TZ_IANA_ASIA_0_CALCUTTA\x10\xfc\x01\x12\x19\n\x14TZ_IANA_ASIA_0_CHITA\x10\xfd\x01\x12\x1e\n\x19TZ_IANA_ASIA_0_CHOIBALSAN\x10\xfe\x01\x12\x1d\n\x18TZ_IANA_ASIA_0_CHONGQING\x10\xff\x01\x12\x1d\n\x18TZ_IANA_ASIA_0_CHUNGKING\x10\x80\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_COLOMBO\x10\x81\x02\x12\x19\n\x14TZ_IANA_ASIA_0_DACCA\x10\x82\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_DAMASCUS\x10\x83\x02\x12\x19\n\x14TZ_IANA_ASIA_0_DHAKA\x10\x84\x02\x12\x18\n\x13TZ_IANA_ASIA_0_DILI\x10\x85\x02\x12\x19\n\x14TZ_IANA_ASIA_0_DUBAI\x10\x86\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_DUSHANBE\x10\x87\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_FAMAGUSTA\x10\x88\x02\x12\x18\n\x13TZ_IANA_ASIA_0_GAZA\x10\x89\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_HARBIN\x10\x8a\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_HEBRON\x10\x8b\x02\x12\x1f\n\x1aTZ_IANA_ASIA_0_HO_CHI_MINH\x10\x8c\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_HONG_KONG\x10\x8d\x02\x12\x18\n\x13TZ_IANA_ASIA_0_HOVD\x10\x8e\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_IRKUTSK\x10\x8f\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_ISTANBUL\x10\x90\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_JAKARTA\x10\x91\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_JAYAPURA\x10\x92\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_JERUSALEM\x10\x93\x02\x12\x19\n\x14TZ_IANA_ASIA_0_KABUL\x10\x94\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_KAMCHATKA\x10\x95\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_KARACHI\x10\x96\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_KASHGAR\x10\x97\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_KATHMANDU\x10\x98\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_KATMANDU\x10\x99\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_KHANDYGA\x10\x9a\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_KOLKATA\x10\x9b\x02\x12\x1f\n\x1aTZ_IANA_ASIA_0_KRASNOYARSK\x10\x9c\x02\x12 \n\x1bTZ_IANA_ASIA_0_KUALA_LUMPUR\x10\x9d\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_KUCHING\x10\x9e\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_KUWAIT\x10\x9f\x02\x12\x19\n\x14TZ_IANA_ASIA_0_MACAO\x10\xa0\x02\x12\x19\n\x14TZ_IANA_ASIA_0_MACAU\x10\xa1\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_MAGADAN\x10\xa2\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_MAKASSAR\x10\xa3\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_MANILA\x10\xa4\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_MUSCAT\x10\xa5\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_NICOSIA\x10\xa6\x02\x12 \n\x1bTZ_IANA_ASIA_0_NOVOKUZNETSK\x10\xa7\x02\x12\x1f\n\x1aTZ_IANA_ASIA_0_NOVOSIBIRSK\x10\xa8\x02\x12\x18\n\x13TZ_IANA_ASIA_0_OMSK\x10\xa9\x02\x12\x18\n\x13TZ_IANA_ASIA_0_ORAL\x10\xaa\x02\x12\x1e\n\x19TZ_IANA_ASIA_0_PHNOM_PENH\x10\xab\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_PONTIANAK\x10\xac\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_PYONGYANG\x10\xad\x02\x12\x19\n\x14TZ_IANA_ASIA_0_QATAR\x10\xae\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_QOSTANAY\x10\xaf\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_QYZYLORDA\x10\xb0\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_RANGOON\x10\xb1\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_RIYADH\x10\xb2\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_SAIGON\x10\xb3\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_SAKHALIN\x10\xb4\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_SAMARKAND\x10\xb5\x02\x12\x19\n\x14TZ_IANA_ASIA_0_SEOUL\x10\xb6\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_SHANGHAI\x10\xb7\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_SINGAPORE\x10\xb8\x02\x12!\n\x1cTZ_IANA_ASIA_0_SREDNEKOLYMSK\x10\xb9\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_TAIPEI\x10\xba\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_TASHKENT\x10\xbb\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_TBILISI\x10\xbc\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_TEHRAN\x10\xbd\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_TELAVIV\x10\xbe\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_THIMBU\x10\xbf\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_THIMPHU\x10\xc0\x02\x12\x19\n\x14TZ_IANA_ASIA_0_TOKYO\x10\xc1\x02\x12\x19\n\x14TZ_IANA_ASIA_0_TOMSK\x10\xc2\x02\x12!\n\x1cTZ_IANA_ASIA_0_UJUNG_PANDANG\x10\xc3\x02\x12\x1f\n\x1aTZ_IANA_ASIA_0_ULAANBAATAR\x10\xc4\x02\x12\x1e\n\x19TZ_IANA_ASIA_0_ULAN_BATOR\x10\xc5\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_URUMQI\x10\xc6\x02\x12\x1c\n\x17TZ_IANA_ASIA_0_UST_NERA\x10\xc7\x02\x12\x1d\n\x18TZ_IANA_ASIA_0_VIENTIANE\x10\xc8\x02\x12\x1f\n\x1aTZ_IANA_ASIA_0_VLADIVOSTOK\x10\xc9\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_YAKUTSK\x10\xca\x02\x12\x1a\n\x15TZ_IANA_ASIA_0_YANGON\x10\xcb\x02\x12!\n\x1cTZ_IANA_ASIA_0_YEKATERINBURG\x10\xcc\x02\x12\x1b\n\x16TZ_IANA_ASIA_0_YEREVAN\x10\xcd\x02\x12\x1e\n\x19TZ_IANA_ATLANTIC_0_AZORES\x10\xce\x02\x12\x1f\n\x1aTZ_IANA_ATLANTIC_0_BERMUDA\x10\xcf\x02\x12\x1e\n\x19TZ_IANA_ATLANTIC_0_CANARY\x10\xd0\x02\x12"\n\x1dTZ_IANA_ATLANTIC_0_CAPE_VERDE\x10\xd1\x02\x12\x1e\n\x19TZ_IANA_ATLANTIC_0_FAEROE\x10\xd2\x02\x12\x1d\n\x18TZ_IANA_ATLANTIC_0_FAROE\x10\xd3\x02\x12\x1f\n\x1aTZ_IANA_EUROPE_0_JAN_MAYEN\x10\xd4\x02\x12\x1f\n\x1aTZ_IANA_ATLANTIC_0_MADEIRA\x10\xd5\x02\x12!\n\x1cTZ_IANA_ATLANTIC_0_REYKJAVIK\x10\xd6\x02\x12%\n TZ_IANA_ATLANTIC_0_SOUTH_GEORGIA\x10\xd7\x02\x12!\n\x1cTZ_IANA_ATLANTIC_0_ST_HELENA\x10\xd8\x02\x12\x1f\n\x1aTZ_IANA_ATLANTIC_0_STANLEY\x10\xd9\x02\x12\x1c\n\x17TZ_IANA_AUSTRALIA_0_ACT\x10\xda\x02\x12!\n\x1cTZ_IANA_AUSTRALIA_0_ADELAIDE\x10\xdb\x02\x12!\n\x1cTZ_IANA_AUSTRALIA_0_BRISBANE\x10\xdc\x02\x12$\n\x1fTZ_IANA_AUSTRALIA_0_BROKEN_HILL\x10\xdd\x02\x12!\n\x1cTZ_IANA_AUSTRALIA_0_CANBERRA\x10\xde\x02\x12\x1f\n\x1aTZ_IANA_AUSTRALIA_0_CURRIE\x10\xdf\x02\x12\x1f\n\x1aTZ_IANA_AUSTRALIA_0_DARWIN\x10\xe0\x02\x12\x1e\n\x19TZ_IANA_AUSTRALIA_0_EUCLA\x10\xe1\x02\x12\x1f\n\x1aTZ_IANA_AUSTRALIA_0_HOBART\x10\xe2\x02\x12\x1c\n\x17TZ_IANA_AUSTRALIA_0_LHI\x10\xe3\x02\x12!\n\x1cTZ_IANA_AUSTRALIA_0_LINDEMAN\x10\xe4\x02\x12"\n\x1dTZ_IANA_AUSTRALIA_0_LORD_HOWE\x10\xe5\x02\x12"\n\x1dTZ_IANA_AUSTRALIA_0_MELBOURNE\x10\xe6\x02\x12\x1c\n\x17TZ_IANA_AUSTRALIA_0_NSW\x10\xe7\x02\x12\x1e\n\x19TZ_IANA_AUSTRALIA_0_NORTH\x10\xe8\x02\x12\x1e\n\x19TZ_IANA_AUSTRALIA_0_PERTH\x10\xe9\x02\x12#\n\x1eTZ_IANA_AUSTRALIA_0_QUEENSLAND\x10\xea\x02\x12\x1e\n\x19TZ_IANA_AUSTRALIA_0_SOUTH\x10\xeb\x02\x12\x1f\n\x1aTZ_IANA_AUSTRALIA_0_SYDNEY\x10\xec\x02\x12!\n\x1cTZ_IANA_AUSTRALIA_0_TASMANIA\x10\xed\x02\x12!\n\x1cTZ_IANA_AUSTRALIA_0_VICTORIA\x10\xee\x02\x12\x1d\n\x18TZ_IANA_AUSTRALIA_0_WEST\x10\xef\x02\x12#\n\x1eTZ_IANA_AUSTRALIA_0_YANCOWINNA\x10\xf0\x02\x12\x1b\n\x16TZ_IANA_AMERICA_0_ACRE\x10\xf1\x02\x12\x1d\n\x18TZ_IANA_BRAZIL_0_NORONHA\x10\xf2\x02\x12\x1b\n\x16TZ_IANA_AMERICA_0_EAST\x10\xf3\x02\x12\x1b\n\x16TZ_IANA_AMERICA_0_WEST\x10\xf4\x02\x12\x1e\n\x19TZ_IANA_CANADA_0_ATLANTIC\x10\xf5\x02\x12\x1d\n\x18TZ_IANA_CANADA_0_CENTRAL\x10\xf6\x02\x12\x1d\n\x18TZ_IANA_CANADA_0_EASTERN\x10\xf7\x02\x12\x1e\n\x19TZ_IANA_CANADA_0_MOUNTAIN\x10\xf8\x02\x12"\n\x1dTZ_IANA_CANADA_0_NEWFOUNDLAND\x10\xf9\x02\x12\x1d\n\x18TZ_IANA_CANADA_0_PACIFIC\x10\xfa\x02\x12"\n\x1dTZ_IANA_CANADA_0_SASKATCHEWAN\x10\xfb\x02\x12\x1b\n\x16TZ_IANA_CANADA_0_YUKON\x10\xfc\x02\x12\x10\n\x0bTZ_IANA_CET\x10\xfd\x02\x12 \n\x1bTZ_IANA_CHILE_0_CONTINENTAL\x10\xfe\x02\x12!\n\x1cTZ_IANA_CHILE_0_EASTERISLAND\x10\xff\x02\x12\x14\n\x0fTZ_IANA_CST6CDT\x10\x80\x03\x12\x1b\n\x16TZ_IANA_AMERICA_0_CUBA\x10\x81\x03\x12\x10\n\x0bTZ_IANA_EET\x10\x82\x03\x12\x1b\n\x16TZ_IANA_AFRICA_0_EGYPT\x10\x83\x03\x12\x1a\n\x15TZ_IANA_EUROPE_0_EIRE\x10\x84\x03\x12\x14\n\x0fTZ_IANA_EST5EDT\x10\x85\x03\x12\x14\n\x0fTZ_IANA_ETC_GMT\x10\x86\x03\x12\x16\n\x11TZ_IANA_ETC_GMTP0\x10\x87\x03\x12\x16\n\x11TZ_IANA_ETC_GMTP1\x10\x88\x03\x12\x17\n\x12TZ_IANA_ETC_GMTP10\x10\x89\x03\x12\x17\n\x12TZ_IANA_ETC_GMTP11\x10\x8a\x03\x12\x17\n\x12TZ_IANA_ETC_GMTP12\x10\x8b\x03\x12\x16\n\x11TZ_IANA_ETC_GMTP2\x10\x8c\x03\x12\x16\n\x11TZ_IANA_ETC_GMTP3\x10\x8d\x03\x12\x16\n\x11TZ_IANA_ETC_GMTP4\x10\x8e\x03\x12\x16\n\x11TZ_IANA_ETC_GMTP5\x10\x8f\x03\x12\x16\n\x11TZ_IANA_ETC_GMTP6\x10\x90\x03\x12\x16\n\x11TZ_IANA_ETC_GMTP7\x10\x91\x03\x12\x16\n\x11TZ_IANA_ETC_GMTP8\x10\x92\x03\x12\x16\n\x11TZ_IANA_ETC_GMTP9\x10\x93\x03\x12\x16\n\x11TZ_IANA_ETC_GMTM0\x10\x94\x03\x12\x16\n\x11TZ_IANA_ETC_GMTM1\x10\x95\x03\x12\x17\n\x12TZ_IANA_ETC_GMTM10\x10\x96\x03\x12\x17\n\x12TZ_IANA_ETC_GMTM11\x10\x97\x03\x12\x17\n\x12TZ_IANA_ETC_GMTM12\x10\x98\x03\x12\x17\n\x12TZ_IANA_ETC_GMTM13\x10\x99\x03\x12\x17\n\x12TZ_IANA_ETC_GMTM14\x10\x9a\x03\x12\x16\n\x11TZ_IANA_ETC_GMTM2\x10\x9b\x03\x12\x16\n\x11TZ_IANA_ETC_GMTM3\x10\x9c\x03\x12\x16\n\x11TZ_IANA_ETC_GMTM4\x10\x9d\x03\x12\x16\n\x11TZ_IANA_ETC_GMTM5\x10\x9e\x03\x12\x16\n\x11TZ_IANA_ETC_GMTM6\x10\x9f\x03\x12\x16\n\x11TZ_IANA_ETC_GMTM7\x10\xa0\x03\x12\x16\n\x11TZ_IANA_ETC_GMTM8\x10\xa1\x03\x12\x16\n\x11TZ_IANA_ETC_GMTM9\x10\xa2\x03\x12\x15\n\x10TZ_IANA_ETC_GMT0\x10\xa3\x03\x12\x1a\n\x15TZ_IANA_ETC_GREENWICH\x10\xa4\x03\x12\x14\n\x0fTZ_IANA_ETC_UCT\x10\xa5\x03\x12\x1a\n\x15TZ_IANA_ETC_UNIVERSAL\x10\xa6\x03\x12\x14\n\x0fTZ_IANA_ETC_UTC\x10\xa7\x03\x12\x15\n\x10TZ_IANA_ETC_ZULU\x10\xa8\x03\x12\x1f\n\x1aTZ_IANA_EUROPE_0_AMSTERDAM\x10\xa9\x03\x12\x1d\n\x18TZ_IANA_EUROPE_0_ANDORRA\x10\xaa\x03\x12\x1f\n\x1aTZ_IANA_EUROPE_0_ASTRAKHAN\x10\xab\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_ATHENS\x10\xac\x03\x12\x1d\n\x18TZ_IANA_EUROPE_0_BELFAST\x10\xad\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_BELGRADE\x10\xae\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_BERLIN\x10\xaf\x03\x12 \n\x1bTZ_IANA_EUROPE_0_BRATISLAVA\x10\xb0\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_BRUSSELS\x10\xb1\x03\x12\x1f\n\x1aTZ_IANA_EUROPE_0_BUCHAREST\x10\xb2\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_BUDAPEST\x10\xb3\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_BUSINGEN\x10\xb4\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_CHISINAU\x10\xb5\x03\x12 \n\x1bTZ_IANA_EUROPE_0_COPENHAGEN\x10\xb6\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_DUBLIN\x10\xb7\x03\x12\x1f\n\x1aTZ_IANA_EUROPE_0_GIBRALTAR\x10\xb8\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_GUERNSEY\x10\xb9\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_HELSINKI\x10\xba\x03\x12!\n\x1cTZ_IANA_EUROPE_0_ISLE_OF_MAN\x10\xbb\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_ISTANBUL\x10\xbc\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_JERSEY\x10\xbd\x03\x12!\n\x1cTZ_IANA_EUROPE_0_KALININGRAD\x10\xbe\x03\x12\x1a\n\x15TZ_IANA_EUROPE_0_KIEV\x10\xbf\x03\x12\x1b\n\x16TZ_IANA_EUROPE_0_KIROV\x10\xc0\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_LISBON\x10\xc1\x03\x12\x1f\n\x1aTZ_IANA_EUROPE_0_LJUBLJANA\x10\xc2\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_LONDON\x10\xc3\x03\x12 \n\x1bTZ_IANA_EUROPE_0_LUXEMBOURG\x10\xc4\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_MADRID\x10\xc5\x03\x12\x1b\n\x16TZ_IANA_EUROPE_0_MALTA\x10\xc6\x03\x12\x1f\n\x1aTZ_IANA_EUROPE_0_MARIEHAMN\x10\xc7\x03\x12\x1b\n\x16TZ_IANA_EUROPE_0_MINSK\x10\xc8\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_MONACO\x10\xc9\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_MOSCOW\x10\xca\x03\x12\x1d\n\x18TZ_IANA_EUROPE_0_NICOSIA\x10\xcb\x03\x12\x1a\n\x15TZ_IANA_EUROPE_0_OSLO\x10\xcc\x03\x12\x1b\n\x16TZ_IANA_EUROPE_0_PARIS\x10\xcd\x03\x12\x1f\n\x1aTZ_IANA_EUROPE_0_PODGORICA\x10\xce\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_PRAGUE\x10\xcf\x03\x12\x1a\n\x15TZ_IANA_EUROPE_0_RIGA\x10\xd0\x03\x12\x1a\n\x15TZ_IANA_EUROPE_0_ROME\x10\xd1\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_SAMARA\x10\xd2\x03\x12 \n\x1bTZ_IANA_EUROPE_0_SAN_MARINO\x10\xd3\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_SARAJEVO\x10\xd4\x03\x12\x1d\n\x18TZ_IANA_EUROPE_0_SARATOV\x10\xd5\x03\x12 \n\x1bTZ_IANA_EUROPE_0_SIMFEROPOL\x10\xd6\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_SKOPJE\x10\xd7\x03\x12\x1b\n\x16TZ_IANA_EUROPE_0_SOFIA\x10\xd8\x03\x12\x1f\n\x1aTZ_IANA_EUROPE_0_STOCKHOLM\x10\xd9\x03\x12\x1d\n\x18TZ_IANA_EUROPE_0_TALLINN\x10\xda\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_TIRANE\x10\xdb\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_TIRASPOL\x10\xdc\x03\x12\x1f\n\x1aTZ_IANA_EUROPE_0_ULYANOVSK\x10\xdd\x03\x12\x1e\n\x19TZ_IANA_EUROPE_0_UZHGOROD\x10\xde\x03\x12\x1b\n\x16TZ_IANA_EUROPE_0_VADUZ\x10\xdf\x03\x12\x1d\n\x18TZ_IANA_EUROPE_0_VATICAN\x10\xe0\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_VIENNA\x10\xe1\x03\x12\x1d\n\x18TZ_IANA_EUROPE_0_VILNIUS\x10\xe2\x03\x12\x1f\n\x1aTZ_IANA_EUROPE_0_VOLGOGRAD\x10\xe3\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_WARSAW\x10\xe4\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_ZAGREB\x10\xe5\x03\x12 \n\x1bTZ_IANA_EUROPE_0_ZAPOROZHYE\x10\xe6\x03\x12\x1c\n\x17TZ_IANA_EUROPE_0_ZURICH\x10\xe7\x03\x12\x18\n\x13TZ_IANA_EUROPE_0_GB\x10\xe8\x03\x12\x1d\n\x18TZ_IANA_EUROPE_0_GB_RIRE\x10\xe9\x03\x12\x10\n\x0bTZ_IANA_GMT\x10\xea\x03\x12\x11\n\x0cTZ_IANA_GMT0\x10\xeb\x03\x12\x16\n\x11TZ_IANA_GREENWICH\x10\xec\x03\x12\x1c\n\x17TZ_IANA_ASIA_0_HONGKONG\x10\xed\x03\x12\x1f\n\x1aTZ_IANA_ATLANTIC_0_ICELAND\x10\xee\x03\x12"\n\x1dTZ_IANA_INDIAN_0_ANTANANARIVO\x10\xef\x03\x12\x1c\n\x17TZ_IANA_INDIAN_0_CHAGOS\x10\xf0\x03\x12\x1f\n\x1aTZ_IANA_INDIAN_0_CHRISTMAS\x10\xf1\x03\x12\x1b\n\x16TZ_IANA_INDIAN_0_COCOS\x10\xf2\x03\x12\x1c\n\x17TZ_IANA_INDIAN_0_COMORO\x10\xf3\x03\x12\x1f\n\x1aTZ_IANA_INDIAN_0_KERGUELEN\x10\xf4\x03\x12\x1a\n\x15TZ_IANA_INDIAN_0_MAHE\x10\xf5\x03\x12\x1e\n\x19TZ_IANA_INDIAN_0_MALDIVES\x10\xf6\x03\x12\x1f\n\x1aTZ_IANA_INDIAN_0_MAURITIUS\x10\xf7\x03\x12\x1d\n\x18TZ_IANA_AFRICA_0_MAYOTTE\x10\xf8\x03\x12\x1d\n\x18TZ_IANA_INDIAN_0_REUNION\x10\xf9\x03\x12\x18\n\x13TZ_IANA_ASIA_0_IRAN\x10\xfa\x03\x12\x1a\n\x15TZ_IANA_ASIA_0_ISRAEL\x10\xfb\x03\x12\x14\n\x0fTZ_IANA_JAMAICA\x10\xfc\x03\x12\x19\n\x14TZ_IANA_ASIA_0_JAPAN\x10\xfd\x03\x12\x16\n\x11TZ_IANA_KWAJALEIN\x10\xfe\x03\x12\x1b\n\x16TZ_IANA_AFRICA_0_LIBYA\x10\xff\x03\x12\x19\n\x14TZ_IANA_EUROPE_0_MET\x10\x80\x04\x12 \n\x1bTZ_IANA_MEXICO_0_BAJA_NORTE\x10\x81\x04\x12\x1e\n\x19TZ_IANA_MEXICO_0_BAJA_SUR\x10\x82\x04\x12\x1d\n\x18TZ_IANA_MEXICO_0_GENERAL\x10\x83\x04\x12\x14\n\x0fTZ_IANA_MST7MDT\x10\x84\x04\x12\x1c\n\x17TZ_IANA_AMERICA_0NAVAJO\x10\x85\x04\x12\x19\n\x14TZ_IANA_PACIFIC_0_NZ\x10\x86\x04\x12\x1e\n\x19TZ_IANA_PACIFIC_0_NZ_CHAT\x10\x87\x04\x12\x1b\n\x16TZ_IANA_PACIFIC_0_APIA\x10\x88\x04\x12\x1f\n\x1aTZ_IANA_PACIFIC_0_AUCKLAND\x10\x89\x04\x12#\n\x1eTZ_IANA_PACIFIC_0_BOUGAINVILLE\x10\x8a\x04\x12\x1e\n\x19TZ_IANA_PACIFIC_0_CHATHAM\x10\x8b\x04\x12\x1c\n\x17TZ_IANA_PACIFIC_0_CHUUK\x10\x8c\x04\x12\x1d\n\x18TZ_IANA_PACIFIC_0_EASTER\x10\x8d\x04\x12\x1c\n\x17TZ_IANA_PACIFIC_0_EFATE\x10\x8e\x04\x12 \n\x1bTZ_IANA_PACIFIC_0_ENDERBURY\x10\x8f\x04\x12\x1e\n\x19TZ_IANA_PACIFIC_0_FAKAOFO\x10\x90\x04\x12\x1b\n\x16TZ_IANA_PACIFIC_0_FIJI\x10\x91\x04\x12\x1f\n\x1aTZ_IANA_PACIFIC_0_FUNAFUTI\x10\x92\x04\x12 \n\x1bTZ_IANA_PACIFIC_0_GALAPAGOS\x10\x93\x04\x12\x1e\n\x19TZ_IANA_PACIFIC_0_GAMBIER\x10\x94\x04\x12"\n\x1dTZ_IANA_PACIFIC_0_GUADALCANAL\x10\x95\x04\x12\x1b\n\x16TZ_IANA_PACIFIC_0_GUAM\x10\x96\x04\x12\x1f\n\x1aTZ_IANA_PACIFIC_0_HONOLULU\x10\x97\x04\x12\x1f\n\x1aTZ_IANA_PACIFIC_0_JOHNSTON\x10\x98\x04\x12!\n\x1cTZ_IANA_PACIFIC_0_KIRITIMATI\x10\x99\x04\x12\x1d\n\x18TZ_IANA_PACIFIC_0_KOSRAE\x10\x9a\x04\x12 \n\x1bTZ_IANA_PACIFIC_0_KWAJALEIN\x10\x9b\x04\x12\x1d\n\x18TZ_IANA_PACIFIC_0_MAJURO\x10\x9c\x04\x12 \n\x1bTZ_IANA_PACIFIC_0_MARQUESAS\x10\x9d\x04\x12\x1d\n\x18TZ_IANA_PACIFIC_0_MIDWAY\x10\x9e\x04\x12\x1c\n\x17TZ_IANA_PACIFIC_0_NAURU\x10\x9f\x04\x12\x1b\n\x16TZ_IANA_PACIFIC_0_NIUE\x10\xa0\x04\x12\x1e\n\x19TZ_IANA_PACIFIC_0_NORFOLK\x10\xa1\x04\x12\x1d\n\x18TZ_IANA_PACIFIC_0_NOUMEA\x10\xa2\x04\x12 \n\x1bTZ_IANA_PACIFIC_0_PAGO_PAGO\x10\xa3\x04\x12\x1c\n\x17TZ_IANA_PACIFIC_0_PALAU\x10\xa4\x04\x12\x1f\n\x1aTZ_IANA_PACIFIC_0_PITCAIRN\x10\xa5\x04\x12\x1e\n\x19TZ_IANA_PACIFIC_0_POHNPEI\x10\xa6\x04\x12\x1d\n\x18TZ_IANA_PACIFIC_0_PONAPE\x10\xa7\x04\x12#\n\x1eTZ_IANA_PACIFIC_0_PORT_MORESBY\x10\xa8\x04\x12 \n\x1bTZ_IANA_PACIFIC_0_RAROTONGA\x10\xa9\x04\x12\x1d\n\x18TZ_IANA_PACIFIC_0_SAIPAN\x10\xaa\x04\x12\x1c\n\x17TZ_IANA_PACIFIC_0_SAMOA\x10\xab\x04\x12\x1d\n\x18TZ_IANA_PACIFIC_0_TAHITI\x10\xac\x04\x12\x1d\n\x18TZ_IANA_PACIFIC_0_TARAWA\x10\xad\x04\x12 \n\x1bTZ_IANA_PACIFIC_0_TONGATAPU\x10\xae\x04\x12\x1b\n\x16TZ_IANA_PACIFIC_0_TRUK\x10\xaf\x04\x12\x1b\n\x16TZ_IANA_PACIFIC_0_WAKE\x10\xb0\x04\x12\x1d\n\x18TZ_IANA_PACIFIC_0_WALLIS\x10\xb1\x04\x12\x1a\n\x15TZ_IANA_PACIFIC_0_YAP\x10\xb2\x04\x12\x1c\n\x17TZ_IANA_EUROPE_0_POLAND\x10\xb3\x04\x12\x1e\n\x19TZ_IANA_EUROPE_0_PORTUGAL\x10\xb4\x04\x12\x17\n\x12TZ_IANA_ASIA_0_PRC\x10\xb5\x04\x12\x1e\n\x19TZ_IANA_AMERICA_0_PST8PDT\x10\xb6\x04\x12\x17\n\x12TZ_IANA_ASIA_0_ROK\x10\xb7\x04\x12\x16\n\x11TZ_IANA_SINGAPORE\x10\xb8\x04\x12\x1c\n\x17TZ_IANA_SYSTEMV_EST5EDT\x10\xb9\x04\x12\x1d\n\x18TZ_IANA_SYYSTEMV_MST7MDT\x10\xba\x04\x12\x1c\n\x17TZ_IANA_SYSTEMV_PST8PDT\x10\xbb\x04\x12\x14\n\x0fTZ_IANA_PST8PDT\x10\xbc\x04\x12\x1c\n\x17TZ_IANA_EUROPE_0_TURKEY\x10\xbd\x04\x12\x10\n\x0bTZ_IANA_UCT\x10\xbe\x04\x12\x16\n\x11TZ_IANA_UNIVERSAL\x10\xbf\x04\x12\x1d\n\x18TZ_IANA_AMERICA_0_ALASKA\x10\xc0\x04\x12\x1f\n\x1aTZ_IANA_AMERICA_0_ALEUTIAN\x10\xc1\x04\x12\x1e\n\x19TZ_IANA_AMERICA_0_ARIZONA\x10\xc2\x04\x12\x1e\n\x19TZ_IANA_AMERICA_0_CENTRAL\x10\xc3\x04\x12#\n\x1eTZ_IANA_AMERICA_0_EAST_INDIANA\x10\xc4\x04\x12\x1e\n\x19TZ_IANA_AMERICA_0_EASTERN\x10\xc5\x04\x12\x1d\n\x18TZ_IANA_AMERICA_0_HAWAII\x10\xc6\x04\x12%\n TZ_IANA_AMERICA_0_INDIANA_STARKE\x10\xc7\x04\x12\x1f\n\x1aTZ_IANA_AMERICA_0_MICHIGAN\x10\xc8\x04\x12\x1f\n\x1aTZ_IANA_AMERICA_0_MOUNTAIN\x10\xc9\x04\x12\x1e\n\x19TZ_IANA_AMERICA_0_PACIFIC\x10\xca\x04\x12"\n\x1dTZ_IANA_AMERICA_0_PACIFIC_NEW\x10\xcb\x04\x12\x1c\n\x17TZ_IANA_AMERICA_0_SAMOA\x10\xcc\x04\x12\x11\n\x0cTZ_IANA_W_SU\x10\xcd\x04\x12\x10\n\x0bTZ_IANA_WET\x10\xce\x04\x12\x11\n\x0cTZ_IANA_ZULU\x10\xcf\x04\x12\x10\n\x0bTZ_IANA_EST\x10\xd0\x04\x12\x10\n\x0bTZ_IANA_HST\x10\xd1\x04\x12\x10\n\x0bTZ_IANA_MST\x10\xd2\x04\x12\x10\n\x0bTZ_IANA_ACT\x10\xd3\x04\x12\x10\n\x0bTZ_IANA_CST\x10\xd4\x04\x12\x10\n\x0bTZ_IANA_PST\x10\xd5\x04*\xcd\x18\n\x05TzUtc\x12\x12\n\x0eTZ_UTC_INVALID\x10\x00\x12\x0f\n\x0bTZ_UTC_0000\x10\x01\x12\x31\n-TZ_UTC_MINUS1200_INTERNATIONAL_DATE_LINE_WEST\x10\x02\x12(\n$TZ_UTC_MINUS1100_MIDWAY_ISLAND_SAMOA\x10\x03\x12\x1b\n\x17TZ_UTC_MINUS1000_HAWAII\x10\x04\x12\x1b\n\x17TZ_UTC_MINUS0900_ALASKA\x10\x05\x12!\n\x1dTZ_UTC_MINUS0800_PACIFIC_TIME\x10\x06\x12,\n(TZ_UTC_MINUS0800_TIJUANA_BAJA_CALIFORNIA\x10\x07\x12\x1c\n\x18TZ_UTC_MINUS0700_ARIZONA\x10\x08\x12"\n\x1eTZ_UTC_MINUS0700_MOUNTAIN_TIME\x10\t\x12-\n)TZ_UTC_MINUS0700_CHIHUAHUA_LAPAZ_MAZATLAN\x10\n\x12$\n TZ_UTC_MINUS0600_CENTRAL_AMERICA\x10\x0b\x12!\n\x1dTZ_UTC_MINUS0600_CENTRAL_TIME\x10\x0c\x12,\n(TZ_UTC_MINUS0600_GUADALAJARA_MEXICO_CITY\x10\r\x12!\n\x1dTZ_UTC_MINUS0600_SASKATCHEWAN\x10\x0e\x12\x30\n,TZ_UTC_MINUS0500_BOGOTA_LIMA_QUITO_RIOBRANCO\x10\x0f\x12!\n\x1dTZ_UTC_MINUS0500_EASTERN_TIME\x10\x10\x12\x1c\n\x18TZ_UTC_MINUS0500_INDIANA\x10\x11\x12"\n\x1eTZ_UTC_MINUS0400_ATLANTIC_TIME\x10\x12\x12\x1a\n\x16TZ_UTC_MINUS0400_LAPAZ\x10\x13\x12\x1b\n\x17TZ_UTC_MINUS0400_MANAUS\x10\x14\x12\x1d\n\x19TZ_UTC_MINUS0400_SANTIAGO\x10\x15\x12\x1c\n\x18TZ_UTC_MINUS0430_CARACAS\x10\x16\x12!\n\x1dTZ_UTC_MINUS0330_NEWFOUNDLAND\x10\x17\x12\x1d\n\x19TZ_UTC_MINUS0300_BRASILIA\x10\x18\x12,\n(TZ_UTC_MINUS0300_BUENOS_AIRES_GEORGETOWN\x10\x19\x12\x1e\n\x1aTZ_UTC_MINUS0300_GREENLAND\x10\x1a\x12\x1f\n\x1bTZ_UTC_MINUS0300_MONTEVIDEO\x10\x1b\x12!\n\x1dTZ_UTC_MINUS0200_MID_ATLANTIC\x10\x1c\x12\x1b\n\x17TZ_UTC_MINUS0100_AZORES\x10\x1d\x12"\n\x1eTZ_UTC_MINUS0100_CAPE_VERDE_IS\x10\x1e\x12.\n*TZ_UTC_0000_CASABLANCA_MONTROVIA_REYKJAVIK\x10\x1f\x12.\n*TZ_UTC_0000_DUBLIN_EDINBURGH_LISBON_LONDON\x10 \x12.\n*TZ_UTC_PLUS0100_AMSTERDAM_BERLIN_BERN_ROME\x10!\x12\x30\n,TZ_UTC_PLUS0100_BELGRADE_BRATISLAVA_BUDAPEST\x10"\x12.\n*TZ_UTC_PLUS0100_BRUSSELS_COPENHAGEN_MADRID\x10#\x12\x31\n-TZ_UTC_PLUS0100_SARAJEVO_SKOPJE_WARSAW_ZAGREB\x10$\x12\'\n#TZ_UTC_PLUS0100_WEST_CENTRAL_AFRICA\x10%\x12\x19\n\x15TZ_UTC_PLUS0200_AMMAN\x10&\x12-\n)TZ_UTC_PLUS0200_ATHENS_BUCHAREST_ISTANBUL\x10\'\x12\x1a\n\x16TZ_UTC_PLUS0200_BEIRUT\x10(\x12\x19\n\x15TZ_UTC_PLUS0200_MINSK\x10)\x12\x19\n\x15TZ_UTC_PLUS0200_CAIRO\x10*\x12#\n\x1fTZ_UTC_PLUS0200_HARARE_PRETORIA\x10+\x12.\n*TZ_UTC_PLUS0200_HELSINKI_KYIV_RIGA_VILNIUS\x10,\x12\x1d\n\x19TZ_UTC_PLUS0200_JERUSALEM\x10-\x12\x1c\n\x18TZ_UTC_PLUS0200_WINDHOEK\x10.\x12\x1b\n\x17TZ_UTC_PLUS0300_BAGHDAD\x10/\x12!\n\x1dTZ_UTC_PLUS0300_KUWAIT_RIYADH\x10\x30\x12\x32\n.TZ_UTC_PLUS0300_MOSCOW_ST_PETERSBURG_VOLGOGRAD\x10\x31\x12\x1b\n\x17TZ_UTC_PLUS0300_NAIROBI\x10\x32\x12\x1b\n\x17TZ_UTC_PLUS0300_TBILISI\x10\x33\x12\x1a\n\x16TZ_UTC_PLUS0330_TEHRAN\x10\x34\x12$\n TZ_UTC_PLUS0400_ABU_DHABI_MUSCAT\x10\x35\x12\x18\n\x14TZ_UTC_PLUS0400_BAKU\x10\x36\x12*\n&TZ_UTC_PLUS0400_CAUCASUS_STANDARD_TIME\x10\x37\x12\x1b\n\x17TZ_UTC_PLUS0400_YEREVAN\x10\x38\x12\x19\n\x15TZ_UTC_PLUS0430_KABUL\x10\x39\x12 \n\x1cTZ_UTC_PLUS0500_EKATERINBURG\x10:\x12.\n*TZ_UTC_PLUS0500_ISLAMABAD_KARACHI_TASHKENT\x10;\x12*\n&TZ_UTC_PLUS0530_CHENNAI_KOLKATA_MUMBAI\x10<\x12\'\n#TZ_UTC_PLUS0530_SRI_JAYAWARDENEPURA\x10=\x12\x1d\n\x19TZ_UTC_PLUS0545_KATHMANDU\x10>\x12&\n"TZ_UTC_PLUS0600_ALMATY_NOVOSIBIRSK\x10?\x12 \n\x1cTZ_UTC_PLUS0600_ASTANA_DHAKA\x10@\x12\x1a\n\x16TZ_UTC_PLUS0630_YANGON\x10\x41\x12)\n%TZ_UTC_PLUS0700_BANGKOK_HANOI_JAKARTA\x10\x42\x12\x1f\n\x1bTZ_UTC_PLUS0700_KRASNOYARSK\x10\x43\x12/\n+TZ_UTC_PLUS0800_BEIJING_CHONGQING_HONG_KONG\x10\x44\x12(\n$TZ_UTC_PLUS0800_IRKUTSK_ULAAN_BATAAR\x10\x45\x12*\n&TZ_UTC_PLUS0800_KUALA_LUMPUR_SINGAPORE\x10\x46\x12\x19\n\x15TZ_UTC_PLUS0800_PERTH\x10G\x12\x1a\n\x16TZ_UTC_PLUS0800_TAIPEI\x10H\x12\'\n#TZ_UTC_PLUS0900_OSAKA_SAPPORO_TOKYO\x10I\x12\x19\n\x15TZ_UTC_PLUS0900_SEOUL\x10J\x12\x1b\n\x17TZ_UTC_PLUS0900_YAKUTSK\x10K\x12\x1c\n\x18TZ_UTC_PLUS0930_ADELAIDE\x10L\x12\x1a\n\x16TZ_UTC_PLUS0930_DARWIN\x10M\x12\x1c\n\x18TZ_UTC_PLUS1000_BRISBANE\x10N\x12-\n)TZ_UTC_PLUS1000_CANBERRA_MELBOURNE_SYDNEY\x10O\x12%\n!TZ_UTC_PLUS1000_GUAM_PORT_MORESBY\x10P\x12\x1a\n\x16TZ_UTC_PLUS1000_HOBART\x10Q\x12\x1f\n\x1bTZ_UTC_PLUS1000_VLADIVOSTOK\x10R\x12%\n!TZ_UTC_PLUS1100_MAGADAN_SOLOMONIS\x10S\x12\'\n#TZ_UTC_PLUS1200_AUCKLAND_WELLINGTON\x10T\x12.\n*TZ_UTC_PLUS1200_FIJI_KAMCHATKA_MARSHALL_IS\x10U\x12\x1e\n\x1aTZ_UTC_PLUS1300_NUKU_ALOFA\x10VBl\n*com.flexport.os.grpc.type.datetime.v1beta1B\x0eTimeZonesProtoP\x01\xea\x02+Flexport::OS::Grpc::Type::DateTime::V1Beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "flexport.os.grpc.type.datetime.v1beta1.time_zones_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n*com.flexport.os.grpc.type.datetime.v1beta1B\016TimeZonesProtoP\001\352\002+Flexport::OS::Grpc::Type::DateTime::V1Beta1"
    _globals["_TZIANA"]._serialized_start = 246
    _globals["_TZIANA"]._serialized_end = 18944
    _globals["_TZUTC"]._serialized_start = 18947
    _globals["_TZUTC"]._serialized_end = 22096
    _globals["_TIMEZONE"]._serialized_start = 100
    _globals["_TIMEZONE"]._serialized_end = 242
# @@protoc_insertion_point(module_scope)