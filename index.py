import requests
import json
import prettytable
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['LEU0252885100','LEU0252884800'],"startyear":"2016", "endyear":"2020"})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
for series in json_data['Results']['series']:
    x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
    seriesId = series['LEU0252884500']
    for item in series['Median wkly earnings']:
        year = item['2020']
        period = item['Qtr4']
        value = item['integer']
        footnotes=""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','

        if 'M01' <= period <= 'M12':
            x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    output = open(&quot;c:\\temp\\&quot; + seriesId + &quot;.txt&quot;,&quot;w&quot;)
    output.write (x.get_string())
    output.close()
