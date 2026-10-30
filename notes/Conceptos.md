# 🧠 Conceptos

> Fundamentos de la terminal: usuarios, permisos, redirecciones, búsquedas y primeros scripts.

**63** comandos · **66** parámetros · **17** temas  ·  [⬅ Volver al índice](../README.md)

## Temas

1. [Comandos básicos de Linux [1-2]](#comandos-basicos-de-linux-1-2)
2. [Comandos básicos de Linux [2-2]](#comandos-basicos-de-linux-2-2)
3. [Control del flujo stderr-stdout, operadores y procesos en segundo plano](#control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano)
4. [Descriptores de archivo](#descriptores-de-archivo)
5. [Lectura e interpretación de permisos [1-2]](#lectura-e-interpretacion-de-permisos-1-2)
6. [Lectura e interpretación de permisos [2-2]](#lectura-e-interpretacion-de-permisos-2-2)
7. [Asignación de permisos [1-2]](#asignacion-de-permisos-1-2)
8. [Asignación de permisos [2-2]](#asignacion-de-permisos-2-2)
9. [Notación octal de permisos](#notacion-octal-de-permisos)
10. [Permisos especiales - Sticky Bit](#permisos-especiales-sticky-bit)
11. [Control de atributos de ficheros - Chattr y Lsattr](#control-de-atributos-de-ficheros-chattr-y-lsattr)
12. [Permisos especiales - SUID y SGID](#permisos-especiales-suid-y-sgid)
13. [Privilegios especiales - Capabilities](#privilegios-especiales-capabilities)
14. [Uso de bashrc y zshrc](#uso-de-bashrc-y-zshrc)
15. [Actualización y Upgradeo del sistema](#actualizacion-y-upgradeo-del-sistema)
16. [Búsquedas a nivel de sistema](#busquedas-a-nivel-de-sistema)
17. [Creación de scripts en Bash](#creacion-de-scripts-en-bash)

---

<a id="comandos-basicos-de-linux-1-2"></a>

## Comandos básicos de Linux [1-2]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `whoami` | Muestra el nombre del usuario con el que estás conectado actualmente | `whoami` |
| `id` | Muestra información del usuario: UID, GID y grupos a los que pertenece | `id root` |
| `sudo` | Ejecuta un solo comando con permisos de administrador sin cambiar de usuario | `sudo apt update` |
| `exit` | Cierra la sesión actual o sale de una sesión elevada (como root) | `exit` |
| `cat` | Muestra el contenido de un archivo en la terminal | `cat notas.txt` |
| `which` | Muestra la ubicación donde está instalado un comando o programa | `which python3` |
| `echo` | Imprime texto o el valor de una variable en la terminal | `echo "Hola mundo"` |
| `grep` | Busca y filtra líneas de texto que coincidan con un patrón | `grep "error" log.txt` |
| `\|` | Pipe: conecta la salida de un comando como entrada del siguiente | `cat /etc/passwd \| grep root` |
| `Ctrl + L` | Atajo que limpia la pantalla de la terminal sin perder el historial | `Ctrl + L (equivale a escribir clear)` |

<details open>
<summary><b>🔧 Parámetros y usos (4)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `sudo` | `su` | Cambia a la sesión de root de forma permanente hasta que salgas | `sudo su` |
| `grep` | `-n` | Muestra el número de línea de cada coincidencia | `grep -n "root" /etc/passwd` |
| `cat` | `/etc/group` | Archivo con los grupos existentes y sus usuarios | `cat /etc/group` |
| `echo` | `$PATH` | Variable con las carpetas donde el sistema busca los comandos | `echo $PATH` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="comandos-basicos-de-linux-2-2"></a>

## Comandos básicos de Linux [2-2]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `pwd` | Muestra la ruta completa del directorio actual | `pwd` |
| `ls` | Lista archivos y carpetas del directorio actual | `ls /etc` |
| `cd` | Cambia de directorio | `cd /var/log` |
| `bash` | Intérprete de comandos que procesa y ejecuta lo que escribes | `bash script.sh` |
| `command` | Con -v muestra la ruta o ubicación de un comando, similar a which | `command -v python3` |

<details open>
<summary><b>🔧 Parámetros y usos (12)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `command` | `-v` | Muestra la ruta de un comando, similar a which | `command -v python3` |
| `ls` | `-l` | Lista en formato detallado (permisos, dueño, tamaño, fecha) | `ls -l /etc` |
| `cd` | `.` | Se queda en la carpeta actual | `cd .` |
| `cd` | `..` | Sube un nivel a la carpeta anterior | `cd ..` |
| `cd` | `(ruta absoluta)` | Va a una ubicación específica desde la raíz del sistema | `cd /var/log` |
| `cd` | `(ruta relativa)` | Va a una ubicación según el directorio actual | `cd ../documentos` |
| `cd` | `/` | Va directo a la raíz del sistema | `cd /` |
| `cd` | `~` | Va a la carpeta personal (home) del usuario | `cd ~` |
| `echo` | `$HOME` | Variable con la ruta de la carpeta personal del usuario | `echo $HOME` |
| `echo` | `$SHELL` | Variable con la ruta del intérprete de comandos en uso (bash, zsh) | `echo $SHELL` |
| `cat` | `/etc/passwd` | Archivo con información básica de los usuarios (UID, home, shell) | `cat /etc/passwd` |
| `cat` | `/etc/shells` | Archivo con las shells disponibles e instaladas | `cat /etc/shells` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano"></a>

## Control del flujo stderr-stdout, operadores y procesos en segundo plano

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `disown` | Desvincula un proceso en segundo plano de la terminal para que siga corriendo al cerrarla | `sleep 100 & disown` |
| `;` | Ejecuta comandos en secuencia sin importar si el anterior falló | `cd /tmp ; ls` |
| `&&` | Ejecuta el siguiente comando solo si el anterior tuvo éxito | `mkdir prueba && cd prueba` |
| `\|\|` | Ejecuta el siguiente comando solo si el anterior falló | `ping -c 1 8.8.8.8 \|\| echo "sin conexión"` |
| `&` | Ejecuta el comando en segundo plano dejando la terminal libre | `sleep 60 &` |
| `2>/dev/null` | Envía los errores (stderr) a /dev/null para no mostrarlos | `find / -name "*.conf" 2>/dev/null` |
| `2>&1` | Redirige stderr a stdout, mostrando todo junto | `ls /noexiste > salida.txt 2>&1` |
| `&>/dev/null` | Envía salida normal y errores a /dev/null, ocultando todo | `ping -c 1 8.8.8.8 &>/dev/null` |

<details open>
<summary><b>🔧 Parámetros y usos (2)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `cat` | `/etc/hosts` | Archivo con asociaciones manuales entre IP y dominios sin usar DNS | `cat /etc/hosts` |
| `echo` | `$?` | Código de salida del último comando (0 éxito, otro valor error) | `ls /noexiste ; echo $?` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="descriptores-de-archivo"></a>

## Descriptores de archivo

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `>` | Redirige la salida a un archivo sobrescribiendo su contenido | `echo "hola" > archivo.txt` |
| `>>` | Redirige la salida a un archivo agregándola al final | `echo "otra línea" >> archivo.txt` |
| `exec` | Manipula los descriptores de archivo de la sesión actual (abrir, cerrar, redirigir) | `exec 3<> archivo.txt` |

<details open>
<summary><b>🔧 Parámetros y usos (5)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `exec` | `3<> file` | Abre "file" en lectura y escritura asignándolo al descriptor 3 | `exec 3<> archivo.txt` |
| `exec` | `>&3` | Redirige la salida estándar de la sesión al descriptor 3 | `exec >&3` |
| `exec` | `3>&-` | Cierra el descriptor 3 | `exec 3>&-` |
| `exec` | `5>&3` | Duplica el descriptor 3 en el descriptor 5 | `exec 5>&3` |
| `exec` | `8>&3-` | Duplica el descriptor 3 en el 8 y cierra el 3 original | `exec 8>&3-` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="lectura-e-interpretacion-de-permisos-1-2"></a>

## Lectura e interpretación de permisos [1-2]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `touch` | Crea un archivo vacío o actualiza su fecha de modificación si ya existe | `touch nuevo.txt` |
| `rm` | Elimina archivos o carpetas | `rm viejo.txt` |
| `nano` | Editor de texto sencillo en la terminal | `nano notas.txt` |
| `vi` | Editor de texto avanzado y potente, con curva de aprendizaje mayor que nano | `vi notas.txt` |

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="lectura-e-interpretacion-de-permisos-2-2"></a>

## Lectura e interpretación de permisos [2-2]

<details open>
<summary><b>🔧 Parámetros y usos (2)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `cat` | `/etc/shadow` | Archivo donde se guardan las contraseñas de usuarios cifradas | `sudo cat /etc/shadow` |
| `cat` | `/etc/login.defs` | Configuración del sistema; ENCRYPT_METHOD define el método de cifrado de contraseñas | `grep ENCRYPT_METHOD /etc/login.defs` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="asignacion-de-permisos-1-2"></a>

## Asignación de permisos [1-2]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `mkdir` | Crea una nueva carpeta | `mkdir proyectos` |
| `su` | Cambia de usuario en la terminal pidiendo su contraseña | `su - juan` |
| `chmod` | Modifica permisos de archivo o carpeta; + agrega y - quita permiso | `chmod 755 script.sh` |
| `chgrp` | Cambia el grupo propietario de un archivo o carpeta | `chgrp desarrollo archivo.txt` |
| `*` | Comodín que representa cualquier cosa para seleccionar varios archivos | `ls *.txt` |

<details open>
<summary><b>🔧 Parámetros y usos (3)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `chmod` | `o+w` | Agrega permiso de escritura a "others" (otros usuarios) | `chmod o+w archivo.txt` |
| `chmod` | `o-w` | Quita permiso de escritura a "others" (otros usuarios) | `chmod o-w archivo.txt` |
| `rm` | `-r` | Elimina carpetas con todo su contenido de forma recursiva | `rm -r carpeta_vieja` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="asignacion-de-permisos-2-2"></a>

## Asignación de permisos [2-2]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `useradd` | Crea un nuevo usuario en el sistema | `sudo useradd juan` |
| `passwd` | Establece o cambia la contraseña de un usuario | `sudo passwd juan` |
| `chown` | Cambia el dueño y/o grupo propietario de un archivo o carpeta | `sudo chown juan:desarrollo archivo.txt` |
| `groupadd` | Crea un nuevo grupo en el sistema | `sudo groupadd desarrollo` |
| `usermod` | Modifica propiedades de un usuario existente (grupo, home, shell) | `sudo usermod -s /bin/zsh juan` |

<details open>
<summary><b>🔧 Parámetros y usos (4)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `useradd` | `-s` | Define la shell del nuevo usuario | `sudo useradd -s /bin/bash juan` |
| `useradd` | `-d` | Define la carpeta home del nuevo usuario | `sudo useradd -d /home/juan juan` |
| `usermod` | `-a` | Junto con -G agrega al usuario a un grupo sin quitarlo de los actuales | `sudo usermod -a -G sudo juan` |
| `usermod` | `-G` | Define los grupos secundarios del usuario | `sudo usermod -G desarrollo,docker juan` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="notacion-octal-de-permisos"></a>

## Notación octal de permisos

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `chmod` | `755` | Notación octal: r=4, w=2, x=1 y se suman por bloque (propietario, grupo, otros); 755 equivale a rwxr-xr-x y 777 a permisos completos para todos | `chmod 755 script.sh` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="permisos-especiales-sticky-bit"></a>

## Permisos especiales - Sticky Bit

<details open>
<summary><b>🔧 Parámetros y usos (1)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `chmod` | `+t` | Activa el Sticky Bit en una carpeta: solo el dueño del archivo o root puede borrarlo o renombrarlo | `chmod +t /tmp/compartida` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="control-de-atributos-de-ficheros-chattr-y-lsattr"></a>

## Control de atributos de ficheros - Chattr y Lsattr

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `cp` | Copia archivos o carpetas de un lugar a otro | `cp archivo.txt copia.txt` |
| `lsattr` | Muestra los atributos especiales de un archivo (más allá de los permisos normales) | `lsattr archivo.txt` |
| `chattr` | Cambia los atributos especiales de un archivo (por ejemplo hacerlo inmutable) | `sudo chattr +i archivo.txt` |

<details open>
<summary><b>🔧 Parámetros y usos (3)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `rm` | `-f` | Fuerza la eliminación sin pedir confirmación, incluso si está protegido contra escritura | `rm -f archivo_protegido.txt` |
| `chattr` | `+i` | Hace el archivo inmutable: nadie puede modificarlo, borrarlo ni renombrarlo, ni root, hasta quitar el atributo | `sudo chattr +i archivo.txt` |
| `chattr` | `-V` | Modo detallado (verbose) al modificar el atributo | `sudo chattr -V +i archivo.txt` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="permisos-especiales-suid-y-sgid"></a>

## Permisos especiales - SUID y SGID

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `xargs` | Toma la salida de un comando y la usa como argumento de otro | `find . -name "*.log" \| xargs ls -l` |
| `find` | Busca archivos y carpetas según criterios (nombre, tipo, permisos, fecha, etc.) | `find /home -name "*.txt"` |

<details open>
<summary><b>🔧 Parámetros y usos (4)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `chmod` | `4000` | Valor octal del permiso especial SUID en notación numérica | `chmod 4755 programa` |
| `chmod` | `u+s` | Forma simbólica de activar SUID (bit s en ejecución del propietario) | `chmod u+s programa` |
| `chmod` | `2000` | Valor octal del permiso especial SGID en notación numérica | `chmod 2755 carpeta` |
| `chmod` | `g+s` | Forma simbólica de activar SGID (bit s en ejecución del grupo) | `chmod g+s carpeta` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="privilegios-especiales-capabilities"></a>

## Privilegios especiales - Capabilities

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `getcap` | Muestra las Capabilities asignadas a un archivo | `getcap /usr/bin/ping` |
| `setcap` | Asigna Capabilities específicas a un archivo sin dar todos los privilegios de root | `sudo setcap cap_net_raw+ep /usr/bin/ping` |
| `!$` | Representa el último argumento del comando anterior para reutilizarlo | `mkdir proyecto  y luego  cd !$` |

<details open>
<summary><b>🔧 Parámetros y usos (2)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `getcap` | `-r` | Busca y muestra Capabilities de forma recursiva en subcarpetas | `getcap -r / 2>/dev/null` |
| `setcap` | `-r` | Elimina las Capabilities asignadas a un archivo | `sudo setcap -r /usr/bin/ping` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="uso-de-bashrc-y-zshrc"></a>

## Uso de bashrc y zshrc

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `hostname` | Muestra o cambia el nombre del equipo en la red | `hostname` |
| `ifconfig` | Muestra y configura las interfaces de red (IP de cada tarjeta) | `ifconfig eth0` |
| `iwconfig` | Como ifconfig, pero para interfaces inalámbricas (WiFi) | `iwconfig wlan0` |
| `awk` | Procesa y filtra texto por columnas | `awk '{print $2}' datos.txt` |
| `cut` | Extrae partes de una línea de texto, dividiendo por un delimitador | `cut -d ":" -f 1 /etc/passwd` |
| `$()` | Ejecuta el comando entre paréntesis y devuelve su resultado (sustitución de comandos) | `echo "Estoy en $(pwd)"` |
| `function nombre(){ Comandos }` | Define una función personalizada que agrupa varios comandos bajo un nombre | `function saludar(){ echo "Hola $1"; }` |

<details open>
<summary><b>🔧 Parámetros y usos (7)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `ls` | `-a` | Muestra todos los archivos incluyendo los ocultos (con punto) | `ls -a ~` |
| `hostname` | `-I` | Muestra la o las direcciones IP asignadas al equipo | `hostname -I` |
| `cut` | `-d` | Define el delimitador para dividir el texto en columnas | `cut -d ":" -f 1 /etc/passwd` |
| `cut` | `-f` | Selecciona el número de campo (columna) a extraer | `cut -d ":" -f 3 /etc/passwd` |
| `awk` | `'{print $1}'` | Imprime la primera columna de cada línea | `ls -l \| awk '{print $1}'` |
| `alias` | `nombre='ruta_absoluta'` | Crea un atajo para ejecutar un comando o ruta larga con una palabra corta | `alias ll='ls -la'` |
| `export` | `nombre_de_la_variable` | Convierte una variable en variable de entorno disponible para otros procesos | `export MI_VAR="hola"` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="actualizacion-y-upgradeo-del-sistema"></a>

## Actualización y Upgradeo del sistema

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `parrot-upgrade` | Actualiza Parrot OS de forma segura sin romper componentes propios | `sudo parrot-upgrade` |
| `reboot` | Reinicia el equipo | `sudo reboot` |
| `apt` | Gestor de paquetes de Debian: actualiza la lista de paquetes (update) e instala sus actualizaciones (upgrade) | `sudo apt update` |

<details open>
<summary><b>🔧 Parámetros y usos (3)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `apt` | `update` | Actualiza la lista de paquetes disponibles desde los repositorios sin instalar nada | `sudo apt update` |
| `apt` | `upgrade` | Instala las actualizaciones de los paquetes instalados (no usar en Parrot) | `sudo apt upgrade` |
| `sudo` | `pacman -Syu` | Arch Linux: sincroniza la lista de paquetes y actualiza todo el sistema | `sudo pacman -Syu` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="busquedas-a-nivel-de-sistema"></a>

## Búsquedas a nivel de sistema

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `neofetch` | Muestra información del sistema (kernel, RAM, CPU, logo de la distro) de forma visual | `neofetch` |

<details open>
<summary><b>🔧 Parámetros y usos (8)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `find` | `-name` | Busca archivos por nombre exacto o con comodines | `find -name '*xampl*.sh'` |
| `find` | `-type` | Filtra por tipo: archivo (f) o carpeta (d) | `find /home -type f` |
| `find` | `-perm` | Filtra por los permisos específicos del archivo | `find / -perm -4000 2>/dev/null` |
| `find` | `-group` | Filtra por grupo propietario | `find /home -group desarrollo` |
| `find` | `-user` | Filtra por usuario propietario | `find /home -user juan` |
| `find` | `-writable` | Muestra solo archivos sobre los que tienes permiso de escritura | `find /etc -writable 2>/dev/null` |
| `find` | `-executable` | Muestra solo archivos sobre los que tienes permiso de ejecución | `find /usr/bin -executable -type f` |
| `find` | `-readable` | Muestra solo archivos sobre los que tienes permiso de lectura | `find /var -readable 2>/dev/null` |

</details>

<sub>[⬆ Arriba](#temas)</sub>

---

<a id="creacion-de-scripts-en-bash"></a>

## Creación de scripts en Bash

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `tail` | Muestra las últimas líneas de un archivo (10 por defecto), útil para logs | `tail /var/log/syslog` |
| `#!/bin/bash` | Shebang: primera línea del script, indica el intérprete (Bash) | `#!/bin/bash   (primera línea de script.sh)` |
| `variable="Hola"` | Declara una variable asignándole texto (sin espacios alrededor del =) | `saludo="Hola"; echo $saludo` |
| `$variable o ${variable}` | Accede al valor de una variable; las llaves delimitan el nombre si está pegado a otro texto | `archivo="datos"; echo "${archivo}_backup.txt"` |

<details open>
<summary><b>🔧 Parámetros y usos (5)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `tail` | `-n` | Define cuántas líneas finales mostrar | `tail -n 20 /var/log/syslog` |
| `awk` | `'NR==2'` | Muestra solo la línea número 2 (NR = número de registro) | `awk 'NR==2' archivo.txt` |
| `awk` | `FS="/"` | Define "/" como separador de campo (FS) para dividir en columnas | `echo "/home/juan" \| awk '{print $2}' FS="/"` |
| `echo` | `-e` | Activa la interpretación de caracteres especiales (\n, \t) en el texto impreso | `echo -e "línea1\nlínea2"` |
| `echo` | `-e "\n"` | \n representa un salto de línea; requiere el parámetro -e | `echo -e "Hola\nMundo"` |

</details>

<sub>[⬆ Arriba](#temas)</sub>
