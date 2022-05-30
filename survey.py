class AnonymousSurvey:
    """Collect anonymous answers"""
    def __init__(self, question):
        """Save question and get ready to save answer"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show question"""
        print(self.question)

    def store_responses(self, new_response):
        """Save one answer"""
        self.responses.append(new_response)

    def show_results(self):
        """Show every given answer"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")