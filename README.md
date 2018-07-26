# declutter
Fast way to quickly organize cluttered files into approximate categories.  
I personally use this to declutter my desktop where I have a bad habit of dumping stuff.  
### Install from pip
`pip install -U declutter`
### Help
```
declutter

Usage:
    declutter
    declutter [[options] <args>...]...
    declutter -h | --help

Options:
    -h --help                            Show help message.
    --exclude_files <files>...           Exclude specific list of files from being decluttered.
    --exclude_ext <exts>...              Exclude these file extensions from being decluttered.
    --include_shortcuts                  Include shortcuts with extensions .url or .lnk to be decluttered.
Examples:
    declutter --exclude_files myfile.txt random.docx
    declutter --exclude_ext gif jpg
```
