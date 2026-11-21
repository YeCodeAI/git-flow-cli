import subprocess

from typing import List
from dataclasses import dataclass

@dataclass(frozen=True)
class RunnerResult:
    stdout: str
    stderr: str
    returncode: int

class Runner:

    def run(self, commands: List[str]) -> RunnerResult:
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            encoding='utf-8',
            shell=False
        )

        if result.returncode != 0:
            return RunnerResult(
                stdout='',
                stderr=result.stderr.strip(),
                returncode=result.returncode
            )
        
        return RunnerResult(
            stdout=result.stdout,
            stderr='',
            returncode=result.returncode
        )