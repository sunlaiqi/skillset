- [Expose a local web server to the internet](#expose-a-local-web-server-to-the-internet)
  - [ngrok](#ngrok)
  - [ngrok’s advanced features](#ngroks-advanced-features)
  - [PageKite](#pagekite)
  - [localtunnel](#localtunnel)
  - [boringproxy](#boringproxy)
  - [BrowserStack](#browserstack)
- [Port Forwarding](#port-forwarding)

# Expose a local web server to the internet

## ngrok

https://ngrok.com

`ngrok` allows you to expose a web server running on your local machine to the internet. Just tell ngrok what port your web server is listening on.

If you don't know what port your web server is listening on, it's probably port 80, the default for HTTP.

Example: Expose a web server on port 80 of your local machine to the internet
```bash
$ ngrok http 80
```

```
ngrok by @inconshreveable                                                                                                                (Ctrl+C to quit)
                                                                                                                                                         
Session Status                online                                                                                                                     
Session Expires               1 hour, 59 minutes                                                                                                         
Version                       2.3.40                                                                                                                     
Region                        United States (us)                                                                                                         
Web Interface                 http://127.0.0.1:4040                                                                                                      
Forwarding                    http://f0d6-2600-8801-2f24-1200-dddd-ef21-565d-28df.ngrok.io -> http://localhost:80                                        
Forwarding                    https://f0d6-2600-8801-2f24-1200-dddd-ef21-565d-28df.ngrok.io -> http://localhost:80                                       
                                                                                                                                                         
Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                
                              0       0       0.00    0.00    0.00    0.00                                                                               
```

You can check all requests details using built-in dashboard for ngrok at http://localhost:4040

You can even replay a request by clicking the **Replay** button on the right. That will re-run a request for you over the tunnel.

## ngrok’s advanced features

Password protection allows you to prevent random members of the public from accessing your site:
```bash
$ ngrok http -auth="username:password" 80
```
Custom subdomains are for when you don’t want to have to remember that randomly generated URL! If you sign up to a paid ngrok plan, you can reserve a subdomain so others can’t take it. The following allows you to view your localhost at `nogophersinmytunnel.ngrok.com`:
```bash
ngrok http -subdomain nogophersinmytunnel 80
```

Custom domains are for when you’d prefer to not have “ngrok” in your URL for the tunneled project. Paid plans allow you to use your own domains, rather than needing to use ngrok.com:
```bash
$ ngrok http -hostname="tunnel.yourdomain.com" 80
```

You can even tunnel to an IP address on your local network that otherwise would not be accessible to the outside world:
```bash
$ ngrok http 192.168.0.27:80
```
Or you can create a tunnel for other non-HTTP services:
```bash
$ ngrok tcp 22
```
There are a bunch of other things you can do, from running multiple tunnels at once to creating a config file to save all these settings for future use.

## PageKite

PageKite is a Python-based “dynamic tunnel based reverse proxy” that works on Windows, macOS, Linux, and even Android devices! It’s very similar to ngrok but has been around for quite a bit longer, and it appears quite a bit more battle-tested for a larger set of uses. They’ve even got it working with the Minecraft protocol to allow people to run a Minecraft server on their local machine.

You can sign up for a free trial for a month and 2.5GB of transfer quota. After that it has a pay-what-you-want system (a minimum of USD$4 a month, or free if you work on free open-source software). You do need to pay more to get more in this case though, with those paying larger amounts getting a larger quota, a longer term of service, custom subdomains, and so forth.

PageKite doesn’t appear to have a traffic inspector like ngrok, but it does have rather incredible features like a built-in firewall that blocks access to common attack targets like /wp-admin, /xampp, phpMyAdmin pages … and so on. It can be disabled if you’re okay with these being public.

They’ve even got a front-end relay server in Sydney, Australia, so this could potentially provide faster speeds for Australian developers.

How to use PageKite

Go to PageKite.net and download the version for your OS. For Windows users, you’ll need to make sure you have Python installed first. For macOS and Linux, you can use a simple cURL command to install it straight from your command line.

Once downloaded, run this command to run a tunnel to your localhost server. You choose a specific subdomain which you use each time (rather than the random allocation in ngrok). I’ve chosen hurrygetintothefancytunnel here:
```bash
$ pagekite.py 80 hurrygetintothefancytunnel.pagekite.me
```
On my Mac recently, I needed to run with python3 at the start, so try that if the above doesn’t work:
```bash
$ python3 pagekite.py 80 hurrygetintothefancytunnel.pagekite.me
```
It’ll run through and sign you up to the service if you’re not already signed up. Then you’ll have localhost up and running for the world!

Advanced Features of PageKite

PageKite has some more impressive additional features.

One example: there’s no need for a web server. If you don’t have a server running, it has an inbuilt web server that can run your static files like this:
```bash
$ pagekite.py /path/to/folder igotthattunnelvision.pagekite.me
```
Like ngrok, you can restrict access via password:
```bash
$ pagekite.py 80 terelekkayatuneli.pagekite.me +password/username=password
```
Or restrict access via IP addresses:
```bash
$ pagekite.py 80 arcadefirecamethroughmywindow.pagekite.me +ip/1.2.3.4=ok +ip/4.5.6=ok
```
As mentioned above, you can even run all of this on your phone. I installed an Android web server called kWS and then ran PageKite to expose it to the Web.

Just like ngrok, PageKite can do multiple tunnels at once, and it supports having your own domain, and supports setting up a configuration file for your tunnels. 

## localtunnel

localtunnel is a tunneling service that was initially built in Node but also has Go-based and C#/.NET clients.

How to use localtunnel

You can install it globally on your device like most npm packages:
```bash
$ npm install -g localtunnel
```
In order to start a tunnel to your localhost on port 80, you run this command:
```bash
$ lt --port 80
```
It’ll run just like ngrok and PageKite! It gives you a subdomain something like the one I was given: https://loud-ladybug-21.loca.lt.

Advanced features of localtunnel

Getting a free custom subdomain is totally doable here, as long as the subdomain hasn’t been taken. To use a custom subdomain, just run it with the --subdomain parameter:
```bash
$ lt --port 80 --subdomain platypusestunneltoo
```
One of the very handy features localtunnel provides is a Node API that allows you to generate localtunnels via JavaScript to use in your automated tests:
```js
const localtunnel = require('localtunnel');

(async () => {
  const tunnel = await localtunnel({ port: 3000 });

  // Your tunnel URL will appear as tunnel.url

  tunnel.on('close', () => {
    // Do something once the tunnel is closed
  });
})();
```

## boringproxy

boringproxy is a newer option that’s totally free and open source under the MIT license! Its main focus appears to be making it easier for people to self host websites on their computers. It comes as a single executable file that works as the server and the client in one. There’s an executable for a range of Linux systems and Windows. macOS is listed as “untested”. I haven’t been able to get it to work on my Mac personally, but if you have access to a Linux box or a Raspberry Pi, this just might be the solution for you. It’s all written in Go and is open for contributors.

Its features in brief:

- 100% free and open source under the MIT license
- can be completely self hosted
- has built-in reverse proxy
- supports custom domains/subdomains

How to Use boringproxy

The main steps are easiest followed on the boringproxy documentation, as it’s different for different platforms.

Overall, it involves:

- downloading the server instance via curl (for example, `curl -LO https://github.com/boringproxy/boringproxy/releases/download/v0.6.0/boringproxy-linux-x86_64`)
- chmoding the executable that was downloaded (for example, `chmod +x boringproxy-linux-x86_64`)
- setting up binding to ports 80 and 443 (for example, `sudo setcap cap_net_bind_service=+ep boringproxy-linux-x86_64`)
- setting up the executable on the client too

Advanced features of boringproxy

Auto HTTPS certificates are automatically managed for you via Let’s Encrypt. No need to stress about getting certificates for testing, as it happens behind the scenes.

Web interface for configuration is automatically set up to allow you to manage users, access tokens and tunnels.

You can tunnel web applications with ease. Self host web apps like Etherpad (shown in the video above), give them their own subdomain, and then you can access them from anywhere.

## BrowserStack

BrowserStack provides provides automated screenshots and virtual machines to test your website against a range of devices and browsers. If the reason you’re wanting to access localhost is for testing, BrowserStack might be of interest to you.

You can use the above methods to test localhost sites in the BrowserStack virtual machines, but it also has a browser extension for Chrome and Firefox allowing you to provide access to your localhost from their servers.

However, this functionality is only for the BrowserStack services and isn’t accessible to the general public. BrowserStack comes with a free trial, after which it will cost you a monthly fee to use the service. It’d be handy for cases where the sole reason you’re looking to access localhost is to do device testing.

How to use BrowserStack

Sign up for a trial at BrowserStack.com. They’ve actually got the process of local testing documented quite well on their website, so have a read of that if you’re interested in going this route.

In the end, though, it’ll allow you to test your localhost sites in virtual machines run over the Web like so:

Playing Favorites

After playing around with all of these options, my personal favorites would have to be ngrok and PageKite.

PageKite seems like the most multifaceted solution with a huge amount of potential. It’s been developed and extended to fit a range of uses over the years, making it a really impressive application!

ngrok is great too for its simplicity and the traffic inspector. It has more than enough features for most web developers looking to access their localhost from the Web.

# Port Forwarding







