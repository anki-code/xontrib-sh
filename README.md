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

Start the line with `! ` (exclamation point with space) then paste the sh-compatible commands after it and run. 
The commands syntax will be tested in the shells from list (if installed) and the commands will be run in 
the first matching shell. By default list of shells contains bash and sh. 

The commands will be executed in the environment that will be inherited from current but if the commands modify 
the environment there will no changes in source xonsh environment.

To set the list of shells use environment variable before loading the xontrib:
```python
$XONTRIB_SH_SHELLS = ['bash', 'sh']  # default
xontrib load sh
```

## The main use case

The main use case of `xontrib-sh` is when you copy and paste the sh-commands from some article or instruction 
and this commands are environment agnostic and you want to run it without rewriting it on xonsh or run sh-shell. 

For example you've found snippet of bash commands that checks existing of `curl`:
```bash
TMP=/tmp && cd $TMP && ( [[ -x $(command -v curl) ]] && echo "Curl! :)" || echo "No curl! :(" )  
```

You hesitate how xonsh will execute this and you're absolutely right there will be syntax error. 
To run this just start with `! ` and paste the commands. As result you'll see the right message.

## Examples

### One line: brace expansion
```bash
! echo 01.{05..10}
``` 
```
bash:
01.05 01.06 01.07 01.08 01.09 01.10
```

### Many lines: for loop
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

Use shells list carefully! If you have an idea how to improve the shell detection pull requests are welcome!

## Links 
* This package is the part of [ergopack](https://github.com/anki-code/xontrib-ergopack) - the pack of ergonomic xontribs.
* This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
