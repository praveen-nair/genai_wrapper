Simple GenAI wrapper
====================

A simple GenAI wrapper that leverages SAP's AI Core to seamlessly translate requests into LLM calls.

# How to install?
**Tip**: It's always best to create an environment and install the package there.

Install the wrapper library, execute the below command:
```bash
pip install genai_wrapper
```
# How to use?
## Prepare you connection:
Create a config file `config.json` with content as shown below:
```json
{
    "ai_core": {
        "secret": {
            "clientid": "<Enter value from the generated secret key>",
            "clientsecret": "<Enter value from the generated secret key>",
            "url": "<Enter value from the generated secret key>",
            "identityzone": "",
            "identityzoneid": "",
            "appname": "",
            "serviceurls": {
                "AI_API_URL": "<Enter value from the generated secret key>"
            }
        },
        "resource_group": "<Enter your ai-core resource group where you have deployed the models>"
    },
    "gen_ai": {
        "<Give a name to identify the model>": {
            "deploymentid": "<Enter the deployment Id>",
            "model_name": "<Enter the model name as per SAP's llm model name definition>",
            "parameters": {
                "max_tokens": 100,
                "temperature": 0.1,
                "frequency_penalty": 0.0,
                "presence_penalty": 0.0
            }
        },
        "model_gpt-4o": {
            "deploymentid": "d123456789012345",
            "model_name": "gpt-4o",
            "parameters": {
                "max_tokens": 500,
                "temperature": 1.0,
                "frequency_penalty": 0.0,
                "presence_penalty": 0.0
            }
        },
        "text-embedding": {
            "deploymentid": "d123456789054321"
        }
    },
    "hana_vec_store": {
        "host": "<Enter your HANA machine host>",
        "port": 443,
        "userid": "<Enter your user id>",
        "password": "<Enter your password>",
        "ssl_cert_validation": false
    }
}
```
**Tip**: To avoid errors, copy the JSON `secret-key` content generated for AI Core from your SAP BTP sub-account and paste it into `ai_core` > `secret`. Ensure no details within the key are modified.

## Perform a simple chat:
```py
from genai_wrapper.wrapper  import GenAIWrapper, ChatObject

# Make sure to pass the path of your config file if the config.json is not in the same directory.
gen_ai = GenAIWrapper(
    config_file="config.json"
)

chat = ChatObject()
chat.add_message("Who are you?")

gen_ai.chat("model_gpt-4o", chat)

print(chat.get_answer())
```

## Perform a simple embedding call:
```py
from genai_wrapper.wrapper  import GenAIWrapper

# Make sure to pass the path of your config file if the config.json is not in the same directory.
gen_ai = GenAIWrapper(
    config_file="config.json"
)

embed = gen_ai.embedding("text-embedding", "Hello World!")

print( embed )
```

## Perform similarity search in HANA Db:
```py
from genai_wrapper.wrapper  import GenAIWrapper

# Make sure to pass the path of your config file if the config.json is not in the same directory.
gen_ai = GenAIWrapper(
    config_file="config.json"
)

hana_vec_object = HANAVectorObject(
    table="TABLE_PRODUCT_MASTER",
    columns="*",
    vector_col="VECTOR_PRODUCT_DESC",
    k=3
)
result = gen_ai.embedding_vec_store( "text-embedding", hana_vec_object, vec_text="notebook" )

print(result)

gen_ai.close()
```

### [Check out the examples folder for more code.](https://github.com/praveen-nair/genai_wrapper/tree/master/examples)

# Found an issue/ Have a suggestion?
**IMP**: This package is for educational use and is not meant to replace other libraries.

If something is not working as expected or you have ideas for improvements, please feel free to open an issue or submit a pull request.