# ✂️ Text Processing

> Filter, cut, transform and sort text coming from files or other commands.

**9** commands · **18** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`echo`](#cmd-echo) | Prints text or a variable's value to the terminal |
| [`awk`](#cmd-awk) | Processes and filters text by columns |
| [`cut`](#cmd-cut) | Extracts parts of a line of text, splitting it by a delimiter |
| [`tr`](#cmd-tr) | Translates or replaces characters of the incoming text with others |
| [`sed`](#cmd-sed) | Finds, replaces, deletes or modifies text in a file or stream, usually with regular expressions |
| [`sort`](#cmd-sort) | Sorts the lines of a file or text, alphabetically or numerically |
| [`uniq`](#cmd-uniq) | Removes consecutive duplicate lines; usually used after sort |
| [`tee`](#cmd-tee) | Shows a command's output on screen and saves it to a file at the same time |
| [`sponge`](#cmd-sponge) | Reads all of its input before writing it to a file, avoiding problems when overwriting the same file you're reading |

---

<a id="cmd-echo"></a>

## `echo`

Prints text or a variable's value to the terminal

```bash
echo "Hello world"
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `$PATH` | Variable holding the folders where the system looks for commands | `echo $PATH` |
| `$HOME` | Variable holding the path of the user's home folder | `echo $HOME` |
| `$SHELL` | Variable holding the path of the shell in use (bash, zsh) | `echo $SHELL` |
| `$?` | Exit code of the last command (0 = success, anything else = error) | `ls /doesnotexist ; echo $?` |
| `-e` | Enables special characters (\n, \t) in the printed text | `echo -e "line1\nline2"` |
| `-e "\n"` | \n is a line break; it needs the -e flag | `echo -e "Hello\nWorld"` |
| `"obase=10; ibase=16; $hexNum" \| bc` | Converts a variable's hexadecimal value to decimal using bc | `hexNum="FF"; echo "obase=10; ibase=16; $hexNum" \| bc` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-awk"></a>

## `awk`

Processes and filters text by columns

```bash
awk '{print $2}' data.txt
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `'{print $1}'` | Prints the first column of each line | `ls -l \| awk '{print $1}'` |
| `'NR==2'` | Shows only line number 2 (NR = record number) | `awk 'NR==2' file.txt` |
| `FS="/"` | Sets "/" as the field separator (FS) to split the text into columns | `echo "/home/john" \| awk '{print $2}' FS="/"` |
| `'{print $2}' FS=":"` | Uses ":" as the field separator (FS) and prints the second column of each line | `echo "a:b:c" \| awk '{print $2}' FS=":"` |
| `'NF{print $NF}'` | Prints the last field of each line; NF is the number of fields and $NF the value of the last one | `echo "one two three" \| awk 'NF{print $NF}'` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-cut"></a>

## `cut`

Extracts parts of a line of text, splitting it by a delimiter

```bash
cut -d ":" -f 1 /etc/passwd
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-d` | Sets the delimiter used to split the text into columns | `cut -d ":" -f 1 /etc/passwd` |
| `-f` | Selects the field (column) number to extract | `cut -d ":" -f 3 /etc/passwd` |
| `-d ':' -f 2` | Splits each line using ":" as the delimiter and extracts only the second field | `echo "a:b:c" \| cut -d ':' -f 2` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-tr"></a>

## `tr`

Translates or replaces characters of the incoming text with others

```bash
echo "a:b:c" | tr ':' ' '
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `':' ' '` | Replaces every ":" with a space in the processed text | `echo "a:b:c" \| tr ':' ' '` |
| `'[A-Za-z]' '[N-ZA-Mn-za-m]'` | Replaces each letter with the one 13 positions ahead, applying the ROT13 cipher | `echo "Uryyb" \| tr '[A-Za-z]' '[N-ZA-Mn-za-m]'` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sed"></a>

## `sed`

Finds, replaces, deletes or modifies text in a file or stream, usually with regular expressions

```bash
sed 's/old/new/g' file.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sort"></a>

## `sort`

Sorts the lines of a file or text, alphabetically or numerically

```bash
sort names.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-uniq"></a>

## `uniq`

Removes consecutive duplicate lines; usually used after sort

```bash
sort names.txt | uniq
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-u` | Shows only completely unique lines, the ones that never repeat | `sort data.txt \| uniq -u` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-tee"></a>

## `tee`

Shows a command's output on screen and saves it to a file at the same time

```bash
ls | tee list.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sponge"></a>

## `sponge`

Reads all of its input before writing it to a file, avoiding problems when overwriting the same file you're reading

```bash
sort data.txt | sponge data.txt
```

<sub>[⬆ Back to top](#commands)</sub>
