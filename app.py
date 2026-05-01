from flask import Flask
import os
from dotenv import load_dotenv()
load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
  return {"message": os.getenv('VAR1')}

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
  
