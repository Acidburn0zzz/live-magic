import gtk
import os.path

from DebianLive import Config, utils

class WizardController(object):

    def on_wizard_apply(self, _):
        build_dir = utils.get_build_dir()
        data = self.view.get_wizard_completed_details()

        # Use cdebootstrap if available
        if os.path.exists('/usr/bin/cdebootstrap'):
            data['bootstrap'] = 'cdebootstrap'

        self.model = Config(build_dir, **data)

        self.view.do_dim_wizard()
        self.do_show_build_window(lambda: gtk.main_quit())

    def on_wizard_expert_mode_selected(self, _):
        self.view.do_hide_wizard()
        self.view.do_show_main_window()

    def get_suggested_mirror(self):
        s = utils.SourcesList()
        return s.get_mirror()

    def on_wizard_cancel(self, *args):
        if self.view.do_show_wizard_cancel_confirm_window():
            gtk.main_quit()
