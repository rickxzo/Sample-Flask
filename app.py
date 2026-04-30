from flask import Flask

app = Flask()

@app.route('/', methods=['GET', 'POST'])
def root():
  return {"message": "Hello World"}

if __name__ == "__main__":
  app.run()
