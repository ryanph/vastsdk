#!/usr/bin/env python3

import vast_token
import logging
from vastsdk.api import ViewPoliciesApi

log = logging.getLogger("vast_viewpolicies")

settings = vast_token.read_settings()
log.debug(settings)

vastApiClient = vast_token.create_client()
vastViewPoliciesApi = ViewPoliciesApi(vastApiClient)

log.info("Fetching configured View Policies")
viewpolicies = vastViewPoliciesApi.get_viewpolicies()
for policy in viewpolicies:
    log.info(policy)

assert not list(filter(lambda viewpolicy: viewpolicy.name == settings['test_viewpolicy_data']['name'], viewpolicies)), \
    "Test View Policy {} must not exist on the target VMS instance".format(settings['test_viewpolicy_data']['name'])

log.info("Creating a new View Policy")
test_viewpolicy = vastViewPoliciesApi.create_viewpolicy({
    "name": settings["test_viewpolicy_data"]["name"],
    "flavor": settings["test_viewpolicy_data"]["flavor"],
    "auth_source": settings["test_viewpolicy_data"]["auth_source"]
})
log.debug(test_viewpolicy)

log.info("Updating View Policy {} (ID: {})".format(test_viewpolicy.name, test_viewpolicy.id))
updated_viewpolicy = vastViewPoliciesApi.update_viewpolicy_by_id(id=test_viewpolicy.id,view_policy={
    "flavor": settings['test_viewpolicy_data']['patch_flavor']
})
log.debug(updated_viewpolicy)

log.info("Deleting View Policy {} (ID: {})".format(test_viewpolicy.name, test_viewpolicy.id))
vastViewPoliciesApi.delete_viewpolicy_by_id(id=test_viewpolicy.id)

log.info("Test run complete")