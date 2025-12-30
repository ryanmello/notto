from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from core.database import get_db
from models.note import Note

router = APIRouter()

class NoteCreate(BaseModel):
    content: str

class NoteResponse(BaseModel):
    id: int
    content: str
    timestamp: str

    class Config:
        from_attributes = True

@router.get("/")
async def get_notes():
    return {}

@router.get("/{note_id}")
async def get_note(note_id: int):
    return {"note_id": note_id}

@router.post("/create", response_model=NoteResponse)
async def create_note(note_data: NoteCreate, db: AsyncSession = Depends(get_db)):
    note = Note(content=note_data.content)
    db.add(note)
    await db.commit()
    await db.refresh(note)
    return NoteResponse(
        id=note.id,
        content=note.content,
        timestamp=note.timestamp.isoformat()
    )

@router.put("/update")
async def update_note():
    return {}

@router.delete("/{note_id}")
async def delete_note(note_id: int):
    return {"note_id": note_id}
    