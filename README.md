<p align="center">  
Paste and run commands from bash, fish, zsh in <a href="https://xon.sh">xonsh shell</a>.
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

Start a line with an exclamation point — `!` — then paste the sh-compatible commands 
after it and run. The commands syntax will be tested in installed shells 
and the commands will be run in the first matching shell. By default was set two shells: bash and sh. 
You can add other to the list of shells.

The commands will be executed in the environment that will be inherited from current
but if the commands modify the environment there will no changes in source xonsh environment.

To set the list of shells use environment variable before loading the xontrib:
```python
$XONTRIB_SH_SHELLS = ['bash', 'sh']  # default
xontrib load sh
```

## Use cases

### The main use case

The main use case of `xontrib-sh` is when you copy and paste the sh-commands from some article or instruction 
and this commands are environment agnostic and you want to run it without rewriting it on xonsh or run sh-shell. 

For example you've found [xxh local](https://github.com/xxh/xxh#using-xxh-inplace-without-ssh-connection) snippet:
```bash
XH=~/.xxh \
 && XD=https://github.com/xxh/xxh-portable/raw/master/result/xxh-portable-musl-alpine-Linux-x86_64.tar.gz \
 && mkdir -p $XH && cd $XH \
 && ( [[ -x $(command -v curl) ]] && curl -L $XD || wget -O- $XD ) | tar zxf - xxh \
 && echo 'Usage: ./xxh local [+s xonsh/zsh/fish/osquery/bash]'
```

It's bash and it's environment agnostic and you hesitate how xonsh will execute this. Just start with `!` and 
paste this commands. As result you've installed `xxh local` and stayed in xonsh.

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

## Known issues

If you want to use many shells the syntax checking is not determine the shell exactly right.
If you have bash and fish in the list of shells the short fish command may be determined as bash command.
As result the command will be failed. Use multi shell list carefully.

Bad example:
```python
$XONTRIB_SH_SHELLS = ['bash', 'fish']
xontrib load sh
# Run fish command:
! set -U EDITOR vim
# bash: line 0: set: -U: invalid option
```

If you have an idea how to improve the shell detection pull requests are welcome!

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
