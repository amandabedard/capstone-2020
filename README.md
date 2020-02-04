# capstone-2020
Chat vulnerabilities capstone project

**Python 3.6**

**Packages**: flask, nltk, rivescript

To run:
- Make sure the dependencies listed above are installed
- In the capstone-2020 repo, run the following: **python .\vuln-bot\chatApi.py**
- Should see it running on http://127.0.0.1:5000/ 

Sample request:
-----
**POST** on http://127.0.0.1:5000/chat

**Body (JSON):**
```javascript
{
	"utterance": "hi"
}
```
**Response:**
```javascript
{
    "metadata": "{'end': False, 'auth': False, 'user': None, 'text': 'hey', 'lastRes': None, 'lastUtt': None, 'utterance': 'hi'}",
    "response": "hey",
    "status": 200
}
```