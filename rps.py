import serial
import sys

baudrate = 115200

try:
	port=sys.argv[1]
	ch=int(sys.argv[2])
	st=int(sys.argv[3])
except:
	print( "Invalid arguments or not provided!" )
	exit(1)


dev=serial.Serial()
dev.port=port
dev.baudrate=baudrate
dev.open()

toSend = ( (ch & 15) | ((st << 4) & 240) )
toSend = toSend.to_bytes( 1, 'little' )

dev.write( toSend )

dev.close()

exit(0)
