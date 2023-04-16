def ExtractUserName(page):
    node = page.find('div', {'class': 'name-line'})
    # print(node.contents[0].split(" ")[1])
    username = node.contents[0].split(" ")[1]
    return username

def ExtractCheckinToken(page):
    token = page.find('input', {'name': '_token'})
    token = token.get('value')
    return token

def ExtractParttimeUsuallyId(page, projectName):
    alert = page.find('div', {'class': 'alert alert-danger text-center'})
    
    if alert == None:
        table = page.find('table', {'id': 'table1'})
        tr = table.findAll('tr')
        for r in tr:
            checkinTable = r.findAll('td')
            if checkinTable != []:
                if checkinTable[1].contents[0] == projectName:
                    ParttimeUsuallyId = int(checkinTable[5].find('a').get('href').split("=")[1])
                    # print(type(ParttimeUsuallyId))
                    # print(ParttimeUsuallyId)
                    return ParttimeUsuallyId
                else:
                    continue
                
    return "No Project Name"
                