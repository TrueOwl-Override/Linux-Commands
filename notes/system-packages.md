# 📦 System & Packages

> Update the system, manage packages and check system info.

**4** commands · **2** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`apt`](#cmd-apt) | Debian's package manager: refreshes the package list (update) and installs available updates (upgrade) |
| [`parrot-upgrade`](#cmd-parrot-upgrade) | Safely upgrades Parrot OS without breaking its own components |
| [`reboot`](#cmd-reboot) | Restarts the machine |
| [`neofetch`](#cmd-neofetch) | Shows system info (kernel, RAM, CPU, distro logo) in a visual way |

---

<a id="cmd-apt"></a>

## `apt`

Debian's package manager: refreshes the package list (update) and installs available updates (upgrade)

```bash
sudo apt update
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `update` | Refreshes the list of available packages from the repositories without installing anything | `sudo apt update` |
| `upgrade` | Installs updates for the packages you have installed (don't use it on Parrot) | `sudo apt upgrade` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-parrot-upgrade"></a>

## `parrot-upgrade`

Safely upgrades Parrot OS without breaking its own components

```bash
sudo parrot-upgrade
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-reboot"></a>

## `reboot`

Restarts the machine

```bash
sudo reboot
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-neofetch"></a>

## `neofetch`

Shows system info (kernel, RAM, CPU, distro logo) in a visual way

```bash
neofetch
```

<sub>[⬆ Back to top](#commands)</sub>
