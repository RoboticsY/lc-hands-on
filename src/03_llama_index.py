from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('./llama_data').load_data()
index = GPTVectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
print(query_engine.query("Vision Pro はARデバイスですか？"))

# インデックスの保存
index.storage_context.persist()