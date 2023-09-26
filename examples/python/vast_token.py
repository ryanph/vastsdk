#!/usr/bin/env python3

import logging
import json
import urllib3
import vastsdk

from vastsdk.api import TokenApi

logging.basicConfig(level=logging.DEBUG)

def read_settings():

    log = logging.getLogger("read_settings")
    log.info("Reading configuration from file settings.json")

    with open("settings.json") as f:
        return json.load(f)

def create_client(settings=read_settings()):

    log = logging.getLogger("create_client")
    log.info("Creating API Client for {}".format(settings['vms_url']))

    config = vastsdk.Configuration(
        host = settings['vms_url']
    )

    if settings['verify_ssl'] is False:
        log.info("Disabling SSL verification and warnings")
        config.verify_ssl = settings['verify_ssl']
        urllib3.disable_warnings() 

    vastApiClient = vastsdk.ApiClient(config)

    tokens = create_token(vastApiClient, settings['vms_username'], settings['vms_password'])
    log.info("Appending token to API client for future requests")
    config.access_token = str(tokens.access)
    
    return vastApiClient

def create_token(vastApiClient, username, password):

    log = logging.getLogger("create_token")
    log.info("Requesting API token for {}".format(username))

    tokenApiClient = TokenApi(vastApiClient)

    tokens = tokenApiClient.create_tokens({ "username": username, "password": password })
    log.debug(tokens)
    return tokens

if __name__ == "__main__":
    log = logging.getLogger("vast_token")
    client = create_client()
    log.info("Test run complete")