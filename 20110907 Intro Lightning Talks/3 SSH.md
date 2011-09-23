# SSH

## Remote control

Using ssh we can remote control another computer.  Here I log in to an eecs student server: <server1>.  I can now run any shell commands on <server1> as if I was typing them in on a keyboard connected directly to the computer.

_At this point in the presentation, windows begin to spontaneously appear on my computer, which is projected to the room._

## (Un)remote control

It works the other way around, too.  I can give someone else access to my computer.  Here, my friend John is running commands on my computer and making dialog boxes come up.

## Public key authentication

    ssh-keygen

I just ran ssh-keygen, which generated a key pair.  The private key is secret, and I hold on to it.  It is mathematically linked to the public key, which I can distribute freely. 

    ssh-copy-id <server1>

I just sent the public key to <server1>.  Using my public key, eecslinab can generate mathematical “tests,” which my computer solves using my private key.  In this way, I can use my keypair to log me in, instead of my password.

## Security

Now lets say that you are using the wifi in a coffeeshop, and you are worried that someone is snooping on you as you surf.  

    sudo wireshark -i eth0 -k

ssh is encrypted, so you don't have to worry about anyone snooping on your keystrokes as they go down the wire.

## More features

Furthermore, you can send traffic over ssh.  I've configured a computer of mine, <server2>, with a proxy on port 3128.

I can then ssh into it using the command

    ssh -L 3128:localhost:3128 <server2>

If I configure my web browser to use the proxy `localhost` on port 3128, the data will be sent securely over the wire to <server2>, and <server2> will retrieve the webpage for me.  In high school, this was my go-to tool for accessing blacklisted websites.

ssh is brimming with features for moving traffic over secure tunnels.  Check out the manpage, or Google, for more info.

    man ssh
