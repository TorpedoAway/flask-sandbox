from flask import Flask, Response
import csv
import io

app = Flask(__name__)

@app.route('/csv')
def generate_csv():
    data = [['Name', 'Age', 'City'],
            ['Alice', '30', 'New York'],
            ['Bob', '25', 'London'],
            ['Charlie', '35', 'Paris']]
    
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerows(data)
    output = si.getvalue()

    return Response(output, mimetype='text/csv', headers={'Content-Disposition': 'attachment; filename=data.csv'})

if __name__ == '__main__':
    app.run(debug=True)
