import subprocess

# Lista dei bot da avviare
bots = [
    "main_bot.py",
    "Laura_bot.py",
    "Sara_bot.py",
    "Gabriele_bot.py",
    "Beatrice_bot.py",
    "Francesco_bot.py",
    "Chris_bot.py"
]

processes = []

for bot in bots:
    print(f"🚀 Avvio di {bot}...")
    p = subprocess.Popen(["python", bot])
    processes.append(p)

print("✅ Tutti i bot sono stati avviati.")

# Mantiene il servizio attivo
for p in processes:
    p.wait()
