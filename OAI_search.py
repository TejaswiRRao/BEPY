import openai
import typesense
import os

# OAI key
openai.api_key = "sk __n8n_BLANK_VALUE_e5362baf-c777-4d57-a609-6eaf1f9e87f6"  

# Typesense Connectoon
client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': 8108,
        'protocol': 'http'
    }],
    'api_key': 'xyz',
    'connection_timeout_seconds': 2
})

# user IP
user_query = input("Ask something: ")

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a search assistant. Convert the user's natural language question into a simple keyword-based query."},
        {"role": "user", "content": user_query}
    ]
)

search_keywords = response.choices[0].message.content.strip()
print(f"🔎 GPT keyword result: {search_keywords}")

# Searchability 
search_params = {
    'q': search_keywords,
    'query_by': 'text',
    'sort_by': 'timestamp:desc',
    'per_page': 5
}

results = client.collections['logs'].documents.search(search_params)

#  Results
print("\n📄 Matching Logs:")
for hit in results['hits']:
    doc = hit['document']
    print(f"- {doc['text']} (User: {doc['user']})")