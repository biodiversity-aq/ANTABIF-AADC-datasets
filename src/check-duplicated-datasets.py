import csv
import os
import requests
import xml.etree.ElementTree as ET


def get_item_from_ipt_rss(rss_url):
    # Send a GET request to the RSS feed
    response = requests.get(rss_url)

    # Check if the request was successful
    if response.status_code == 200:
        item_set = set()
        # Parse the XML content of the response
        root = ET.fromstring(response.content)

        for item in root.iter('item'):
            # Extract titles and remove everything from " - Version" onwards
            title = item.find('title').text.split(" - Version")[0]
            item_set.add(title)
    else:
        print(f"Failed to retrieve RSS feed. Status code: {response.status_code}")
    return item_set


def get_datasets_from_gbif_installation(installation_key):
    # variables
    titles = set()
    offset = 0
    limit = 300
    end_of_records = False
    api_url = 'https://api.gbif.org/v1/installation/{}/dataset'.format(installation_key)

    while not end_of_records:
        response = requests.get(api_url, params={'limit': limit, 'offset': offset})
        if response.status_code == 200:
            data = response.json()
            for dataset in data['results']:
                titles.add(dataset['title'])
            offset += limit
            end_of_records = data['endOfRecords']
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            break

    return titles


# URL of the RSS feed
aadc_rss_url = 'https://data.aad.gov.au/ipt/rss.do'
antabif_rss_url = 'https://ipt.biodiversity.aq/rss.do'


# Get sets of datasets from each installation
aadc_ipt_datasets = get_item_from_ipt_rss('https://data.aad.gov.au/ipt/rss.do')
antabif_ipt_datasets = get_item_from_ipt_rss('https://ipt.biodiversity.aq/rss.do')
aadc_digir_datasets = get_datasets_from_gbif_installation('5ffda196-f762-11e1-a439-00145eb45e9a')


# check for duplicates on our IPT
# duplicates are same item from the 2 sets based on dataset title
ipt_duplicates = aadc_ipt_datasets & antabif_ipt_datasets
digir_duplicates = aadc_digir_datasets & antabif_ipt_datasets


# print duplicates to console, so far there is no duplicates based on dataset title
print(ipt_duplicates)
print(digir_duplicates)


# extend all the lists into 1, specifying their installations
dataset_list = [[i, 'AADC DiGIR'] for i in aadc_digir_datasets]
dataset_list.extend([[i, 'AADC IPT'] for i in aadc_ipt_datasets])
dataset_list.extend([[i, 'ANTABIF IPT'] for i in antabif_ipt_datasets])


# sort the list based on installation first, then dataset title
sorted_dataset = sorted(dataset_list, key=lambda x: (x[1], x[0]))


# write to file
file_path = os.path.join('..', 'data', 'datasets_from_installations.txt')
with open(file_path, 'w', newline='\n') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(['dataset', 'installation'])
    writer.writerows(sorted_dataset)







