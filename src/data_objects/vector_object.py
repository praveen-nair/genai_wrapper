import json

from genai_wrapper import GenAIWrapperException

class HANAVectorObject:
    def __init__( self, **kwargs: dict ) -> None:
        self.table = kwargs.get( "table", None )
        self.columns = kwargs.get( "columns", None )
        if not self.table:
            raise GenAIWrapperException("Db table cannot be empty!")
        else:
            if type(self.columns) == list:
                self.columns = ", ".join(self.columns)
        self.vector_col = kwargs.get( "vector_col", None )
        if not self.vector_col:
            raise GenAIWrapperException("You need to pass at least 1 vector store column")
        self.conditions = kwargs.get( "conditions", None )
        if self.conditions:
            self.conditions = None if len( self.conditions.trim() ) == 0 else self.conditions
        self.k = kwargs.get( "k", 3 )

    def _process_output_( self, records: list ) -> dict:
        self._result = {
            "total_records": 0,
            "records": {}
        }
        if len( records ) > 0:
            self._result = {
                "total_records": len( records ),
                "records": { key.strip(): [] for key in records[0].column_names }
            }
            for row in records:
                for col in self._result["records"].keys():
                    self._result["records"][col].append( row[col] )

        return self._result