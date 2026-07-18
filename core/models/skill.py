from typing import List, Optional
from pydantic import BaseModel


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

    prerequisite_skills: List[str] = []

    related_skills: List[str] = []

    misconceptions: List[str] = []

    vocabulary: List[str] = []

    bloom_level: str

    estimated_teaching_time: int

    progression_weight: float

    workbook_weight: float

    mastery_weight: float

    teacher_notes: Optional[str] = None
