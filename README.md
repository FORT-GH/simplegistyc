# simplegistyc

simplegistyc is a gistyc just more convenient, because it allows you to create, update the gists, without creating a file.

<i>simplegistyc has only been tested on Windows operating systems.</i>

---

## Prerequisites "taken from gistyc"

1. Python 3.8 (recommendation: using a virtual environment)
2. A <i>GitHub Personal access token</i> with GIST access:
  - Click on your personal account profile (top right)
  - Click <b>Settings</b>
  - On the left menu bar go to <b>Developer settings</b> and choose <b>Personal access tokens</b>
  - <b>Generate new token</b> and write a name (note) of your token. The note does not affect the functionality, but choose a note that describes the purpose of the token e.g., <i>GIST_token</i>
  - Set a mark at <b>gist</b> (<i>Create gists</i>) and click on <b>Generate token</b> at the bottom of the page
  - IMPORTANT: The displayed token appears only once. Copy it and store it in your GitHub project as a secret and / or locally as an environment variable.

---

## Installation
```bash
pip install simplegistyc
```

... or install it from the main branch of this [repository](https://github.com/FORT-GitHub/simplegistyc). You can also download the entire repository to run the tests, download the CI/CD scripts etc.

---

## Python library calls

<i>Please note: ./tests provides some examples that can be reproduced / applied.<br>
We assume:
- TOKEN: is the GIST access token
- FILEPATH: the name of the imaginary file (with extension)
- TEXT: text in FILEPATH
- ID_GIST: ID of a GIST.</i>

### Create a GIST

```python
import simplegistyc

create = simplegistyc.api.create_gist(filepath = FILEPATH , text = TEXT , token = TOKEN)
```

### Update a GIST

Updating a GIST requires either ONLY the FILEPATH or the FILEPATH AND a corresponding ID_GIST, if the GIST repository contains file names that occur more than once. Hint: keep your GIST repository clean from same-name files!

Update using ONLY the FILEPATH:

```python
import simplegistyc

update = simplegistyc.api.update_gist(filepath = FILEPATH , text = TEXT , token = TOKEN , id = ID_GIST)
```

## Get GISTs update

Please note: one can obtain a list of all GISTs via:

```python
import simplegistyc

update_url = simplegistyc.api.update_urlgists(filepath = FILEPATH , auth_token = TOKEN)
```

Best,<br>
FORT
