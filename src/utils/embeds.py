from utils.helpers import *
from disnake.ui import Button, Select, View


class EmbedFactory:
    def __init__(
        self,
        title: str = None,
        description: str = None,
        author: str = None,
        author_url: str = None,
        colour: disnake.Colour = disnake.Colour.og_blurple(),
        infobox: dict = None,
        options: list = None,
        thumbnail_url: str = None,
        button_label: str = None,
        button_url: str = None,
    ):
        self.title = title
        self.description = description
        self.author = author
        self.author_url = author_url
        self.colour = colour
        self.infobox = infobox
        self.options = options
        self.thumbnail_url = thumbnail_url
        self.button_label = button_label
        self.button_url = button_url

    def create(
        self,
        title: str = None,
        description: str = None,
        author: str = None,
        author_url: str = None,
        colour: disnake.Colour = None,
        infobox: dict = None,
        options: list = None,
        thumbnail_url: str = None,
        button_label: str = None,
        button_url: str = None,
        button_emoji: disnake.PartialEmoji = None
    ):

        embed = disnake.Embed()
        view = View(timeout=None)

        embed.title = self.title if not title else title
        embed.description = self.description if not description else description
        embed.colour = self.colour if not colour else colour

        if options:
            dropdown = create_dropdown(options)
            view.add_item(dropdown)
            return (embed, view)

        if thumbnail_url:
            embed.set_thumbnail(url=thumbnail_url)

        if infobox:
            infobox.pop('Image', 'Icon')
            for i in list(infobox.items())[:3]:
                embed.add_field(name=i[0], value=i[1], inline=True)

        if button_url:
            if button_label:
                button = create_link_button(
                    button_label, button_url, button_emoji)
                view.add_item(button)
                return (embed, view)
            button = create_link_button('Visit Page', button_url, button_emoji)
            view.add_item(button)
            return (embed, view)
        return (embed)


'''
Creates a regular button for interaction responses.
:param label: (String) - Represents a label for the button.
:param url: (String) - Represents a hyperlink (URL) for the button.
'''


def create_button(label=None, emoji=None) -> None:
    button = Button(label=label, style=disnake.ButtonStyle.grey, emoji=emoji)
    return (button)


'''
Creates a hyperlink button for interaction responses.
:param label: (String) - Represents a label for the button.
:param url: (String) - Represents a hyperlink (URL) for the button.
'''


def create_link_button(label, url, emoji=None) -> None:
    button = Button(
        label=label,
        style=disnake.ButtonStyle.link,
        url=url,
        emoji=emoji)
    return (button)


'''
Creates a dropdown menu for interaction responses.
:param options: (List) - Represents a list of options (labels) for the dropdown.
'''


def create_dropdown(options) -> None:
    dropdown = Select(placeholder='Select an option.', options=[])
    for option in options:
        dropdown.add_option(label=option)
    return (dropdown)
