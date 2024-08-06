## selfTool

selfTool is a command line tool that serves the requirement of executing sequential commands multiple times and recording the occurrence of specific keywords.

### # Usage

```bash=
pyhton run_tests.py <commands.txt> <keywords.txt> -n <repeat_time>
``` 

### # commands.txt

```text=
ls -l
ls -al
```

### # keywords.txt
```text= 
wxw
3 M
```

### # Result:

```text=
3 M: <occurrence time>
wxw: <occurrence time>
```


