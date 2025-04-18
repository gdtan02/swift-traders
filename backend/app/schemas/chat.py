from pydantic import BaseModel
from typing import Dict, Optional, List, Any, Union

# Chat API endpoints
class ChatRequestModel(BaseModel):
    modelName: str
    timestamp: str
    messages: Union[str, List[str]]
    modelMetrics: Optional[Dict[str, Any]] = None
    
class ChatResponseModel(BaseModel):
    text: Optional[str] = None
    scores: Optional[Dict[str, Any]] = None