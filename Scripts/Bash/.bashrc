#command to reset bash rc
#. ~/.bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# adds color to ls
alias ls='ls --color=auto'

# adds color to grep
alias grep='grep --color=auto'

# command prompt formatting 
PS1='[\u@\h \W]\$ '

# makes ssh work with xterm
[ "$TERM" = "xterm-kitty" ] && alias ssh="kitty +kitten ssh"

# removes sudo -s from .bash_history
HISTIGNORE='*sudo -S*'

# starship shell setup
eval "$(starship init bash)"

# command = timer 1m 1s
timer() {
    local M=$1; shift
    local S=$1; shift
    echo "timer set for $M $S"
    (sleep $M $S && notify-send "Time's up" && mpv /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga)
}