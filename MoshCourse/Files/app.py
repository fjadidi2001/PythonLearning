from pathlib import Path

path = Path('eco')
print(path.exists())
path = Path('emails')
print(path.exists())
# path = Path('emails')
# print(path.mkdir())
# print(path.rmdir())
path = Path()
# return all py file in this directory
print(path.glob('*.py'))
