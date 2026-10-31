# 🔀 Pipes, Redirection & Operators

> Chain commands, decide where output and errors go, and run things in the background.

**12** commands · **6** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`\|`](#cmd-sym-124) | Pipe: sends one command's output as the next command's input |
| [`;`](#cmd-sym-59) | Runs commands in sequence whether or not the previous one failed |
| [`&&`](#cmd-sym-38-38) | Runs the next command only if the previous one succeeded |
| [`\|\|`](#cmd-sym-124-124) | Runs the next command only if the previous one failed |
| [`&`](#cmd-sym-38) | Runs the command in the background, leaving the terminal free |
| [`>`](#cmd-sym-62) | Redirects output to a file, overwriting its contents |
| [`>>`](#cmd-sym-62-62) | Redirects output to a file, appending it to the end |
| [`2>/dev/null`](#cmd-2-dev-null) | Sends errors (stderr) to /dev/null so they aren't shown |
| [`2>&1`](#cmd-2-1) | Redirects stderr to stdout, showing everything together |
| [`&>/dev/null`](#cmd-dev-null) | Sends both normal output and errors to /dev/null, hiding everything |
| [`exec`](#cmd-exec) | Manipulates the current session's file descriptors (open, close, redirect) |
| [`disown`](#cmd-disown) | Detaches a background process from the terminal so it keeps running after you close it |

---

<a id="cmd-sym-124"></a>

## `|`

Pipe: sends one command's output as the next command's input

```bash
cat /etc/passwd | grep root
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sym-59"></a>

## `;`

Runs commands in sequence whether or not the previous one failed

```bash
cd /tmp ; ls
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sym-38-38"></a>

## `&&`

Runs the next command only if the previous one succeeded

```bash
mkdir test && cd test
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sym-124-124"></a>

## `||`

Runs the next command only if the previous one failed

```bash
ping -c 1 8.8.8.8 || echo "no connection"
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sym-38"></a>

## `&`

Runs the command in the background, leaving the terminal free

```bash
sleep 60 &
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sym-62"></a>

## `>`

Redirects output to a file, overwriting its contents

```bash
echo "hello" > file.txt
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `/dev/null` | Special file that works as a trash bin: anything sent to it is discarded | `echo "hello" > /dev/null` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sym-62-62"></a>

## `>>`

Redirects output to a file, appending it to the end

```bash
echo "another line" >> file.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-2-dev-null"></a>

## `2>/dev/null`

Sends errors (stderr) to /dev/null so they aren't shown

```bash
find / -name "*.conf" 2>/dev/null
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-2-1"></a>

## `2>&1`

Redirects stderr to stdout, showing everything together

```bash
ls /doesnotexist > output.txt 2>&1
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-dev-null"></a>

## `&>/dev/null`

Sends both normal output and errors to /dev/null, hiding everything

```bash
ping -c 1 8.8.8.8 &>/dev/null
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-exec"></a>

## `exec`

Manipulates the current session's file descriptors (open, close, redirect)

```bash
exec 3<> file.txt
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `3<> file` | Opens "file" for reading and writing as descriptor 3 | `exec 3<> file.txt` |
| `>&3` | Redirects the session's standard output to descriptor 3 | `exec >&3` |
| `3>&-` | Closes descriptor 3 | `exec 3>&-` |
| `5>&3` | Duplicates descriptor 3 into descriptor 5 | `exec 5>&3` |
| `8>&3-` | Duplicates descriptor 3 into 8 and closes the original 3 | `exec 8>&3-` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-disown"></a>

## `disown`

Detaches a background process from the terminal so it keeps running after you close it

```bash
sleep 100 & disown
```

<sub>[⬆ Back to top](#commands)</sub>
