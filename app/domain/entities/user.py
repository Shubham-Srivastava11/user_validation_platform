from dataclasses import dataclass
from typing import List

@dataclass
class Email:
    value: str
    trust_score: int
    provider: str
    is_valid: bool

@dataclass
class Phone:
    value: str
    trust_score: int
    provider: str
    is_valid: bool

@dataclass
class User:
    linkedin: str
    name: str
    emails: List[Email]
    phones: List[Phone]

    def best_email(self):
        valid = [e for e in self.emails if e.is_valid]
        if not valid:
            return None
        return max(valid, key=lambda x: x.trust_score)

    def best_phone(self):
        valid = [p for p in self.phones if p.is_valid]
        if not valid:
            return None
        return max(valid, key=lambda x: x.trust_score)
