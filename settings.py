import os
import yaml

class SettingsManager:
    default_settings = {
        'library': '~/.ppp/library',
        'salt': '200',
        'select1': '#documents a.rel-link',
        'select2': '#documents a.rel-link',
        'authors_class1': '__title',
        'authors_text':  'Tags List:',
        'authors_class2': '__content',
        'database': '~/.ppp/library.db'
    }

    def __init__(self):
        home_folder = os.path.expanduser("~")
        self.file_path = os.path.join(home_folder, '.ppp/settings.yaml')
        self.settings = self._load_settings()

    def _load_settings(self):
        try:
            with open(self.file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            return {}

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

    def save_settings(self, settings, file_path):
        with open(file_path, 'w') as config_file:
            yaml.dump(settings, config_file)

    def reset_settings(self):
        self.save_settings(self.default_settings, self.file_path)
