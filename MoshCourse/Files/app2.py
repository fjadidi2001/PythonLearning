from pathlib import Path
path = Path()
for file in path.glob('*.py'):
    print(file)

for file2 in path.glob('*'):
    print(file2)