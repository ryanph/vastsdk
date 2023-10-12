#!/usr/bin/env python3

import vast_token
import logging
from vastsdk.api import UsersApi, GroupsApi

log = logging.getLogger("vast_users")
logging.basicConfig(level=logging.DEBUG)

settings = vast_token.read_settings()
vastApiClient = vast_token.create_client()
vastUsersApi = UsersApi(vastApiClient)
vastGroupsApi = GroupsApi(vastApiClient)

log.info("Querying for user {}".format(settings['test_query_data']['username']))
res = vastUsersApi.query_user(username=settings['test_query_data']['username'])
log.info(res)

log.info("Querying for group {}".format(settings['test_query_data']['groupname']))
res = vastGroupsApi.query_group(groupname=settings['test_query_data']['groupname'])
log.info(res)