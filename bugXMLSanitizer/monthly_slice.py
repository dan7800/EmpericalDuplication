import xml.etree.ElementTree as ET
from datetime import datetime
import glob


def get_xml_file(file_path):
    with open(file_path, 'r') as file:
        print('file =', file_path)
        tree = ET.parse(file_path)
        root = tree.getroot()
        return file.name, root


def separate_into_month(file_name, xml_file):

    xml_dictionary = {}
    for bug in xml_file.findall('bug'):
        # date format = 2018-05-14 05:11:21 +0000
        creation_ts = bug.find('creation_ts').text
        datetime_obj = datetime.strptime(creation_ts, '%Y-%m-%d %H:%M:%S %z')

        # filename would be like = new_dataset/mozilla_reports/2011_1.xml
        month_file_name = '{}_{}_{}.xml'.format(file_name, datetime_obj.year, datetime_obj.month)
        if month_file_name in xml_dictionary:
            bugs = xml_dictionary[month_file_name]
            bugs.append(bug)
            xml_dictionary[month_file_name] = bugs
        else:
            bugs = ET.Element('bugs')
            bugs.append(bug)
            xml_dictionary[month_file_name] = bugs

    for file_name in xml_dictionary:
        xml_element = xml_dictionary[file_name]
        tree = ET.ElementTree(element=xml_element)
        tree.write(open(file_name, 'wb'))

    print(xml_dictionary)


def monthly_slice_directory(dir_path):
    files = glob.glob(dir_path)
    for file_path in files:
        print('reading ', file_path)
        file_name, xml_file = get_xml_file(file_path)
        separate_into_month(file_name, xml_file)



