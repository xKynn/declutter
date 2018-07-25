"""
declutter

Usage:
    declutter
    declutter [options] <args>...
    declutter -h | --help

Options:
    -h --help                         Show this message.
    --exclude_files <files>...           Exclude specific list of files from being decluttered.
    --exclude_ext <exts>...              Exclude these file extensions from being decluttered.
"""
examples = """
Examples:
    declutter --exclude_files myfile.txt random.docx
    declutter --exclude_ext gif jpg
"""

import argparse
import sys

from docopt import docopt
from os import listdir
from os.path import isfile, join
from pathlib import Path
from shutil import move

extensions = {
    ('aif', 'cda', 'mid', 'midi','mp3', 'mpa', 'ogg', 'wav', 'wma', 'wpl'): "Music",
    ('7z', 'arj', 'deb', 'pkg', 'rar', 'rpm', 'tar', 'gz', 'z', 'zip'): "Compressed",
    ('bin', 'dmg', 'iso', 'toast', 'vcd'): "Disc Images",
    ('csv', 'dat', 'db', 'dbf', 'log', 'mdb', 'sav' , 'sql', 'tar', 'xml'): "Data",
    ('apk', 'bat', 'bin', 'cgi', 'pl', 'com', 'exe', 'gadget', 'jar', 'wsf'): "Executables",
    ('lnk', 'url'): "Shortcuts",
    ('ai', 'bmp', 'gif', 'ico', 'jpeg', 'jpg', 'png', 'ps', 'psd', 'svg', 'tif', 'tiff'): "Images",
    ('asp', 'aspx', 'css', 'html', 'htm', 'js', 'php', 'rss', 'xhtml'): "Web",
    ('ppt' ,'pptx', 'pps', 'xlr', 'xls', 'xlsx', 'doc', 'docx', 'pdf', 'rtf', 'txt'): "Documents",
    ('c', 'class', 'cpp', 'cs', 'h', 'java', 'sh', 'swift', 'vb', 'py'): "Coding",
    ('3g2', '3gp', 'avi', 'flv', 'h264', 'm4v', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg', 'rm', 'swf', 'vob',
     'wmv'): "Videos"
    }

def main():
    parser = argparse.ArgumentParser(description='Declutter a folder and move files with common extensions to'
                                     'categorized folders.', epilog=examples)
    parser.add_argument('--exclude_files', nargs='+', help='Exclude specific list of files from being decluttered.')
    parser.add_argument('--exclude_ext', nargs='+', help='Exclude these file extensions from being decluttered.')
    parser.add_argument('--include_shortcuts', action='store_true', help="Include windows or web shortcuts for being decluttered.")
    args = parser.parse_args(sys.argv[1:])
    files = [f for f in listdir() if isfile(join('', f))]
    if args.exclude_files:
        ex_files = ', '.join(args.exclude_files)
    else:
        ex_files = "None"
    if args.exclude_ext:
        ex_ext = ', '.join(args.exclude_ext)
    else:
        ex_ext = "None"
    while 1:
        confirm = input("Are you sure you want to declutter current directory with options?:\n" \
                        f"Exclude Files:  {ex_files}\nExclude Extensions: {ex_ext}\nInclude Shortcuts?: {args.include_shortcuts}\nConfirm (y/n)\n")
        if confirm in ['y', 'n']:
            if confirm == 'y':
                break
            else:
                return
    for file in files:
        ext = '.'.join(file.split('.')[1:])
        if args.exclude_files and file in args.exclude_files:
            continue
        elif args.exclude_ext and ext in args.exclude_ext:
            continue
        elif not args.include_shortcuts and ext in ('lnk', 'url'):
            continue
        name = file.split('.')[0]
        cat = None
        for k, v in extensions.items():
            if file.split('.')[-1].lower() in k:
                cat = v
                break
        if not cat:
            continue
        cat_dir = Path().cwd() / cat
        if not cat_dir.is_dir():
            cat_dir.mkdir()
        num_append = 0
        while 1:
            dest_file = cat_dir / (name + (f" ({num_append})" if num_append else "") + '.' + ext)
            print(dest_file)
            if dest_file.is_file():
                num_append += 1
                continue
            break
        move((Path().cwd() / file).as_posix(), dest_file.as_posix())

if __name__ == '__main__':
    main()