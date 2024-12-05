import os
from schema_engine import SchemaEngine
from sqlalchemy import create_engine

# 1.connect to the database engine
db_name= 'aan_1'
db_path = f'./{db_name}.sqlite'
abs_path = os.path.abspath(db_path)
assert os.path.exists(abs_path)
db_engine = create_engine(f'sqlite:///{abs_path}')

# 2.Construct M-Schema
schema_engine = SchemaEngine(engine=db_engine, db_name=db_name)
mschema = schema_engine.mschema
mschema_str = mschema.to_mschema()
print(mschema_str)
mschema.save(f'./{db_name}.json')

# 3.Use for Text-to-SQL
dialect = db_engine.dialect.name
question = ''
evidence = ''
prompt = """You are now a {dialect} data analyst, and you are given a database schema as follows:

【Schema】
{db_schema}

【Question】
{question}

【Evidence】
{evidence}

Please read and understand the database schema carefully, and generate an executable SQL based on the user's question and evidence. The generated SQL is protected by ```sql and ```.
""".format(dialect=dialect, question=question, db_schema=mschema_str, evidence=evidence)

# Replace the function call_llm() with your own function or method to interact with a LLM API.
# response = call_llm(prompt)
