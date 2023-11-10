#!/usr/bin/env python3

import vast_token
import logging
import time
from vastsdk.api import ViewsApi, TasksApi

log = logging.getLogger("vast_views")
settings = vast_token.read_settings()

vastApiClient = vast_token.create_client()
vastViewsApi = ViewsApi(vastApiClient)
vastTaskApi = TasksApi(vastApiClient)

log.warning("************************************************************")
log.warning("This test does not yet run against a vanilla system.")
log.warning("Please ensure the templates and views in settings.json exist")
log.warning("************************************************************")

log.info("Fetching configured View")
view = vastViewsApi.get_view_by_id(id=127)
log.debug(view)

payload = {
    "target_path": "OSP/General",
    "template_view_id": 127,
    "template_dir_path": "General/dir_template",
    "template_file_path": "General/file_template.txt"
}
log.info("Starting bulk permission repair on View 127")
log.info(payload)
task = vastViewsApi.start_bulk_permission_repair(
    id=127, bulk_permission_repair_request=payload
)
log.info(task)

while True:
    log.info("Fetching information for task {}".format(task.async_task.id))
    task_info = vastTaskApi.get_vtask_by_id(id=task.async_task.id)
    logging.info(task_info)
    if task_info.state != 'RUNNING':
        break
    else:
        time.sleep(5)