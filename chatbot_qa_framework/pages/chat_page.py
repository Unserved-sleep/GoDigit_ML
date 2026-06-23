from playwright.sync_api import Page

class ChatPage:
    def __init__(self, page: Page):
        self.page = page
        self.prompt_box = page.get_by_placeholder("Ask anything…")
        self.send_button = page.locator("[type='submit']")

    def open(self):
        self.page.goto(
            "https://arena.ai/"
        )

    def enter_message(self, message):
        self.prompt_box.fill(message)

    def click_send(self):
        self.send_button.click()

    def send_message(self, message):
        self.enter_message(message)
        self.click_send()

    def get_response_count(self):
        return self.page.locator(
            "div.prose"
        ).count()