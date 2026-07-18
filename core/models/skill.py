from typing import List, Optional
from pydantic import BaseModel, Field


class Skill(BaseModel):
    skill_id: str
    curriculum: str
    stage: str
    term: int
    unit: str
    learning_object: str

    name: str
    description: str
    learning_objective: str

    bloom_level: str

    prerequisite_skills: List[str] = Field(default_factory=list)
    related_skills: List[str] = Field(default_factory=list)

    vocabulary: List[str] = Field(default_factory=list)
    misconceptions: List[str] = Field(default_factory=list)

    estimated_teaching_time: int = 15

    progression_weight: float = 0.30
    workbook_weight: float = 0.30
    mastery_weight: float = 0.40

    teacher_notes: Optional[str] = None
