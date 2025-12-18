from pathlib import Path
p = Path('pyproject.toml')
data = p.read_bytes()
if data.startswith(b'\xef\xbb\xbf'):
    p.write_bytes(data[len(b'\xef\xbb\xbf'):])
    print('BOM removed')
else:
    print('No BOM')
