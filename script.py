from bs4 import BeautifulSoup
import re
import csv
import html5lib

with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html5lib')

start_tag = ""

all_p_tags = soup.find_all('p')
for tag in all_p_tags:
    if tag.get('align') == "CENTER" and "TRUSTEES AND OFFICERS" in tag.get_text():
        start_tag = tag
        break

if start_tag:
    extracted_content = []
    current_tag = start_tag

    while current_tag:
        extracted_content.append(str(current_tag))
        current_tag = current_tag.next_sibling
        if current_tag and current_tag.name == 'p' and current_tag.get('align') == 'CENTER' and current_tag.find('a', attrs={'name': re.compile(r'^ref\d+')}):
            break

    result = '\n'.join(extracted_content)

    with open('extracted_content.html', 'w', encoding='utf-8') as file:
        file.write(result)

with open("extracted_content.html") as fp:
    soup = BeautifulSoup(fp, 'html5lib')

target_heading = ""

all_p_tags = soup.find_all('p')
for tag in all_p_tags:
    if tag.get('align') == "CENTER" and "Interested Trustees" in tag.get_text():
        target_heading = tag
        break

if target_heading:
    target_table = target_heading.find_parent('table')
    if(target_table):
        with open('extracted_table1.html', 'w', encoding='utf-8') as file:
            file.write(str(target_table))

target_heading = ""

all_p_tags = soup.find_all('p')
for tag in all_p_tags:
    if tag.get('align') == "CENTER" and "Independent Trustees" in tag.get_text():
        target_heading = tag
        break

if target_heading:
    target_table = target_heading.find_parent('table')
    if(target_table):
        with open('extracted_table2.html', 'w', encoding='utf-8') as file:
            file.write(str(target_table))

def process_table(file_name):
    with open(file_name, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    rows = soup.find_all('tr')
    results = []

    i = 1
    while i < len(rows):
        trustees = [re.sub(r'<.*?>', '', td.text.strip()) for td in rows[i].find_all('td')[1:]]
        i += 1

        for _ in range(8):
            if i >= len(rows):
                break

            cells = rows[i].find_all('td')
            if len(cells) > 1:
                fund_name = re.sub(r'<.*?>', '', cells[0].text.strip())
                dollar_ranges = [re.sub(r'<.*?>', '', cell.text.strip()) for cell in cells[1:]]

                for trustee, dollar_range in zip(trustees, dollar_ranges):
                    results.append([trustee, fund_name, dollar_range])

            i += 1

    return results

results_table1 = process_table('extracted_table1.html')
results_table2 = process_table('extracted_table2.html')

combined_results = results_table1 + results_table2

with open('combined_trustee_fund_holdings.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Trustee', 'Parameter', 'Dollar Range'])
    csvwriter.writerows(combined_results)

print("Data has been written to combined_trustee_fund_holdings.csv")