from typing import List, Dict, Any
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field



class summary(BaseModel):
    short_summary: str = Field(description='summary')
    fun_facts: List[str] = Field(description='fun facts')
    approach_points: List[str] = Field(description='approach points')
    
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "short_summary": self.short_summary,
            "fun_facts": self.fun_facts,
            "approach_points": self.approach_points,
        }


summary_parser = PydanticOutputParser(pydantic_object=summary)


