from shutil import which

_shells = list(__xonsh__.env.get('XONTRIB_SH_SHELLS', ['bash', 'sh']))
_installed_shells = []

@events.on_transform_command
def onepath(cmd, **kw):
    if len(cmd) > 2 and cmd.startswith('! '):
        if not _installed_shells:
            for s in _shells:
                if which(s):
                    _installed_shells.append(s)

        shell_cmd = cmd[1:].strip()

        if not shell_cmd:
            return cmd

        first_compatible_shell = None
        check_output_all = ''
        for s in _installed_shells:
            check_output = $(@(s) -nc @(shell_cmd) 2>&1).strip()
            if check_output == '':
                first_compatible_shell = s
                break
            check_output_all += f'\n\n{s}:\n\n{check_output}'

        if first_compatible_shell:
            return f'{first_compatible_shell} -c @({repr(shell_cmd)})'
        else:
            return f'echo @({repr(check_output_all.lstrip())})'
    return cmd