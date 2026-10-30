# 🔑 SSH & Remote Access

> Connect to remote machines and manage SSH keys.

**4** commands · **6** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`ssh`](#cmd-ssh) | Connects remotely and securely to another machine over the network, using a password or an SSH key |
| [`sshpass`](#cmd-sshpass) | Passes the SSH password directly in the command; handy for automation |
| [`ssh-keygen`](#cmd-ssh-keygen) | Generates an SSH key pair (public and private) to log in without a password |
| [`ssh-copy-id`](#cmd-ssh-copy-id) | Copies your SSH public key to a remote server's authorized_keys |

---

<a id="cmd-ssh"></a>

## `ssh`

Connects remotely and securely to another machine over the network, using a password or an SSH key

```bash
ssh user@192.168.1.10
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-p` | Sets the port to connect to when the SSH server doesn't use the default one (22) | `ssh -p 2222 user@192.168.1.10` |
| `bandit0@bandit.labs.overthewire.org -p 2220` | Connects to the Bandit server as bandit0 on port 2220 instead of 22 | `ssh bandit0@bandit.labs.overthewire.org -p 2220` |
| `-i` | Sets which private key file to use to authenticate over SSH | `ssh -i ~/.ssh/id_ed25519 user@192.168.1.10` |
| `user@host "command"` | Runs a command directly on the remote server when connecting, without loading a full interactive session or the user's bashrc | `ssh user@192.168.1.10 "ls -la"` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sshpass"></a>

## `sshpass`

Passes the SSH password directly in the command; handy for automation

```bash
sshpass -p 'my_password' ssh user@192.168.1.10
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-p` | Gives the password directly in the command so you don't have to type it when connecting over SSH | `sshpass -p 'my_password' ssh user@192.168.1.10` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-ssh-keygen"></a>

## `ssh-keygen`

Generates an SSH key pair (public and private) to log in without a password

```bash
ssh-keygen -t ed25519
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-ssh-copy-id"></a>

## `ssh-copy-id`

Copies your SSH public key to a remote server's authorized_keys

```bash
ssh-copy-id user@192.168.1.10
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-i` | Sets which public key file to copy when you have several keys | `ssh-copy-id -i ~/.ssh/id_ed25519.pub user@192.168.1.10` |

<sub>[⬆ Back to top](#commands)</sub>
