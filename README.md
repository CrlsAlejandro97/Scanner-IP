# Scanner-IP

Librerías:
•	Nmap: Se utiliza para realizar los métodos de escaneo de la IP que se ingresa
•	re: Se utiliza para realizar validación de los datos de entrada
•	json: Se utiliza para enviar la salida en formato json
•	request: Se utiliza para realizar las peticiones http

Descripción: En primera instancia, se realizan las validaciones de ip y puerto que correspondan con su expresión regular, una vez que esto se realiza se procede a scanner la ip en el rango de puertos indicado, se solicita al usuario que ingrese el inicio y fin del rango.
Recorremos el diccionario con los protocolos que fueron analizados, se itera sobre cada protocolo para obtener el análisis de los puertos para obtener el banner, según la técnica banner Gabbing.
Para finalizar, se intenta enviar la información a través de un post a la url especificada pero como se indico en la consigna es una url fake por lo que se almacena la información obtenida en archivo con extensión json.
