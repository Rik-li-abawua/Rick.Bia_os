from fastapi import APIRouter
from backend.services.chat_service import ChatService

router = APIRouter(prefix='/chat', tags=['chat'])
service = ChatService()

@router.post('/')
def chat(payload: dict):
    prompt = payload.get('prompt','')
    result = service.process(prompt)
    return {'prompt': prompt, 'result': result}
