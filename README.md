# VAST Management Service (VMS) SDK

Vast Management Service (VMS) SDK built with [OpenAPI-Generator](https://github.com/OpenAPITools/openapi-generator). The purpose of this library is to support the creation of the Ansible Collection [ryanph.vast](https://github.com/ryanph/ansible-vast).

While the VAST Management Service does include a Swagger specification it is inconsistent with the actual API (return codes, request bodes and data types) preventing strict typing and integration with IDEs. Given the purpose of the library is to support the Ansible module the specification is not intended to be general purpose and instead only contain the requirements for this module.

Examples for published languages are available under [/examples](/examples/).

## Versioning

The version tag used for this project and generated libraries do not align with VAST Data Platform versioning, it is specific to this project.

## Installing

Python: `pip3 install https://github.com/ryanph/vastsdk/releases/download/v1.4.0/vastsdk-python-1.4.0.tgz`

## Building

Clone the repository and install dependencies with `npm install`. Build libraries for your language:

* Python: `npm run build-python`
* PHP: `npm run build-php`

Built libraries are written to `build/`.

## Notes

VAST Data and VAST Management Service are properties of [VAST](https://vastdata.com).