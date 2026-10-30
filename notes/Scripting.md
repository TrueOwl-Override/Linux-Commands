# 📜 Scripting

> Herramientas para escribir scripts en Bash: opciones, condicionales, aritmética y peticiones HTTP.

**9** comandos · **7** parámetros · **1** temas  ·  [⬅ Volver al índice](../README.md)

## Temas

1. [Scripting en Bash [1-6]](#scripting-en-bash-1-6)

---

<a id="scripting-en-bash-1-6"></a>

## Scripting en Bash [1-6]

| Comando | Qué hace | Ejemplo |
|:--|:--|:--|
| `curl` | Realiza peticiones a una URL desde la terminal (HTTP, HTTPS, etc.) y muestra la respuesta | `curl -s -X GET https://ejemplo.com` |
| `batcat` | Muestra el contenido de un archivo como cat, pero con resaltado de sintaxis y números de línea | `batcat script.sh` |
| `js-beautify` | Da formato legible (saltos de línea e indentación) a código JavaScript o JSON compactado | `curl -s -X GET https://ejemplo.com/bundle.js \| js-beautify` |
| `getopts` | Procesa una por una las opciones (-m, -h...) que recibe un script; normalmente se usa dentro de un while | `while getopts "m:h" arg; do ... done` |
| `case` | Compara el valor de una variable contra varios patrones y ejecuta el bloque del que coincida; se cierra con esac | `case $arg in m) echo "opción m";; esac` |
| `declare` | Declara variables asignándoles atributos, por ejemplo que sean de tipo entero | `declare -i contador=0` |
| `let` | Realiza operaciones aritméticas sobre variables | `let contador+=1` |
| `if` | Condicional: ejecuta un bloque si se cumple la condición y otro (else) si no; se cierra con fi | `if [ $n -eq 1 ]; then echo "uno"; else echo "otro"; fi` |
| `$OPTARG` | Variable que guarda el valor que acompaña a la opción que está procesando getopts | `m) nombre=$OPTARG;;` |

<details open>
<summary><b>🔧 Parámetros y usos (7)</b></summary>

| Comando | Parámetro | Qué hace | Ejemplo |
|:--|:--|:--|:--|
| `curl` | `-s` | Modo silencioso: no muestra la barra de progreso ni mensajes de error | `curl -s https://ejemplo.com` |
| `curl` | `-X GET` | Define el método HTTP de la petición (GET, POST, PUT...) | `curl -s -X GET https://ejemplo.com` |
| `getopts` | `"m:h" arg` | Lista de opciones válidas que se guardan en arg; los ":" tras una letra indican que esa opción recibe un valor, que queda en $OPTARG | `while getopts "m:h" arg; do case $arg in m) nombre=$OPTARG;; h) ayuda;; esac; done` |
| `case` | `m) comando;;` | Define un patrón dentro de case y el bloque a ejecutar si coincide; ;; cierra ese bloque | `case $arg in m) echo "opción m";; esac` |
| `declare` | `-i` | Define la variable como entera, para que su valor se trate como número | `declare -i contador=0` |
| `let` | `+=` | Suma un valor al que ya tiene la variable | `let contador+=1` |
| `if` | `-eq` | Compara si dos números son iguales (equal to) | `if [ $a -eq $b ]; then echo "iguales"; fi` |

</details>

<sub>[⬆ Arriba](#temas)</sub>
