# pip install lxml
from lxml import etree

def validate_xml(employees, employe_schema):
    try:
        # Load the XML document and XML schema
        xml_tree = etree.parse(employees)
        xsd_tree = etree.parse(employe_schema)
        
        # Create an XML schema object
        xmlschema = etree.XMLSchema(xsd_tree)
        
        # Validate the XML document against the schema
        is_valid = xmlschema.validate(xml_tree)
        
        if is_valid:
            print("The XML document is valid.")
        else:
            print("The XML document is not valid.")
            print("Validation errors:")
            for error in xmlschema.error_log:
                print(f"Line {error.line}, Column {error.column}: {error.message}")
    except etree.XMLSyntaxError as e:
        print("XML Syntax Error:", e)

if __name__ == "__main__":
    employees = "employees.xml"
    employe_schema = "employee_schema.xsd"
    validate_xml(employees, employe_schema)
