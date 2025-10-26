import subprocess

bots = [
    "main_bot.py",
    "Laura_bot.py",
    "Sara_bot.py",
    "Gabriele_bot.py",
    "Chris_bot.py"
    "Francesco_bot.py"
    "Beatrice_bot.py"
]

processes = []

for bot in bots:
    p = subprocess.Popen(["python", bot])
    processes.append(p)

# Rimane in esecuzione finché tutti i bot girano
for p in processes:
    p.wait()
