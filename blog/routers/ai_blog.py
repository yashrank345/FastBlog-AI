from fastapi import APIRouter , Depends
from pydantic import BaseModel
from blog.repository.ai_blog_generator import generate_blog
from blog import schemas, oauth2

router = APIRouter(
    prefix="/ai_blog",
    tags=["AI Blog Generator"]
)

class BlogRequest(BaseModel):
    topic: str
    context_word : str


@router.post("/")
def create_ai_blog(data: BlogRequest,current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog_content = generate_blog(data.topic , data.context_word)
    return {"topic": data.topic, "blog": blog_content}
