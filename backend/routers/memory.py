from fastapi import APIRouter
from backend.services.memory_service import MemoryService

router = APIRouter(prefix='/memory', tags=['memory'])
service = MemoryService()

@router.get('/')
def list_memory():
    return service.get_all()

@router.post('/')
def save_memory(payload:dict):
    service.save(payload.get('user_id','default'), payload.get('content',''))
    return {'saved': True}
