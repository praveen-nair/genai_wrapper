import json

import genai_wrapper
from genai_wrapper import *

class GenAIWrapper:
    __author__ = "https://github.com/praveen-nair"
    __version__ = "00.00.04.202411"

    def __init__( self, **kwargs: dict ) -> None:
        global central_config
        config_content = kwargs.get("config_file", None)
        if config_content:
            with open( config_content, 'r' ) as file:
                config_content = json.load( file )
        else:
            config_content = kwargs.get("config_content", None)
            if config_content:
                config_content = json.loads( config_content )
            else:
                config_content = kwargs.get("config_dict", None)
                if not config_content:
                    raise GenAIWrapperException("Either config_file, config_content, or config_dict must be provided as input.")

        genai_wrapper.central_config = config_content
        AICore.init()

    def chat( self, llm_model: dict, chat_object: ChatObject ) -> str:
        return Chat(
            llm_model=llm_model
        ).query(chat_object)
        
    def embedding( self, llm_model: dict, text: str ) -> list:
        return Embeddings(
            llm_model=llm_model
        ).query( text=text )
    
    def embedding_vec_store( self, llm_model: dict, hana_vector_object: HANAVectorObject, **kwargs: dict ) -> None:
        if not genai_wrapper.hana_db_client:
            HANADb.init()

        hana_vector_object.k = kwargs.get( "k", hana_vector_object.k )
        vec_query = kwargs.get("vec_value", None)
        if not vec_query:
            vec_query = kwargs.get("vec_text", None)
            if not vec_query:
                raise GenAIWrapperException("Either vec_value or vec_text must be passed!")
            else:
                vec_query = self.embedding( llm_model, vec_query )

        cursor = genai_wrapper.hana_db_client.cursor()

        cursor.execute( f"SELECT TOP {hana_vector_object.k} {hana_vector_object.columns}, COSINE_SIMILARITY({hana_vector_object.vector_col}, TO_REAL_VECTOR('{vec_query}')) AS SIM_SCORE FROM {hana_vector_object.table} {f"WHERE {hana_vector_object.conditions}" if hana_vector_object.conditions else ""} ORDER BY SIM_SCORE DESC;" )

        result = hana_vector_object._process_output_( cursor.fetchall() )

        cursor.close()

        return result

    def close( self ):
        if not genai_wrapper.hana_db_client:
            HANADb.close() 