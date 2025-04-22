import click
import keyring


options = {
    "postgres": {
        "name": "PostgreSQL",
        "source": "docker",
        "token": ["password"]
    },
    "tailscale": {
        "name": "Tailscale",
        "source": "keyring",
        "token": ["api_key"]
    },
    "cloudflare": {
        "name": "Cloudflare",
        "source": "keyring",
        "token": ["api_key"]
    },
    "vultr": {
        "name": "Vultr",
        "source": "keyring",
        "token": ["api_key"]
    }
}


@click.group()
def secrets():
    pass

@secrets.command(name="set")
@click.argument('service')
@click.argument('key')
@click.argument('value')
def secrets_set(service, key, value):
    print("Hellow Secrets Set :wave:")

@secrets.command(name="clear")
@click.argument('service')
def secrets_clear(service):
    print("Hellow Secrets Get :wave:")

@secrets.command(name="list")
def secrets_list():
    for service,values in options.items():
        if values['source'] == "keyring":
            for token in values['token']:
                check = keyring.get_password(service, token)
                if check is None:
                    print(f"✓ - {values['name'] | {token}}")
                else:
                    print(f"X - {values['name'] | {token}}")
