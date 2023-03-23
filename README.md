# The script for removing files and folders recursively.


### Script arguments
```
| Name                         | Description                                     |
|------------------------------|-------------------------------------------------|
| --path                       | Folder to check                                 |
|------------------------------|-------------------------------------------------|
| --key-to-delete              | Folders or files to delete                      |
|------------------------------|-------------------------------------------------|
| --wildcard                   | Use wildcard? (f.e. .terraform*) default: False |
|------------------------------|-------------------------------------------------|
```

To delete all folders node_modules from /Users/eugeneroslyakov/Desktop/REPO folder
```
python3 remove_all_terraform_cache.py --path /Users/eugeneroslyakov/Desktop/REPO --key-to-delete node_modules
```

To delete all folders .terraform* .terragrunt* from /Users/eugeneroslyakov/Desktop/REPO folder
```
python3 remove_all_terraform_cache.py --path /Users/eugeneroslyakov/Desktop/REPO --key-to-delete node_modules .terraform .terragrunt --wildcard
```