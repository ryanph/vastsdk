#!/usr/bin/env python3

import vast_token
import logging
from vastsdk.api import QuotasApi

log = logging.getLogger("vast_quotas")
logging.basicConfig(level=logging.DEBUG)

settings = vast_token.read_settings()
vastApiClient = vast_token.create_client()
vastQuotasApi = QuotasApi(vastApiClient)

logging.info("Fetching all quotas")
quotas = vastQuotasApi.list_quotas()
logging.info(quotas)

logging.info("Creating a new quota")
new_quota = vastQuotasApi.create_quota(settings['test_quota_data'])
logging.info(new_quota)

logging.info("Fetching a specific quota")
specific_quota = vastQuotasApi.get_quota_by_id(id=new_quota.id)
logging.info(specific_quota)

logging.info("Search for a specific quota by name")
specific_quota = vastQuotasApi.list_quotas(name=settings['test_quota_data']['name'])
logging.info(specific_quota)

logging.info("Search for a specific quota by path")
specific_quota = vastQuotasApi.list_quotas(path=settings['test_quota_data']['path'])
logging.info(specific_quota)

logging.info("Updating Quota")
updated_quota = vastQuotasApi.update_quota_by_id(id=new_quota.id, quota={"hard_limit": settings['test_quota_data']['hard_limit'] * 2})
logging.info(updated_quota)

logging.info("Deleting Quota")
vastQuotasApi.delete_quota_by_id(id=new_quota.id)