#!/usr/bin/env python3

import vast_token
import logging
from vastsdk.api import ViewsApi
from vastsdk.api import ViewPoliciesApi
from vastsdk.models import ViewShareAclAclInner

log = logging.getLogger("vast_views")
settings = vast_token.read_settings()

vastApiClient = vast_token.create_client()
vastViewsApi = ViewsApi(vastApiClient)
vastViewPoliciesApi = ViewPoliciesApi(vastApiClient)

policy_name = 'mixed_policy'
log.info("Searching for View Policy {}".format(policy_name))
policy_objects = vastViewPoliciesApi.get_viewpolicies(name=policy_name)
log.debug(policy_objects)
assert len(policy_objects) == 1, "View Policy mixed_policy must exist for this example"

log.info("Searching for View with path /mixed")
view_object = vastViewsApi.list_views(path="/mixed")
log.debug(view_object)
assert len(view_object) == 0, "View with path /mixed should not exist for this example"

payload = {
    "path": "/mixed",
    "share": "my_mixed_view",
    "protocols": ['SMB','NFS'],
    "policy_id": int(policy_objects[0].id),
    "share_acl": {
        "enabled": True,
        "acl": [
            {
                "grantee": "users",
                "perm": "FULL",
                "is_sid": True,
                "sid_str": settings['test_user_data']['sid'],
            }
        ]
    },
    "create_dir": True
}

log.info("Creating new view my_mixed_view")
log.debug(payload)
new_view = vastViewsApi.create_view(view = payload)
log.debug(new_view)