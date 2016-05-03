# -*- coding: utf-8 -*-
import json
with open('twitter_results.json') as data_file:    
    data = json.load(data_file)
output = open('twitter_view.html', 'w+')

i=0
while (i<20):
	str="<b>" + data[i]['date'] + '</b>: ' + data[i]['tweet']
	output.write(str.encode('utf-8'))
	i=i+1