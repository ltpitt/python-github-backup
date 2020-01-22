# GitHub Backup
Python script to backup all GitHub repositories for the specified user.  
It will also take care of rotation of backups and of their retention period.

## Requirements
* Python: if you have Linux or Mac you should be good to go and you should skip to the next step, if you're on Windows and you like lazy'n'great you can install Python with a couple clicks from: http://ninite.com
* Python Pip: here are [installation instructions](https://pip.pypa.io/en/stable/installing/).  

## How to install

Once Python and Python Pip are installed:

    $ git clone https://github.com/ltpitt/python-github-backup.git
    $ cd python-github-backup
    $ pip install .

## Usage

To use it:

    $ github-backup --help

Output:   
```bash
Usage: github-backup [OPTIONS]

  GitHub Backup will backup all repositories for the specified user with
  options for retention

Options:
  -r, --retention-period INTEGER  Maximum number of full backups your want to
                                  keep, expressed in days (2 will keep, for
                                  example, today's and yesterday's backups and
                                  delete the older ones)
  -u, --username TEXT             Specify a GitHub username  [required]
  -p, --backup-folder-path TEXT   Specify the backup folder path  [required]
  --help                          Show this message and exit.
```

## How to schedule automatic script execution
* If you have Windows: https://technet.microsoft.com/en-us/library/cc748993(v=ws.11).aspx
* If you have Linux or Mac: https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/

### Contribution guidelines ###

* If you have any idea or suggestion contact directly the Repo Owner

### Who do I talk to? ###

* ltpitt: Repo Owner
