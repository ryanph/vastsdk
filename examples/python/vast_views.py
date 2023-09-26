#!/usr/bin/env python3

import vast_token
import logging
from vastsdk.api import ViewsApi

log = logging.getLogger("vast_views")
settings = vast_token.read_settings()

vastApiClient = vast_token.create_client()
vastViewsApi = ViewsApi(vastApiClient)

log.info("Fetching configured Views")
views = vastViewsApi.list_views()
for view in views:
    log.debug(view)

assert not list(filter(lambda view: view.name == settings['test_view_data']['name'], views)), \
    "Test View {} must not exist on the target VMS instance".format(settings['test_view_data']['name'])

log.info("Creating a View")
new_view = vastViewsApi.create_view(settings['test_view_data'])
log.debug(new_view)

log.info("Updating a View")
updated_view = vastViewsApi.update_view_by_id(id=new_view.id, view={
    "protocols": settings['test_view_data']['patch_protocols']
})
log.debug(updated_view)

log.info("Deleting a View")
vastViewsApi.delete_view_by_id(id=new_view.id)

log.info("Test run complete")