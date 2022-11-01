from matplotlib.font_manager import json_dump
import nmap
import re
import json
import requests

url = 'http://127.0.0.1/example/fake_url.php'
nm = nmap.PortScanner()

#Expresion regular de IPS
regex_ips = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
#Expresion regular de puertos
regex_port = r'^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$' 

#IP a analizar
ip = input('Ingrese una ip:\n')
#Validaciones
if re.match(regex_ips,ip):
 port_begin = input('Ingrese un puerto inicio:\n')
 port_end = input('Ingrese un puerto final:\n')
 if re.match(regex_port,port_begin) and re.match(regex_port,port_end):
    ports = port_begin+'-'+port_end
    request = nm.scan (ip, ports, arguments='-Pn -sV -A')
    print('IP: ',ip)
    print('Estado: ',nm[ip].state())
    print("----------------------------")
    for protocol in nm[ip].all_protocols():
      print('Protocolo: ',protocol)
      allports = nm[ip][protocol].keys()
      for port in allports:
         print('    ',port,'Estado: ',nm[ip][protocol][port]['state'],' ',nm[ip][protocol][port]['name'],' ',nm[ip][protocol][port]['version'])
   
    print('Fin de analisis ..\n')
    print('-----------------------------')
    print('Enviando info ..')
    request = json.dumps(request, indent=4)
    try:
     r = requests.post(url, json=request)
    except requests.exceptions.RequestException as e:
       print('No se puedo establecer la conexión..')
       for i in range(3):
         print('...')
       print('Almacenando informacion en data.json\n')
       with open("data.json", "w") as outfile:
        outfile.write(request)
       raise SystemExit(e)
    

 else:
    print('Puertos incorrentos\n')

else:
    print('La IP no es correcta')
