# M-Schema: a semi-structure representation of database schema
## Introduction
MSchema is a semi-structured schema representation of database structure, which could be used in various scenarios such as Text-to-SQL.
This repository contains the code for connecting to the database and constructing M-Schema.
We support a variety of relational databases, such as MySQL, PostgreSQL, Oracle, etc.

<p align="center">
  <img src="https://github.com/XGenerationLab/M-Schema/blob/main/schema_representation.png" alt="image" width="800"/>
</p>

## Requirements
+ python >= 3.9

You can install the required packages with the following command:
```shell
pip install -r requirements.txt
```

## Quick Start
You can just connect to the database using [```sqlalchemy```](https://www.sqlalchemy.org/) and construct M-Schema representation.

1. Create a database connection.

Take PostgreSQL as an example:
```python
from sqlalchemy import create_engine
db_engine = create_engine(f"postgresql+psycopg2://{db_user_name}:{db_pwd}@{db_host}:{port}/{db_name}")
```

Connect to MySQL:
```python
db_engine = create_engine(f"mysql+pymysql://{db_user_name}:{db_pwd}@{db_host}:{port}/{db_name}")
```

Connect to SQLite:
```python
import os
db_path = ""
abs_path = os.path.abspath(db_path)
db_engine = create_engine(f'sqlite:///{abs_path}')
```

2. Construct M-Schema representation.
```python
from schema_engine import SchemaEngine

schema_engine = SchemaEngine(engine=db_engine, db_name=db_name)
mschema = schema_engine.mschema
mschema_str = mschema.to_mschema()
print(mschema_str)
mschema.save(f'./{db_name}.json')
```

3. Use for Text-to-SQL.
```python
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
```


## Citation
If you find our work helpful, feel free to give us a cite.
```bibtex
@article{xiyansql,
      title={A Preview of XiYan-SQL: A Multi-Generator Ensemble Framework for Text-to-SQL}, 
      author={Yingqi Gao and Yifu Liu and Xiaoxia Li and Xiaorong Shi and Yin Zhu and Yiming Wang and Shiqi Li and Wei Li and Yuntao Hong and Zhiling Luo and Jinyang Gao and Liyu Mou and Yu Li},
      year={2024},
      journal={arXiv preprint arXiv:2411.08599},
      url={https://arxiv.org/abs/2411.08599},
      primaryClass={cs.AI}
}
```
