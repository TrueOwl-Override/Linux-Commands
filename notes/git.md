# 🌿 Git

> Version control: clone projects, explore history, work with branches and publish changes.

**9** commands · **8** parameters  ·  [⬅ Back to index](../README.md)

<a id="commands"></a>

| Command | What it does |
|:--|:--|
| [`git clone`](#cmd-git-clone) | Downloads a full copy of a remote repository (like GitHub), with all its files and history |
| [`git log`](#cmd-git-log) | Lists every commit in the project with its ID, author, date and message |
| [`git show`](#cmd-git-show) | Shows the details and changes applied in a specific commit |
| [`git branch`](#cmd-git-branch) | Creates, lists, deletes and renames branches; it doesn't switch or merge them |
| [`git checkout`](#cmd-git-checkout) | Switches to another branch or takes the project back to a previous commit |
| [`git tag`](#cmd-git-tag) | Lists all the tags in the repo; a tag is a name that permanently marks a specific commit |
| [`git add`](#cmd-git-add) | Adds files to the staging area so they're included in the next commit |
| [`git commit`](#cmd-git-commit) | Saves the staged changes, creating a new version of the project in the local repo |
| [`git push`](#cmd-git-push) | Uploads commits from the local repo to the remote repo |

---

<a id="cmd-git-clone"></a>

## `git clone`

Downloads a full copy of a remote repository (like GitHub), with all its files and history

```bash
git clone https://github.com/user/project.git
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-git-log"></a>

## `git log`

Lists every commit in the project with its ID, author, date and message

```bash
git log
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-git-show"></a>

## `git show`

Shows the details and changes applied in a specific commit

```bash
git show a1b2c3d
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `(commit id)` | Shows every change applied in that commit | `git show a1b2c3d` |
| `(tag name)` | Shows info about the given tag and the commit it points to, with its changes | `git show v1.0` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-git-branch"></a>

## `git branch`

Creates, lists, deletes and renames branches; it doesn't switch or merge them

```bash
git branch
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-a` | Lists every branch in the project, both local and remote | `git branch -a` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-git-checkout"></a>

## `git checkout`

Switches to another branch or takes the project back to a previous commit

```bash
git checkout main
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `(commit id)` | Takes the project back to that point in history, restoring the files that existed then | `git checkout a1b2c3d` |
| `(branch name)` | Switches to the given branch by name | `git checkout develop` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-git-tag"></a>

## `git tag`

Lists all the tags in the repo; a tag is a name that permanently marks a specific commit

```bash
git tag
```

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-git-add"></a>

## `git add`

Adds files to the staging area so they're included in the next commit

```bash
git add file.txt
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-f` | Forces a file into the staging area even if .gitignore ignores it | `git add -f key.txt` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-git-commit"></a>

## `git commit`

Saves the staged changes, creating a new version of the project in the local repo

```bash
git commit -m "First change"
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-m "identifier"` | Sets the message that identifies the commit | `git commit -m "Add key.txt"` |

<sub>[⬆ Back to top](#commands)</sub>

---

<a id="cmd-git-push"></a>

## `git push`

Uploads commits from the local repo to the remote repo

```bash
git push origin master
```

| Parameter | What it does | Example |
|:--|:--|:--|
| `-u origin branch` | Pushes commits to the given branch on the origin remote and links it so later push/pull don't need it spelled out | `git push -u origin master` |

<sub>[⬆ Back to top](#commands)</sub>
