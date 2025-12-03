import subprocess  # nosec B404

def add(a, b):
    return a + b
def sub(a, b):
    return a - b

def run_command(cmd):
    # ❌ Vulnerable: shell=True allows command injection
    return subprocess.Popen(cmd, shell=False) # nosec B603
