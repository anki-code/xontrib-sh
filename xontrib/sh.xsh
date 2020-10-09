from shutil import which

_shells = ['bash', 'zsh', 'fish', 'sh']
_installed_shells = []

@events.on_transform_command
def onepath(cmd, **kw):
    if cmd and cmd[0] == '!':
        if not _installed_shells:
            for s in _shells:
                if which(s):
                    _installed_shells.append(s)

        cmd = cmd[1:].strip()

        first_compatible_shell = None
        for s in _installed_shells:
            if $(@(s) -nc @(cmd) 2>&1).strip() == '':
                first_compatible_shell = s
                break

        if first_compatible_shell:
            shell_cmd = first_compatible_shell + ' -c'
            printx(f'{{BOLD_WHITE}}{first_compatible_shell}:{{RESET}}\n\r', end='')
        else:
            try_to_install = ''
            not_installed_shells = [s for s in _shells if s not in _installed_shells]
            if len(not_installed_shells) > 0:
                try_to_install = f'Try to install {",".join(not_installed_shells)}.'
            printx(f'{{BOLD_WHITE}}Checked {", ".join(_installed_shells)} with no success. {try_to_install}{{RESET}}\n\r', end='')
            shell_cmd = 'echo'

        return f'{shell_cmd} @({repr(cmd)})'
    return cmd