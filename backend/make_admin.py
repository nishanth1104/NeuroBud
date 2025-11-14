from app.database.connection import SessionLocal
from app.models.user import User

# Your email
ADMIN_EMAIL = "nishanth4011@gmail.com"  

db = SessionLocal()

try:
    user = db.query(User).filter(User.email == ADMIN_EMAIL).first()
    
    if user:
        user.is_admin = True
        db.commit()
        print(f"✅ {ADMIN_EMAIL} is now an admin!")
    else:
        print(f"❌ User {ADMIN_EMAIL} not found. Please sign in first.")
finally:
    db.close()