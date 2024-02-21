Setup
Clone the repository:
bash
Copy code
git clone <repository_url>
cd <repository_name>
Install dependencies:
bash
Copy code
pip install python-dotenv fastapi uvicorn supabase-python
Set up environment variables:
Create a .env file in the root directory with the following variables:

plaintext
Copy code
SUPABASE_URL=<your_supabase_url>
SUPABASE_KEY=<your_supabase_key>
Replace <your_supabase_url> and <your_supabase_key> with your Supabase URL and key respectively.

Run the API:
bash
Copy code
uvicorn main:app --reload
The API will be running at http://localhost:8000.

Endpoints
Get all legend data
bash
Copy code
GET /getLegendData
Retrieve all data about legendary characters.

Get legend by alias
bash
Copy code
GET /getLegend/{alias}
Retrieve data about a legendary character by their alias.

Get legends by class
vbnet
Copy code
GET /getClass/{class}
Retrieve data about legendary characters by their class.

Add a new legend
bash
Copy code
POST /addLegend
Add data about a new legendary character.

Request Body
json
Copy code
{
  "alias": "string",
  "quote": "string",
  "wiki": "string",
  "realname": "string",
  "age": 0,
  "homeworld": "string",
  "class_": "string",
  "classpassive": "string",
  "tactical": "string",
  "tacticalwiki": "string",
  "passive": "string",
  "passivewiki": "string",
  "ultimate": "string",
  "ultimatewiki": "string"
}
Replace "string" and 0 with the respective values for the new legendary character.
