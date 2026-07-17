from dataclasses import dataclass, asdict
from datetime import datetime, timezone


@dataclass
class IntelligenceMonitoring:
    component: str = "enterprise_intelligence"
    status: str = "healthy"
    events_checked: int = 0
    alerts: int = 0
    last_check: str = ""

    def __post_init__(self):
        if not self.last_check:
            self.last_check = datetime.now(timezone.utc).isoformat()

    def run_check(self):
        return self.to_dict()

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_mapping(cls, data=None):
        data = data or {}

        return cls(
            component=data.get(
                "component",
                "enterprise_intelligence"
            ),
            status=data.get(
                "status",
                "healthy"
            ),
            events_checked=data.get(
                "events_checked",
                0
            ),
            alerts=data.get(
                "alerts",
                0
            ),
            last_check=data.get(
                "last_check",
                ""
            ),
        )
