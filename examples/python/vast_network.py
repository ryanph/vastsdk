#!/usr/bin/env python3

import vast_token
import logging
import time
from vastsdk.exceptions import NotFoundException
from vastsdk.api import NetworkApi

log = logging.getLogger("vast_network")
logging.basicConfig(level=logging.DEBUG)

settings = vast_token.read_settings()
vastApiClient = vast_token.create_client()

vastNetworkApi = NetworkApi(vastApiClient)

logging.info("Listing VIP Pools")
pools = vastNetworkApi.list_vippools()
logging.info(pools)

logging.info("Listing VIP Pools with the PROTOCOLS role")
pools = vastNetworkApi.list_vippools(role="PROTOCOLS")
logging.info(pools)