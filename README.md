# swim-service-descriptions
Templates for SWIM service descriptions

These templates are meant to be used by the service providers as the stepping point, from which they may prepare their own Service Descriptions on the SWIM Registry.

The descriptions are based on the IBL's SWIM Weather Software product and the technical information should be valid for the currently released version of the software.

The information which should be modified by the providers is marked by the service providers.
You can search for placeholders by searching for "!!". This is then followed by short explanation of the expected content.

Disclaimer: Before publishing the service definition, please make sure to search the document for all "!!" and make sure that no placeholder is left in the document.

## Formatting of text fields

It is not clear what syntax should be used in the text fields, but some of them support basic HTML tags such as:
- `<p>`, `<a href="URL">link-text</a>`, `<ul>`, `<ol>`, `<li>`.

This could however be just a coincidence, because many existing service descriptions are using only plain text

## Placeholders (!!)

The placeholders that start with "!!" should be filled in by the organisation that is going to provide the SWIM service.

Examples:

- `!!ORGANISATION-ABBREVIATION` - Abbreviation of the meteorological organisation providing the SWIM service.
- `!!FULL-ORGANISATION_NAME` - Full name of the organisation providing the SWIM service (e.g. "Slovak Hydrometeorological Service)
- `!!COUNTRY` - The organisation is expected to put here country or contries for which the meteorological data is issued.
- `!!ICAO-COUNTRY-CODE` - 2-letter ICAO country code (ED - Germany, LZ - Slovakia).
- `!!PROVIDER-DESCRIPTION-HTML` - This can be a longer HTML formatted rich text describing the general duties of the organisation that is providing the service. DWD provides a longer description that can be seen on https://eur-registry.swim.aero/services/dwd-taf-iwxxm-10
- `!!LIFECYCLE-STAGE(OPERATIONAL|PROSPECTIVE|RETIRED)` - Service lifecycle stage. One of `OPERATIONAL`, `PROSPECTIVE`, or `RETIRED`. The values are documented on page https://reference.swim.aero/information-services/service-categories/CodeLifeCycleStageType.html
- `!!LIFECYCLE_STAGE_START_DATE(YYYY-MM-DD)` - Date indicating when the service entered the declared lifecycle stage, in format 2025-12-01.

- `!!EDR_WEBSERVICE_DESCRIPTION` - Example : This is the connection between the service provider and the customer via EDR. You need to contact the !!ORGANIZATION-ABBREVIATION aviation customer service for getting the credentials to retreive the specific layer which is described in this sevice description. 
- `"!!EDR_WEBSERVICE_URL"` - Base URL indicating, where the EDR webservice is running

## Useful links

- [SWIM Service Description Specification on EUROCONTROL Website](https://www.eurocontrol.int/publication/eurocontrol-specification-swim-service-description-sd)
- [SWIM Service Description Specification 2.0 in PDF](https://www.eurocontrol.int/sites/default/files/2022-03/eurocontrol-swim-service-description-specification-v2-0.pdf)
- [Service Metadata Schema Repository](https://github.com/eurocontrol-swim/service-metadata-schema)

## Validator

The repository includes a Python validator script to validate service descriptions against the official JSON schema.

See [VALIDATOR.md](VALIDATOR.md) for detailed setup and usage instructions.

