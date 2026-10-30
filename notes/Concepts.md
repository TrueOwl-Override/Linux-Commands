# 🧠 Concepts

> Terminal fundamentals: users, permissions, redirection, searching and package management.

**58** commands · **66** parameters · **17** topics  ·  [⬅ Back to index](../README.md)

## Topics

1. [Basic Linux commands [1-2]](#basic-linux-commands-1-2)
2. [Basic Linux commands [2-2]](#basic-linux-commands-2-2)
3. [Controlling stderr/stdout, operators and background processes](#controlling-stderr-stdout-operators-and-background-processes)
4. [File descriptors](#file-descriptors)
5. [Reading and understanding permissions [1-2]](#reading-and-understanding-permissions-1-2)
6. [Reading and understanding permissions [2-2]](#reading-and-understanding-permissions-2-2)
7. [Assigning permissions [1-2]](#assigning-permissions-1-2)
8. [Assigning permissions [2-2]](#assigning-permissions-2-2)
9. [Octal permission notation](#octal-permission-notation)
10. [Special permissions - Sticky Bit](#special-permissions-sticky-bit)
11. [File attributes - chattr and lsattr](#file-attributes-chattr-and-lsattr)
12. [Special permissions - SUID and SGID](#special-permissions-suid-and-sgid)
13. [Special privileges - Capabilities](#special-privileges-capabilities)
14. [Using .bashrc and .zshrc](#using-bashrc-and-zshrc)
15. [Updating and upgrading the system](#updating-and-upgrading-the-system)
16. [System-wide searches](#system-wide-searches)
17. [Reading text output](#reading-text-output)

---

<a id="basic-linux-commands-1-2"></a>

## Basic Linux commands [1-2]

| Command | What it does | Example |
|:--|:--|:--|
| `whoami` | Shows the name of the user you're currently logged in as | `whoami` |
| `id` | Shows user info: UID, GID and the groups they belong to | `id root` |
| `sudo` | Runs a single command with administrator privileges without switching users | `sudo apt update` |
| `exit` | Closes the current session or leaves an elevated session (like root) | `exit` |
| `cat` | Prints a file's contents to the terminal | `cat notes.txt` |
| `which` | Shows where a command or program is installed | `which python3` |
| `echo` | Prints text or a variable's value to the terminal | `echo "Hello world"` |
| `grep` | Searches and filters lines of text that match a pattern | `grep "error" log.txt` |
| `\|` | Pipe: sends one command's output as the next command's input | `cat /etc/passwd \| grep root` |
| `Ctrl + L` | Shortcut that clears the terminal screen without losing your history | `Ctrl + L (same as typing clear)` |

<details open>
<summary><b>🔧 Parameters & usage (4)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `sudo` | `su` | Switches to the root session permanently until you exit | `sudo su` |
| `grep` | `-n` | Shows the line number of each match | `grep -n "root" /etc/passwd` |
| `cat` | `/etc/group` | File listing the existing groups and their members | `cat /etc/group` |
| `echo` | `$PATH` | Variable holding the folders where the system looks for commands | `echo $PATH` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="basic-linux-commands-2-2"></a>

## Basic Linux commands [2-2]

| Command | What it does | Example |
|:--|:--|:--|
| `pwd` | Shows the full path of the current directory | `pwd` |
| `ls` | Lists the files and folders in the current directory | `ls /etc` |
| `cd` | Changes directory | `cd /var/log` |
| `bash` | The command interpreter that processes and runs what you type | `bash script.sh` |
| `command` | With -v, shows the path of a command, similar to which | `command -v python3` |

<details open>
<summary><b>🔧 Parameters & usage (12)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `command` | `-v` | Shows the path of a command, similar to which | `command -v python3` |
| `ls` | `-l` | Detailed listing (permissions, owner, size, date) | `ls -l /etc` |
| `cd` | `.` | Stays in the current folder | `cd .` |
| `cd` | `..` | Goes up one level to the parent folder | `cd ..` |
| `cd` | `(absolute path)` | Goes to a specific location starting from the system root | `cd /var/log` |
| `cd` | `(relative path)` | Goes to a location relative to the current directory | `cd ../documents` |
| `cd` | `/` | Goes straight to the system root | `cd /` |
| `cd` | `~` | Goes to the user's home folder | `cd ~` |
| `echo` | `$HOME` | Variable holding the path of the user's home folder | `echo $HOME` |
| `echo` | `$SHELL` | Variable holding the path of the shell in use (bash, zsh) | `echo $SHELL` |
| `cat` | `/etc/passwd` | File with basic user info (UID, home, shell) | `cat /etc/passwd` |
| `cat` | `/etc/shells` | File listing the shells installed and available | `cat /etc/shells` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="controlling-stderr-stdout-operators-and-background-processes"></a>

## Controlling stderr/stdout, operators and background processes

| Command | What it does | Example |
|:--|:--|:--|
| `disown` | Detaches a background process from the terminal so it keeps running after you close it | `sleep 100 & disown` |
| `;` | Runs commands in sequence whether or not the previous one failed | `cd /tmp ; ls` |
| `&&` | Runs the next command only if the previous one succeeded | `mkdir test && cd test` |
| `\|\|` | Runs the next command only if the previous one failed | `ping -c 1 8.8.8.8 \|\| echo "no connection"` |
| `&` | Runs the command in the background, leaving the terminal free | `sleep 60 &` |
| `2>/dev/null` | Sends errors (stderr) to /dev/null so they aren't shown | `find / -name "*.conf" 2>/dev/null` |
| `2>&1` | Redirects stderr to stdout, showing everything together | `ls /doesnotexist > output.txt 2>&1` |
| `&>/dev/null` | Sends both normal output and errors to /dev/null, hiding everything | `ping -c 1 8.8.8.8 &>/dev/null` |

<details open>
<summary><b>🔧 Parameters & usage (2)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `cat` | `/etc/hosts` | File with manual IP-to-domain mappings that skip DNS | `cat /etc/hosts` |
| `echo` | `$?` | Exit code of the last command (0 = success, anything else = error) | `ls /doesnotexist ; echo $?` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="file-descriptors"></a>

## File descriptors

| Command | What it does | Example |
|:--|:--|:--|
| `>` | Redirects output to a file, overwriting its contents | `echo "hello" > file.txt` |
| `>>` | Redirects output to a file, appending it to the end | `echo "another line" >> file.txt` |
| `exec` | Manipulates the current session's file descriptors (open, close, redirect) | `exec 3<> file.txt` |

<details open>
<summary><b>🔧 Parameters & usage (5)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `exec` | `3<> file` | Opens "file" for reading and writing as descriptor 3 | `exec 3<> file.txt` |
| `exec` | `>&3` | Redirects the session's standard output to descriptor 3 | `exec >&3` |
| `exec` | `3>&-` | Closes descriptor 3 | `exec 3>&-` |
| `exec` | `5>&3` | Duplicates descriptor 3 into descriptor 5 | `exec 5>&3` |
| `exec` | `8>&3-` | Duplicates descriptor 3 into 8 and closes the original 3 | `exec 8>&3-` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="reading-and-understanding-permissions-1-2"></a>

## Reading and understanding permissions [1-2]

| Command | What it does | Example |
|:--|:--|:--|
| `touch` | Creates an empty file, or updates its modification date if it already exists | `touch new.txt` |
| `rm` | Deletes files or folders | `rm old.txt` |
| `nano` | Simple text editor in the terminal | `nano notes.txt` |
| `vi` | Advanced, powerful text editor with a steeper learning curve than nano | `vi notes.txt` |

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="reading-and-understanding-permissions-2-2"></a>

## Reading and understanding permissions [2-2]

<details open>
<summary><b>🔧 Parameters & usage (2)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `cat` | `/etc/shadow` | File where users' encrypted passwords are stored | `sudo cat /etc/shadow` |
| `cat` | `/etc/login.defs` | System configuration; ENCRYPT_METHOD sets how passwords are hashed | `grep ENCRYPT_METHOD /etc/login.defs` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="assigning-permissions-1-2"></a>

## Assigning permissions [1-2]

| Command | What it does | Example |
|:--|:--|:--|
| `mkdir` | Creates a new folder | `mkdir projects` |
| `su` | Switches to another user in the terminal, asking for their password | `su - john` |
| `chmod` | Changes the permissions of a file or folder; + adds and - removes a permission | `chmod 755 script.sh` |
| `chgrp` | Changes the group that owns a file or folder | `chgrp developers file.txt` |
| `*` | Wildcard that matches anything, to select several files at once | `ls *.txt` |

<details open>
<summary><b>🔧 Parameters & usage (3)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `chmod` | `o+w` | Adds write permission for "others" (other users) | `chmod o+w file.txt` |
| `chmod` | `o-w` | Removes write permission for "others" (other users) | `chmod o-w file.txt` |
| `rm` | `-r` | Deletes folders and everything inside them recursively | `rm -r old_folder` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="assigning-permissions-2-2"></a>

## Assigning permissions [2-2]

| Command | What it does | Example |
|:--|:--|:--|
| `useradd` | Creates a new user on the system | `sudo useradd john` |
| `passwd` | Sets or changes a user's password | `sudo passwd john` |
| `chown` | Changes the owner and/or owning group of a file or folder | `sudo chown john:developers file.txt` |
| `groupadd` | Creates a new group on the system | `sudo groupadd developers` |
| `usermod` | Modifies an existing user's properties (group, home, shell) | `sudo usermod -s /bin/zsh john` |

<details open>
<summary><b>🔧 Parameters & usage (4)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `useradd` | `-s` | Sets the new user's shell | `sudo useradd -s /bin/bash john` |
| `useradd` | `-d` | Sets the new user's home folder | `sudo useradd -d /home/john john` |
| `usermod` | `-a` | Together with -G, adds the user to a group without removing them from their current ones | `sudo usermod -a -G sudo john` |
| `usermod` | `-G` | Sets the user's secondary groups | `sudo usermod -G developers,docker john` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="octal-permission-notation"></a>

## Octal permission notation

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `chmod` | `755` | Octal notation: r=4, w=2, x=1, added up per block (owner, group, others); 755 means rwxr-xr-x and 777 means full permissions for everyone | `chmod 755 script.sh` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="special-permissions-sticky-bit"></a>

## Special permissions - Sticky Bit

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `chmod` | `+t` | Enables the Sticky Bit on a folder: only a file's owner or root can delete or rename it | `chmod +t /tmp/shared` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="file-attributes-chattr-and-lsattr"></a>

## File attributes - chattr and lsattr

| Command | What it does | Example |
|:--|:--|:--|
| `cp` | Copies files or folders from one place to another | `cp file.txt copy.txt` |
| `lsattr` | Shows a file's special attributes (beyond the normal permissions) | `lsattr file.txt` |
| `chattr` | Changes a file's special attributes (for example making it immutable) | `sudo chattr +i file.txt` |

<details open>
<summary><b>🔧 Parameters & usage (3)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `rm` | `-f` | Forces deletion without asking, even if the file is write-protected | `rm -f protected_file.txt` |
| `chattr` | `+i` | Makes the file immutable: nobody, not even root, can modify, delete or rename it until the attribute is removed | `sudo chattr +i file.txt` |
| `chattr` | `-V` | Verbose mode when changing the attribute | `sudo chattr -V +i file.txt` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="special-permissions-suid-and-sgid"></a>

## Special permissions - SUID and SGID

| Command | What it does | Example |
|:--|:--|:--|
| `xargs` | Takes a command's output and uses it as the arguments of another command | `find . -name "*.log" \| xargs ls -l` |
| `find` | Searches for files and folders by criteria (name, type, permissions, date, etc.) | `find /home -name "*.txt"` |

<details open>
<summary><b>🔧 Parameters & usage (4)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `chmod` | `4000` | Octal value of the SUID special permission | `chmod 4755 program` |
| `chmod` | `u+s` | Symbolic way to set SUID (s bit on the owner's execute permission) | `chmod u+s program` |
| `chmod` | `2000` | Octal value of the SGID special permission | `chmod 2755 folder` |
| `chmod` | `g+s` | Symbolic way to set SGID (s bit on the group's execute permission) | `chmod g+s folder` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="special-privileges-capabilities"></a>

## Special privileges - Capabilities

| Command | What it does | Example |
|:--|:--|:--|
| `getcap` | Shows the capabilities assigned to a file | `getcap /usr/bin/ping` |
| `setcap` | Assigns specific capabilities to a file without granting full root privileges | `sudo setcap cap_net_raw+ep /usr/bin/ping` |
| `!$` | Stands for the last argument of the previous command, so you can reuse it | `mkdir project  then  cd !$` |

<details open>
<summary><b>🔧 Parameters & usage (2)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `getcap` | `-r` | Searches for and shows capabilities recursively through subfolders | `getcap -r / 2>/dev/null` |
| `setcap` | `-r` | Removes the capabilities assigned to a file | `sudo setcap -r /usr/bin/ping` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="using-bashrc-and-zshrc"></a>

## Using .bashrc and .zshrc

| Command | What it does | Example |
|:--|:--|:--|
| `hostname` | Shows or changes the machine's network name | `hostname` |
| `ifconfig` | Shows and configures network interfaces (the IP of each card) | `ifconfig eth0` |
| `iwconfig` | Like ifconfig, but for wireless (Wi-Fi) interfaces | `iwconfig wlan0` |
| `awk` | Processes and filters text by columns | `awk '{print $2}' data.txt` |
| `cut` | Extracts parts of a line of text, splitting it by a delimiter | `cut -d ":" -f 1 /etc/passwd` |

<details open>
<summary><b>🔧 Parameters & usage (7)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `ls` | `-a` | Shows all files including hidden ones (those starting with a dot) | `ls -a ~` |
| `hostname` | `-I` | Shows the IP address(es) assigned to the machine | `hostname -I` |
| `cut` | `-d` | Sets the delimiter used to split the text into columns | `cut -d ":" -f 1 /etc/passwd` |
| `cut` | `-f` | Selects the field (column) number to extract | `cut -d ":" -f 3 /etc/passwd` |
| `awk` | `'{print $1}'` | Prints the first column of each line | `ls -l \| awk '{print $1}'` |
| `alias` | `name='absolute_path'` | Creates a shortcut that runs a long command or path with a short word | `alias ll='ls -la'` |
| `export` | `variable_name` | Turns a variable into an environment variable available to other processes | `export MY_VAR="hello"` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="updating-and-upgrading-the-system"></a>

## Updating and upgrading the system

| Command | What it does | Example |
|:--|:--|:--|
| `parrot-upgrade` | Safely upgrades Parrot OS without breaking its own components | `sudo parrot-upgrade` |
| `reboot` | Restarts the machine | `sudo reboot` |
| `apt` | Debian's package manager: refreshes the package list (update) and installs available updates (upgrade) | `sudo apt update` |

<details open>
<summary><b>🔧 Parameters & usage (3)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `apt` | `update` | Refreshes the list of available packages from the repositories without installing anything | `sudo apt update` |
| `apt` | `upgrade` | Installs updates for the packages you have installed (don't use it on Parrot) | `sudo apt upgrade` |
| `sudo` | `pacman -Syu` | Arch Linux: syncs the package list and upgrades the whole system | `sudo pacman -Syu` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="system-wide-searches"></a>

## System-wide searches

| Command | What it does | Example |
|:--|:--|:--|
| `neofetch` | Shows system info (kernel, RAM, CPU, distro logo) in a visual way | `neofetch` |

<details open>
<summary><b>🔧 Parameters & usage (8)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `find` | `-name` | Searches for files by exact name or with wildcards | `find -name '*xampl*.sh'` |
| `find` | `-type` | Filters by type: file (f) or directory (d) | `find /home -type f` |
| `find` | `-perm` | Filters by the file's specific permissions | `find / -perm -4000 2>/dev/null` |
| `find` | `-group` | Filters by owning group | `find /home -group developers` |
| `find` | `-user` | Filters by owning user | `find /home -user john` |
| `find` | `-writable` | Shows only files you have write permission on | `find /etc -writable 2>/dev/null` |
| `find` | `-executable` | Shows only files you have execute permission on | `find /usr/bin -executable -type f` |
| `find` | `-readable` | Shows only files you have read permission on | `find /var -readable 2>/dev/null` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="reading-text-output"></a>

## Reading text output

| Command | What it does | Example |
|:--|:--|:--|
| `tail` | Shows the last lines of a file (10 by default), useful for logs | `tail /var/log/syslog` |

<details open>
<summary><b>🔧 Parameters & usage (5)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `tail` | `-n` | Sets how many lines from the end to show | `tail -n 20 /var/log/syslog` |
| `awk` | `'NR==2'` | Shows only line number 2 (NR = record number) | `awk 'NR==2' file.txt` |
| `awk` | `FS="/"` | Sets "/" as the field separator (FS) to split the text into columns | `echo "/home/john" \| awk '{print $2}' FS="/"` |
| `echo` | `-e` | Enables special characters (\n, \t) in the printed text | `echo -e "line1\nline2"` |
| `echo` | `-e "\n"` | \n is a line break; it needs the -e flag | `echo -e "Hello\nWorld"` |

</details>

<sub>[⬆ Back to top](#topics)</sub>
