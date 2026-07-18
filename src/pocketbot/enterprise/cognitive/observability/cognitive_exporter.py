"""
PocketBot Enterprise X
Cognitive Exporter

Exports cognitive observability data.
"""

import json
from typing import Any, Dict

from .cognitive_dashboard import CognitiveDashboard


class CognitiveExporter:
    """
    Export dashboard data to different formats.
    """

    def __init__(
        self,
        dashboard: CognitiveDashboard,
    ):
        self.dashboard = dashboard

    def export_dict(self) -> Dict[str, Any]:
        """
        Export all dashboard data as dictionary.
        """

        return {
            "summary": self.dashboard.summary(),
            "metrics": self.dashboard.metrics(),
            "events": self.dashboard.events(),
            "traces": self.dashboard.traces(),
        }

    def export_json(
        self,
        indent: int = 2,
    ) -> str:
        """
        Export dashboard data as JSON.
        """

        return json.dumps(
            self.export_dict(),
            indent=indent,
            default=str,
        )
