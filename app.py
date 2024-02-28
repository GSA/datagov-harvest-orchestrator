
from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Configure PostgreSQL connection
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

@app.route('/harvests/new')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def insert_data():
    try:
        cursor = conn.cursor()
        name = request.form['name']
        notification_emails = request.form['notification_emails']
        orgnation_name = request.form['orgnation_name']
        frequency = request.form['frequency']
        url = request.form['url']
        schema_type = request.form['schema_type']
        source_type  = request.form['source_type']
        print(name,notification_emails,orgnation_name,frequency,url,schema_type,source_type)
        #cursor.execute("INSERT INTO public.harvest_source(name,notification_emails,organization_name,frequency,schema_type,source_type) VALUES (%s,%s,%s,%s,%s,%s)", (name,notification_emails,orgnation_name,frequency,schema_type,source_type))
        cursor.execute("INSERT INTO public.harvest_source(name,notification_emails,organization_name,frequency,url,schema_type,source_type) VALUES (%s,%s, %s,%s,%s,%s,%s)", (name,notification_emails,orgnation_name,frequency,url,schema_type,source_type))
        conn.commit()
        cursor.close()
        return jsonify({'message': 'Data inserted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/harvests', methods=['GET'])
def get_record():
    try:
        print("test12233")
        cursor = conn.cursor()
        record_id = request.args.get('id')
        print("record_id",record_id)
        #param_value = request.args.get('param')
        if record_id is not None :
            query = "SELECT * FROM harvest_source WHERE id = %s"
            cursor.execute(query, (record_id,))
        else:
            cursor.execute("SELECT * FROM harvest_source")
        record = cursor.fetchall()
        print("test",record)
        cursor.close()
        if record:
            return jsonify({'record': record})
        else:
            return jsonify({'error': 'No records found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)