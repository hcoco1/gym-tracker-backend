from datetime import datetime

# Any general utility functions would go here
# For example:
def format_timestamp(dt: datetime) -> str:
    return dt.isoformat()

def validate_email_format(email: str) -> bool:
    # Simple email validation logic
    return "@" in email and "." in email.split("@")[-1]