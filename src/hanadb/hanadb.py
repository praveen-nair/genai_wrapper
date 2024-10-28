import genai_wrapper
from genai_wrapper import dbapi

class HANADb:
    def init() -> None:
        genai_wrapper.hana_db_client = dbapi.connect(
            address=genai_wrapper.central_config["hana_vec_store"]["host"],
            port=genai_wrapper.central_config["hana_vec_store"]["port"],
            user=genai_wrapper.central_config["hana_vec_store"]["userid"],
            password=genai_wrapper.central_config["hana_vec_store"]["password"],
            sslValidateCertificate=genai_wrapper.central_config["hana_vec_store"]["ssl_cert_validation"]
        )

    def get_client() -> dbapi:
        return genai_wrapper.hana_db_client
    
    def close() -> None:
        if genai_wrapper.hana_db_client:
            genai_wrapper.hana_db_client.close()

