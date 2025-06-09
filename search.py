import typesense

# Typesense connection
client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': 8108,
        'protocol': 'http'
    }],
    'api_key': 'xyz',
    'connection_timeout_seconds': 2
})

# Searching measures
search_params = {
    'q': 'uploaded',               
    'query_by': 'text',            
    'sort_by': 'timestamp:desc',   
    'per_page': 5                  
}

# search
try:
    results = client.collections['logs'].documents.search(search_params)
    print("🔍 Search results:")
    for hit in results['hits']:
        print(f"- {hit['document']['text']} (user: {hit['document']['user']})")
except Exception as e:
    print(" Error during search:", e)