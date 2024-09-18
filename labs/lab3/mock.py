from unittest.mock import MagicMock

from observer import Subject

def test_observer_mock():
    subject = Subject()
    observer_mock = MagicMock()
    subject.attach(observer_mock)
    
    subject.set_state("new state")
    observer_mock.update.assert_called_with("new state")
