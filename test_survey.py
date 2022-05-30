import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for class 'AnonymousSurvey'"""

    def setUp(self):
        """Create survey and bunch of answers
        for all testing methods"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Ukrainian']

    def test_store_single_response(self):
        """Check single answer to save correctly"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Check three answers saved right"""

        for response in self.responses:
            self.my_survey.store_responses(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
