import pytest
from pages.chat_page import ChatPage

@pytest.mark.parametrize(
    "question",
    [
        "What is AI?",
        "What is Python?",
        "What is Selenium?"
    ]
)
def test_multiple_questions(page, question):
    chat = ChatPage(page)
    chat.open()
    count = chat.get_response_count()
    chat.send_message(question)

    page.wait_for_timeout(5000)
    assert chat.get_response_count() > count