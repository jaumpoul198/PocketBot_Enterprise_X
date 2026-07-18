class ReflectionAnalyzer:

    def analyze(
        self,
        feedback,
    ):

        success = feedback.get(
            "success",
            False,
        )

        return {
            "success": success,
            "quality": (
                "positive"
                if success
                else "negative"
            ),
        }
