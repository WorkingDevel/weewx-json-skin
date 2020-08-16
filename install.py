# installer for the '2Json' skin
# Copyright 2020 Christoph Graupner

from weecfg.extension import ExtensionInstaller


def loader():
    return BasicInstaller()


class BasicInstaller(ExtensionInstaller):
    def __init__(self):
        super(BasicInstaller, self).__init__(
            version = '0.1.0',
            name = '2Json',
            description = 'JSON suitable for consumption from an SPA.',
            author = "Christoph Graupner",
            author_email = "ch.graupner@workingdeveloper.net",
            config = {
                'StdReport': {
                    '2Json': {
                        'skin': '2Json',
                        'HTML_ROOT': '2Json'
                    }
                }
            },
            files = [
                (
                    'skins/2Json', [
                        'skins/2Json/daily.json.tmpl',
                        'skins/2Json/skin.conf'
                    ]
                ),
            ]
        )
