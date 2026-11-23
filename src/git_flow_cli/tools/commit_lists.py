from typing import List, Dict

from ..ui import UI
from ..runner import Runner

RECORD_SEP = '\x1e'
FIELD_SEP = '\x1f'

def _parse_commits(raw_output: str) -> List[Dict[str, str]]:
    commits: List[Dict[str, str]] = []

    for record in raw_output.split(RECORD_SEP):
        cleaned = record.strip()
        if not cleaned:
            continue

        parts = cleaned.split(FIELD_SEP)
        if len(parts) < 4:
            continue

        commit_hash, date, author, subject = parts[0], parts[1], parts[2], parts[3]
        commits.append({
            'hash': commit_hash.strip(),
            'date': date.strip(),
            'author': author.strip(),
            'subject': subject.strip(),
        })

    return commits

def commit_lists() -> None:
    ui = UI()
    runner = Runner()

    check = runner.run(['git', 'rev-parse', '--is-inside-work-tree'])
    if check.returncode != 0:
        ui.error('The current folder is not a Git repository.')
        return
    
    result = runner.run([
        'git',
        'log',
        '--all',
        '--date=format:%Y-%m-%d %H:%M',
        f'--pretty=format:%h{FIELD_SEP}%ad{FIELD_SEP}%an{FIELD_SEP}%s{RECORD_SEP}',
    ])

    if result.returncode != 0:
        ui.error('Failed to retrieve the list of commits.')
        return

    commits = _parse_commits(result.stdout)
    ui.commit_table(commits)

