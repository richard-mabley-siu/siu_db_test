# SIU Python Library
Useful common functions for Salukis.  In the future, this will be in the form of a [pip package](https://pip.pypa.io/en/stable/getting-started/).

## Oracle DB Link Setup
1. [Set up VSCode and the Python Extension and Jupyter Extensions](https://loop.cloud.microsoft/p/eyJ3Ijp7InUiOiJodHRwczovL3NhbHVraS5zaGFyZXBvaW50LmNvbS8%2FbmF2PWN6MGxNa1ltWkQxaUlWWjFRbFp1VFcxa2VUQjVSbVk0UkhjMVRIRnBhbUpJYjBGbGJHaHJWM1JPYTJkbmFsOUpUbGhUUzNoaE9VZHJkR2hzWHpkU1lYcDBSRXh2Vm00NE55MG1aajB3TVZkWlIwdEZWalZHVWs1V1MxSklWVlkwVGtkTFEweFpVRGRDTlU5R1FrVlhKbU05Sm1ac2RXbGtQVEUlM0QiLCJyIjpmYWxzZX0sInAiOnsidSI6Imh0dHBzOi8vc2FsdWtpLnNoYXJlcG9pbnQuY29tLzpmbDovZy9jb250ZW50c3RvcmFnZS9DU1BfMzlhY2ZkYzItYzY4OS00ODFjLTg2ODktNmNiZmM3ZDViZGFmL0VkNElFQWZIYW5oQ3BRcHFaUkRhU3djQk56aEJHR250NlpEWWFYSXJrY1dkb3c%2FbmF2PWN6MGxNa1pqYjI1MFpXNTBjM1J2Y21GblpTVXlSa05UVUY4ek9XRmpabVJqTWkxak5qZzVMVFE0TVdNdE9EWTRPUzAyWTJKbVl6ZGtOV0prWVdZbVpEMWlJWGQyTW5OUFdXNUhTRVZwUjJsWGVWOTRPVmM1Y2pSSFkwMVdWRWM0YzJoTGRFNXBiVXRaYlhFNGNXMWFTMmx5V1RWemJrWlNTVlZrVDBsaFgzRjFVR3dtWmowd01VODJNMUpDU0ZjMlFrRkpRVkJTTTB0UVFrSkxTME5VUzAxVlNVNVZVMWxJSm1NOUpUSkdKbVpzZFdsa1BURSUzRCIsInIiOnRydWV9LCJpIjp7ImkiOiI1ODEwMmNhYy0wYzcyLTRhZjQtYTQ4YS1mOTk0MGIyODI3OGYifX0%3D)
2. Set up a [virtual environment](https://pandas.pydata.org/docs/user_guide/10min.html)
3. [Clone this repo](https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=activity-bar) to your local dev environment via VS Code source control tab
4. Run "pip install -r requirements.txt" to install dependencies.
5. Run "python test_db.py" or open test_db.ipynb in VS Code to open the Juypter Notebook version.
6. Follow prompts to enter your usename and password (for DEV).
7. Ensure that the test query returns data.
8. Modify your query/code as needed.
9. Read more about the [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) and [Pandas](https://pandas.pydata.org/docs/user_guide/10min.html) libraries commonly used for data connections and manipulation in Python. 