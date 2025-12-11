from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import HTTPException, status

# Get all blogs
def get_all(db: Session):
    return db.query(models.Blog).all()

# Create a new blog
def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Delete a blog
def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

# Update a blog
def update(id: int, request: schemas.Blog, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    existing_blog = blog_query.first()
    
    if not existing_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog_query.update(request.dict())
    db.commit()
    return 'updated'

# Show single blog
def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog
