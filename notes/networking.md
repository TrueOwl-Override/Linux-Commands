# 🌐 Networking

> Network interfaces, open ports and sockets, and raw connections with netcat.

**7** commands · **4** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`hostname`](#cmd-hostname) | Shows or changes the machine's network name |
| [`ifconfig`](#cmd-ifconfig) | Shows and configures network interfaces (the IP of each card) |
| [`iwconfig`](#cmd-iwconfig) | Like ifconfig, but for wireless (Wi-Fi) interfaces |
| [`ss`](#cmd-ss) | Shows information about active network sockets, a modern alternative to netstat |
| [`lsof`](#cmd-lsof) | Lists the files opened by running processes, including network connections |
| [`nc`](#cmd-nc) | Netcat: creates manual TCP/UDP connections to send and receive data, scan ports or open remote shells |
| [`ncat`](#cmd-ncat) | Improved netcat (from the Nmap project) with SSL/TLS encryption and authentication support |

---

<a id="cmd-hostname"></a>

## `hostname`

Shows or changes the machine's network name

```bash
hostname
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-I` | Shows the IP address(es) assigned to the machine | `hostname -I` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-ifconfig"></a>

## `ifconfig`

Shows and configures network interfaces (the IP of each card)

```bash
ifconfig eth0
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-iwconfig"></a>

## `iwconfig`

Like ifconfig, but for wireless (Wi-Fi) interfaces

```bash
iwconfig wlan0
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-ss"></a>

## `ss`

Shows information about active network sockets, a modern alternative to netstat

```bash
ss
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-nltp` | Shows listening TCP sockets without resolving names, including the process behind each one | `sudo ss -nltp` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-lsof"></a>

## `lsof`

Lists the files opened by running processes, including network connections

```bash
lsof /var/log/syslog
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-i:` | Filters the output to show only connections related to the given port | `sudo lsof -i:80` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-nc"></a>

## `nc`

Netcat: creates manual TCP/UDP connections to send and receive data, scan ports or open remote shells

```bash
nc 192.168.1.10 80
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-ncat"></a>

## `ncat`

Improved netcat (from the Nmap project) with SSL/TLS encryption and authentication support

```bash
ncat 192.168.1.10 4444
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `--ssl` | Encrypts the connection with SSL/TLS to protect the data being sent | `ncat --ssl 192.168.1.10 443` |

<sub>[⬆ Back to top](#commands)</sub>
