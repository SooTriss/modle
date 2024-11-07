from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Actor(BaseModel):
    name: str
    mbox: str
    objectType: str


class Display(BaseModel):
    en_US: str = Field(..., alias='en-US')


class Verb(BaseModel):
    id: str
    display: Display


class Extensions(BaseModel):
    http___h5p_org_x_api_h5p_local_content_id: int = Field(
        ..., alias='http://h5p.org/x-api/h5p-local-content-id'
    )


class Name(BaseModel):
    en_US: str = Field(..., alias='en-US')


class Definition(BaseModel):
    extensions: Extensions
    name: Name
    interactionType: str
    type: str


class Object(BaseModel):
    id: str
    objectType: str
    definition: Definition


class CategoryItem(BaseModel):
    id: str
    objectType: str


class ContextActivities(BaseModel):
    category: List[CategoryItem]


class Context(BaseModel):
    contextActivities: ContextActivities


class Score(BaseModel):
    min: int
    max: int
    raw: int
    scaled: int


class Result(BaseModel):
    score: Score
    completion: bool
    success: bool
    duration: str


class Statement(BaseModel):
    actor: Actor
    verb: Verb
    object: Object
    context: Context
    result: Result


class Actor1(BaseModel):
    name: str
    mbox: str
    objectType: str


class Display1(BaseModel):
    en_US: str = Field(..., alias='en-US')


class Verb1(BaseModel):
    id: str
    display: Display1


class Extensions1(BaseModel):
    http___h5p_org_x_api_h5p_local_content_id: int = Field(
        ..., alias='http://h5p.org/x-api/h5p-local-content-id'
    )
    http___h5p_org_x_api_h5p_subContentId: str = Field(
        ..., alias='http://h5p.org/x-api/h5p-subContentId'
    )


class Name1(BaseModel):
    en_US: str = Field(..., alias='en-US')


class Description(BaseModel):
    en_US: str = Field(..., alias='en-US')


class Definition1(BaseModel):
    extensions: Extensions1
    name: Name1
    interactionType: str
    type: str
    description: Description


class Object1(BaseModel):
    id: str
    objectType: str
    definition: Definition1


class ParentItem(BaseModel):
    id: str
    objectType: str


class CategoryItem1(BaseModel):
    id: str
    objectType: str


class ContextActivities1(BaseModel):
    parent: List[ParentItem]
    category: List[CategoryItem1]


class Context1(BaseModel):
    contextActivities: ContextActivities1


class Score1(BaseModel):
    min: int
    max: int
    raw: int
    scaled: int


class Result1(BaseModel):
    score: Score1
    completion: bool
    success: bool
    duration: str


class Statement1(BaseModel):
    actor: Actor1
    verb: Verb1
    object: Object1
    context: Context1
    result: Result1


class Actor2(BaseModel):
    name: str
    mbox: str
    objectType: str


class Display2(BaseModel):
    en_US: str = Field(..., alias='en-US')


class Verb2(BaseModel):
    id: str
    display: Display2


class ParentItem1(BaseModel):
    id: str
    objectType: str


class ContextActivities2(BaseModel):
    parent: List[ParentItem1]


class Context2(BaseModel):
    contextActivities: ContextActivities2


class Extensions2(BaseModel):
    http___h5p_org_x_api_h5p_local_content_id: int = Field(
        ..., alias='http://h5p.org/x-api/h5p-local-content-id'
    )
    http___h5p_org_x_api_h5p_subContentId: str = Field(
        ..., alias='http://h5p.org/x-api/h5p-subContentId'
    )


class Definition2(BaseModel):
    interactionType: str
    type: str
    extensions: Extensions2


class Object2(BaseModel):
    id: str
    objectType: str
    definition: Definition2


class Score2(BaseModel):
    raw: int
    min: int
    max: int
    scaled: int


class Result2(BaseModel):
    duration: str
    score: Score2


class Statement2(BaseModel):
    actor: Actor2
    verb: Verb2
    context: Context2
    object: Object2
    result: Result2


class Actor3(BaseModel):
    name: str
    mbox: str
    objectType: str


class Display3(BaseModel):
    en_US: str = Field(..., alias='en-US')


class Verb3(BaseModel):
    id: str
    display: Display3


class ParentItem2(BaseModel):
    id: str
    objectType: str


class ContextActivities3(BaseModel):
    parent: List[ParentItem2]


class Context3(BaseModel):
    contextActivities: ContextActivities3


class Description1(BaseModel):
    en_US: str = Field(..., alias='en-US')


class Description2(BaseModel):
    en_US: str = Field(..., alias='en-US')


class Choice(BaseModel):
    id: str
    description: Description2


class Extensions3(BaseModel):
    http___h5p_org_x_api_h5p_local_content_id: int = Field(
        ..., alias='http://h5p.org/x-api/h5p-local-content-id'
    )
    http___h5p_org_x_api_h5p_subContentId: str = Field(
        ..., alias='http://h5p.org/x-api/h5p-subContentId'
    )


class Definition3(BaseModel):
    description: Description1
    interactionType: str
    correctResponsesPattern: List[str]
    type: str
    choices: List[Choice]
    extensions: Extensions3


class Object3(BaseModel):
    id: str
    objectType: str
    definition: Definition3


class Score3(BaseModel):
    raw: int
    min: int
    max: int
    scaled: int


class Result3(BaseModel):
    response: str
    completion: bool
    success: bool
    duration: str
    score: Score3


class Statement3(BaseModel):
    actor: Actor3
    verb: Verb3
    context: Context3
    object: Object3
    result: Result3


class Child2(BaseModel):
    statement: Statement3


class Child1(BaseModel):
    statement: Statement2
    children: List[Child2]


class Child(BaseModel):
    statement: Statement1
    children: List[Child1]


class Model(BaseModel):
    statement: Optional[Statement] = None
    children: Optional[List[Child]] = None
