
import asyncio
import psutil

async def gather_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    processes = [(p.info["name"], p.info["memory_percent"])
                 for p in psutil.process_iter(['name', 'memory_percent'])]
    top_processes = sorted(processes, key=lambda x: x[1], reverse=True)[:3]

    log = "[task1] System Resource Monitor:\n"
    log += f"  CPU Usage: {cpu}%\n"
    log += f"  RAM Usage: {ram}%\n"
    log += f"  Disk Usage: {disk}%\n"
    log += f"  Top Memory Processes:\n"
    for name, mem in top_processes:
        log += f"    - {name}: {mem:.2f}%\n"

    return log

async def main():
    log = await gather_system_metrics()
    print(log)
    with open("notes.md", "a") as f:
        f.write("\n" + log + "\n")

if __name__ == "__main__":
    asyncio.run(main())
