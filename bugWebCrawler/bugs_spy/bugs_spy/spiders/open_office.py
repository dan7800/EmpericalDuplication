# -*- coding: utf-8 -*-
import scrapy
import re
import xml.etree.ElementTree as ET


class OpenOfficeSpider(scrapy.Spider):
    name = 'openoffice'
    year = 2010

    reports_file_name = 'openoffice_reports_2010.xml'
    log_file_name = 'saved_openoffice_log_2010.txt'
    SETTINGS_SEARCH = 'OPEN_OFFICE_SEARCH_URL'
    SETTINGS_DETAIL_URL = 'OPEN_OFFICE_DETAIL_URL'

    def start_requests(self):
        base_search_url = self.settings.get(self.SETTINGS_SEARCH)
        with open(self.reports_file_name, 'w') as file:
            file.write('')
        with open(self.log_file_name, 'w') as file:
            file.write('')

        # 1. Separate URLS in month range
        # PRODUCTION
        bug_result_urls = self.get_monthly_search_urls(base_search_url)

        # DEVELOPMENT
        # test_url = {'2018-07-30': base_search_url.format('2018-07-30', '2018-07-30')}
        # bug_result_urls = test_url  # TODO: remove this for production

        # 2. Add formatted URLS to urls var array
        for key in bug_result_urls.keys():
            url = bug_result_urls[key]
            self.log_saved_bugs('SEARCH: {} \n'.format(url))
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('queseto = ', response.css('td.bz_id_column a::text').get())

        for item in response.css('td.bz_id_column'):
            bug_id = item.css('td.bz_id_column a::text').get()
            bug_url = self.settings.get(self.SETTINGS_DETAIL_URL).format(bug_id)

            self.log_saved_bugs('Bug:{} \nurl:{}\n'.format(bug_id, bug_url))
            yield scrapy.Request(url=bug_url, callback=self.parse_bug)

    def parse_bug(self, response):
        bug_id = response.xpath('bug/bug_id/text()').get()
        creation_ts = response.xpath('bug/creation_ts/text()').get()
        # save directly into file
        with open(self.reports_file_name, 'a') as file:
            bug_report_xml = response.xpath('bug').get()
            cleaned_bug_report_xml = self.clean_bug_report(bug_report_xml)
            file.writelines(cleaned_bug_report_xml)

        # yield objects to save during terminal execution command 'scrapy crawl bugzilla -o filename.json'
        yield {'id': bug_id, 'date': creation_ts}

    def get_monthly_search_urls(self, base_url):
        # Iterate through months from 1 to 12 and add those to the date ranges, e.g. 2018-01-01-2018-01-30
        monthly_urls = {}
        for m in range(1, 13):
            start_month = "%s-%s-%s" % (self.year, m, 1)
            end_month = "%s-%s-%s" % (self.year, m, 31)
            key = start_month + "-" + end_month

            link = base_url.format(start_month, end_month)
            monthly_urls[key] = link

        return monthly_urls

    def log_saved_bugs(self, message):
        with open(self.log_file_name, 'a') as file:
            file.write(message)

    def clean_bug_report(self, str_xml):
        root_xml = ET.fromstring(str_xml.encode('utf-8'))
        exclude_nodes = self.get_exclude_nodes()
        for node_name in exclude_nodes:
            node_to_exclude = root_xml.findall(node_name)
            if node_to_exclude is None:
                print("{} - element not found".format(node_name))
            else:
                for sub_node in node_to_exclude:
                    root_xml.remove(sub_node)

        # result = ET.tostring(root_xml, encoding='unicode') + '\n'
        result = ET.tostring(root_xml) + '\n'
        result = re.sub(r'\n\s*\n*', '\n', result)
        return result

    def get_exclude_nodes(self):
        with open(self.settings.get('EXCLUDE_NODES_KEYWORDS'), 'r') as file:
            return file.read().splitlines()
