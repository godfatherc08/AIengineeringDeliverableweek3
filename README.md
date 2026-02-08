# Setup Notes – Video Game Ideas Generator

## 1. Get Your Groq API Key (Free Tier)
1. Go to: https://console.groq.com/
2. Sign up / log in
3. Click **API Keys** in the left menu
4. Create a new key
5. **Copy the key** — it starts with `gsk_`


## 2. Create a `.env` file (recommended & safest way)

In the same folder as your `app.py`, create a file named `.env`
```env
# .env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
