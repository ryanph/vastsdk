#!/usr/bin/env python3

import vast_token
import logging
from vastsdk.api import UsersApi

log = logging.getLogger("vast_users")
logging.basicConfig(level=logging.DEBUG)

settings = vast_token.read_settings()
vastApiClient = vast_token.create_client()
vastUsersApi = UsersApi(vastApiClient)

log.info("Fetching available Users")
users = vastUsersApi.list_users()
if users.count:
    for user in users:
        log.info(user)
else:
    log.error("No users configured")

assert not list(filter(lambda user: user.name == settings['test_user_data']['name'], users)), \
    "Test user account {} must not exist on the target VMS instance".format(settings['test_user_data']['name'])

log.info("Creating test user {} with UID {}".format(settings['test_user_data']['name'], settings['test_user_data']['uid']))
new_user = vastUsersApi.create_user({
    "name": settings['test_user_data']['name'],
    "uid": settings['test_user_data']['uid']
})
log.debug(new_user)

log.info("Looking up test user by name ({})".format(settings['test_user_data']['name']))
search_results = vastUsersApi.list_users(name=settings['test_user_data']['name'])
log.debug(search_results)
assert search_results[0].name == settings['test_user_data']['name'], \
    "Test user account {} should be returned from search"
test_user = search_results[0]

log.info("Creating an S3 Access Key for user {}".format(settings['test_user_data']['name']))
access_key = vastUsersApi.create_user_access_key_by_id(id=test_user.id)
log.debug(access_key)

log.info("Deleting S3 Access Key {} for user {} (ID: {})".format(
    access_key.access_key, settings['test_user_data']['name'], test_user.id)
)
vastUsersApi.delete_user_access_key_by_id(
    id=test_user.id,
    delete_user_access_key_by_id_request={
        "access_key": access_key.access_key
    }
)

log.info("Updating test user {} (ID: {})".format(settings['test_user_data']['name'], str(test_user.id)))
updated_user = vastUsersApi.update_user_by_id(id=test_user.id,user={"uid":settings['test_user_data']['patch_uid']})
log.debug(updated_user)

log.info("Deleting test user {} (ID: {})".format(settings['test_user_data']['name'], str(test_user.id)))
vastUsersApi.delete_user_by_id(id=test_user.id)

log.info("Test run complete")