import requests
import argparse
import sys
import time

def ensure_login_details(infile):
    # Read login details from the provided file.
    secrets = {}
    for line in infile:
        if '=' not in line:
            continue
        key, value = line.strip().split('=')
        secrets[key] = value

    email = secrets.get('email')
    password = secrets.get('password')

    if not email or not password:
        raise KeyError("Email or password not found in the secrets file.")
    return email, password
    

def make_login_request(email, password):
     
    URL = 'https://select.live/login'

    form_data = {
        'email': email,
        'pwd': password
    }
    response = requests.post(URL, data=form_data)

    return response.headers.get('Set-Cookie')

def main():

    # Ensure user imputs a file containing their login details.
    parser = argparse.ArgumentParser(
        prog='Select Live Solar',
        description="Secrets file needed to access select live API."
    )

    parser.add_argument(
        'infile',
        metavar='[Path to Secrets File]',
        type=argparse.FileType('r'),
        help='This program requireds a file containing your login details as email and password variables.'
    )
    
    parser.add_argument(
        'count',
        metavar='[Number of Updates]',
        type=int,
        default=1,
        help='Number of times to return updates from Select Live.'
    )

    args = parser.parse_args()

    try:
        # Obtain login details from the provided file.
        email, password = ensure_login_details(args.infile)

        # Make login request to obtain user cookie.
        user_cookie = make_login_request(email, password)

        for _ in range(args.count):
            # Use the cookie to access the systems list.
            response = requests.get('https://select.live/systems/list', headers={
                'Cookie': user_cookie,
                'Referer' :'https://select.live/myprofile',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                'Host' : 'select.live',
            })

            if response.status_code == 200:
                print("Successfully accessed the systems list.")
                print(response.text)

            # Select Live only updates every 5 seconds so it's pointless to request data more frequently.
            time.sleep(5)

    except KeyError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        sys.exit(2)
    finally:
    # Close file
        args.infile.close()
    

if __name__ == "__main__":
    main()