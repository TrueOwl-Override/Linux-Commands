# 🧪 Labs

> Comandos aprendidos resolviendo laboratorios (OverTheWire Bandit): SSH, filtrado, binarios, cron, git y más.

**58** comandos · **65** parámetros · **29** temas  ·  [⬅ Volver al índice](../README.md)

## Temas

1. [Conexiones SSH](#conexiones-ssh)
2. [Lectura de archivos especiales [1-2]](#lectura-de-archivos-especiales-1-2)
3. [Lectura de archivos especiales [2-2]](#lectura-de-archivos-especiales-2-2)
4. [Directorios y archivos ocultos](#directorios-y-archivos-ocultos)
5. [Búsquedas precisas de archivos [1-2]](#busquedas-precisas-de-archivos-1-2)
6. [Métodos de filtrado de datos [1-2]](#metodos-de-filtrado-de-datos-1-2)
7. [Método de filtrado de datos [2-2]](#metodo-de-filtrado-de-datos-2-2)
8. [Interpretación de archivos binarios](#interpretacion-de-archivos-binarios)
9. [Codificación y decodificación en base64](#codificacion-y-decodificacion-en-base64)
10. [Cifrado césar y uso de tr](#cifrado-cesar-y-uso-de-tr)
11. [Descompresor recursivo en Bash](#descompresor-recursivo-en-bash)
12. [Pares de claves y conexiones SSH](#pares-de-claves-y-conexiones-ssh)
13. [Uso de netcat para realizar conexiones](#uso-de-netcat-para-realizar-conexiones)
14. [Uso de conexiones encriptadas](#uso-de-conexiones-encriptadas)
15. [Creando nuestros propios escáneres en Bash](#creando-nuestros-propios-escaneres-en-bash)
16. [Ejecución de comandos por SSH](#ejecucion-de-comandos-por-ssh)
17. [Detección de diferencias entre archivos](#deteccion-de-diferencias-entre-archivos)
18. [Abusando de privilegio SUID para migrar de usuario](#abusando-de-privilegio-suid-para-migrar-de-usuario)
19. [Abusando de tareas Cron [1-3]](#abusando-de-tareas-cron-1-3)
20. [Abusando de tareas Cron [2-3]](#abusando-de-tareas-cron-2-3)
21. [Abusando de tareas Cron [3-3]](#abusando-de-tareas-cron-3-3)
22. [Escapando del contexto de un comando](#escapando-del-contexto-de-un-comando)
23. [Fuerza bruta aplicada a conexiones](#fuerza-bruta-aplicada-a-conexiones)
24. [Operando con proyectos de Github [1-5]](#operando-con-proyectos-de-github-1-5)
25. [Operando con proyectos de Github [2-5]](#operando-con-proyectos-de-github-2-5)
26. [Operando con proyectos de Github [3-5]](#operando-con-proyectos-de-github-3-5)
27. [Operando con proyectos de Github [4-5]](#operando-con-proyectos-de-github-4-5)
28. [Operando con proyectos de Github [5-5]](#operando-con-proyectos-de-github-5-5)
29. [Argumentos posicionales en Bash](#argumentos-posicionales-en-bash)

---

<a id="conexiones-ssh"></a>

## Conexiones SSH

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `ssh` | Conecta de forma remota y segura a otro equipo por la red, con usuario y contraseña o clave SSH | `ssh usuario@192.168.1.10` |
| `sshpass` | Pasa la contraseña de una conexión SSH directamente en el comando; útil para automatizar scripts | `sshpass -p 'mi_clave' ssh usuario@192.168.1.10` |
| `export` | Convierte una variable en variable de entorno, disponible para otros procesos abiertos desde esa terminal | `export TERM=xterm` |

<details open>
<summary><b>🔧 Parámetros y usos (4)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `ssh` | `-p` | Especifica el puerto al que conectarse cuando el servidor SSH no usa el puerto por defecto (22) | `ssh -p 2222 usuario@192.168.1.10` |
| `export` | `TERM=xterm` | Define el tipo de terminal; útil ante problemas de compatibilidad en una conexión remota | `export TERM=xterm` |
| `sshpass` | `-p` | Indica la contraseña directamente en el comando para no escribirla manualmente al conectarse por SSH | `sshpass -p 'mi_clave' ssh usuario@192.168.1.10` |
| `ssh` | `bandit0@bandit.labs.overthewire.org -p 2220` | Se conecta al servidor de Bandit con el usuario bandit0 en el puerto 2220 en vez del 22 | `ssh bandit0@bandit.labs.overthewire.org -p 2220` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="lectura-de-archivos-especiales-1-2"></a>

## Lectura de archivos especiales [1-2]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `rev` | Invierte el orden de los caracteres de cada línea, mostrando el texto al revés | `echo "hola" \| rev` |
| `tr` | Traduce o reemplaza caracteres del texto que recibe por otros | `echo "a:b:c" \| tr ':' ' '` |
| `head` | Muestra las primeras líneas de un archivo o texto (10 por defecto) | `head -n 1 archivo.txt` |

<details open>
<summary><b>🔧 Parámetros y usos (10)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `cat` | `/home/bandit1/-` | Lee el archivo llamado "-" con su ruta absoluta, evitando que cat lo confunda con la entrada estándar | `cat /home/bandit1/-` |
| `cat` | `./-` | Lee el archivo "-" indicando que está en el directorio actual, evitando la confusión con stdin | `cat ./-` |
| `cat` | `$(pwd)/-` | Combina pwd (ruta actual) con el nombre del archivo; mismo efecto que la ruta absoluta | `cat $(pwd)/-` |
| `grep` | `-r "\w"` | Busca recursivamente líneas con al menos un carácter alfanumérico para encontrar contenido en archivos de cualquier carpeta | `grep -r "\w" /home/usuario/` |
| `cut` | `-d ':' -f 2` | Divide cada línea usando ":" como delimitador y extrae solo el segundo campo | `echo "a:b:c" \| cut -d ':' -f 2` |
| `tr` | `':' ' '` | Reemplaza cada ":" por un espacio en el texto procesado | `echo "a:b:c" \| tr ':' ' '` |
| `awk` | `'{print $2}' FS=":"` | Usa ":" como separador de campo (FS) e imprime la segunda columna de cada línea | `echo "a:b:c" \| awk '{print $2}' FS=":"` |
| `awk` | `'NF{print $NF}'` | Imprime el último campo de cada línea; NF es el número de campos y $NF el valor del último | `echo "uno dos tres" \| awk 'NF{print $NF}'` |
| `tail` | `-n 1` | Muestra únicamente la última línea del archivo o texto procesado | `tail -n 1 archivo.txt` |
| `head` | `-n 1` | Muestra únicamente la primera línea del archivo o texto procesado | `head -n 1 archivo.txt` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="lectura-de-archivos-especiales-2-2"></a>

## Lectura de archivos especiales [2-2]

<details open>
<summary><b>🔧 Parámetros y usos (4)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `cat` | `"spaces in this filename"` | Lee un archivo con espacios usando comillas para que se interprete como un solo nombre | `cat "spaces in this filename"` |
| `cat` | `spaces\ in\ this\ filename` | Lee un archivo con espacios escapando cada espacio con barra invertida para que no sean separadores de argumentos | `cat spaces\ in\ this\ filename` |
| `cat` | `s*` | Usa un comodín para completar el nombre automáticamente, siempre que no haya otros archivos que empiecen igual | `cat s*` |
| `cat` | `home/bandit/s*` | Igual que el anterior, especificando la ruta donde se encuentra el archivo | `cat home/bandit/s*` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="directorios-y-archivos-ocultos"></a>

## Directorios y archivos ocultos

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `file` | Analiza un archivo y muestra qué tipo de contenido tiene, sin importar su extensión | `file imagen.png` |

<details open>
<summary><b>🔧 Parámetros y usos (2)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `find` | `.` | Lista todos los archivos y carpetas del directorio actual, incluyendo subdirectorios | `find .` |
| `grep` | `-vE "bashrc\\|profile"` | Muestra las líneas que NO coinciden con "bashrc" ni "profile"; -v invierte la coincidencia y -E permite regex extendidas (\\| significa "o") | `ls -a \| grep -vE "bashrc\|profile"` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="busquedas-precisas-de-archivos-1-2"></a>

## Búsquedas precisas de archivos [1-2]

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `find` | `-size` | Filtra la búsqueda según el tamaño del archivo | `find -size 1033c` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="metodos-de-filtrado-de-datos-1-2"></a>

## Métodos de filtrado de datos [1-2]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `sed` | Busca, reemplaza, elimina o modifica texto de un archivo o flujo de datos, generalmente con expresiones regulares | `sed 's/viejo/nuevo/g' archivo.txt` |

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="metodo-de-filtrado-de-datos-2-2"></a>

## Método de filtrado de datos [2-2]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `sort` | Ordena las líneas de un archivo o texto, alfabética o numéricamente | `sort nombres.txt` |
| `uniq` | Elimina líneas duplicadas consecutivas; normalmente se usa después de sort | `sort nombres.txt \| uniq` |

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `uniq` | `-u` | Muestra solo las líneas completamente únicas, que no se repiten en el texto | `sort datos.txt \| uniq -u` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="interpretacion-de-archivos-binarios"></a>

## Interpretación de archivos binarios

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `strings` | Muestra las cadenas de texto legible (ASCII) dentro de un archivo binario; útil para hallar información oculta | `strings programa.bin` |

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="codificacion-y-decodificacion-en-base64"></a>

## Codificación y decodificación en base64

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `base64` | Convierte un texto o archivo a formato Base64, o lo decodifica de vuelta a su forma original, según el parámetro usado | `echo "hola" \| base64` |

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `base64` | `-d` | Decodifica un texto en Base64 devolviéndolo a su forma original | `echo "aG9sYQ==" \| base64 -d` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="cifrado-cesar-y-uso-de-tr"></a>

## Cifrado césar y uso de tr

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `tr` | `'[A-Za-z]' '[N-ZA-Mn-za-m]'` | Reemplaza cada letra por la que está 13 posiciones adelante, aplicando el cifrado ROT13 | `echo "Uryyb" \| tr '[A-Za-z]' '[N-ZA-Mn-za-m]'` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="descompresor-recursivo-en-bash"></a>

## Descompresor recursivo en Bash

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `xxd` | Muestra el contenido de un archivo en formato hexadecimal | `xxd archivo.bin` |
| `tee` | Muestra la salida de un comando en pantalla y la guarda en un archivo a la vez | `ls \| tee lista.txt` |
| `sponge` | Lee toda la entrada antes de escribirla en un archivo, evitando problemas al sobrescribir el mismo archivo leído | `sort datos.txt \| sponge datos.txt` |
| `ghex` | Editor hexadecimal con interfaz gráfica para ver y modificar bytes de un archivo | `ghex archivo.bin` |
| `7z` | Comprime y descomprime archivos en formato .7z | `7z a respaldo.7z carpeta/` |
| `sleep` | Pausa la ejecución del script un tiempo determinado en segundos | `sleep 5` |
| `trap` | Captura una señal (como Ctrl+C) y ejecuta una función en vez de terminar el script de inmediato | `trap ctrl_c INT` |
| `!?` | Busca en el historial el comando más reciente que contenga el texto indicado y lo vuelve a ejecutar | `!?ssh` |
| `while` | Bucle que repite un bloque de código mientras se cumpla una condición | `while [ $i -lt 5 ]; do echo $i; i=$((i+1)); done` |

<details open>
<summary><b>🔧 Parámetros y usos (9)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `xxd` | `-p` | Muestra la salida en hexadecimal plano, sin direcciones ni texto al lado | `xxd -p archivo.bin` |
| `xxd` | `-s` | Salta a un offset específico del archivo antes de mostrarlo en hexadecimal | `xxd -s 16 archivo.bin` |
| `xxd` | `-r` | Revierte un volcado hexadecimal de vuelta a binario | `xxd -r datos.hex salida.bin` |
| `7z` | `l` | Lista el contenido de un archivo comprimido sin extraerlo | `7z l respaldo.7z` |
| `7z` | `x` | Extrae el contenido de un archivo comprimido respetando la estructura de carpetas | `7z x respaldo.7z` |
| `trap` | `ctrl_c INT` | Captura la señal Ctrl+C y ejecuta una función en vez de terminar el script de inmediato | `trap ctrl_c INT` |
| `exit` | `1` | Termina el script con código de salida 1, indicando error | `exit 1` |
| `function` | `ctrl_c(){}` | Define la función ctrl_c, que se ejecuta cuando trap captura Ctrl+C | `function ctrl_c(){ echo "Saliendo..."; exit 1; }` |
| `while` | `[ ]; do; done` | Repite el bloque de código mientras la condición entre corchetes sea verdadera | `while [ -f archivo.gz ]; do gunzip archivo.gz; done` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="pares-de-claves-y-conexiones-ssh"></a>

## Pares de claves y conexiones SSH

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `ssh-keygen` | Genera un par de claves SSH (pública y privada) para autenticarse sin contraseña | `ssh-keygen -t ed25519` |
| `ssh-copy-id` | Copia la clave pública SSH generada hacia authorized_keys de un servidor remoto | `ssh-copy-id usuario@192.168.1.10` |

<details open>
<summary><b>🔧 Parámetros y usos (3)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `ssh-copy-id` | `-i` | Especifica el archivo de clave pública a copiar cuando hay varias claves | `ssh-copy-id -i ~/.ssh/id_ed25519.pub usuario@192.168.1.10` |
| `ssh` | `-i` | Especifica el archivo de clave privada a usar para autenticarse por SSH | `ssh -i ~/.ssh/id_ed25519 usuario@192.168.1.10` |
| `cat` | `~/.ssh/authorized_keys` | Archivo con las claves públicas SSH autorizadas para entrar a esa cuenta sin contraseña | `cat ~/.ssh/authorized_keys` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="uso-de-netcat-para-realizar-conexiones"></a>

## Uso de netcat para realizar conexiones

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `nc` | Herramienta de línea de comandos (netcat) para crear conexiones TCP/UDP manuales, enviar/recibir datos, escanear puertos o crear shells remotas | `nc 192.168.1.10 80` |
| `ss` | Muestra información sobre los sockets de red activos, alternativa moderna a netstat | `ss` |
| `lsof` | Muestra una lista de archivos abiertos por los procesos en ejecución, incluyendo conexiones de red | `lsof /var/log/syslog` |
| `ps` | Muestra los procesos en ejecución en el sistema | `ps` |
| `bc` | Calculadora de la terminal; permite hacer operaciones y convertir números entre bases (hexadecimal, decimal) | `echo "obase=10; ibase=16; FF" \| bc` |
| `for` | Bucle que recorre una lista de elementos uno por uno y ejecuta un bloque de código por cada uno | `for i in $(seq 1 5); do echo $i; done` |

<details open>
<summary><b>🔧 Parámetros y usos (8)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `ss` | `-nltp` | Muestra sockets en escucha TCP, sin resolver nombres, mostrando el proceso asociado | `sudo ss -nltp` |
| `lsof` | `-i:` | Filtra la salida mostrando solo las conexiones relacionadas con el puerto especificado | `sudo lsof -i:80` |
| `ps` | `-faux` | Muestra todos los procesos de todos los usuarios en formato detallado y jerárquico | `ps -faux` |
| `ps` | `-eo command` | Muestra solo la columna del comando ejecutado por cada proceso | `ps -eo command` |
| `echo` | `"obase=10; ibase=16; $hexNum" \| bc` | Convierte el valor hexadecimal de una variable a decimal usando bc | `hexNum="FF"; echo "obase=10; ibase=16; $hexNum" \| bc` |
| `cat` | `/proc/net/tcp` | Archivo virtual con las conexiones TCP activas (IP, puertos y estado) en formato hexadecimal | `cat /proc/net/tcp` |
| `while` | `read line; do; done` | Lee una entrada línea por línea y ejecuta el bloque de código por cada línea leída | `cat lista.txt \| while read line; do echo $line; done` |
| `for` | `line in; do; done` | Recorre uno por uno los elementos de una lista y ejecuta el bloque por cada elemento | `for line in $(cat lista.txt); do echo $line; done` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="uso-de-conexiones-encriptadas"></a>

## Uso de conexiones encriptadas

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `ncat` | Versión mejorada de netcat (proyecto Nmap) con soporte para conexiones cifradas SSL/TLS y autenticación | `ncat 192.168.1.10 4444` |

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `ncat` | `--ssl` | Cifra la conexión usando SSL/TLS para proteger los datos transmitidos | `ncat --ssl 192.168.1.10 443` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="creando-nuestros-propios-escaneres-en-bash"></a>

## Creando nuestros propios escáneres en Bash

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `seq` | Genera una secuencia de números dentro de un rango, útil para bucles o scripts | `seq 1 10` |
| `mktemp` | Crea un archivo temporal con nombre único, evitando conflictos con otros archivos | `mktemp` |
| `wait` | Espera a que terminen uno o varios procesos en segundo plano antes de continuar | `sleep 5 & wait` |
| `tput` | Controla aspectos de la terminal, como ocultar o volver a mostrar el cursor | `tput civis` |
| `(comando)` | Ejecuta el comando dentro de un subshell, en un proceso hijo separado del script principal | `(ping -c 1 192.168.1.1) &` |
| `/dev/tcp/$ip/$port` | Ruta especial de Bash que abre una conexión TCP a la IP y puerto indicados como si fuera un archivo, sin netcat | `echo '' > /dev/tcp/127.0.0.1/22 && echo "abierto"` |

<details open>
<summary><b>🔧 Parámetros y usos (4)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `mktemp` | `-d` | Crea una carpeta temporal en vez de un archivo, con nombre único | `mktemp -d` |
| `timeout` | `1 bash -c ""` | Ejecuta un comando con un límite de tiempo (1 segundo); si no termina, se cancela | `timeout 1 bash -c "echo > /dev/tcp/127.0.0.1/22" && echo "abierto"` |
| `tput` | `civis` | Oculta el cursor de la terminal | `tput civis` |
| `tput` | `cnorm` | Vuelve a mostrar el cursor de la terminal en su forma normal | `tput cnorm` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="ejecucion-de-comandos-por-ssh"></a>

## Ejecución de comandos por SSH

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `ssh` | `usuario@host "comando"` | Ejecuta un comando directamente en el servidor remoto al conectar, sin cargar una sesión interactiva completa ni el bashrc del usuario | `ssh usuario@192.168.1.10 "ls -la"` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="deteccion-de-diferencias-entre-archivos"></a>

## Detección de diferencias entre archivos

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `diff` | Compara dos archivos línea por línea y muestra las diferencias entre ellos | `diff archivo1.txt archivo2.txt` |

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="abusando-de-privilegio-suid-para-migrar-de-usuario"></a>

## Abusando de privilegio SUID para migrar de usuario

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `bash` | Inicia una nueva instancia del intérprete Bash, para abrir shell interactiva, ejecutar scripts o evadir shells limitadas | `bash` |

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `bash` | `-p` | Inicia la shell en modo privilegiado, evitando que se reseteen el UID/GID efectivos, útil para mantener privilegios obtenidos por SUID | `bash -p` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="abusando-de-tareas-cron-1-3"></a>

## Abusando de tareas Cron [1-3]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `crontab` | Permite ver, crear y editar las tareas Cron (tareas programadas) de un usuario | `crontab -l` |

<details open>
<summary><b>🔧 Parámetros y usos (2)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `ls` | `/etc/cron.d` | Directorio donde se almacenan los archivos de configuración de las tareas Cron del sistema | `ls -l /etc/cron.d` |
| `crontab` | `* * * * * comando` | Formato de una tarea Cron: Minuto Hora Día-del-mes Mes Día-de-la-semana Comando; el * significa todos los valores (cada minuto, hora, etc.) | `* * * * * /home/user/script.sh` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="abusando-de-tareas-cron-2-3"></a>

## Abusando de tareas Cron [2-3]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `md5sum` | Calcula y muestra el hash MD5 de un archivo o entrada, útil para comprobar si su contenido ha cambiado | `md5sum archivo.txt` |

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="abusando-de-tareas-cron-3-3"></a>

## Abusando de tareas Cron [3-3]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `stat` | Muestra información detallada de un archivo o directorio: permisos, tamaño y fechas de acceso y modificación | `stat archivo.txt` |
| `timeout` | Ejecuta un comando y lo termina automáticamente si supera el tiempo especificado | `timeout 5 ping 8.8.8.8` |
| `watch` | Ejecuta un comando de forma repetida a intervalos regulares y muestra su salida actualizada en pantalla | `watch ls -l /tmp` |

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `watch` | `-n 1` | Define el intervalo en segundos entre cada ejecución del comando; en este caso cada 1 segundo | `watch -n 1 ls -l /tmp` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="escapando-del-contexto-de-un-comando"></a>

## Escapando del contexto de un comando

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `more` | Muestra la salida de un comando o archivo una página a la vez (espacio avanza, q sale) | `cat /etc/passwd \| more` |

<details open>
<summary><b>🔧 Parámetros y usos (3)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `more` | `v` | Desde more, abre el modo visual (editor vi) sobre el contenido | `v (dentro de more)` |
| `more` | `:set shell=/bin/bash` | Ya en el modo visual (tras Esc + Shift + :), define Bash como la shell a usar | `:set shell=/bin/bash` |
| `more` | `:shell` | Abre una shell interactiva desde el modo visual, escapando del contexto de more | `:shell` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="fuerza-bruta-aplicada-a-conexiones"></a>

## Fuerza bruta aplicada a conexiones

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `{0000..9999}` | Expansión de llaves: genera una secuencia de valores (aquí del 0000 al 9999), útil como secuenciador en bucles | `for i in {0000..9999}; do echo $i; done` |

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="operando-con-proyectos-de-github-1-5"></a>

## Operando con proyectos de Github [1-5]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `git clone` | Descarga una copia completa de un repositorio remoto (como GitHub), con todos sus archivos e historial | `git clone https://github.com/usuario/proyecto.git` |

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="operando-con-proyectos-de-github-2-5"></a>

## Operando con proyectos de Github [2-5]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `git log` | Lista todos los commits del proyecto con su identificador, autor, fecha y mensaje | `git log` |
| `git show` | Muestra las propiedades y los cambios aplicados en un commit concreto | `git show a1b2c3d` |

<details open>
<summary><b>🔧 Parámetros y usos (2)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `git show` | `(id del commit)` | Muestra todos los cambios que se aplicaron en ese commit | `git show a1b2c3d` |
| `git checkout` | `(id del commit)` | Regresa el proyecto a ese punto de la historia, restaurando los archivos que existían entonces | `git checkout a1b2c3d` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="operando-con-proyectos-de-github-3-5"></a>

## Operando con proyectos de Github [3-5]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `git branch` | Crea, lista, elimina y renombra ramas; no sirve para cambiar de rama ni para unirlas | `git branch` |
| `git checkout` | Cambia a otra rama o regresa el proyecto al estado de un commit anterior | `git checkout main` |

<details open>
<summary><b>🔧 Parámetros y usos (2)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `git branch` | `-a` | Lista todas las ramas del proyecto, tanto locales como remotas | `git branch -a` |
| `git checkout` | `(nombre de la rama)` | Cambia a la rama indicada por su nombre | `git checkout develop` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="operando-con-proyectos-de-github-4-5"></a>

## Operando con proyectos de Github [4-5]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `git tag` | Lista todas las etiquetas (tags) del repositorio; un tag es un nombre que marca de forma inalterable un commit específico | `git tag` |

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `git show` | `(nombre del tag)` | Muestra la información del tag indicado y del commit al que apunta, con sus cambios | `git show v1.0` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="operando-con-proyectos-de-github-5-5"></a>

## Operando con proyectos de Github [5-5]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `git add` | Agrega archivos al área de preparación para incluirlos en el próximo commit | `git add archivo.txt` |
| `git commit` | Guarda los cambios preparados creando una nueva versión del proyecto en el repositorio local | `git commit -m "Primer cambio"` |
| `git push` | Sube los commits del repositorio local al repositorio remoto | `git push origin master` |

<details open>
<summary><b>🔧 Parámetros y usos (3)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `git add` | `-f` | Fuerza agregar el archivo al área de preparación aunque esté ignorado por el .gitignore | `git add -f key.txt` |
| `git commit` | `-m "identifier"` | Define el mensaje que identifica al commit | `git commit -m "Agrego key.txt"` |
| `git push` | `-u origin branch` | Sube los commits a la rama indicada del remoto origin y la deja vinculada para que los siguientes push/pull no necesiten especificarla | `git push -u origin master` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="argumentos-posicionales-en-bash"></a>

## Argumentos posicionales en Bash

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `$0` | Variable con el nombre del script que se invocó desde la terminal | `echo $0` |
| `$1, $2...` | Primer, segundo (y así sucesivamente) argumento recibido desde la línea de comandos | `./script.sh hola mundo → echo $1` |
| `$#` | Contiene el número de argumentos recibidos desde la línea de comandos | `echo "Recibí $# argumentos"` |
| `$*` | Contiene todos los argumentos recibidos desde la línea de comandos en una sola variable | `echo "Argumentos: $*"` |

<sub>[⬆ Arriba](#temas)</sub>
