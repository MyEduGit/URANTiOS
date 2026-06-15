# 📘 My OpenClaw Setup Checklist

A simple, step-by-step guide to running my own OpenClaw AI agent on Railway.

Read one step at a time. Take a break if you need to. Nothing here is urgent.

---

## ⚠️ Read this first — the one rule that matters

Your **API key** is like a **credit card**. Whoever gets it can spend your money.

- Only type your API key into **your own Railway URL** (the one Railway gives *you*).
- **Never** paste it into a chat, an email, or any other website.
- Use the **official OpenClaw** template. Search "OpenClaw" on railway.com and
  pick the one from the official OpenClaw project. There are many copies — some
  could be fake.

If anything ever feels off, **stop** and ask for help before typing a password
or key.

---

## The 5 Steps

### Step 1 — Sign in to Railway
- Go to **railway.com**.
- Click **Sign in with GitHub**.
- That's it for this step.

### Step 2 — Start the OpenClaw template
- On railway.com, **search for "OpenClaw"**.
- Pick the **official** OpenClaw template.
- Click **Deploy**. Railway sets it up for you. No terminal needed.

### Step 3 — Set two secret values
In your project: **Variables** (or **Settings → Variables**), add:
- `SETUP_PASSWORD` — a **strong password you do not use anywhere else**.
- `OPENCLAW_GATEWAY_TOKEN` — a long random string (the wizard can make one).

Write both down somewhere safe and private.

### Step 4 — Get your web address
- Open **Settings → Networking** (sometimes called **Public Networking** or
  **Domains**).
- Copy the **URL** Railway shows you. That is your private OpenClaw address.

### Step 5 — Finish setup in the browser
- Open your URL, then add **/setup** at the end.
- Log in with your `SETUP_PASSWORD`.
- Paste your **LLM API key** (Anthropic, OpenAI, or Google) when asked.
- Done. Your agent is live.

---

## 📱 How to reach my agent later
- Open the **URL** from Railway (**Settings → Networking / Domains**).
- Keep it private, or connect it to a chat app like Telegram later.

---

## 🧠 Quick memory card
1. **Sign in:** railway.com → Sign in with GitHub.
2. **Deploy:** search "OpenClaw" → official template → Deploy.
3. **Protect:** add `SETUP_PASSWORD` + `OPENCLAW_GATEWAY_TOKEN` in Variables.
4. **Address:** copy your URL from Settings → Networking.
5. **Finish:** open `your-url/setup`, log in, paste your API key.

---

## ℹ️ Good to know
- **OpenClaw** is real and open-source. It used to be called **Clawdbot**, and
  before that **Moltbot**. Same project, new name.
- The actual deploy runs from **Railway's template**, not from this URANTiOS
  repository. This file is just your saved guide.
- These steps happen in **your own browser and Railway account**. An assistant
  cannot click through them on your Mac for you — but you can do each step at
  your own pace, and ask for help any time you get stuck.
