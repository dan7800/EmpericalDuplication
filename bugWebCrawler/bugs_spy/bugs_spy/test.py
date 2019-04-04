import xml.etree.ElementTree as ET

# Reading a file of strings
proxy_list = []

with open('/Users/virginiapujols/PycharmProjects/bug_web_crawler/bugs_spy/test_xml.txt') as file:
    str_xml = file.read()
    root_xml = ET.fromstring(str_xml)
    exclude_nodes = MyConstants.EXCLUDE_NODES_KEYWORDS
    for node_name in exclude_nodes:
        node_to_exclude = root_xml.findall(node_name)
        if node_to_exclude is None:
            print("element not found")
        else:
            for sub_node in node_to_exclude:
                root_xml.remove(sub_node)

    result = ET.tostring(root_xml, encoding='unicode')
    print('finish')
