# 🔐 Permissions & Attributes

> Control who can read, write and run files, plus special attributes and capabilities.

**7** commands · **12** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`chmod`](#cmd-chmod) | Changes the permissions of a file or folder; + adds and - removes a permission |
| [`chown`](#cmd-chown) | Changes the owner and/or owning group of a file or folder |
| [`chgrp`](#cmd-chgrp) | Changes the group that owns a file or folder |
| [`lsattr`](#cmd-lsattr) | Shows a file's special attributes (beyond the normal permissions) |
| [`chattr`](#cmd-chattr) | Changes a file's special attributes (for example making it immutable) |
| [`getcap`](#cmd-getcap) | Shows the capabilities assigned to a file |
| [`setcap`](#cmd-setcap) | Assigns specific capabilities to a file without granting full root privileges |

---

<a id="cmd-chmod"></a>

## `chmod`

Changes the permissions of a file or folder; + adds and - removes a permission

```bash
chmod 755 script.sh
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `o+w` | Adds write permission for "others" (other users) | `chmod o+w file.txt` |
| `o-w` | Removes write permission for "others" (other users) | `chmod o-w file.txt` |
| `755` | Octal notation: r=4, w=2, x=1, added up per block (owner, group, others); 755 means rwxr-xr-x and 777 means full permissions for everyone | `chmod 755 script.sh` |
| `+t` | Enables the Sticky Bit on a folder: only a file's owner or root can delete or rename it | `chmod +t /tmp/shared` |
| `4000` | Octal value of the SUID special permission | `chmod 4755 program` |
| `u+s` | Symbolic way to set SUID (s bit on the owner's execute permission) | `chmod u+s program` |
| `2000` | Octal value of the SGID special permission | `chmod 2755 folder` |
| `g+s` | Symbolic way to set SGID (s bit on the group's execute permission) | `chmod g+s folder` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-chown"></a>

## `chown`

Changes the owner and/or owning group of a file or folder

```bash
sudo chown john:developers file.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-chgrp"></a>

## `chgrp`

Changes the group that owns a file or folder

```bash
chgrp developers file.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-lsattr"></a>

## `lsattr`

Shows a file's special attributes (beyond the normal permissions)

```bash
lsattr file.txt
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-chattr"></a>

## `chattr`

Changes a file's special attributes (for example making it immutable)

```bash
sudo chattr +i file.txt
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `+i` | Makes the file immutable: nobody, not even root, can modify, delete or rename it until the attribute is removed | `sudo chattr +i file.txt` |
| `-V` | Verbose mode when changing the attribute | `sudo chattr -V +i file.txt` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-getcap"></a>

## `getcap`

Shows the capabilities assigned to a file

```bash
getcap /usr/bin/ping
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-r` | Searches for and shows capabilities recursively through subfolders | `getcap -r / 2>/dev/null` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-setcap"></a>

## `setcap`

Assigns specific capabilities to a file without granting full root privileges

```bash
sudo setcap cap_net_raw+ep /usr/bin/ping
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-r` | Removes the capabilities assigned to a file | `sudo setcap -r /usr/bin/ping` |

<sub>[⬆ Back to top](#commands)</sub>
