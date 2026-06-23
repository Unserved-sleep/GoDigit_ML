from pages.chat_page import ChatPage

def test_chat_response(page):
    chat = ChatPage(page)
    chat.open()
    initial_count = chat.get_response_count()

    chat.send_message(
        "What is Artificial Intelligence?"
    )
    page.wait_for_timeout(30000)
    final_count = chat.get_response_count()

    assert final_count > initial_count