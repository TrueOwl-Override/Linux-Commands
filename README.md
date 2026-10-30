<div align="center">

# 🐧 Linux Commands

**My Linux command notes, organized by topic, with copy-ready examples.**

![Commands](https://img.shields.io/badge/commands-102-2ea44f?style=for-the-badge) ![Parameters](https://img.shields.io/badge/parameters-121-0969da?style=for-the-badge) ![Topics](https://img.shields.io/badge/topics-43-8250df?style=for-the-badge)

🌐 **Searchable web version:** [`docs/index.html`](docs/index.html)

</div>

---

## 📚 Sections

| | Section | Contents | Commands | Parameters |
|:-:|:--|:--|:-:|:-:|
| 🧠 | **[Concepts](notes/Concepts.md)** | Terminal fundamentals: users, permissions, redirection, searching and package management. | 58 | 66 |
| 🧪 | **[Labs](notes/Labs.md)** | Commands learned solving labs (OverTheWire Bandit): SSH, filtering, binaries, cron, git and more. | 44 | 55 |

## 🗂️ Topics

<details>
<summary><b>🧠 Concepts</b> — 17 topics</summary>

- [Basic Linux commands [1-2]](notes/Concepts.md#basic-linux-commands-1-2) — `whoami`, `id`, `sudo`, `exit`, `cat`, `which`, `echo`, `grep`, `|`, `Ctrl + L`
- [Basic Linux commands [2-2]](notes/Concepts.md#basic-linux-commands-2-2) — `pwd`, `ls`, `cd`, `bash`, `command`
- [Controlling stderr/stdout, operators and background processes](notes/Concepts.md#controlling-stderr-stdout-operators-and-background-processes) — `disown`, `;`, `&&`, `||`, `&`, `2>/dev/null`, `2>&1`, `&>/dev/null`
- [File descriptors](notes/Concepts.md#file-descriptors) — `>`, `>>`, `exec`
- [Reading and understanding permissions [1-2]](notes/Concepts.md#reading-and-understanding-permissions-1-2) — `touch`, `rm`, `nano`, `vi`
- [Reading and understanding permissions [2-2]](notes/Concepts.md#reading-and-understanding-permissions-2-2) — <i>parameters only</i>
- [Assigning permissions [1-2]](notes/Concepts.md#assigning-permissions-1-2) — `mkdir`, `su`, `chmod`, `chgrp`, `*`
- [Assigning permissions [2-2]](notes/Concepts.md#assigning-permissions-2-2) — `useradd`, `passwd`, `chown`, `groupadd`, `usermod`
- [Octal permission notation](notes/Concepts.md#octal-permission-notation) — <i>parameters only</i>
- [Special permissions - Sticky Bit](notes/Concepts.md#special-permissions-sticky-bit) — <i>parameters only</i>
- [File attributes - chattr and lsattr](notes/Concepts.md#file-attributes-chattr-and-lsattr) — `cp`, `lsattr`, `chattr`
- [Special permissions - SUID and SGID](notes/Concepts.md#special-permissions-suid-and-sgid) — `xargs`, `find`
- [Special privileges - Capabilities](notes/Concepts.md#special-privileges-capabilities) — `getcap`, `setcap`, `!$`
- [Using .bashrc and .zshrc](notes/Concepts.md#using-bashrc-and-zshrc) — `hostname`, `ifconfig`, `iwconfig`, `awk`, `cut`
- [Updating and upgrading the system](notes/Concepts.md#updating-and-upgrading-the-system) — `parrot-upgrade`, `reboot`, `apt`
- [System-wide searches](notes/Concepts.md#system-wide-searches) — `neofetch`
- [Reading text output](notes/Concepts.md#reading-text-output) — `tail`

</details>

<details>
<summary><b>🧪 Labs</b> — 26 topics</summary>

- [SSH connections](notes/Labs.md#ssh-connections) — `ssh`, `sshpass`, `export`
- [Reading special files [1-2]](notes/Labs.md#reading-special-files-1-2) — `rev`, `tr`, `head`
- [Reading special files [2-2]](notes/Labs.md#reading-special-files-2-2) — <i>parameters only</i>
- [Hidden directories and files](notes/Labs.md#hidden-directories-and-files) — `file`
- [Precise file searches [1-2]](notes/Labs.md#precise-file-searches-1-2) — <i>parameters only</i>
- [Data filtering methods [1-2]](notes/Labs.md#data-filtering-methods-1-2) — `sed`
- [Data filtering methods [2-2]](notes/Labs.md#data-filtering-methods-2-2) — `sort`, `uniq`
- [Reading binary files](notes/Labs.md#reading-binary-files) — `strings`
- [Base64 encoding and decoding](notes/Labs.md#base64-encoding-and-decoding) — `base64`
- [Caesar cipher and tr](notes/Labs.md#caesar-cipher-and-tr) — <i>parameters only</i>
- [Recursive decompression](notes/Labs.md#recursive-decompression) — `xxd`, `tee`, `sponge`, `ghex`, `7z`, `sleep`, `!?`
- [SSH key pairs and connections](notes/Labs.md#ssh-key-pairs-and-connections) — `ssh-keygen`, `ssh-copy-id`
- [Making connections with netcat](notes/Labs.md#making-connections-with-netcat) — `nc`, `ss`, `lsof`, `ps`, `bc`
- [Encrypted connections](notes/Labs.md#encrypted-connections) — `ncat`
- [Running commands over SSH](notes/Labs.md#running-commands-over-ssh) — <i>parameters only</i>
- [Finding differences between files](notes/Labs.md#finding-differences-between-files) — `diff`
- [Abusing SUID to switch users](notes/Labs.md#abusing-suid-to-switch-users) — `bash`
- [Abusing Cron jobs [1-3]](notes/Labs.md#abusing-cron-jobs-1-3) — `crontab`
- [Abusing Cron jobs [2-3]](notes/Labs.md#abusing-cron-jobs-2-3) — `md5sum`
- [Abusing Cron jobs [3-3]](notes/Labs.md#abusing-cron-jobs-3-3) — `stat`, `timeout`, `watch`
- [Escaping a command's context](notes/Labs.md#escaping-a-command-s-context) — `more`
- [Working with GitHub projects [1-5]](notes/Labs.md#working-with-github-projects-1-5) — `git clone`
- [Working with GitHub projects [2-5]](notes/Labs.md#working-with-github-projects-2-5) — `git log`, `git show`
- [Working with GitHub projects [3-5]](notes/Labs.md#working-with-github-projects-3-5) — `git branch`, `git checkout`
- [Working with GitHub projects [4-5]](notes/Labs.md#working-with-github-projects-4-5) — `git tag`
- [Working with GitHub projects [5-5]](notes/Labs.md#working-with-github-projects-5-5) — `git add`, `git commit`, `git push`

</details>

## 🔤 Alphabetical command index

| Command | What it does | Section |
|:--|:--|:--|
| `2>&1` | Redirects stderr to stdout, showing everything together | [Concepts](notes/Concepts.md#controlling-stderr-stdout-operators-and-background-processes) |
| `2>/dev/null` | Sends errors (stderr) to /dev/null so they aren't shown | [Concepts](notes/Concepts.md#controlling-stderr-stdout-operators-and-background-processes) |
| `7z` | Compresses and extracts .7z archives | [Labs](notes/Labs.md#recursive-decompression) |
| `apt` | Debian's package manager: refreshes the package list (update) and installs available updates (upgrade) | [Concepts](notes/Concepts.md#updating-and-upgrading-the-system) |
| `awk` | Processes and filters text by columns | [Concepts](notes/Concepts.md#using-bashrc-and-zshrc) |
| `base64` | Encodes text or a file to Base64, or decodes it back to its original form, depending on the flag | [Labs](notes/Labs.md#base64-encoding-and-decoding) |
| `bash` | The command interpreter that processes and runs what you type | [Concepts](notes/Concepts.md#basic-linux-commands-2-2) |
| `bc` | Terminal calculator; does arithmetic and converts numbers between bases (hexadecimal, decimal) | [Labs](notes/Labs.md#making-connections-with-netcat) |
| `cat` | Prints a file's contents to the terminal | [Concepts](notes/Concepts.md#basic-linux-commands-1-2) |
| `cd` | Changes directory | [Concepts](notes/Concepts.md#basic-linux-commands-2-2) |
| `chattr` | Changes a file's special attributes (for example making it immutable) | [Concepts](notes/Concepts.md#file-attributes-chattr-and-lsattr) |
| `chgrp` | Changes the group that owns a file or folder | [Concepts](notes/Concepts.md#assigning-permissions-1-2) |
| `chmod` | Changes the permissions of a file or folder; + adds and - removes a permission | [Concepts](notes/Concepts.md#assigning-permissions-1-2) |
| `chown` | Changes the owner and/or owning group of a file or folder | [Concepts](notes/Concepts.md#assigning-permissions-2-2) |
| `command` | With -v, shows the path of a command, similar to which | [Concepts](notes/Concepts.md#basic-linux-commands-2-2) |
| `cp` | Copies files or folders from one place to another | [Concepts](notes/Concepts.md#file-attributes-chattr-and-lsattr) |
| `crontab` | Lets you view, create and edit a user's Cron jobs (scheduled tasks) | [Labs](notes/Labs.md#abusing-cron-jobs-1-3) |
| `Ctrl + L` | Shortcut that clears the terminal screen without losing your history | [Concepts](notes/Concepts.md#basic-linux-commands-1-2) |
| `cut` | Extracts parts of a line of text, splitting it by a delimiter | [Concepts](notes/Concepts.md#using-bashrc-and-zshrc) |
| `diff` | Compares two files line by line and shows the differences between them | [Labs](notes/Labs.md#finding-differences-between-files) |
| `disown` | Detaches a background process from the terminal so it keeps running after you close it | [Concepts](notes/Concepts.md#controlling-stderr-stdout-operators-and-background-processes) |
| `echo` | Prints text or a variable's value to the terminal | [Concepts](notes/Concepts.md#basic-linux-commands-1-2) |
| `exec` | Manipulates the current session's file descriptors (open, close, redirect) | [Concepts](notes/Concepts.md#file-descriptors) |
| `exit` | Closes the current session or leaves an elevated session (like root) | [Concepts](notes/Concepts.md#basic-linux-commands-1-2) |
| `export` | Turns a variable into an environment variable, available to other processes started from that terminal | [Labs](notes/Labs.md#ssh-connections) |
| `file` | Analyzes a file and tells you what kind of content it has, regardless of its extension | [Labs](notes/Labs.md#hidden-directories-and-files) |
| `find` | Searches for files and folders by criteria (name, type, permissions, date, etc.) | [Concepts](notes/Concepts.md#special-permissions-suid-and-sgid) |
| `getcap` | Shows the capabilities assigned to a file | [Concepts](notes/Concepts.md#special-privileges-capabilities) |
| `ghex` | Hex editor with a graphical interface to view and modify a file's bytes | [Labs](notes/Labs.md#recursive-decompression) |
| `git add` | Adds files to the staging area so they're included in the next commit | [Labs](notes/Labs.md#working-with-github-projects-5-5) |
| `git branch` | Creates, lists, deletes and renames branches; it doesn't switch or merge them | [Labs](notes/Labs.md#working-with-github-projects-3-5) |
| `git checkout` | Switches to another branch or takes the project back to a previous commit | [Labs](notes/Labs.md#working-with-github-projects-3-5) |
| `git clone` | Downloads a full copy of a remote repository (like GitHub), with all its files and history | [Labs](notes/Labs.md#working-with-github-projects-1-5) |
| `git commit` | Saves the staged changes, creating a new version of the project in the local repo | [Labs](notes/Labs.md#working-with-github-projects-5-5) |
| `git log` | Lists every commit in the project with its ID, author, date and message | [Labs](notes/Labs.md#working-with-github-projects-2-5) |
| `git push` | Uploads commits from the local repo to the remote repo | [Labs](notes/Labs.md#working-with-github-projects-5-5) |
| `git show` | Shows the details and changes applied in a specific commit | [Labs](notes/Labs.md#working-with-github-projects-2-5) |
| `git tag` | Lists all the tags in the repo; a tag is a name that permanently marks a specific commit | [Labs](notes/Labs.md#working-with-github-projects-4-5) |
| `grep` | Searches and filters lines of text that match a pattern | [Concepts](notes/Concepts.md#basic-linux-commands-1-2) |
| `groupadd` | Creates a new group on the system | [Concepts](notes/Concepts.md#assigning-permissions-2-2) |
| `head` | Shows the first lines of a file or text (10 by default) | [Labs](notes/Labs.md#reading-special-files-1-2) |
| `hostname` | Shows or changes the machine's network name | [Concepts](notes/Concepts.md#using-bashrc-and-zshrc) |
| `id` | Shows user info: UID, GID and the groups they belong to | [Concepts](notes/Concepts.md#basic-linux-commands-1-2) |
| `ifconfig` | Shows and configures network interfaces (the IP of each card) | [Concepts](notes/Concepts.md#using-bashrc-and-zshrc) |
| `iwconfig` | Like ifconfig, but for wireless (Wi-Fi) interfaces | [Concepts](notes/Concepts.md#using-bashrc-and-zshrc) |
| `ls` | Lists the files and folders in the current directory | [Concepts](notes/Concepts.md#basic-linux-commands-2-2) |
| `lsattr` | Shows a file's special attributes (beyond the normal permissions) | [Concepts](notes/Concepts.md#file-attributes-chattr-and-lsattr) |
| `lsof` | Lists the files opened by running processes, including network connections | [Labs](notes/Labs.md#making-connections-with-netcat) |
| `md5sum` | Calculates the MD5 hash of a file or input, useful to check whether its content has changed | [Labs](notes/Labs.md#abusing-cron-jobs-2-3) |
| `mkdir` | Creates a new folder | [Concepts](notes/Concepts.md#assigning-permissions-1-2) |
| `more` | Shows a command's output or a file one page at a time (space to advance, q to quit) | [Labs](notes/Labs.md#escaping-a-command-s-context) |
| `nano` | Simple text editor in the terminal | [Concepts](notes/Concepts.md#reading-and-understanding-permissions-1-2) |
| `nc` | Netcat: creates manual TCP/UDP connections to send and receive data, scan ports or open remote shells | [Labs](notes/Labs.md#making-connections-with-netcat) |
| `ncat` | Improved netcat (from the Nmap project) with SSL/TLS encryption and authentication support | [Labs](notes/Labs.md#encrypted-connections) |
| `neofetch` | Shows system info (kernel, RAM, CPU, distro logo) in a visual way | [Concepts](notes/Concepts.md#system-wide-searches) |
| `parrot-upgrade` | Safely upgrades Parrot OS without breaking its own components | [Concepts](notes/Concepts.md#updating-and-upgrading-the-system) |
| `passwd` | Sets or changes a user's password | [Concepts](notes/Concepts.md#assigning-permissions-2-2) |
| `ps` | Shows the processes running on the system | [Labs](notes/Labs.md#making-connections-with-netcat) |
| `pwd` | Shows the full path of the current directory | [Concepts](notes/Concepts.md#basic-linux-commands-2-2) |
| `reboot` | Restarts the machine | [Concepts](notes/Concepts.md#updating-and-upgrading-the-system) |
| `rev` | Reverses the characters of each line, showing the text backwards | [Labs](notes/Labs.md#reading-special-files-1-2) |
| `rm` | Deletes files or folders | [Concepts](notes/Concepts.md#reading-and-understanding-permissions-1-2) |
| `sed` | Finds, replaces, deletes or modifies text in a file or stream, usually with regular expressions | [Labs](notes/Labs.md#data-filtering-methods-1-2) |
| `setcap` | Assigns specific capabilities to a file without granting full root privileges | [Concepts](notes/Concepts.md#special-privileges-capabilities) |
| `sleep` | Pauses for a given number of seconds | [Labs](notes/Labs.md#recursive-decompression) |
| `sort` | Sorts the lines of a file or text, alphabetically or numerically | [Labs](notes/Labs.md#data-filtering-methods-2-2) |
| `sponge` | Reads all of its input before writing it to a file, avoiding problems when overwriting the same file you're reading | [Labs](notes/Labs.md#recursive-decompression) |
| `ss` | Shows information about active network sockets, a modern alternative to netstat | [Labs](notes/Labs.md#making-connections-with-netcat) |
| `ssh` | Connects remotely and securely to another machine over the network, using a password or an SSH key | [Labs](notes/Labs.md#ssh-connections) |
| `ssh-copy-id` | Copies your SSH public key to a remote server's authorized_keys | [Labs](notes/Labs.md#ssh-key-pairs-and-connections) |
| `ssh-keygen` | Generates an SSH key pair (public and private) to log in without a password | [Labs](notes/Labs.md#ssh-key-pairs-and-connections) |
| `sshpass` | Passes the SSH password directly in the command; handy for automation | [Labs](notes/Labs.md#ssh-connections) |
| `stat` | Shows detailed info about a file or directory: permissions, size and access/modification dates | [Labs](notes/Labs.md#abusing-cron-jobs-3-3) |
| `strings` | Shows the readable text strings (ASCII) inside a binary file; useful for finding hidden info | [Labs](notes/Labs.md#reading-binary-files) |
| `su` | Switches to another user in the terminal, asking for their password | [Concepts](notes/Concepts.md#assigning-permissions-1-2) |
| `sudo` | Runs a single command with administrator privileges without switching users | [Concepts](notes/Concepts.md#basic-linux-commands-1-2) |
| `tail` | Shows the last lines of a file (10 by default), useful for logs | [Concepts](notes/Concepts.md#reading-text-output) |
| `tee` | Shows a command's output on screen and saves it to a file at the same time | [Labs](notes/Labs.md#recursive-decompression) |
| `timeout` | Runs a command and kills it automatically if it goes over the given time | [Labs](notes/Labs.md#abusing-cron-jobs-3-3) |
| `touch` | Creates an empty file, or updates its modification date if it already exists | [Concepts](notes/Concepts.md#reading-and-understanding-permissions-1-2) |
| `tr` | Translates or replaces characters of the incoming text with others | [Labs](notes/Labs.md#reading-special-files-1-2) |
| `uniq` | Removes consecutive duplicate lines; usually used after sort | [Labs](notes/Labs.md#data-filtering-methods-2-2) |
| `useradd` | Creates a new user on the system | [Concepts](notes/Concepts.md#assigning-permissions-2-2) |
| `usermod` | Modifies an existing user's properties (group, home, shell) | [Concepts](notes/Concepts.md#assigning-permissions-2-2) |
| `vi` | Advanced, powerful text editor with a steeper learning curve than nano | [Concepts](notes/Concepts.md#reading-and-understanding-permissions-1-2) |
| `watch` | Runs a command repeatedly at regular intervals and shows its updated output | [Labs](notes/Labs.md#abusing-cron-jobs-3-3) |
| `which` | Shows where a command or program is installed | [Concepts](notes/Concepts.md#basic-linux-commands-1-2) |
| `whoami` | Shows the name of the user you're currently logged in as | [Concepts](notes/Concepts.md#basic-linux-commands-1-2) |
| `xargs` | Takes a command's output and uses it as the arguments of another command | [Concepts](notes/Concepts.md#special-permissions-suid-and-sgid) |
| `xxd` | Shows a file's contents in hexadecimal | [Labs](notes/Labs.md#recursive-decompression) |
| `!$` | Stands for the last argument of the previous command, so you can reuse it | [Concepts](notes/Concepts.md#special-privileges-capabilities) |
| `!?` | Finds the most recent command in your history containing the given text and runs it again | [Labs](notes/Labs.md#recursive-decompression) |
| `&` | Runs the command in the background, leaving the terminal free | [Concepts](notes/Concepts.md#controlling-stderr-stdout-operators-and-background-processes) |
| `&&` | Runs the next command only if the previous one succeeded | [Concepts](notes/Concepts.md#controlling-stderr-stdout-operators-and-background-processes) |
| `&>/dev/null` | Sends both normal output and errors to /dev/null, hiding everything | [Concepts](notes/Concepts.md#controlling-stderr-stdout-operators-and-background-processes) |
| `*` | Wildcard that matches anything, to select several files at once | [Concepts](notes/Concepts.md#assigning-permissions-1-2) |
| `;` | Runs commands in sequence whether or not the previous one failed | [Concepts](notes/Concepts.md#controlling-stderr-stdout-operators-and-background-processes) |
| `>` | Redirects output to a file, overwriting its contents | [Concepts](notes/Concepts.md#file-descriptors) |
| `>>` | Redirects output to a file, appending it to the end | [Concepts](notes/Concepts.md#file-descriptors) |
| `\|` | Pipe: sends one command's output as the next command's input | [Concepts](notes/Concepts.md#basic-linux-commands-1-2) |
| `\|\|` | Runs the next command only if the previous one failed | [Concepts](notes/Concepts.md#controlling-stderr-stdout-operators-and-background-processes) |

## 🛠️ How to update

The data lives in [`data/commands.csv`](data/commands.csv) and [`data/parameters.csv`](data/parameters.csv). After editing them, run:

```bash
python3 scripts/build.py
```

This rebuilds this README, the notes in [`notes/`](notes) and the web page in [`docs/`](docs).

> 💡 To publish the web page: **Settings → Pages → Branch `main` / folder `/docs`**.
