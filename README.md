# GerritSpiderForExcel
spider gerrit information to excel

how to use 
1.line 19:set your server ip
MERGED_URL = 'http://xxx.xxx.xxx.xxx:8080/changes/?q=status:merged&n=25&O=81'

2.line 125:set your branch&repository_name
FilterData.filder_project('test.xls','xxx','master')

3.line 49-52：use your own headers

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Cookie': 'GERRIT_UI=GWT; GerritAccount=aSseprswLuBU0N6Zr8Qo6K.rLgUxknKwCq; XSRF_TOKEN=aSseprsTSA4MCp0r1Gz3BJQQGtJqnZ9wUa'
}


Download source code and run the main script
  python spider_excel.py
  
