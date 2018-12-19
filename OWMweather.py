import pyowm

town        = 'Москва' # = input                     ( 'Какой город Вас интересует?: ' )
owm         = pyowm.OWM                 ( '70732ac514bf006244ac74c5f31de5aa', language='en' )
observation = owm.weather_at_place      ( town )
w           = observation.get_weather   ()
temp        = w.get_temperature         ( 'celsius' ) ['temp']
# print(w.get_temperature())
time        = w.get_reference_time      ( 'iso' )
# print(w.get_reference_time())
wind        = w.get_wind                () ['speed']
# print(w.get_wind())
sunrise     = w.get_sunrise_time        ( 'iso' ) 
sunset      = w.get_sunset_time         ( 'iso' )
pressure    = w.get_pressure            () ['press']
status      = w.get_detailed_status     ()
print(w.get_detailed_status())
humidity    = w.get_humidity            ()
print(w.get_humidity())


# print( 'Температура в городе ' + town + ' сейчас: ' + str( int( temp ) ) + ' °C' )
# print( 'Также, в указанном городе сейчас ' + status )
# print( 'Точная дата и время в городе ' + town + ' сейчас: ' + str( time ) )
# print( 'Скорость ветра в городе ' + town + ' сейчас: ' + str( wind ) + ' м/с' )
# print( 'Восход солнца в ' + sunrise + ' закат солнца в ' + sunset )
# print( 'Атмосферное давление в городе ' + town + ' сейчас: ' + str( round( pressure * 100 / 133.32 ) ) + ' мм. рт. ст.' )
# print( 'Влажность воздуха ' + str( humidity ) + '%')