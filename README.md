<div align="center">

# 🐧 Linux Commands

**Mis apuntes de comandos de Linux y Bash, organizados por tema, con ejemplos listos para copiar.**

![Comandos](https://img.shields.io/badge/comandos-130-2ea44f?style=for-the-badge) ![Parámetros](https://img.shields.io/badge/par%C3%A1metros-138-0969da?style=for-the-badge) ![Temas](https://img.shields.io/badge/temas-47-8250df?style=for-the-badge)

🌐 **Versión web con buscador:** [`docs/index.html`](docs/index.html)

</div>

---

## 📚 Secciones

| | Sección | Contenido | Comandos | Parámetros |
|:-:|:--|:--|:-:|:-:|
| 🧠 | **[Conceptos](notes/Conceptos.md)** | Fundamentos de la terminal: usuarios, permisos, redirecciones, búsquedas y primeros scripts. | 63 | 66 |
| 🧪 | **[Labs](notes/Labs.md)** | Comandos aprendidos resolviendo laboratorios (OverTheWire Bandit): SSH, filtrado, binarios, cron, git y más. | 58 | 65 |
| 📜 | **[Scripting](notes/Scripting.md)** | Herramientas para escribir scripts en Bash: opciones, condicionales, aritmética y peticiones HTTP. | 9 | 7 |

## 🗂️ Temas

<details>
<summary><b>🧠 Conceptos</b> — 17 temas</summary>

- [Comandos básicos de Linux [1-2]](notes/Conceptos.md#comandos-basicos-de-linux-1-2) — `whoami`, `id`, `sudo`, `exit`, `cat`, `which`, `echo`, `grep`, `\|`, `Ctrl + L`
- [Comandos básicos de Linux [2-2]](notes/Conceptos.md#comandos-basicos-de-linux-2-2) — `pwd`, `ls`, `cd`, `bash`, `command`
- [Control del flujo stderr-stdout, operadores y procesos en segundo plano](notes/Conceptos.md#control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano) — `disown`, `;`, `&&`, `\|\|`, `&`, `2>/dev/null`, `2>&1`, `&>/dev/null`
- [Descriptores de archivo](notes/Conceptos.md#descriptores-de-archivo) — `>`, `>>`, `exec`
- [Lectura e interpretación de permisos [1-2]](notes/Conceptos.md#lectura-e-interpretacion-de-permisos-1-2) — `touch`, `rm`, `nano`, `vi`
- [Lectura e interpretación de permisos [2-2]](notes/Conceptos.md#lectura-e-interpretacion-de-permisos-2-2) — <i>solo parámetros</i>
- [Asignación de permisos [1-2]](notes/Conceptos.md#asignacion-de-permisos-1-2) — `mkdir`, `su`, `chmod`, `chgrp`, `*`
- [Asignación de permisos [2-2]](notes/Conceptos.md#asignacion-de-permisos-2-2) — `useradd`, `passwd`, `chown`, `groupadd`, `usermod`
- [Notación octal de permisos](notes/Conceptos.md#notacion-octal-de-permisos) — <i>solo parámetros</i>
- [Permisos especiales - Sticky Bit](notes/Conceptos.md#permisos-especiales-sticky-bit) — <i>solo parámetros</i>
- [Control de atributos de ficheros - Chattr y Lsattr](notes/Conceptos.md#control-de-atributos-de-ficheros-chattr-y-lsattr) — `cp`, `lsattr`, `chattr`
- [Permisos especiales - SUID y SGID](notes/Conceptos.md#permisos-especiales-suid-y-sgid) — `xargs`, `find`
- [Privilegios especiales - Capabilities](notes/Conceptos.md#privilegios-especiales-capabilities) — `getcap`, `setcap`, `!$`
- [Uso de bashrc y zshrc](notes/Conceptos.md#uso-de-bashrc-y-zshrc) — `hostname`, `ifconfig`, `iwconfig`, `awk`, `cut`, `$()`, `function nombre(){ Comandos }`
- [Actualización y Upgradeo del sistema](notes/Conceptos.md#actualizacion-y-upgradeo-del-sistema) — `parrot-upgrade`, `reboot`, `apt`
- [Búsquedas a nivel de sistema](notes/Conceptos.md#busquedas-a-nivel-de-sistema) — `neofetch`
- [Creación de scripts en Bash](notes/Conceptos.md#creacion-de-scripts-en-bash) — `tail`, `#!/bin/bash`, `variable="Hola"`, `$variable o ${variable}`

</details>

<details>
<summary><b>🧪 Labs</b> — 29 temas</summary>

- [Conexiones SSH](notes/Labs.md#conexiones-ssh) — `ssh`, `sshpass`, `export`
- [Lectura de archivos especiales [1-2]](notes/Labs.md#lectura-de-archivos-especiales-1-2) — `rev`, `tr`, `head`
- [Lectura de archivos especiales [2-2]](notes/Labs.md#lectura-de-archivos-especiales-2-2) — <i>solo parámetros</i>
- [Directorios y archivos ocultos](notes/Labs.md#directorios-y-archivos-ocultos) — `file`
- [Búsquedas precisas de archivos [1-2]](notes/Labs.md#busquedas-precisas-de-archivos-1-2) — <i>solo parámetros</i>
- [Métodos de filtrado de datos [1-2]](notes/Labs.md#metodos-de-filtrado-de-datos-1-2) — `sed`
- [Método de filtrado de datos [2-2]](notes/Labs.md#metodo-de-filtrado-de-datos-2-2) — `sort`, `uniq`
- [Interpretación de archivos binarios](notes/Labs.md#interpretacion-de-archivos-binarios) — `strings`
- [Codificación y decodificación en base64](notes/Labs.md#codificacion-y-decodificacion-en-base64) — `base64`
- [Cifrado césar y uso de tr](notes/Labs.md#cifrado-cesar-y-uso-de-tr) — <i>solo parámetros</i>
- [Descompresor recursivo en Bash](notes/Labs.md#descompresor-recursivo-en-bash) — `xxd`, `tee`, `sponge`, `ghex`, `7z`, `sleep`, `trap`, `!?`, `while`
- [Pares de claves y conexiones SSH](notes/Labs.md#pares-de-claves-y-conexiones-ssh) — `ssh-keygen`, `ssh-copy-id`
- [Uso de netcat para realizar conexiones](notes/Labs.md#uso-de-netcat-para-realizar-conexiones) — `nc`, `ss`, `lsof`, `ps`, `bc`, `for`
- [Uso de conexiones encriptadas](notes/Labs.md#uso-de-conexiones-encriptadas) — `ncat`
- [Creando nuestros propios escáneres en Bash](notes/Labs.md#creando-nuestros-propios-escaneres-en-bash) — `seq`, `mktemp`, `wait`, `tput`, `(comando)`, `/dev/tcp/$ip/$port`
- [Ejecución de comandos por SSH](notes/Labs.md#ejecucion-de-comandos-por-ssh) — <i>solo parámetros</i>
- [Detección de diferencias entre archivos](notes/Labs.md#deteccion-de-diferencias-entre-archivos) — `diff`
- [Abusando de privilegio SUID para migrar de usuario](notes/Labs.md#abusando-de-privilegio-suid-para-migrar-de-usuario) — `bash`
- [Abusando de tareas Cron [1-3]](notes/Labs.md#abusando-de-tareas-cron-1-3) — `crontab`
- [Abusando de tareas Cron [2-3]](notes/Labs.md#abusando-de-tareas-cron-2-3) — `md5sum`
- [Abusando de tareas Cron [3-3]](notes/Labs.md#abusando-de-tareas-cron-3-3) — `stat`, `timeout`, `watch`
- [Escapando del contexto de un comando](notes/Labs.md#escapando-del-contexto-de-un-comando) — `more`
- [Fuerza bruta aplicada a conexiones](notes/Labs.md#fuerza-bruta-aplicada-a-conexiones) — `{0000..9999}`
- [Operando con proyectos de Github [1-5]](notes/Labs.md#operando-con-proyectos-de-github-1-5) — `git clone`
- [Operando con proyectos de Github [2-5]](notes/Labs.md#operando-con-proyectos-de-github-2-5) — `git log`, `git show`
- [Operando con proyectos de Github [3-5]](notes/Labs.md#operando-con-proyectos-de-github-3-5) — `git branch`, `git checkout`
- [Operando con proyectos de Github [4-5]](notes/Labs.md#operando-con-proyectos-de-github-4-5) — `git tag`
- [Operando con proyectos de Github [5-5]](notes/Labs.md#operando-con-proyectos-de-github-5-5) — `git add`, `git commit`, `git push`
- [Argumentos posicionales en Bash](notes/Labs.md#argumentos-posicionales-en-bash) — `$0`, `$1, $2...`, `$#`, `$*`

</details>

<details>
<summary><b>📜 Scripting</b> — 1 temas</summary>

- [Scripting en Bash [1-6]](notes/Scripting.md#scripting-en-bash-1-6) — `curl`, `batcat`, `js-beautify`, `getopts`, `case`, `declare`, `let`, `if`, `$OPTARG`

</details>

## 🔤 Índice alfabético de comandos

| Comando | Qué hace | Sección |
|:--|:--|:--|
| `2>&1` | Redirige stderr a stdout, mostrando todo junto | [Conceptos](notes/Conceptos.md#control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano) |
| `2>/dev/null` | Envía los errores (stderr) a /dev/null para no mostrarlos | [Conceptos](notes/Conceptos.md#control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano) |
| `7z` | Comprime y descomprime archivos en formato .7z | [Labs](notes/Labs.md#descompresor-recursivo-en-bash) |
| `apt` | Gestor de paquetes de Debian: actualiza la lista de paquetes (update) e instala sus actualizaciones (upgrade) | [Conceptos](notes/Conceptos.md#actualizacion-y-upgradeo-del-sistema) |
| `awk` | Procesa y filtra texto por columnas | [Conceptos](notes/Conceptos.md#uso-de-bashrc-y-zshrc) |
| `base64` | Convierte un texto o archivo a formato Base64, o lo decodifica de vuelta a su forma original, según el parámetro usado | [Labs](notes/Labs.md#codificacion-y-decodificacion-en-base64) |
| `bash` | Intérprete de comandos que procesa y ejecuta lo que escribes | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-2-2) |
| `batcat` | Muestra el contenido de un archivo como cat, pero con resaltado de sintaxis y números de línea | [Scripting](notes/Scripting.md#scripting-en-bash-1-6) |
| `bc` | Calculadora de la terminal; permite hacer operaciones y convertir números entre bases (hexadecimal, decimal) | [Labs](notes/Labs.md#uso-de-netcat-para-realizar-conexiones) |
| `case` | Compara el valor de una variable contra varios patrones y ejecuta el bloque del que coincida; se cierra con esac | [Scripting](notes/Scripting.md#scripting-en-bash-1-6) |
| `cat` | Muestra el contenido de un archivo en la terminal | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-1-2) |
| `cd` | Cambia de directorio | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-2-2) |
| `chattr` | Cambia los atributos especiales de un archivo (por ejemplo hacerlo inmutable) | [Conceptos](notes/Conceptos.md#control-de-atributos-de-ficheros-chattr-y-lsattr) |
| `chgrp` | Cambia el grupo propietario de un archivo o carpeta | [Conceptos](notes/Conceptos.md#asignacion-de-permisos-1-2) |
| `chmod` | Modifica permisos de archivo o carpeta; + agrega y - quita permiso | [Conceptos](notes/Conceptos.md#asignacion-de-permisos-1-2) |
| `chown` | Cambia el dueño y/o grupo propietario de un archivo o carpeta | [Conceptos](notes/Conceptos.md#asignacion-de-permisos-2-2) |
| `command` | Con -v muestra la ruta o ubicación de un comando, similar a which | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-2-2) |
| `cp` | Copia archivos o carpetas de un lugar a otro | [Conceptos](notes/Conceptos.md#control-de-atributos-de-ficheros-chattr-y-lsattr) |
| `crontab` | Permite ver, crear y editar las tareas Cron (tareas programadas) de un usuario | [Labs](notes/Labs.md#abusando-de-tareas-cron-1-3) |
| `Ctrl + L` | Atajo que limpia la pantalla de la terminal sin perder el historial | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-1-2) |
| `curl` | Realiza peticiones a una URL desde la terminal (HTTP, HTTPS, etc.) y muestra la respuesta | [Scripting](notes/Scripting.md#scripting-en-bash-1-6) |
| `cut` | Extrae partes de una línea de texto, dividiendo por un delimitador | [Conceptos](notes/Conceptos.md#uso-de-bashrc-y-zshrc) |
| `declare` | Declara variables asignándoles atributos, por ejemplo que sean de tipo entero | [Scripting](notes/Scripting.md#scripting-en-bash-1-6) |
| `diff` | Compara dos archivos línea por línea y muestra las diferencias entre ellos | [Labs](notes/Labs.md#deteccion-de-diferencias-entre-archivos) |
| `disown` | Desvincula un proceso en segundo plano de la terminal para que siga corriendo al cerrarla | [Conceptos](notes/Conceptos.md#control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano) |
| `echo` | Imprime texto o el valor de una variable en la terminal | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-1-2) |
| `exec` | Manipula los descriptores de archivo de la sesión actual (abrir, cerrar, redirigir) | [Conceptos](notes/Conceptos.md#descriptores-de-archivo) |
| `exit` | Cierra la sesión actual o sale de una sesión elevada (como root) | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-1-2) |
| `export` | Convierte una variable en variable de entorno, disponible para otros procesos abiertos desde esa terminal | [Labs](notes/Labs.md#conexiones-ssh) |
| `file` | Analiza un archivo y muestra qué tipo de contenido tiene, sin importar su extensión | [Labs](notes/Labs.md#directorios-y-archivos-ocultos) |
| `find` | Busca archivos y carpetas según criterios (nombre, tipo, permisos, fecha, etc.) | [Conceptos](notes/Conceptos.md#permisos-especiales-suid-y-sgid) |
| `for` | Bucle que recorre una lista de elementos uno por uno y ejecuta un bloque de código por cada uno | [Labs](notes/Labs.md#uso-de-netcat-para-realizar-conexiones) |
| `function nombre(){ Comandos }` | Define una función personalizada que agrupa varios comandos bajo un nombre | [Conceptos](notes/Conceptos.md#uso-de-bashrc-y-zshrc) |
| `getcap` | Muestra las Capabilities asignadas a un archivo | [Conceptos](notes/Conceptos.md#privilegios-especiales-capabilities) |
| `getopts` | Procesa una por una las opciones (-m, -h...) que recibe un script; normalmente se usa dentro de un while | [Scripting](notes/Scripting.md#scripting-en-bash-1-6) |
| `ghex` | Editor hexadecimal con interfaz gráfica para ver y modificar bytes de un archivo | [Labs](notes/Labs.md#descompresor-recursivo-en-bash) |
| `git add` | Agrega archivos al área de preparación para incluirlos en el próximo commit | [Labs](notes/Labs.md#operando-con-proyectos-de-github-5-5) |
| `git branch` | Crea, lista, elimina y renombra ramas; no sirve para cambiar de rama ni para unirlas | [Labs](notes/Labs.md#operando-con-proyectos-de-github-3-5) |
| `git checkout` | Cambia a otra rama o regresa el proyecto al estado de un commit anterior | [Labs](notes/Labs.md#operando-con-proyectos-de-github-3-5) |
| `git clone` | Descarga una copia completa de un repositorio remoto (como GitHub), con todos sus archivos e historial | [Labs](notes/Labs.md#operando-con-proyectos-de-github-1-5) |
| `git commit` | Guarda los cambios preparados creando una nueva versión del proyecto en el repositorio local | [Labs](notes/Labs.md#operando-con-proyectos-de-github-5-5) |
| `git log` | Lista todos los commits del proyecto con su identificador, autor, fecha y mensaje | [Labs](notes/Labs.md#operando-con-proyectos-de-github-2-5) |
| `git push` | Sube los commits del repositorio local al repositorio remoto | [Labs](notes/Labs.md#operando-con-proyectos-de-github-5-5) |
| `git show` | Muestra las propiedades y los cambios aplicados en un commit concreto | [Labs](notes/Labs.md#operando-con-proyectos-de-github-2-5) |
| `git tag` | Lista todas las etiquetas (tags) del repositorio; un tag es un nombre que marca de forma inalterable un commit específico | [Labs](notes/Labs.md#operando-con-proyectos-de-github-4-5) |
| `grep` | Busca y filtra líneas de texto que coincidan con un patrón | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-1-2) |
| `groupadd` | Crea un nuevo grupo en el sistema | [Conceptos](notes/Conceptos.md#asignacion-de-permisos-2-2) |
| `head` | Muestra las primeras líneas de un archivo o texto (10 por defecto) | [Labs](notes/Labs.md#lectura-de-archivos-especiales-1-2) |
| `hostname` | Muestra o cambia el nombre del equipo en la red | [Conceptos](notes/Conceptos.md#uso-de-bashrc-y-zshrc) |
| `id` | Muestra información del usuario: UID, GID y grupos a los que pertenece | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-1-2) |
| `if` | Condicional: ejecuta un bloque si se cumple la condición y otro (else) si no; se cierra con fi | [Scripting](notes/Scripting.md#scripting-en-bash-1-6) |
| `ifconfig` | Muestra y configura las interfaces de red (IP de cada tarjeta) | [Conceptos](notes/Conceptos.md#uso-de-bashrc-y-zshrc) |
| `iwconfig` | Como ifconfig, pero para interfaces inalámbricas (WiFi) | [Conceptos](notes/Conceptos.md#uso-de-bashrc-y-zshrc) |
| `js-beautify` | Da formato legible (saltos de línea e indentación) a código JavaScript o JSON compactado | [Scripting](notes/Scripting.md#scripting-en-bash-1-6) |
| `let` | Realiza operaciones aritméticas sobre variables | [Scripting](notes/Scripting.md#scripting-en-bash-1-6) |
| `ls` | Lista archivos y carpetas del directorio actual | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-2-2) |
| `lsattr` | Muestra los atributos especiales de un archivo (más allá de los permisos normales) | [Conceptos](notes/Conceptos.md#control-de-atributos-de-ficheros-chattr-y-lsattr) |
| `lsof` | Muestra una lista de archivos abiertos por los procesos en ejecución, incluyendo conexiones de red | [Labs](notes/Labs.md#uso-de-netcat-para-realizar-conexiones) |
| `md5sum` | Calcula y muestra el hash MD5 de un archivo o entrada, útil para comprobar si su contenido ha cambiado | [Labs](notes/Labs.md#abusando-de-tareas-cron-2-3) |
| `mkdir` | Crea una nueva carpeta | [Conceptos](notes/Conceptos.md#asignacion-de-permisos-1-2) |
| `mktemp` | Crea un archivo temporal con nombre único, evitando conflictos con otros archivos | [Labs](notes/Labs.md#creando-nuestros-propios-escaneres-en-bash) |
| `more` | Muestra la salida de un comando o archivo una página a la vez (espacio avanza, q sale) | [Labs](notes/Labs.md#escapando-del-contexto-de-un-comando) |
| `nano` | Editor de texto sencillo en la terminal | [Conceptos](notes/Conceptos.md#lectura-e-interpretacion-de-permisos-1-2) |
| `nc` | Herramienta de línea de comandos (netcat) para crear conexiones TCP/UDP manuales, enviar/recibir datos, escanear puertos o crear shells remotas | [Labs](notes/Labs.md#uso-de-netcat-para-realizar-conexiones) |
| `ncat` | Versión mejorada de netcat (proyecto Nmap) con soporte para conexiones cifradas SSL/TLS y autenticación | [Labs](notes/Labs.md#uso-de-conexiones-encriptadas) |
| `neofetch` | Muestra información del sistema (kernel, RAM, CPU, logo de la distro) de forma visual | [Conceptos](notes/Conceptos.md#busquedas-a-nivel-de-sistema) |
| `parrot-upgrade` | Actualiza Parrot OS de forma segura sin romper componentes propios | [Conceptos](notes/Conceptos.md#actualizacion-y-upgradeo-del-sistema) |
| `passwd` | Establece o cambia la contraseña de un usuario | [Conceptos](notes/Conceptos.md#asignacion-de-permisos-2-2) |
| `ps` | Muestra los procesos en ejecución en el sistema | [Labs](notes/Labs.md#uso-de-netcat-para-realizar-conexiones) |
| `pwd` | Muestra la ruta completa del directorio actual | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-2-2) |
| `reboot` | Reinicia el equipo | [Conceptos](notes/Conceptos.md#actualizacion-y-upgradeo-del-sistema) |
| `rev` | Invierte el orden de los caracteres de cada línea, mostrando el texto al revés | [Labs](notes/Labs.md#lectura-de-archivos-especiales-1-2) |
| `rm` | Elimina archivos o carpetas | [Conceptos](notes/Conceptos.md#lectura-e-interpretacion-de-permisos-1-2) |
| `sed` | Busca, reemplaza, elimina o modifica texto de un archivo o flujo de datos, generalmente con expresiones regulares | [Labs](notes/Labs.md#metodos-de-filtrado-de-datos-1-2) |
| `seq` | Genera una secuencia de números dentro de un rango, útil para bucles o scripts | [Labs](notes/Labs.md#creando-nuestros-propios-escaneres-en-bash) |
| `setcap` | Asigna Capabilities específicas a un archivo sin dar todos los privilegios de root | [Conceptos](notes/Conceptos.md#privilegios-especiales-capabilities) |
| `sleep` | Pausa la ejecución del script un tiempo determinado en segundos | [Labs](notes/Labs.md#descompresor-recursivo-en-bash) |
| `sort` | Ordena las líneas de un archivo o texto, alfabética o numéricamente | [Labs](notes/Labs.md#metodo-de-filtrado-de-datos-2-2) |
| `sponge` | Lee toda la entrada antes de escribirla en un archivo, evitando problemas al sobrescribir el mismo archivo leído | [Labs](notes/Labs.md#descompresor-recursivo-en-bash) |
| `ss` | Muestra información sobre los sockets de red activos, alternativa moderna a netstat | [Labs](notes/Labs.md#uso-de-netcat-para-realizar-conexiones) |
| `ssh` | Conecta de forma remota y segura a otro equipo por la red, con usuario y contraseña o clave SSH | [Labs](notes/Labs.md#conexiones-ssh) |
| `ssh-copy-id` | Copia la clave pública SSH generada hacia authorized_keys de un servidor remoto | [Labs](notes/Labs.md#pares-de-claves-y-conexiones-ssh) |
| `ssh-keygen` | Genera un par de claves SSH (pública y privada) para autenticarse sin contraseña | [Labs](notes/Labs.md#pares-de-claves-y-conexiones-ssh) |
| `sshpass` | Pasa la contraseña de una conexión SSH directamente en el comando; útil para automatizar scripts | [Labs](notes/Labs.md#conexiones-ssh) |
| `stat` | Muestra información detallada de un archivo o directorio: permisos, tamaño y fechas de acceso y modificación | [Labs](notes/Labs.md#abusando-de-tareas-cron-3-3) |
| `strings` | Muestra las cadenas de texto legible (ASCII) dentro de un archivo binario; útil para hallar información oculta | [Labs](notes/Labs.md#interpretacion-de-archivos-binarios) |
| `su` | Cambia de usuario en la terminal pidiendo su contraseña | [Conceptos](notes/Conceptos.md#asignacion-de-permisos-1-2) |
| `sudo` | Ejecuta un solo comando con permisos de administrador sin cambiar de usuario | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-1-2) |
| `tail` | Muestra las últimas líneas de un archivo (10 por defecto), útil para logs | [Conceptos](notes/Conceptos.md#creacion-de-scripts-en-bash) |
| `tee` | Muestra la salida de un comando en pantalla y la guarda en un archivo a la vez | [Labs](notes/Labs.md#descompresor-recursivo-en-bash) |
| `timeout` | Ejecuta un comando y lo termina automáticamente si supera el tiempo especificado | [Labs](notes/Labs.md#abusando-de-tareas-cron-3-3) |
| `touch` | Crea un archivo vacío o actualiza su fecha de modificación si ya existe | [Conceptos](notes/Conceptos.md#lectura-e-interpretacion-de-permisos-1-2) |
| `tput` | Controla aspectos de la terminal, como ocultar o volver a mostrar el cursor | [Labs](notes/Labs.md#creando-nuestros-propios-escaneres-en-bash) |
| `tr` | Traduce o reemplaza caracteres del texto que recibe por otros | [Labs](notes/Labs.md#lectura-de-archivos-especiales-1-2) |
| `trap` | Captura una señal (como Ctrl+C) y ejecuta una función en vez de terminar el script de inmediato | [Labs](notes/Labs.md#descompresor-recursivo-en-bash) |
| `uniq` | Elimina líneas duplicadas consecutivas; normalmente se usa después de sort | [Labs](notes/Labs.md#metodo-de-filtrado-de-datos-2-2) |
| `useradd` | Crea un nuevo usuario en el sistema | [Conceptos](notes/Conceptos.md#asignacion-de-permisos-2-2) |
| `usermod` | Modifica propiedades de un usuario existente (grupo, home, shell) | [Conceptos](notes/Conceptos.md#asignacion-de-permisos-2-2) |
| `variable="Hola"` | Declara una variable asignándole texto (sin espacios alrededor del =) | [Conceptos](notes/Conceptos.md#creacion-de-scripts-en-bash) |
| `vi` | Editor de texto avanzado y potente, con curva de aprendizaje mayor que nano | [Conceptos](notes/Conceptos.md#lectura-e-interpretacion-de-permisos-1-2) |
| `wait` | Espera a que terminen uno o varios procesos en segundo plano antes de continuar | [Labs](notes/Labs.md#creando-nuestros-propios-escaneres-en-bash) |
| `watch` | Ejecuta un comando de forma repetida a intervalos regulares y muestra su salida actualizada en pantalla | [Labs](notes/Labs.md#abusando-de-tareas-cron-3-3) |
| `which` | Muestra la ubicación donde está instalado un comando o programa | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-1-2) |
| `while` | Bucle que repite un bloque de código mientras se cumpla una condición | [Labs](notes/Labs.md#descompresor-recursivo-en-bash) |
| `whoami` | Muestra el nombre del usuario con el que estás conectado actualmente | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-1-2) |
| `xargs` | Toma la salida de un comando y la usa como argumento de otro | [Conceptos](notes/Conceptos.md#permisos-especiales-suid-y-sgid) |
| `xxd` | Muestra el contenido de un archivo en formato hexadecimal | [Labs](notes/Labs.md#descompresor-recursivo-en-bash) |
| `!$` | Representa el último argumento del comando anterior para reutilizarlo | [Conceptos](notes/Conceptos.md#privilegios-especiales-capabilities) |
| `!?` | Busca en el historial el comando más reciente que contenga el texto indicado y lo vuelve a ejecutar | [Labs](notes/Labs.md#descompresor-recursivo-en-bash) |
| `#!/bin/bash` | Shebang: primera línea del script, indica el intérprete (Bash) | [Conceptos](notes/Conceptos.md#creacion-de-scripts-en-bash) |
| `$#` | Contiene el número de argumentos recibidos desde la línea de comandos | [Labs](notes/Labs.md#argumentos-posicionales-en-bash) |
| `$()` | Ejecuta el comando entre paréntesis y devuelve su resultado (sustitución de comandos) | [Conceptos](notes/Conceptos.md#uso-de-bashrc-y-zshrc) |
| `$*` | Contiene todos los argumentos recibidos desde la línea de comandos en una sola variable | [Labs](notes/Labs.md#argumentos-posicionales-en-bash) |
| `$0` | Variable con el nombre del script que se invocó desde la terminal | [Labs](notes/Labs.md#argumentos-posicionales-en-bash) |
| `$1, $2...` | Primer, segundo (y así sucesivamente) argumento recibido desde la línea de comandos | [Labs](notes/Labs.md#argumentos-posicionales-en-bash) |
| `$OPTARG` | Variable que guarda el valor que acompaña a la opción que está procesando getopts | [Scripting](notes/Scripting.md#scripting-en-bash-1-6) |
| `$variable o ${variable}` | Accede al valor de una variable; las llaves delimitan el nombre si está pegado a otro texto | [Conceptos](notes/Conceptos.md#creacion-de-scripts-en-bash) |
| `&` | Ejecuta el comando en segundo plano dejando la terminal libre | [Conceptos](notes/Conceptos.md#control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano) |
| `&&` | Ejecuta el siguiente comando solo si el anterior tuvo éxito | [Conceptos](notes/Conceptos.md#control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano) |
| `&>/dev/null` | Envía salida normal y errores a /dev/null, ocultando todo | [Conceptos](notes/Conceptos.md#control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano) |
| `(comando)` | Ejecuta el comando dentro de un subshell, en un proceso hijo separado del script principal | [Labs](notes/Labs.md#creando-nuestros-propios-escaneres-en-bash) |
| `*` | Comodín que representa cualquier cosa para seleccionar varios archivos | [Conceptos](notes/Conceptos.md#asignacion-de-permisos-1-2) |
| `/dev/tcp/$ip/$port` | Ruta especial de Bash que abre una conexión TCP a la IP y puerto indicados como si fuera un archivo, sin netcat | [Labs](notes/Labs.md#creando-nuestros-propios-escaneres-en-bash) |
| `;` | Ejecuta comandos en secuencia sin importar si el anterior falló | [Conceptos](notes/Conceptos.md#control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano) |
| `>` | Redirige la salida a un archivo sobrescribiendo su contenido | [Conceptos](notes/Conceptos.md#descriptores-de-archivo) |
| `>>` | Redirige la salida a un archivo agregándola al final | [Conceptos](notes/Conceptos.md#descriptores-de-archivo) |
| `{0000..9999}` | Expansión de llaves: genera una secuencia de valores (aquí del 0000 al 9999), útil como secuenciador en bucles | [Labs](notes/Labs.md#fuerza-bruta-aplicada-a-conexiones) |
| `\|` | Pipe: conecta la salida de un comando como entrada del siguiente | [Conceptos](notes/Conceptos.md#comandos-basicos-de-linux-1-2) |
| `\|\|` | Ejecuta el siguiente comando solo si el anterior falló | [Conceptos](notes/Conceptos.md#control-del-flujo-stderr-stdout-operadores-y-procesos-en-segundo-plano) |

## 🛠️ Cómo actualizar

Los datos viven en [`data/comandos.csv`](data/comandos.csv) y [`data/parametros.csv`](data/parametros.csv) (exportados de la hoja *Comandos de Linux*). Tras editarlos:

```bash
python3 scripts/build.py
```

Esto regenera este README, las notas de [`notes/`](notes) y la web de [`docs/`](docs).

> 💡 Para ver la web online: **Settings → Pages → Branch `main` / carpeta `/docs`**.
