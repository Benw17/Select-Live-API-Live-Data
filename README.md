# Select Live Solar API Client

A command-line Python tool that authenticates with the Select Live Solar platform and retrieves system data.

## Features
- Reads login credentials from a secure secrets file
- Logs into the Select Live dashboard via POST
- Persists cookies and session for subsequent requests
- Retrieves the user’s systems list for solar monitoring

## Future Plans
```bash
python select_live.py secrets.txt
```

## Future Plans

- I plan on adding a loop function to loop and return a live update, taking a numerical value as an arguement for the length of time.