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
- `!!LIFECYCLE-STAGE-START-DATE(YYYY-MM-DD)` - Date indicating when the service entered the declared lifecycle stage, in format 2025-12-01.
- `!!AVAILABILITY-STATEMENT`
  - SWIM-SERV-180 describes this field as:
    > The availability is typically expressed as a percentage representing the ratio between minimum target uptime versus maximum uptime. The service provider needs to describe the service outages he intends to mask/alleviate. The availability i information needs to be expressed for various situations, e.g., planned and unplanned outages. The service provider needs to describe the schedule of planned outages. Example of availability: >= 99.95 % of Continuous Operations.
  - Example from DWD which refers to a solution running as a HA cluster:
    > "The technical infrastructure is highly available and maintained an availability >= 99.8% during a month in the past. The system has intended downtimes 5 minutes once a month for security patching."
  - For hot-standby HA clusters based on Corosync/PCS/Pacemaker/DRBD a reasonable availability statement is:
    > The technical infrastructure is using a hot standby cluster with expected availability of 99.95% which should mask hardware failures, security patching of the OS, and software updates.
  - For installations that do not use any high availability mechanism, but at least regular backups or snapshots of the installation have been set up:
    > The expected availability of the system is 98% of continuous runtime per year. OS patching, kernel updates, and hardware upgrades will require scheduled downtime where the service is unavailable. In the event of hardware failure, service restoration relies on hardware replacement and system restarts.
- `!!RECOVERABILITY-STATEMENT`
  - Defined as:
    > The degree to which, in the event of an interruption or a failure, the desired state of the service can be re-established.
  - If a disaster recovery system is available, the statement could include:
    > There exists a fallback system which ensures recovery after incidents.
  - When a hot-standby HA cluster has been deployed, the statement can include:
    > On switchover of the hot-standby HA cluster the status of the database and queues is preserved.
- `!!MTLS-STATEMENT-OPTIONAL` - If authentication using EACP client certificates has been configured and works with any WAF firewalls that might have been used, the following statement can be included:
    > Users connecting to the public interfaces must present a valid EACP client certificate, which must be futher whitelisted in the service based on the details of the Distinuished Name portions of the client certificate such as Common Name, Organisation, Email.
- `!!GENERAL-TERMS-AND-CONDITIONS-URL` - General terms and conditions of business and delivery for services provided by the organisation operating the SWIM service.
  - DWD includes this link to their General Terms and Conditions: <https://www.dwd.de/EN/service/terms/terms_conditions_download.pdf>
  - More information is provided in SWIM-SERV-150 of [SWIM Service Description Specification](https://www.eurocontrol.int/publication/eurocontrol-specification-swim-service-description-sd
- `!!DATE-OF-SERVICE-OPERATION(YYYY-MM-DD)` - Date at which the service went into operation or is planned to become operational.

- `!!CUSTOMER-SUBSCRIPTION-INFORMATION` - This part should provide information about how the consumers will subscribe to the data consumption. Example: For subscribing to data the consumer needs to contact the Service Provider and needs to request the credentials. After registration, the consumer is provided the endpoints both EDR and AMQP interfaces.

- `!!EDR-WEBSERVICE-DESCRIPTION` - Example: This is the connection between the service provider and the customer via EDR. You need to contact the !!ORGANISATION-ABBREVIATION aviation customer service for getting the credentials for the interface use. 
- `"!!EDR-WEBSERVICE-URL"` - Base URL indicating, where the EDR webservice is running. Should be public DNS entry of EDR webservice.

- `!!AMQP-BROKER-URL` - Base URL indicating, where the AMQP broker is running. Should be public DNS entry of AMQP broker.

## Useful links

- [SWIM Service Description Specification on EUROCONTROL Website](https://www.eurocontrol.int/publication/eurocontrol-specification-swim-service-description-sd)
- [SWIM Service Description Specification 2.0 in PDF](https://www.eurocontrol.int/sites/default/files/2022-03/eurocontrol-swim-service-description-specification-v2-0.pdf)
- [Service Metadata Schema Repository](https://github.com/eurocontrol-swim/service-metadata-schema)

## Validator

The repository includes a Python validator script to validate service descriptions against the official JSON schema.

See [VALIDATOR.md](VALIDATOR.md) for detailed setup and usage instructions.

