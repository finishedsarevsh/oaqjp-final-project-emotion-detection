"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def _make_mock_response(self, dominant_emotion_name, score=0.9):
        """Build a mock requests.Response whose JSON matches Watson's schema."""
        emotions = {
            "anger": 0.1,
            "disgust": 0.1,
            "fear": 0.1,
            "joy": 0.1,
            "sadness": 0.1,
        }
        emotions[dominant_emotion_name] = score

        import json
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.text = json.dumps({
            "emotionPredictions": [{"emotion": emotions}]
        })
        return mock_resp

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        """'I am glad this happened' should return joy as dominant emotion."""
        mock_post.return_value = self._make_mock_response("joy")
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        """'I am really mad about this' should return anger as dominant emotion."""
        mock_post.return_value = self._make_mock_response("anger")
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, mock_post):
        """'I feel disgusted just hearing about this' should return disgust."""
        mock_post.return_value = self._make_mock_response("disgust")
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        """'I am so sad about this' should return sadness as dominant emotion."""
        mock_post.return_value = self._make_mock_response("sadness")
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, mock_post):
        """'I am really afraid that this will happen' should return fear."""
        mock_post.return_value = self._make_mock_response("fear")
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
