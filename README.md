<p align="center">  
Paste and run commands from bash, fish, zsh, tcsh in <a href="https://xon.sh">xonsh shell</a>.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and stay tuned.
</p>


## Install
```bash
xpip install -U xontrib-sh
echo 'xontrib load sh' >> ~/.xonshrc
# Reload xonsh
```

## Usage

There are two ways to invoke an sh-compatible command:

####1. With a shell detected automatically

Start the line with 

`!` ` ` (exclamation mark with space)

then paste the sh-compatible commands after it and run. 
The commands syntax will be tested in the shells from list (if installed) and the commands will be run in 
the first matching shell. By default list of shells contains bash and sh. 

The commands will be executed in the environment that will be inherited from current but if the commands modify 
the environment there will no changes in source xonsh environment.

To set the list of shells use environment variable before loading the xontrib:
```python
$XONTRIB_SH_SHELLS = ['bash', 'sh']  # default
xontrib load sh
```

####2. With a shell specified manually

Same as above, but add the required shell name between the exclamation mark and space, either:

`!bash` ` ` the full shell name OR

`!b` ` ` only its first letter

then paste sh-compatible commands after it and run.

Each shell name (or only its first letter, or both, depending on the value of the two environment variables listed below) from the configured list will be matched against the full/short name specified in the prefix, and the commands will be run in the first matching shell (if installed).

```python
# Given '!b ', match 'b' to the first letter of each shell in $XONTRIB_SH_SHELLS (use the first shell starting with 'b')
$XONTRIB_SH_USEFIRST = True # default True
# Given '!bash ', match 'bash' to the full name of each shell in $XONTRIB_SH_SHELLS
$XONTRIB_SH_USEFULL  = True # default True
```

## The main use case

The main use case of `xontrib-sh` is when you copy and paste the sh-commands from some article or instruction 
and this commands are environment agnostic and you want to run it without rewriting it on xonsh or run sh-shell. 

For example you've found snippet of bash commands that check existing of `curl`:
```bash
TMP=/tmp && cd $TMP && ( [[ -x $(command -v curl) ]] && echo "Yes" || echo "No" )  
```

You hesitate how xonsh will execute this and you're absolutely right there will be syntax error. 
To run this just start with `! ` or `!b ` or `!bash ` and paste the commands. As result you'll see the right message.

## Examples

### Bash brace expansion
```bash
! echo 01.{05..10}
    #OR
!b echo 01.{05..10}    # unless $XONTRIB_SH_MATCHFIRST = False (default is True)
    #OR
!bash echo 01.{05..10} # unless $XONTRIB_SH_MATCHFULL  = False (default is True)
``` 
```
bash:
01.05 01.06 01.07 01.08 01.09 01.10
```

### Loop
```bash
! for i in 1 2 3
do
   echo $i
done
```
```
bash:
1
2
3
```

### Use environment variables to pass values from xonsh to sh
```python
$ENV = 'hello'
! echo $ENV!
```
```
bash:
hello!
```

## Known issues

#### Determining the shell on short command

In case of usage many different shells the detection of the shell works perfect when the commands contain shell-specific syntax.
But if you run the short command that could be valid in all shells the first matched shell will be chosen but it's could be wrong. 
 
For example you have bash and fish in the list of shells. The short fish command may be determined as bash command.
As result the command will be failed:
```python
$XONTRIB_SH_SHELLS = ['bash', 'fish']
xontrib load sh
# Run fish command:
! set -U EDITOR vim
# bash: line 0: set: -U: invalid option
```
However, the command with the fish shell __specified explicitly__ will succeed
```python
# Run fish command in a manually set fish shell
# requires option '$XONTRIB_SH_MATCHFULL = True', which is the default value
!fish set -U EDITOR vim
```

Use shells list carefully! If you have an idea how to improve the shell detection pull requests are welcome!

#### Why it's better than [xonsh subprocess macros](https://xon.sh/tutorial_macros.html#subprocess-macros)?

Xonsh subprocess macros is not supporting multiline commands and require more keystrokes.


## Links 
* This package is the part of [ergopack](https://github.com/anki-code/xontrib-ergopack) - the pack of ergonomic xontribs.
* This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
