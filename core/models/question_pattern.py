from typing import List, Dict
from pydantic import BaseModel, Field


class QuestionPattern(BaseModel):

    pattern_id: str

    skill_id: str

    name: str

    description: str

    style: str

    difficulty: str

    template: str

    variables: Dict[str, str] = Field(default_factory=dict)

    constraints: List[str] = Field(default_factory=list)

    answer_formula: str

    explanation_template: str
