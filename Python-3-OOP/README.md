to print all files in folder
```sh
find . -type f -exec echo "=== {} ===" \; -exec cat {} \;
```
