from shutil import which

_shells = list(__xonsh__.env.get('XONTRIB_SH_SHELLS', ['bash', 'sh']))
_bash_win = 'bash.exe'
_installed_shells = []
_match_first_char = __xonsh__.env.get('XONTRIB_SH_MATCHFIRST', True)
_match_full_name = __xonsh__.env.get('XONTRIB_SH_MATCHFULL', True)
_shells_without_syntax_check = ['pwsh', 'powershell', 'cmd']


@events.on_transform_command
def onepath(cmd, **kw):
    cmd_flag = '-c' # *sh flag to execute the specified commands, change to '/C' for cmd

    if len(cmd) > 2 and cmd.startswith('! '):
        if not _installed_shells:
            for s in _shells:
                exists = which(s)
                if exists:
                    if not exists.lower().endswith(_bash_win):
                        _installed_shells.append(s.rstrip('.exe').lower())
        if not _installed_shells:
            ret_val = "xontrib-sh: No known shell is installed: " \
                + ", ".join(map(str, _shells))
            return f'echo @({repr(ret_val)})'

        shell_cmd = cmd[1:].strip()

        if not shell_cmd:
            return cmd

        first_compatible_shell = None
        check_output_all = ''
        if len(_shells) == 1:   # skip syntax check for a single shell
            if _installed_shells[0] == 'cmd':
                cmd_flag = '/C'
            return f'{_installed_shells[0]} {cmd_flag} @({repr(shell_cmd)})'
        for s in _installed_shells:
            if s in _shells_without_syntax_check:  # skip shells that don't have a syntax check
                continue
            check_output = __xonsh__.subproc_captured_stdout([s, '-nc', shell_cmd, '2>&1']).strip()
            if check_output == '':
                first_compatible_shell = s
                break
            check_output_all += f'\n\n{s}:\n\n{check_output}'

        if first_compatible_shell:
            return f'{first_compatible_shell} {cmd_flag} @({repr(shell_cmd)})'
        else:
            return f'echo @({repr(check_output_all.lstrip())})'
    elif len(cmd) > 3 and cmd.startswith('!')\
                  and not cmd.startswith('![')\
                  and not cmd.startswith('!('):
        first_compatible_shell = None
        if _match_first_char:
            for shell in _shells:
                if cmd.startswith('!' + shell[0] + ' '):
                    exists = which(shell)
                    if exists:
                        if not exists.lower().endswith(_bash_win):
                            first_compatible_shell = shell
                    break
        if _match_full_name:
            for shell in _shells:
                if cmd.startswith('!' + shell + ' '):
                    exists = which(shell)
                    if exists:
                        if not exists.lower().endswith(_bash_win):
                            first_compatible_shell = shell
                    break

        shell_cmd = cmd[cmd.find(' '):].strip()

        if not shell_cmd:
            return cmd

        if first_compatible_shell:
            if first_compatible_shell == 'cmd':
                cmd_flag = '/C'
            return f'{first_compatible_shell} {cmd_flag} @({repr(shell_cmd)})'
        else:
            ret_val = "xontrib-sh: '" + cmd[1:cmd.find(" ")] + "'" \
                + " is not matching any known shell" \
                + " (or a matching shell isn't installed): " \
                + ", ".join(map(str, _shells))
            return f'echo @({repr(ret_val)})'

    return cmd
