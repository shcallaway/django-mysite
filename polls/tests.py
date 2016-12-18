import datetime
from django.utils import timezone
# Import the TestCase class!
from django.test import TestCase
from .models import Question

# Create a TestCase subclass for the Question object
class QuestionMethodTests(TestCase):

	# Define a method to test the was_published_recently method
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

# Run with: python manage.py test polls