import nmap
import re

nm = nmap.PortScanner()

#Expresion regular de ips
regex_ips = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
#Expresion regular de puertos
regex_port = r'^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$' 

#IP a analizar
ip = input('Ingrese una ip:\n')

if re.match(regex_ips,ip):
 print('--Definimos un rango de puertos con el siguiente formato (inicio-fin)--\n')
 print('\n')
 port_begin = input('Ingrese un puerto inicio:\n')
 port_end = input('Ingrese un puerto final:\n')
 if re.match(regex_port,port_begin) and re.match(regex_port,port_end):
    ports = port_begin+'-'+port_end
    request = nm.scan(ip, ports)
    print(request)
 else:
    print('Puertos incorrentos\n')

else:
    print('La IP no es correcta')
