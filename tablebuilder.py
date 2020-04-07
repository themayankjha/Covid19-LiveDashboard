import requests
from flask_table import Table, Col

class ItemTable(Table):
    statename = Col('State Name')
    confirm = Col('Confirmed Cases')
    totaldeath= Col('Total Deaths')
    totalrecovered=Col('Total recovered')
class Item(object):
    def __init__(self, statename, confirm, totaldeath, totalrecovered ):
        self.statename = statename
        self.confirm = confirm
        self.totaldeath=totaldeath
        self.totalrecovered=totalrecovered
def tablebuilder():
    items=[]
    data = requests.get("https://api.rootnet.in/covid19-in/stats/latest")
    data = data.json()
    regional=data['data']['regional']
    for state in regional:
        name=state['loc']
        confirmedCasesIndian=state['confirmedCasesIndian']
        confirmedCasesForeign=state['confirmedCasesForeign']
        totalconfirmcases=confirmedCasesForeign+confirmedCasesIndian
        deaths=state['deaths']
        discharged=state['discharged']
        statedat=Item(name,totalconfirmcases,deaths,discharged)
        items.append(statedat)
    table = ItemTable(items)
    return table