# 🔍 Searching

> Find files anywhere on the system and locate where commands live.

**5** commands · **14** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`find`](#cmd-find) | Searches for files and folders by criteria (name, type, permissions, date, etc.) |
| [`grep`](#cmd-grep) | Searches and filters lines of text that match a pattern |
| [`which`](#cmd-which) | Shows where a command or program is installed |
| [`command`](#cmd-command) | With -v, shows the path of a command, similar to which |
| [`xargs`](#cmd-xargs) | Takes a command's output and uses it as the arguments of another command |

---

<a id="cmd-find"></a>

## `find`

Searches for files and folders by criteria (name, type, permissions, date, etc.)

```bash
find /home -name "*.txt"
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-name` | Searches for files by exact name or with wildcards | `find -name '*xampl*.sh'` |
| `-type` | Filters by type: file (f) or directory (d) | `find /home -type f` |
| `-perm` | Filters by the file's specific permissions | `find / -perm -4000 2>/dev/null` |
| `-group` | Filters by owning group | `find /home -group developers` |
| `-user` | Filters by owning user | `find /home -user john` |
| `-writable` | Shows only files you have write permission on | `find /etc -writable 2>/dev/null` |
| `-executable` | Shows only files you have execute permission on | `find /usr/bin -executable -type f` |
| `-readable` | Shows only files you have read permission on | `find /var -readable 2>/dev/null` |
| `.` | Lists every file and folder in the current directory, including subdirectories | `find .` |
| `-size` | Filters the search by file size | `find -size 1033c` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-grep"></a>

## `grep`

Searches and filters lines of text that match a pattern

```bash
grep "error" log.txt
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-n` | Shows the line number of each match | `grep -n "root" /etc/passwd` |
| `-r "\w"` | Recursively finds lines with at least one alphanumeric character to locate content in files in any folder | `grep -r "\w" /home/user/` |
| `-vE "bashrc\\|profile"` | Shows the lines that do NOT match "bashrc" or "profile"; -v inverts the match and -E enables extended regex (\\| means "or") | `ls -a \| grep -vE "bashrc\|profile"` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-which"></a>

## `which`

Shows where a command or program is installed

```bash
which python3
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-command"></a>

## `command`

With -v, shows the path of a command, similar to which

```bash
command -v python3
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-v` | Shows the path of a command, similar to which | `command -v python3` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-xargs"></a>

## `xargs`

Takes a command's output and uses it as the arguments of another command

```bash
find . -name "*.log" | xargs ls -l
```

<sub>[⬆ Back to top](#commands)</sub>
