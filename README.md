# eyeBeam

A tool based in python and functional similar as eyeWitness

## Installation

### Prerequisites

- [Install PhantomJS on Ubuntu / Kali linux 2018 v3][1]

The download file can be found in [here][2]

```
sudo apt-get update
sudo apt-get install build-essential chrpath libssl-dev libxft-dev
sudo apt-get install libfreetype6 libfreetype6-dev
sudo apt-get install libfontconfig1 libfontconfig1-dev

cd ~
export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
sudo tar xvjf $PHANTOM_JS.tar.bz2

sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

phantomjs --version
```

- [Install Heimdall][3]

Firstly, you need to install PhantomJS from above.

```
pip install heimdall
```

## Why eyeBeam
Simply the eyeWitness is not working well and lack of maintainence.

## To Do
Try multi-threads to increase speed faster.







[1]: https://gist.github.com/julionc/7476620
[2]: http://phantomjs.org/download.html
[3]: https://github.com/DistilledLtd/heimdall

