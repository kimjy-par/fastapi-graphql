import strawberry

from strawberry.scalars import JSON
from typing import List

@strawberry.type
class InferenceResult:
    data: JSON