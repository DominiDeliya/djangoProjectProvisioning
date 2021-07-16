# djangoProjectProvisioning
Goal of this project is to create a provisioning server that will supply IP phones with their
configuration.

Requirements
● Device(phone) has a model

● Device model has a vendor

● Device can be assigned to only one customer

● Device can have multiple DSS's

● Customer can have multiple extensions, but extension can have only one customer

● Extension is unique per group

● DSS can only have two types - BLF or SPD.

  ○ If BLF, value should be populated with the extension field from the Extension
  model.
  ○ User can enter a custom label(DSS) for that extension, but if they don't you
  should display name from related extension table (but do not save it to
  label in DSS model)
  ○ For SPD, value and label are mandatory
