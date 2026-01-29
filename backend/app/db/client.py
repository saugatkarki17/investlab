import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    raise ValueError(" Supabase URL or Key is missing from .env")

# Initialize the client
supabase: Client = create_client(url, key)

def get_user_balance(user_id: int):
    """Example of calling the API to get balance"""
    response = supabase.table("portfolio_balance").select("*").eq("user_id", user_id).execute()
    # Supabase returns a generic response object
    if response.data:
        return response.data[0]
    return None

if __name__ == "__main__":
    # Test the connection
    print("🔌 Testing Supabase API connection...")
    users = supabase.table("users").select("*").execute()
    print(f"✅ Users found: {users.data}")

# Loads .env variables (SUPABASE_URL and SUPABASE_KEY).
#Creates a Supabase client to interact with the database.
#Defines a function get_user_balance to fetch a user's portfolio balance.
#Tests the connection by fetching all users and printing them.