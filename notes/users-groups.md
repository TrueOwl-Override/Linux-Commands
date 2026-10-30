# 👤 Users & Groups

> Check who you are, switch users, and manage accounts, passwords and groups.

**9** commands · **6** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`whoami`](#cmd-whoami) | Shows the name of the user you're currently logged in as |
| [`id`](#cmd-id) | Shows user info: UID, GID and the groups they belong to |
| [`sudo`](#cmd-sudo) | Runs a single command with administrator privileges without switching users |
| [`su`](#cmd-su) | Switches to another user in the terminal, asking for their password |
| [`exit`](#cmd-exit) | Closes the current session or leaves an elevated session (like root) |
| [`useradd`](#cmd-useradd) | Creates a new user on the system |
| [`usermod`](#cmd-usermod) | Modifies an existing user's properties (group, home, shell) |
| [`passwd`](#cmd-passwd) | Sets or changes a user's password |
| [`groupadd`](#cmd-groupadd) | Creates a new group on the system |

---

<a id="cmd-whoami"></a>

## `whoami`

Shows the name of the user you're currently logged in as

```bash
whoami
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-id"></a>

## `id`

Shows user info: UID, GID and the groups they belong to

```bash
id root
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sudo"></a>

## `sudo`

Runs a single command with administrator privileges without switching users

```bash
sudo apt update
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `su` | Switches to the root session permanently until you exit | `sudo su` |
| `pacman -Syu` | Arch Linux: syncs the package list and upgrades the whole system | `sudo pacman -Syu` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-su"></a>

## `su`

Switches to another user in the terminal, asking for their password

```bash
su - john
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-exit"></a>

## `exit`

Closes the current session or leaves an elevated session (like root)

```bash
exit
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-useradd"></a>

## `useradd`

Creates a new user on the system

```bash
sudo useradd john
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-s` | Sets the new user's shell | `sudo useradd -s /bin/bash john` |
| `-d` | Sets the new user's home folder | `sudo useradd -d /home/john john` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-usermod"></a>

## `usermod`

Modifies an existing user's properties (group, home, shell)

```bash
sudo usermod -s /bin/zsh john
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-a` | Together with -G, adds the user to a group without removing them from their current ones | `sudo usermod -a -G sudo john` |
| `-G` | Sets the user's secondary groups | `sudo usermod -G developers,docker john` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-passwd"></a>

## `passwd`

Sets or changes a user's password

```bash
sudo passwd john
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-groupadd"></a>

## `groupadd`

Creates a new group on the system

```bash
sudo groupadd developers
```

<sub>[⬆ Back to top](#commands)</sub>
