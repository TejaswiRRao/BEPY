import typesense
import uuid
import time

#Typesense connection
client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': 8108,
        'protocol': 'http'
    }],
    'api_key': 'xyz',
    'connection_timeout_seconds': 2
})

# Sample data
log = {
    "user": "tejaswi",
    "action": "upload",
    "target": "report.pdf"
}

#wGenerate human_readable text
human_text = f"{log['user'].capitalize()} {log['action']}ed {log['target']}"

# document construction
document = {
    "id": str(uuid.uuid4()), 
    "user": log["user"],
    "action": log["action"],
    "target": log["target"],
    "text": human_text,
    "timestamp": int(time.time())
}

# Indexing
try:
    response = client.collections['logs'].documents.create(document)
    print(" Log indexed:", response)
except Exception as e:
    print(" Error indexing log:", e)