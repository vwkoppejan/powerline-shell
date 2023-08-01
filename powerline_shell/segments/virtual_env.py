import os
from ..utils import BasicSegment


class Segment(BasicSegment):
    def add_to_powerline(self):
        env = os.getenv('VIRTUAL_ENV') \
            or os.getenv('CONDA_ENV_PATH') \
            or os.getenv('CONDA_DEFAULT_ENV')
        if os.getenv('VIRTUAL_ENV') \
            and os.path.basename(env) == '.virtual_env':
            env = os.path.basename(os.path.dirname(env))
        if not env:
            return

        env_name = os.path.basename(env)
        if self.powerline.segment_conf("virtual_env", "poetry-suffix") == False:
            if 'poetry' in os.path.abspath(env):
                env_name = "-".join(env_name.split('-')[0:-2 ])

        bg = self.powerline.theme.VIRTUAL_ENV_BG
        fg = self.powerline.theme.VIRTUAL_ENV_FG
        self.powerline.append(" " + env_name + " ", fg, bg)
