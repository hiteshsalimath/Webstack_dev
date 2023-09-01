from lxml import etree

# Load XML
xml_tree = etree.parse("D:\WEB STACK DEV\Lab_05_Xml-html\employee_data.xml")

# Load XSL
xsl_transform = etree.XSLT(etree.parse("D:\WEB STACK DEV\Lab_05_Xml-html\employee_transform.xsl"))

# Apply XSLT transformation
html_tree = xsl_transform(xml_tree)

# Validate against XSD
xmlschema = etree.XMLSchema(etree.parse("D:\WEB STACK DEV\Lab_05_Xml-html\employee_schema.xsd"))
if xmlschema.validate(xml_tree):
    print("XML is valid against XSD.")
else:
    print("XML is not valid against XSD.")
    exit(1)

# Write transformed HTML to a file
with open("output.html", "w", encoding="utf-8") as output_file:
    output_file.write(etree.tostring(html_tree, pretty_print=True).decode("utf-8"))