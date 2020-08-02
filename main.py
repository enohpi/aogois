# Running report generation in 'Redmine'

import red_api
import template_doc
import csv_parser

if __name__ == '__main__':
    url = 'http://red.eltex.loc'
    #url = 'http://172.29.32.1'
    #csv_parser.url_issue = url + '/issues/'
    red_api_key = ""
    # date = red_api.mouth_report  # Example, 2020-06-30 (today - 1 mouth)
    date = '2020-06-28'

    red_api.put_api(url, red_api_key, gen_csv=True, start_date=date)
    template_doc.create_report(url, red_api_key)
