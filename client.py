from requests import get, post
import sys
import config


if __name__ == '__main__':
    settings = config.Settings()
    args = sys.argv[1:]

    try:
        if args[0] == 'get':
            response = get(settings.base_url + f'/get/{args[1]}')
        elif args[0] == 'history':
            response = get(settings.base_url + f'/history/{args[1]}')
        elif args[0] == 'set':
            response = post(settings.base_url + '/set', json={'key': args[1], 'value': args[2]})
        else:
            raise ValueError()
    except (IndexError, ValueError):
        print("Invalid command")
    else:
        print(response.json().get("message"))
