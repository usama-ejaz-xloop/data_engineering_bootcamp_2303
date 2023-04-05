# Linux refresher
Practice working with Linux shell and SSH.

- [Linux refresher](#linux-refresher)
  - [Bash tab completion](#bash-tab-completion)
  - [Bash history](#bash-history)
  - [Basic file management](#basic-file-management)
    - [pwd - prints the current working directory](#pwd---prints-the-current-working-directory)
    - [cd - change directory](#cd---change-directory)
    - [ls - display the contents of a directory](#ls---display-the-contents-of-a-directory)
    - [touch - create file](#touch---create-file)
    - [cp - copy](#cp---copy)
    - [mv - move/rename](#mv---moverename)
    - [rm - remove](#rm---remove)
    - [cat -  display file contents](#cat----display-file-contents)
  - [Pipe](#pipe)
    - [Pipe examples:](#pipe-examples)
  - [Redirection](#redirection)
    - [Output Redirection](#output-redirection)
    - [Input redirection](#input-redirection)
  - [Wildcards](#wildcards)
    - [Wildcard examples:](#wildcard-examples)
  - [Aliases](#aliases)
  - [Secure Shell (ssh)](#secure-shell-ssh)
  - [Remote Sync (rsync)](#remote-sync-rsync)
  - [screen](#screen)
  - [Cron](#cron)

## Bash tab completion
Bash completion is a functionality through which Bash helps users type their commands more quickly and easily. It does this by presenting possible options when users press the `[Tab]` key while typing a command. If multiple completions are possible, then `[Tab]` lists them all. Tab completion also works for variables and path names.

## Bash history
The bash shell remembers the commands you type and stores them in a history file. To scroll through your bash history use following keyboard shortcuts.

- `Up Arrow` or `Ctrl+P`: Go to the previous command in your history.
- `Down Arrow` or `Ctrl+N`: Go to the next command in your history.
- `Ctrl+R`: Recall the last command matching the characters you provide. Press this shortcut and start typing to search your bash history for a command.

You can print your entire bash history to the screen by running a single command:

    history


You can do search history following way (more on pipes and grep later):

    history | grep your_search

## Basic file management
### pwd - prints the current working directory
Both commands will display the current working directory.

    pwd
    echo $PWD

### cd - change directory
Relative path - change directory to subfolder of current working directory.

    cd dir/subdir

Absolute path - change directory to subfolder starting from root /.

    cd /dir/subdir

Change directory relative to home directory.

    cd ~/dir

Change directory relative to current working directory.

    cd ./dir

Change directory relative to parent directory.

    cd ../dir

Get back to your last working directory and prints the directory path.

    cd -

Two options to work with spaces in names.

    cd 'Dir name with space'
    cd Dir\ name\ with\ space

### ls - display the contents of a directory
Display content of current or provided directory.

    ls
    ls [dir]

List files in long format with human readable file sizes.

    ls -lh

List files including hidden files.

    ls -a

List the contents of the directory with its subdirectories.

    ls *

List all files and directories with their corresponding subdirectories down to the last file.

    ls -R

List files and sort by date and time (usually used to find recently edited files).

    ls -t

### touch - create file
Create a new empty file if the file with a filename does not exist. And if already exists then will change its modify time.

    touch filename

### cp - copy
Copy files and directories

    cp source/file destination/

Copy a directory, including all its files and subdirectories.

    cp -rf source destination

### mv - move/rename
It will rename the filename to new_filename.

    mv filename new_filename

It will remove the file filename from the source folder and would be creating a file with the same name and content in the destination folder.

    mv source/filename destination/

### rm - remove
It will remove the filename file from the directory.

    rm filename

It will remove the directory, including all its files and subdirectories.

    rm -rf

### cat -  display file contents
View content of a file.

    cat filename

Add line numbers.

    cat -n filename
## Pipe
The Pipe is a command in Linux that lets you use two or more commands such that output of one command serves as input to the next.

### Pipe examples:
View content of a file and pause after one page (one screen).

    cat somefile | less
    cat somefile | more

View top or bottom n lines of a file.

    cat somefile | head -5
    cat somefile | tail -3

Count the number of files.

    ls | wc -l

Print lines with searched text sort them and omit repeated lines.

    grep search_text file | sort | unique

List all running processes but display lines with word systemd only.

    ps -ef | grep systemd

## Redirection
Redirection is a feature in Linux that allows to change the standard input/output devices. The basic workflow of any Linux command is that it takes an input and give an output.
- The standard output (`stdout`) device is the screen.
- The standard input (`stdin`) device is the keyboard.

With redirection, the above standard input/output can be changed.

### Output Redirection
The `>` symbol is used for output (`stdout`) redirection. Output of any command, or piped commands may be redirected. Below example redirects directory listing output to `some_file`. If there is an existing file with the same name, the redirected command will delete the contents of that file and overwrite it.”

    ls -al > some_file

If you do not want a file to be overwritten but want to add more content to an existing file, then you should use `>>` operator.

    ls -al|grep search_text >> some_file

Outputs can be redirected also to devices, not just files. This redirects find permission errors (2 stands for `stderr` output) to `/dev/null` device (just hide them). Following find search for all files (`-type f`) starting from `/`, its output is piped to grep which limits output to lines matching `search_text`.

    find / -type f 2>/dev/null |grep search_text

### Input redirection
The `<` symbol is used for input(STDIN) redirection. In this example some_file is redirected to cat input.

    cat < some_file

## Wildcards
Wildcards are symbols or special characters that represent other characters. You can use them with any command such as `ls` or `rm` command to list or remove files matching a given criteria, receptively.
- An asterisk (`*`) – matches one or more occurrences of any character, including no character.
- Question mark (`?`) – represents or matches a single occurrence of any character.
- Bracketed characters (`[ ]`) – matches any occurrence of character enclosed in the square brackets. It is possible to use different types of characters (alphanumeric characters): numbers, letters, other special characters etc.

### Wildcard examples:
List all files with names starting with k.

    ls -l k*

List all `.tr` files

    ls -l *.tr

List all files with tar in name (.tar but also .tar.gz, .tar.bz)

    ls -l *tar*

List all files starting with any of letters in range from a to o:

    ls -l [a-o]*

## Aliases
An bash shell alias is nothing but the shortcut to commands. The alias command allows the user to launch any command or group of commands (including options and filenames) by entering a single word. You can add user-defined aliases to `~/.bash_aliases` file (create it if not existing as it is included by `~/.bashrc`). To display a list of all defined aliases use:

    alias

Use following syntax to create new ones:

    alias name=value
    alias name='command'
    alias name='command arg1 arg2'
    alias name='/path/to/script'
    alias name='/path/to/script.pl arg1'

## Secure Shell (ssh)
SSH is a protocol used to securely log onto remote systems. It is the most common way to access remote Linux servers.
The most straightforward form of the command is:

    ssh remote_host

This command assumes that your username on the remote system is the same as your username on your local system.
If your username is different on the remote system, you can specify it:

    ssh remote_username@remote_host

While it is helpful to be able to log in to a remote system using passwords, it is faster and more secure to set up key-based authentication.
To Create SSH Key (AWS supports RSA with 2048 and 4096 lengths):

    ssh-keygen -t rsa -b 2048

To Transfer Your Public Key to the Server:

    ssh-copy-id remote_host

This will start an SSH session. After you enter your password, it will copy your public key to the server’s authorized keys file, which will allow you to log in without the password next time.
More on AWS and keys here:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

## Remote Sync (rsync)
`rsync` is used for copying and synchronizing files and directories remotely as well as locally. It supports copying links, devices, owners, groups, and permissions. It’s faster than `scp` because rsync uses a remote-update protocol which allows transferring just the differences between two sets of files.
The basic syntax of the rsync command

    rsync options source destination

Some common options used with rsync commands
- `-v` : verbose
- `-r` : copies data recursively (but don’t preserve timestamps and permission while transferring data
- `-a` : archive mode, which allows copying files recursively and it also preserves symbolic links, file permissions, user & group ownership, and timestamps
- `-z` : compress file data
- `-h` : human-readable, output numbers in a human-readable format

Following example will sync a directory from a local machine to a remote machine.

    rsync -avzh /home/notebooks user@remote_host:/backup/

## screen
`screen` command in Linux provides the ability to launch and use multiple shell sessions from a single ssh session. When a process is started with `screen`, the process can be detached from session & then can reattach the session at a later time. When the session is detached, the process that was originally started from the screen is still running and managed by the screen itself.
To install the `screen` command:

    sudo apt-get install screen

To start a new window within the screen and also gives a name to the window:

    screen -S window_name

It creates a session which is identified by that name. The name can be used to reattach screen at a later stage. To detach from window while running some command press `Ctrl-A` and `d`.
To see available screens run:

    screen -ls

To reattach a screen session:

    screen -r window_name

## Cron
`Cron` is a system daemon used to execute tasks at designated times. A `crontab` file is a simple text file containing a list of commands meant to be run at specified times. The commands in the `crontab` file (and their run times) are checked by the `cron` daemon, which executes them in the system background. Each user (including `root`) has a `crontab` file. The `cron` daemon checks a user's `crontab` file regardless of whether the user is actually logged into the system or not.
To schedule a job, open up your `crontab` for editing and add a task written in the form of a `cron` expression. The syntax for `cron` expressions can be broken down into two elements: the schedule and the command to run. The five time-and-date fields are as follows: minute (0-59), hour (0-23, 0 = midnight), day (1-31), month (1-12), weekday (0-6, 0 = Sunday). An asterisk (`*`) can be used so that every instance (every hour, every weekday, every month, etc.) of a time period is used. Together with a command to run, tasks scheduled in a `crontab` are structured like the following:

    minute hour day_of_month month day_of_week command_to_run

To start editing `crontab`:

    crontab -e

To list existing `crontab`:

    crontab -l

Examples:

    * * * * * echo ‘Run this command every minute’ >> /directory/path/file.log
    45 04 * * * echo ‘Run this command every morning at 4:45am’ >> /directory/path/file.log
    30 17 * * 1 echo ‘Run this command every Monday at 5:30pm’ >> /directory/path/file.log
    */15 * * * * echo ‘Run this command every 15 minutes’ >> /directory/path/file.log

