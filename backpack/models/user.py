from backpack.db.orm.model import table, Model, Field, GenerationStrategy, Default
from backpack.db.orm.types import String, Date, DateTime, Boolean
from backpack.utils.token_generator import token

@table("User")
class User(Model):

    id = Field(String, column="userId", primary_key=True, generator=GenerationStrategy.UUID)
    username = Field(String(25), required=True, unique=True)
    email = Field(String(50), required=True, unique=True)
    password = Field(String, required=True)
    birth_date = Field(Date, column="birthDate", required=True)
    verification_token = Field(String, column="verificationToken")
    token_sent_at = Field(DateTime, column="tokenSentAt", required=True, default=Default.NOW)
    verified = Field(Boolean, required=True, default=False)
    created_at = Field(DateTime, column="createdAt", required=True, default=Default.NOW)
    updated_at = Field(DateTime, column="updatedAt", required=True, default=Default.NOW)

    def __init__(self, 
        username: String = None,
        email: String = None,
        password: String = None,
        birth_date: Date = None
    ):
        super().__init__(username=username, email=email, password=password, birth_date=birth_date)

    def generate_verification_token(self):
        self.verification_token = token()
        self.token_sent_at = DateTime.now()

        return self.verification_token
    
    def to_dict(self):
        return {
            "userId": self.id,
            "username": self.username,
            "email": self.email,
            "birthDate": self.birth_date,
            "verified": self.verified,
            "createdAt": self.created_at
        }