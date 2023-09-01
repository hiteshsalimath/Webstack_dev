import xmlschema

xml_file = "D:\WEB STACK DEV\Lab_Ex_4_XML\employees.xml"
xsd_file = "D:\WEB STACK DEV\Lab_Ex_4_XML\employe_schema.xsd"

validator = xmlschema.XMLSchema(xsd_file)
if validator.is_valid(xml_file):
    print("XML file is valid against the XSD schema.")
else:
    print("XML file is not valid against the XSD schema.")
    print(validator.validate(xml_file))