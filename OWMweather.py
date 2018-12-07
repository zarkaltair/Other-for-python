import pyowm

town        = input                     ( 'Какой город Вас интересует?: ' )
owm         = pyowm.OWM                 ( '70732ac514bf006244ac74c5f31de5aa', language='ru' )
observation = owm.weather_at_place      ( town )
w           = observation.get_weather   ()
temp        = w.get_temperature         ( 'celsius' ) ['temp']
time        = w.get_reference_time      ( 'iso' )
wind        = w.get_wind                () ['speed']
sunrise     = w.get_sunrise_time        ( 'iso' ) 
sunset      = w.get_sunset_time         ( 'iso' )
pressure    = w.get_pressure            () ['press']
status      = w.get_detailed_status     ()


print( 'Температура в городе ' + town + ' сейчас: ' + str( int( temp ) ) + ' C*' )
print( 'Также, в указанном городе ' + status )
print( 'Точная дата и время в городе ' + town + ' сейчас: ' + str( time ) )
print( 'Скорость ветра в городе ' + town + ' сейчас: ' + str( wind ) + ' м/с' )
print( 'Восход солнца в ' + sunrise + ' закат солнца в ' + sunset )
print( 'Атмосферное давление в городе ' + town + ' сейчас: ' + str( pressure ) + ' миллиметров ртутного столба' )
