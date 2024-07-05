from flask import Flask, render_template, request, send_file
import pdfkit
import os
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def show():
    return render_template('table.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
     # Retrieve textarea values from the form
    table1_content = request.form['textarea1']
    table2_content = request.form['textarea2']
    
    # Render the HTML template with the data
    rendered_html = render_template('table.html', table1= table1_content, table2 = table2_content)

    # Specify the path to wkhtmltopdf if needed
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    # Generate PDF from the rendered HTML
    pdf_file = pdfkit.from_string(rendered_html, False, configuration=config)

    # Create a response with the PDF file
    return send_file(io.BytesIO(pdf_file), download_name='table.pdf', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
