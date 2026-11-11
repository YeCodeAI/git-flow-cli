import subprocess

from typing import List

class GitRunner:
    def run(self, commands: List[str]) -> str:
        result = subprocess.run(
            ['git'] + commands,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        if result.returncode != 0:
            return result.stderr
        
        return result.stdout