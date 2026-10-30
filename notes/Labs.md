# 🧪 Labs

> Commands learned solving labs (OverTheWire Bandit): SSH, filtering, binaries, cron, git and more.

**44** commands · **55** parameters · **26** topics  ·  [⬅ Back to index](../README.md)

## Topics

1. [SSH connections](#ssh-connections)
2. [Reading special files [1-2]](#reading-special-files-1-2)
3. [Reading special files [2-2]](#reading-special-files-2-2)
4. [Hidden directories and files](#hidden-directories-and-files)
5. [Precise file searches [1-2]](#precise-file-searches-1-2)
6. [Data filtering methods [1-2]](#data-filtering-methods-1-2)
7. [Data filtering methods [2-2]](#data-filtering-methods-2-2)
8. [Reading binary files](#reading-binary-files)
9. [Base64 encoding and decoding](#base64-encoding-and-decoding)
10. [Caesar cipher and tr](#caesar-cipher-and-tr)
11. [Recursive decompression](#recursive-decompression)
12. [SSH key pairs and connections](#ssh-key-pairs-and-connections)
13. [Making connections with netcat](#making-connections-with-netcat)
14. [Encrypted connections](#encrypted-connections)
15. [Running commands over SSH](#running-commands-over-ssh)
16. [Finding differences between files](#finding-differences-between-files)
17. [Abusing SUID to switch users](#abusing-suid-to-switch-users)
18. [Abusing Cron jobs [1-3]](#abusing-cron-jobs-1-3)
19. [Abusing Cron jobs [2-3]](#abusing-cron-jobs-2-3)
20. [Abusing Cron jobs [3-3]](#abusing-cron-jobs-3-3)
21. [Escaping a command's context](#escaping-a-command-s-context)
22. [Working with GitHub projects [1-5]](#working-with-github-projects-1-5)
23. [Working with GitHub projects [2-5]](#working-with-github-projects-2-5)
24. [Working with GitHub projects [3-5]](#working-with-github-projects-3-5)
25. [Working with GitHub projects [4-5]](#working-with-github-projects-4-5)
26. [Working with GitHub projects [5-5]](#working-with-github-projects-5-5)

---

<a id="ssh-connections"></a>

## SSH connections

| Command | What it does | Example |
|:--|:--|:--|
| `ssh` | Connects remotely and securely to another machine over the network, using a password or an SSH key | `ssh user@192.168.1.10` |
| `sshpass` | Passes the SSH password directly in the command; handy for automation | `sshpass -p 'my_password' ssh user@192.168.1.10` |
| `export` | Turns a variable into an environment variable, available to other processes started from that terminal | `export TERM=xterm` |

<details open>
<summary><b>🔧 Parameters & usage (4)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `ssh` | `-p` | Sets the port to connect to when the SSH server doesn't use the default one (22) | `ssh -p 2222 user@192.168.1.10` |
| `export` | `TERM=xterm` | Sets the terminal type; useful when a remote connection has compatibility issues | `export TERM=xterm` |
| `sshpass` | `-p` | Gives the password directly in the command so you don't have to type it when connecting over SSH | `sshpass -p 'my_password' ssh user@192.168.1.10` |
| `ssh` | `bandit0@bandit.labs.overthewire.org -p 2220` | Connects to the Bandit server as bandit0 on port 2220 instead of 22 | `ssh bandit0@bandit.labs.overthewire.org -p 2220` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="reading-special-files-1-2"></a>

## Reading special files [1-2]

| Command | What it does | Example |
|:--|:--|:--|
| `rev` | Reverses the characters of each line, showing the text backwards | `echo "hello" \| rev` |
| `tr` | Translates or replaces characters of the incoming text with others | `echo "a:b:c" \| tr ':' ' '` |
| `head` | Shows the first lines of a file or text (10 by default) | `head -n 1 file.txt` |

<details open>
<summary><b>🔧 Parameters & usage (10)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `cat` | `/home/bandit1/-` | Reads the file named "-" by its absolute path, so cat doesn't confuse it with standard input | `cat /home/bandit1/-` |
| `cat` | `./-` | Reads the "-" file by pointing to the current directory, avoiding the stdin confusion | `cat ./-` |
| `cat` | `$(pwd)/-` | Combines pwd (the current path) with the file name; same effect as the absolute path | `cat $(pwd)/-` |
| `grep` | `-r "\w"` | Recursively finds lines with at least one alphanumeric character to locate content in files in any folder | `grep -r "\w" /home/user/` |
| `cut` | `-d ':' -f 2` | Splits each line using ":" as the delimiter and extracts only the second field | `echo "a:b:c" \| cut -d ':' -f 2` |
| `tr` | `':' ' '` | Replaces every ":" with a space in the processed text | `echo "a:b:c" \| tr ':' ' '` |
| `awk` | `'{print $2}' FS=":"` | Uses ":" as the field separator (FS) and prints the second column of each line | `echo "a:b:c" \| awk '{print $2}' FS=":"` |
| `awk` | `'NF{print $NF}'` | Prints the last field of each line; NF is the number of fields and $NF the value of the last one | `echo "one two three" \| awk 'NF{print $NF}'` |
| `tail` | `-n 1` | Shows only the last line of the file or text | `tail -n 1 file.txt` |
| `head` | `-n 1` | Shows only the first line of the file or text | `head -n 1 file.txt` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="reading-special-files-2-2"></a>

## Reading special files [2-2]

<details open>
<summary><b>🔧 Parameters & usage (4)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `cat` | `"spaces in this filename"` | Reads a file with spaces by wrapping its name in quotes so it's treated as a single name | `cat "spaces in this filename"` |
| `cat` | `spaces\ in\ this\ filename` | Reads a file with spaces by escaping each space with a backslash so they don't split the arguments | `cat spaces\ in\ this\ filename` |
| `cat` | `s*` | Uses a wildcard to complete the name automatically, as long as no other file starts the same way | `cat s*` |
| `cat` | `home/bandit/s*` | Same as above, but specifying the path where the file is | `cat home/bandit/s*` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="hidden-directories-and-files"></a>

## Hidden directories and files

| Command | What it does | Example |
|:--|:--|:--|
| `file` | Analyzes a file and tells you what kind of content it has, regardless of its extension | `file image.png` |

<details open>
<summary><b>🔧 Parameters & usage (2)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `find` | `.` | Lists every file and folder in the current directory, including subdirectories | `find .` |
| `grep` | `-vE "bashrc\\|profile"` | Shows the lines that do NOT match "bashrc" or "profile"; -v inverts the match and -E enables extended regex (\\| means "or") | `ls -a \| grep -vE "bashrc\|profile"` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="precise-file-searches-1-2"></a>

## Precise file searches [1-2]

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `find` | `-size` | Filters the search by file size | `find -size 1033c` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="data-filtering-methods-1-2"></a>

## Data filtering methods [1-2]

| Command | What it does | Example |
|:--|:--|:--|
| `sed` | Finds, replaces, deletes or modifies text in a file or stream, usually with regular expressions | `sed 's/old/new/g' file.txt` |

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="data-filtering-methods-2-2"></a>

## Data filtering methods [2-2]

| Command | What it does | Example |
|:--|:--|:--|
| `sort` | Sorts the lines of a file or text, alphabetically or numerically | `sort names.txt` |
| `uniq` | Removes consecutive duplicate lines; usually used after sort | `sort names.txt \| uniq` |

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `uniq` | `-u` | Shows only completely unique lines, the ones that never repeat | `sort data.txt \| uniq -u` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="reading-binary-files"></a>

## Reading binary files

| Command | What it does | Example |
|:--|:--|:--|
| `strings` | Shows the readable text strings (ASCII) inside a binary file; useful for finding hidden info | `strings program.bin` |

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="base64-encoding-and-decoding"></a>

## Base64 encoding and decoding

| Command | What it does | Example |
|:--|:--|:--|
| `base64` | Encodes text or a file to Base64, or decodes it back to its original form, depending on the flag | `echo "hello" \| base64` |

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `base64` | `-d` | Decodes Base64 text back to its original form | `echo "aG9sYQ==" \| base64 -d` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="caesar-cipher-and-tr"></a>

## Caesar cipher and tr

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `tr` | `'[A-Za-z]' '[N-ZA-Mn-za-m]'` | Replaces each letter with the one 13 positions ahead, applying the ROT13 cipher | `echo "Uryyb" \| tr '[A-Za-z]' '[N-ZA-Mn-za-m]'` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="recursive-decompression"></a>

## Recursive decompression

| Command | What it does | Example |
|:--|:--|:--|
| `xxd` | Shows a file's contents in hexadecimal | `xxd file.bin` |
| `tee` | Shows a command's output on screen and saves it to a file at the same time | `ls \| tee list.txt` |
| `sponge` | Reads all of its input before writing it to a file, avoiding problems when overwriting the same file you're reading | `sort data.txt \| sponge data.txt` |
| `ghex` | Hex editor with a graphical interface to view and modify a file's bytes | `ghex file.bin` |
| `7z` | Compresses and extracts .7z archives | `7z a backup.7z folder/` |
| `sleep` | Pauses for a given number of seconds | `sleep 5` |
| `!?` | Finds the most recent command in your history containing the given text and runs it again | `!?ssh` |

<details open>
<summary><b>🔧 Parameters & usage (5)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `xxd` | `-p` | Shows plain hexadecimal output, without addresses or text alongside | `xxd -p file.bin` |
| `xxd` | `-s` | Skips to a specific offset in the file before showing it in hexadecimal | `xxd -s 16 file.bin` |
| `xxd` | `-r` | Turns a hex dump back into binary | `xxd -r data.hex output.bin` |
| `7z` | `l` | Lists an archive's contents without extracting it | `7z l backup.7z` |
| `7z` | `x` | Extracts an archive's contents keeping its folder structure | `7z x backup.7z` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="ssh-key-pairs-and-connections"></a>

## SSH key pairs and connections

| Command | What it does | Example |
|:--|:--|:--|
| `ssh-keygen` | Generates an SSH key pair (public and private) to log in without a password | `ssh-keygen -t ed25519` |
| `ssh-copy-id` | Copies your SSH public key to a remote server's authorized_keys | `ssh-copy-id user@192.168.1.10` |

<details open>
<summary><b>🔧 Parameters & usage (3)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `ssh-copy-id` | `-i` | Sets which public key file to copy when you have several keys | `ssh-copy-id -i ~/.ssh/id_ed25519.pub user@192.168.1.10` |
| `ssh` | `-i` | Sets which private key file to use to authenticate over SSH | `ssh -i ~/.ssh/id_ed25519 user@192.168.1.10` |
| `cat` | `~/.ssh/authorized_keys` | File with the SSH public keys allowed to log into that account without a password | `cat ~/.ssh/authorized_keys` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="making-connections-with-netcat"></a>

## Making connections with netcat

| Command | What it does | Example |
|:--|:--|:--|
| `nc` | Netcat: creates manual TCP/UDP connections to send and receive data, scan ports or open remote shells | `nc 192.168.1.10 80` |
| `ss` | Shows information about active network sockets, a modern alternative to netstat | `ss` |
| `lsof` | Lists the files opened by running processes, including network connections | `lsof /var/log/syslog` |
| `ps` | Shows the processes running on the system | `ps` |
| `bc` | Terminal calculator; does arithmetic and converts numbers between bases (hexadecimal, decimal) | `echo "obase=10; ibase=16; FF" \| bc` |

<details open>
<summary><b>🔧 Parameters & usage (6)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `ss` | `-nltp` | Shows listening TCP sockets without resolving names, including the process behind each one | `sudo ss -nltp` |
| `lsof` | `-i:` | Filters the output to show only connections related to the given port | `sudo lsof -i:80` |
| `ps` | `-faux` | Shows every process from every user in a detailed tree format | `ps -faux` |
| `ps` | `-eo command` | Shows only the command column for each process | `ps -eo command` |
| `echo` | `"obase=10; ibase=16; $hexNum" \| bc` | Converts a variable's hexadecimal value to decimal using bc | `hexNum="FF"; echo "obase=10; ibase=16; $hexNum" \| bc` |
| `cat` | `/proc/net/tcp` | Virtual file with the active TCP connections (IPs, ports and state) in hexadecimal | `cat /proc/net/tcp` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="encrypted-connections"></a>

## Encrypted connections

| Command | What it does | Example |
|:--|:--|:--|
| `ncat` | Improved netcat (from the Nmap project) with SSL/TLS encryption and authentication support | `ncat 192.168.1.10 4444` |

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `ncat` | `--ssl` | Encrypts the connection with SSL/TLS to protect the data being sent | `ncat --ssl 192.168.1.10 443` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="running-commands-over-ssh"></a>

## Running commands over SSH

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `ssh` | `user@host "command"` | Runs a command directly on the remote server when connecting, without loading a full interactive session or the user's bashrc | `ssh user@192.168.1.10 "ls -la"` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="finding-differences-between-files"></a>

## Finding differences between files

| Command | What it does | Example |
|:--|:--|:--|
| `diff` | Compares two files line by line and shows the differences between them | `diff file1.txt file2.txt` |

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="abusing-suid-to-switch-users"></a>

## Abusing SUID to switch users

| Command | What it does | Example |
|:--|:--|:--|
| `bash` | Starts a new Bash shell, to get an interactive shell, run scripts or escape restricted shells | `bash` |

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `bash` | `-p` | Starts the shell in privileged mode so the effective UID/GID aren't reset; useful to keep privileges gained through SUID | `bash -p` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="abusing-cron-jobs-1-3"></a>

## Abusing Cron jobs [1-3]

| Command | What it does | Example |
|:--|:--|:--|
| `crontab` | Lets you view, create and edit a user's Cron jobs (scheduled tasks) | `crontab -l` |

<details open>
<summary><b>🔧 Parameters & usage (2)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `ls` | `/etc/cron.d` | Directory holding the configuration files of the system's Cron jobs | `ls -l /etc/cron.d` |
| `crontab` | `* * * * * command` | Cron job format: Minute Hour Day-of-month Month Day-of-week Command; * means every value (every minute, hour, etc.) | `* * * * * /home/user/script.sh` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="abusing-cron-jobs-2-3"></a>

## Abusing Cron jobs [2-3]

| Command | What it does | Example |
|:--|:--|:--|
| `md5sum` | Calculates the MD5 hash of a file or input, useful to check whether its content has changed | `md5sum file.txt` |

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="abusing-cron-jobs-3-3"></a>

## Abusing Cron jobs [3-3]

| Command | What it does | Example |
|:--|:--|:--|
| `stat` | Shows detailed info about a file or directory: permissions, size and access/modification dates | `stat file.txt` |
| `timeout` | Runs a command and kills it automatically if it goes over the given time | `timeout 5 ping 8.8.8.8` |
| `watch` | Runs a command repeatedly at regular intervals and shows its updated output | `watch ls -l /tmp` |

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `watch` | `-n 1` | Sets the interval in seconds between runs; here every 1 second | `watch -n 1 ls -l /tmp` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="escaping-a-command-s-context"></a>

## Escaping a command's context

| Command | What it does | Example |
|:--|:--|:--|
| `more` | Shows a command's output or a file one page at a time (space to advance, q to quit) | `cat /etc/passwd \| more` |

<details open>
<summary><b>🔧 Parameters & usage (3)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `more` | `v` | From inside more, opens visual mode (the vi editor) on the content | `v (inside more)` |
| `more` | `:set shell=/bin/bash` | Once in visual mode (after Esc + Shift + :), sets Bash as the shell to use | `:set shell=/bin/bash` |
| `more` | `:shell` | Opens an interactive shell from visual mode, escaping more's context | `:shell` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="working-with-github-projects-1-5"></a>

## Working with GitHub projects [1-5]

| Command | What it does | Example |
|:--|:--|:--|
| `git clone` | Downloads a full copy of a remote repository (like GitHub), with all its files and history | `git clone https://github.com/user/project.git` |

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="working-with-github-projects-2-5"></a>

## Working with GitHub projects [2-5]

| Command | What it does | Example |
|:--|:--|:--|
| `git log` | Lists every commit in the project with its ID, author, date and message | `git log` |
| `git show` | Shows the details and changes applied in a specific commit | `git show a1b2c3d` |

<details open>
<summary><b>🔧 Parameters & usage (2)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `git show` | `(commit id)` | Shows every change applied in that commit | `git show a1b2c3d` |
| `git checkout` | `(commit id)` | Takes the project back to that point in history, restoring the files that existed then | `git checkout a1b2c3d` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="working-with-github-projects-3-5"></a>

## Working with GitHub projects [3-5]

| Command | What it does | Example |
|:--|:--|:--|
| `git branch` | Creates, lists, deletes and renames branches; it doesn't switch or merge them | `git branch` |
| `git checkout` | Switches to another branch or takes the project back to a previous commit | `git checkout main` |

<details open>
<summary><b>🔧 Parameters & usage (2)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `git branch` | `-a` | Lists every branch in the project, both local and remote | `git branch -a` |
| `git checkout` | `(branch name)` | Switches to the given branch by name | `git checkout develop` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="working-with-github-projects-4-5"></a>

## Working with GitHub projects [4-5]

| Command | What it does | Example |
|:--|:--|:--|
| `git tag` | Lists all the tags in the repo; a tag is a name that permanently marks a specific commit | `git tag` |

<details open>
<summary><b>🔧 Parameters & usage (1)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `git show` | `(tag name)` | Shows info about the given tag and the commit it points to, with its changes | `git show v1.0` |

</details>

<sub>[⬆ Back to top](#topics)</sub>

---

<a id="working-with-github-projects-5-5"></a>

## Working with GitHub projects [5-5]

| Command | What it does | Example |
|:--|:--|:--|
| `git add` | Adds files to the staging area so they're included in the next commit | `git add file.txt` |
| `git commit` | Saves the staged changes, creating a new version of the project in the local repo | `git commit -m "First change"` |
| `git push` | Uploads commits from the local repo to the remote repo | `git push origin master` |

<details open>
<summary><b>🔧 Parameters & usage (3)</b></summary>

| Command | Parameter | What it does | Example |
|:--|:--|:--|:--|
| `git add` | `-f` | Forces a file into the staging area even if .gitignore ignores it | `git add -f key.txt` |
| `git commit` | `-m "identifier"` | Sets the message that identifies the commit | `git commit -m "Add key.txt"` |
| `git push` | `-u origin branch` | Pushes commits to the given branch on the origin remote and links it so later push/pull don't need it spelled out | `git push -u origin master` |

</details>

<sub>[⬆ Back to top](#topics)</sub>
