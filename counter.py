from pathlib import Path
from sys import path, argv

import re

script_dir = Path(path[0])

if len(argv) > 1:
    for arg in argv[1:]:
        if re.match(r'.*\.py', arg):
            file_path = script_dir / arg
            if file_path.is_file():
                print(arg.upper())
                print(len(re.findall(
                    r'^class.*$',
                    file_path.read_text('utf-8'),
                    re.M
                )), 'classes')
else:
    pass
