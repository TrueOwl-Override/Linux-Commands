# 📝 Viewing & Editing Files

> Read files in the terminal, page through output, compare files and edit text.

**8** commands · **21** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`cat`](#cmd-cat) | Prints a file's contents to the terminal |
| [`more`](#cmd-more) | Shows a command's output or a file one page at a time (space to advance, q to quit) |
| [`head`](#cmd-head) | Shows the first lines of a file or text (10 by default) |
| [`tail`](#cmd-tail) | Shows the last lines of a file (10 by default), useful for logs |
| [`rev`](#cmd-rev) | Reverses the characters of each line, showing the text backwards |
| [`diff`](#cmd-diff) | Compares two files line by line and shows the differences between them |
| [`nano`](#cmd-nano) | Simple text editor in the terminal |
| [`vi`](#cmd-vi) | Advanced, powerful text editor with a steeper learning curve than nano |

---

<a id="cmd-cat"></a>

## `cat`

Prints a file's contents to the terminal

```bash
cat notes.txt
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `/etc/group` | File listing the existing groups and their members | `cat /etc/group` |
| `/etc/passwd` | File with basic user info (UID, home, shell) | `cat /etc/passwd` |
| `/etc/shells` | File listing the shells installed and available | `cat /etc/shells` |
| `/etc/hosts` | File with manual IP-to-domain mappings that skip DNS | `cat /etc/hosts` |
| `/etc/shadow` | File where users' encrypted passwords are stored | `sudo cat /etc/shadow` |
| `/etc/login.defs` | System configuration; ENCRYPT_METHOD sets how passwords are hashed | `grep ENCRYPT_METHOD /etc/login.defs` |
| `/home/bandit1/-` | Reads the file named "-" by its absolute path, so cat doesn't confuse it with standard input | `cat /home/bandit1/-` |
| `./-` | Reads the "-" file by pointing to the current directory, avoiding the stdin confusion | `cat ./-` |
| `$(pwd)/-` | Combines pwd (the current path) with the file name; same effect as the absolute path | `cat $(pwd)/-` |
| `"spaces in this filename"` | Reads a file with spaces by wrapping its name in quotes so it's treated as a single name | `cat "spaces in this filename"` |
| `spaces\ in\ this\ filename` | Reads a file with spaces by escaping each space with a backslash so they don't split the arguments | `cat spaces\ in\ this\ filename` |
| `s*` | Uses a wildcard to fill in the file name, as long as no other file starts the same way | `cat s*` |
| `home/bandit/s*` | Same wildcard trick, but including the path to the file | `cat home/bandit/s*` |
| `~/.ssh/authorized_keys` | File with the SSH public keys allowed to log into that account without a password | `cat ~/.ssh/authorized_keys` |
| `/proc/net/tcp` | Virtual file with the active TCP connections (IPs, ports and state) in hexadecimal | `cat /proc/net/tcp` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-more"></a>

## `more`

Shows a command's output or a file one page at a time (space to advance, q to quit)

```bash
cat /etc/passwd | more
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `v` | From inside more, opens visual mode (the vi editor) on the content | `v (inside more)` |
| `:set shell=/bin/bash` | Once in visual mode (after Esc + Shift + :), sets Bash as the shell to use | `:set shell=/bin/bash` |
| `:shell` | Opens an interactive shell from visual mode, escaping more's context | `:shell` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-head"></a>

## `head`

Shows the first lines of a file or text (10 by default)

```bash
head -n 1 file.txt
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-n 1` | Shows only the first line of the file or text | `head -n 1 file.txt` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-tail"></a>

## `tail`

Shows the last lines of a file (10 by default), useful for logs

```bash
tail /var/log/syslog
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-n` | Sets how many lines from the end to show | `tail -n 20 /var/log/syslog` |
| `-n 1` | Shows only the last line of the file or text | `tail -n 1 file.txt` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-rev"></a>

## `rev`

Reverses the characters of each line, showing the text backwards

```bash
echo "hello" | rev
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-diff"></a>

## `diff`

Compares two files line by line and shows the differences between them

```bash
diff file1.txt file2.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-nano"></a>

## `nano`

Simple text editor in the terminal

```bash
nano notes.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-vi"></a>

## `vi`

Advanced, powerful text editor with a steeper learning curve than nano

```bash
vi notes.txt
```

<sub>[⬆ Back to top](#commands)</sub>
