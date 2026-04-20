El sistema cuenta con 2 tipos de uso, el primero con un login que exporta las cookies.txt que debe existir en la raiz del proyecto como main.py
Yo las obtuve mediante la extension Get cookies.txt, te ayuda a viasualizar tus cookies de forma general y en el sitio web actual
y la estructura se ve asi:
# https://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file! Do not edit.
.instagram.com	TRUE	/	TRUE	1792243704	datr	*****************

.instagram.com	TRUE	/	TRUE	1792243704	ig_did	***************

.instagram.com	TRUE	/	TRUE	1792243704	mid	*******************

.instagram.com	TRUE	/	TRUE	1777304786	wd	*******************

.instagram.com	TRUE	/	TRUE	1792251997	csrftoken	*************

.instagram.com	TRUE	/	TRUE	1792245889	ps_l	1

.instagram.com	TRUE	/	TRUE	1792245889	ps_n	1

.instagram.com	TRUE	/	TRUE	1784475997	ds_user_id	************

.instagram.com	TRUE	/	TRUE	1792251011	sessionid	************-g

.instagram.com	TRUE	/	TRUE	0	rur	"LDC\******\****************"

Se ejecuta mediante el python main.py
La segunda forma es sin login, pero solo deja ver cuentas publicas, en el anterior caso publicas y privadas que yo siga
y se ejecuta mediante el comando python sin_login.py

Ambos lo primero que harán es pedir el username de instgram del cual queremos recopilar la data, verificar si existe, o si la cuenta no es privada
y posrteriormente generará un .xlsx con la data

Nota: Sin embargo por las politicas y estructura web de instagram me es imposible extraer la metadata sin que instagram detecte el script como un bot y bloquee la comunicación
JSON Query to graphql/query: 403 Forbidden when accessing https://www.instagram.com/graphql/query [retrying; skip with ^C]
