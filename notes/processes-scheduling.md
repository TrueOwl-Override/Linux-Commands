# ⏱️ Processes & Scheduling

> See what's running, limit or repeat commands, and schedule jobs with cron.

**5** commands · **4** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`ps`](#cmd-ps) | Shows the processes running on the system |
| [`sleep`](#cmd-sleep) | Pauses for a given number of seconds |
| [`timeout`](#cmd-timeout) | Runs a command and kills it automatically if it goes over the given time |
| [`watch`](#cmd-watch) | Runs a command repeatedly at regular intervals and shows its updated output |
| [`crontab`](#cmd-crontab) | Lets you view, create and edit a user's Cron jobs (scheduled tasks) |

---

<a id="cmd-ps"></a>

## `ps`

Shows the processes running on the system

```bash
ps
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-faux` | Shows every process from every user in a detailed tree format | `ps -faux` |
| `-eo command` | Shows only the command column for each process | `ps -eo command` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-sleep"></a>

## `sleep`

Pauses for a given number of seconds

```bash
sleep 5
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-timeout"></a>

## `timeout`

Runs a command and kills it automatically if it goes over the given time

```bash
timeout 5 ping 8.8.8.8
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-watch"></a>

## `watch`

Runs a command repeatedly at regular intervals and shows its updated output

```bash
watch ls -l /tmp
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-n 1` | Sets the interval in seconds between runs; here every 1 second | `watch -n 1 ls -l /tmp` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-crontab"></a>

## `crontab`

Lets you view, create and edit a user's Cron jobs (scheduled tasks)

```bash
crontab -l
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `* * * * * command` | Cron job format: Minute Hour Day-of-month Month Day-of-week Command; * means every value (every minute, hour, etc.) | `* * * * * /home/user/script.sh` |

<sub>[⬆ Back to top](#commands)</sub>
