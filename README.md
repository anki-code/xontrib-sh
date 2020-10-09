<p align="center">  
Paste and run commands from bash, zsh, fish in <a href="https://xon.sh">xonsh shell</a>.
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
after it and run. The command syntax will be tested in installed shells (bash, zsh, fish, sh) 
and the commands will be run in the first matching shell.

The commands will be executed in the environment that will be inherited from current
but if the commands modify the environment there will no changes in source xonsh environment.

## Use cases

### One line: brace expansion (bash syntax)
```bash
! echo 01.{05..10}
``` 
```
bash:
01.05 01.06 01.07 01.08 01.09 01.10
```

### Many lines: for loop (zsh syntax)
```zsh
! for x (1 2 3); do 
  echo $x; 
done

for x (4 5 6); do 
  echo $x; 
done
```
```
zsh:
1
2
3
4
5
6
```

### Set certain shell for all commands
```python
$XONTRIB_SH_SHELLS = ['zsh']
```

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
