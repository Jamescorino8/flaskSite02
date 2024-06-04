from flask import Flask, request

app = Flask(__name__)

list = []

@app.route('/')
def index():
    return '''
    <html>
      <head>
         <script src="https://unpkg.com/htmx.org@1.9.12"></script>
      </head>
      <body>
      
        <form hx-post='/form_answer' hx-target="#answer" hx-swap='innerHTML'>
          <input id="title" name="title" type="text">
          <button type="submit">Submit</button>
        </form>
        
      </body>
      </head>
    '''

@app.route('/form_answer', methods=['POST'])
def form():
  
    list.append(request.form['title'])

    return list

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
