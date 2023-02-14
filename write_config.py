import configparser


def write_to_ini(username: str, password: str) -> None:

    config = configparser.ConfigParser()
    config.read('settings.ini')
    config['logins']['INACCESS_USERNAME'] = username    # update
    config['logins']['INACCESS_PASSWORD'] = password   # create

    with open('settings.ini', 'w') as configfile:    # save
        config.write(configfile)
