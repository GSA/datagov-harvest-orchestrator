from flask import Flask, request
from harvester.database.interface import HarvesterDBInterface
from harvester.database import init_db
from tests.database.data import new_source, new_job, new_error

app = Flask(__name__)
db = HarvesterDBInterface()

@app.route('/', methods=['GET'])
def index():
    html = "<b>" + init_db.create_tables() + "</b>"
    html += "<ul>"
    for rule in app.url_map.iter_rules():
        if 'static' not in rule.endpoint and 'index' not in rule.endpoint:
            html += (f"<li>{rule.endpoint} : "
                     f"<a href='{rule.rule}'>{rule.rule}</a></li><br>")
    html += "</ul>"
    return html

@app.route('/add_source', methods=['GET'])
def add_harvest_source():
    source=db.add_harvest_source(new_source)
    return(f"Added new source with ID: {source.id}")

@app.route('/add_job', methods=['GET'])
def add_harvest_job():
    source_id = request.args.get('source_id', None)
    if source_id is None:
        return 'Please provide source_id'
    else:
        job=db.add_harvest_job(new_job, source_id)
        return(f"Added new job with ID: {job.id}")

@app.route('/add_error', methods=['GET'])
def add_harvest_error():
    job_id = request.args.get('job_id', None)
    if job_id is None:
        return 'Please provide job_id'
    else:
        err=db.add_harvest_error(new_error, job_id)
        return(f"Added new error with ID: {err.id}")
    
@app.route('/get_all_sources', methods=['GET'])
def get_all_harvest_sources():
    result = db.get_all_harvest_sources()
    return result

@app.route('/get_all_jobs', methods=['GET'])
def get_all_harvest_jobs():
    result = db.get_all_harvest_jobs()
    return result

@app.route('/get_all_errors', methods=['GET'])
def get_all_harvest_errors():
    result = db.get_all_harvest_errors()
    return result

@app.route('/get_source', methods=['GET'])
def get_harvest_source():
    id = request.args.get('id', None)
    if id is None:
        return 'Please provide id'
    else:
        result = db.get_harvest_source(id)
        return result
    
@app.route('/get_job', methods=['GET'])
def get_harvest_job():
    id = request.args.get('id', None)
    if id is None:
        return 'Please provide id'
    else:
        result = db.get_harvest_job(id)
        return result

@app.route('/get_error', methods=['GET'])
def get_harvest_error():
    id = request.args.get('id', None)
    if id is None:
        return 'Please provide id'
    else:
        result = db.get_harvest_error(id)
        return result

@app.route('/harvests/new')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def insert_data():
    try:
        cursor = db.cursor()
        name = request.form['name']
        notification_emails = request.form['notification_emails']
        orgnation_name = request.form['orgnation_name']
        frequency = request.form['frequency']
        url = request.form['url']
        schema_type = request.form['schema_type']
        source_type  = request.form['source_type']
        cursor.execute("INSERT INTO public.harvest_source(name,notification_emails,organization_name,frequency,url,schema_type,source_type) VALUES (%s,%s, %s,%s,%s,%s,%s)", (name,notification_emails,orgnation_name,frequency,url,schema_type,source_type))
        db.commit()
        cursor.close()
        return jsonify({'message': 'Data inserted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/harvests', methods=['GET'])
def get_record():
    try:
        cursor = db.cursor()
        record_id = request.args.get('id')
        if record_id is not None :
            query = "SELECT * FROM harvest_source WHERE id = %s"
            cursor.execute(query, (record_id,))
        else:
            cursor.execute("SELECT * FROM harvest_source")
        record = cursor.fetchall()
        cursor.close()
        if record:
            return jsonify({'record': record})
        else:
            return jsonify({'error': 'No records found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
    