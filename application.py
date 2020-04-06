from flask import Flask, render_template, redirect, url_for
from flask_table import Table, Col
import apiresolver
import tablebuilder
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    summary=apiresolver.getsummary()
    total=summary['total']
    confirmedCasesIndian=summary['confirmedCasesIndian']
    confirmedCasesForeign=summary['confirmedCasesForeign']
    discharged=summary['discharged']
    statelist=apiresolver.statelist()
    deaths=summary['deaths']
    confirmcases=apiresolver.confirmcases()
    deathcases=apiresolver.deathcases()
    dischargedcases=apiresolver.dischargedcases()
    table=tablebuilder.tablebuilder()
    return render_template('dashboard.html', total=total,discharged=discharged,deaths=deaths,confirmedCasesIndian=confirmedCasesIndian,confirmedCasesForeign=confirmedCasesForeign,statelist=statelist,confirmcases=confirmcases,deathcases=deathcases,dischargedcases=dischargedcases,table=table)

if __name__ == '__main__':
    app.run()
