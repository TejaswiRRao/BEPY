import typesense

# Typesense server connectiom
client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': 8108,
        'protocol': 'http'
    }],
    'api_key': 'xyz',
    'connection_timeout_seconds': 2
})

# Data structure
schema = {
    'name': 'logs',
    'fields': [
        { 'name': 'id', 'type': 'string' },
        { 'name': 'user', 'type': 'string' },
        { 'name': 'action', 'type': 'string' },
        { 'name': 'target', 'type': 'string' },
        { 'name': 'text', 'type': 'string' },
        { 'name': 'timestamp', 'type': 'int64' }
    ],
    'default_sorting_field': 'timestamp'
}

# collection
try:
    client.collections.create(schema)
    print(" Collection 'logs' created successfully!")
except Exception as e:
    print("  Error:", e)
