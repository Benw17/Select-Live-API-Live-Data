# Select Live Solar API Client

A command-line Python tool that authenticates with the Select Live Solar platform and retrieves system data.

## Features
- Reads login credentials from a secure secrets file
- Logs into the Select Live dashboard via POST
- Persists cookies and session for subsequent requests
- Retrieves the user’s systems list for solar monitoring

## Usage
```bash
python select_live.py secrets.txt
```

## Future Plans

- I thought about adding in an SMS Gateway to send users important updates directly via Text. 
Things such as offline, battery is at a certain percentage.
