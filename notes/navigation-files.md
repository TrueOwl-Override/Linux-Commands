# 📁 Navigation & Files

> Move around the filesystem and create, copy, delete and inspect files and folders.

**10** commands · **11** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`pwd`](#cmd-pwd) | Shows the full path of the current directory |
| [`ls`](#cmd-ls) | Lists the files and folders in the current directory |
| [`cd`](#cmd-cd) | Changes directory |
| [`mkdir`](#cmd-mkdir) | Creates a new folder |
| [`touch`](#cmd-touch) | Creates an empty file, or updates its modification date if it already exists |
| [`cp`](#cmd-cp) | Copies files or folders from one place to another |
| [`rm`](#cmd-rm) | Deletes files or folders |
| [`file`](#cmd-file) | Analyzes a file and tells you what kind of content it has, regardless of its extension |
| [`stat`](#cmd-stat) | Shows detailed info about a file or directory: permissions, size and access/modification dates |
| [`*`](#cmd-sym-42) | Wildcard that matches anything, to select several files at once |

---

<a id="cmd-pwd"></a>

## `pwd`

Shows the full path of the current directory

```bash
pwd
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-ls"></a>

## `ls`

Lists the files and folders in the current directory

```bash
ls /etc
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-l` | Detailed listing (permissions, owner, size, date) | `ls -l /etc` |
| `-a` | Shows all files including hidden ones (those starting with a dot) | `ls -a ~` |
| `/etc/cron.d` | Directory holding the configuration files of the system's Cron jobs | `ls -l /etc/cron.d` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-cd"></a>

## `cd`

Changes directory

```bash
cd /var/log
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `.` | Stays in the current folder | `cd .` |
| `..` | Goes up one level to the parent folder | `cd ..` |
| `(absolute path)` | Goes to a specific location starting from the system root | `cd /var/log` |
| `(relative path)` | Goes to a location relative to the current directory | `cd ../documents` |
| `/` | Goes straight to the system root | `cd /` |
| `~` | Goes to the user's home folder | `cd ~` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-mkdir"></a>

## `mkdir`

Creates a new folder

```bash
mkdir projects
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-touch"></a>

## `touch`

Creates an empty file, or updates its modification date if it already exists

```bash
touch new.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-cp"></a>

## `cp`

Copies files or folders from one place to another

```bash
cp file.txt copy.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-rm"></a>

## `rm`

Deletes files or folders

```bash
rm old.txt
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-r` | Deletes folders and everything inside them recursively | `rm -r old_folder` |
| `-f` | Forces deletion without asking, even if the file is write-protected | `rm -f protected_file.txt` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-file"></a>

## `file`

Analyzes a file and tells you what kind of content it has, regardless of its extension

```bash
file image.png
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-stat"></a>

## `stat`

Shows detailed info about a file or directory: permissions, size and access/modification dates

```bash
stat file.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sym-42"></a>

## `*`

Wildcard that matches anything, to select several files at once

```bash
ls *.txt
```

<sub>[⬆ Back to top](#commands)</sub>
