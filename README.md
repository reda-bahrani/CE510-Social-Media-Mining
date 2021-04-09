# CE510 - Social Media Mining Project

## VPN Access
[Use VPN for a Secure Connection](https://www.it.northwestern.edu/oncampus/vpn/)

## Python Virtutal Environment
### EECS server login
- murphy.wot.eecs.northwestern.edu
- honlan.wot.eecs.northwestern.edu
- finagle.wot.eecs.northwestern.edu
- Contact TAs for login help and server list etc.


### Create environment
`virtualenv --system-site-packages <env_name>`

1. `--system-site-packages`: to include pre-installed packages from the current python installation.
2. `--no-site-packages`: don’t include pre-installed packages from the current python installation. (default)


### Install libraries
1. `pip install --upgrade pip`
2. `pip install tweepy`
3. Install packages needed for your project ...

## Twitter Application Account
[Twitter Developer Account](https://developer.twitter.com/en)

#### Login to `https://developer.twitter.com/`
![](/images/developer_account.png)

#### Navigate to Developer > Use cases > Academic research
![](/images/use_case_academic.png)

#### Apply for an account
![](/images/app_review.png)
![](/images/apps.png)

## Tweepy Python Library
- [Tweepy Documentation](http://docs.tweepy.org/en/latest/)
- [Very sophisticated code example!](https://github.com/reda-bahrani/CE510-Social-Media-Mining/blob/master/code/tweepy_example.py)
- [Four part tutorial](https://www.youtube.com/watch?v=wlnx-7cm4Gg)

## tmux
- [What is tmux?](https://medium.com/@tholex/what-is-tmux-and-why-would-you-want-it-for-frontend-development-e43e8f370ef2)
- [Tmux Tutorial](https://leimao.github.io/blog/Tmux-Tutorial/)

### Basic commands
1. To start a screen named ce510 `tmux new -t ce510`
2. To detach from a screen hit Ctrl+b then hit d
3. To list active screens `tmux ls` or `tmux list-sessions`
4. To reattach to a screen `tmux attach -t ce510`

## Screen
- [What is screen?](https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/)
- [How To Use Linux Screen](https://linuxize.com/post/how-to-use-linux-screen/)

### Basic commands
1. To start a screen named ce510 `screen -S ce510`
2. To detach from a screen hit Ctrl+a then hit d
3. To list active screens `screen -ls`
4. To reattach to a screen `screen -r ce510`
