from restish import page, resource, templating
from wsgiapptools import flash

class FlashMessagesElement(page.Element):

    def __call__(self, request):
        messages = flash.get_messages(request.environ)
        if not messages:
            return ''
        return templating.render(request, 'flash_messages.html', {'messages': messages})


class BaseResource(resource.Resource):
    pass


class BasePage(page.Page):
    @page.element('flash_message')
    def flash_message(self, request):
        """
        Return a flash message box element.
        """
        return FlashMessagesElement() 


class BaseElement(page.Element):
    pass

