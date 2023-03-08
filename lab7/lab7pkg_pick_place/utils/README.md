# CKCamera configuration for Linux

1. copy `90-ckusb.rules` to `udev` directory

   `cp 90-ckusb.rules /etc/udev/rules.d`

   or just run `install.sh`

   `./install.sh`

2. run `camera_test` in `tools`

3. if you failed to run instal.sh, you may consider following question.

   `chmod +x install.sh`

   or bin/sh^M: bad interpreter: No such file or directory

   `vi install.sh`

   `:set ff `

   if `fileformat=dos`, that is the problem

   `:set ff=unix` and `:wq` save and exit!

