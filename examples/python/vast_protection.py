#!/usr/bin/env python3

import vast_token
import logging
import time
from vastsdk.exceptions import NotFoundException
from vastsdk.api import ProtectionApi

log = logging.getLogger("vast_protection")
logging.basicConfig(level=logging.DEBUG)

settings = vast_token.read_settings()
vastApiClient = vast_token.create_client()

vastProtectionApi = ProtectionApi(vastApiClient)

logging.info("Listing Protection Policies")
policies = vastProtectionApi.list_protectionpolicies()
logging.info(policies)

logging.info("Creating a Protection Policy")
policy = vastProtectionApi.create_protectionpolicy(settings['test_protectionpolicy_data'])
logging.info(policy)

logging.info("Searching for a Protection Policy (by Name)")
search = vastProtectionApi.list_protectionpolicies(name=settings['test_protectionpolicy_data']['name'])
logging.info(search)

logging.info("Updating a Protection Policy")
policy = vastProtectionApi.update_protectionpolicy_by_id(id=policy.id, protection_policy={"name": "renamed_test_policy"})
logging.info(policy)

logging.info("Fetching a specific Protection Policy (by ID)")
policy = vastProtectionApi.get_protectionpolicy_by_id(id=policy.id)
logging.info(policy)

logging.info("Listing Protected Paths")
paths = vastProtectionApi.list_protectedpaths()
logging.info(paths)

logging.info("Creating a Protected Path")
settings['test_protectedpath_data']['protection_policy_id'] = policy.id
logging.info(settings['test_protectedpath_data'])
path = vastProtectionApi.create_protectedpath(settings['test_protectedpath_data'])
logging.info(path)

logging.info("Searching for a Protected Path (by Path)")
path = vastProtectionApi.list_protectedpaths(source_dir=path.source_dir)[0]
logging.info(path)

logging.info("Fetching a specific Protected Path (by ID)")
path = vastProtectionApi.get_protectedpath_by_id(id=path.id)
logging.info(path)

logging.info("Delete a Protected path")
r = vastProtectionApi.delete_protectedpath_by_id(id=path.id)
logging.info(r)

logging.info("Wait for the Protected Path to be deleted")
while True:
    try:
        path = vastProtectionApi.get_protectedpath_by_id(id=path.id)
        log.info("Path still exists: {}. Waiting 20 seconds before checking again.".format(path.protected_path_state))
        time.sleep(20)
    except NotFoundException:
        logging.info("Path has been deleted")
        break

logging.info("Delete a Protection Policy")
r = vastProtectionApi.delete_protectionpolicy_by_id(id=policy.id)
logging.info(r)