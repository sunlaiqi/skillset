


Learn Linux 101: Install a boot manager

Introducing GRUB, GRUB 2, and LILO

https://developer.ibm.com/tutorials/l-lpic1-102-2/


# Boot managers

A boot manager or boot loader is the intermediate piece of code that helps the hardware and firmware of your system load an operating system for you. 

This tutorial discusses the PC boot process and the three main boot loaders that are used in Linux: GRUB, GRUB 2, and LILO with MBR formatted disks. 

The original GRUB, now called GRUB-Legacy, is no longer in active development and has largely been replaced by the newer GRUB 2. Even commercial distributions such as Red Hat Enterprise Linux and SUSE Linux Enterprise Server switched to Grub 2 in 2014. Development of Lilo is scheduled to cease at the end of 2015.

This tutorial focuses on booting with a traditional BIOS and disks formatted with a **Master Boot Record (MBR)**. It also covers some basic information on Extensible Unified Firmware Interface (UEFI) and its associated GUID Partition Table (GPT) and booting issues you might find with these,

# Boot process overview

Code called **BIOS** (for _B_asic _I_nput _O_utput _S_ervice) is stored in non-volatile memory such as a ROM, EEPROM, or flash memory. When the PC is turned on or rebooted, this code is executed. Usually it performs a power-on self test (POST) to check the machine. Finally, it loads the first sector from the **master boot record (MBR)** on the boot drive.

the MBR also contains the partition table, so the amount of executable code in the MBR is less than 512 bytes (446 bytes for MBR, 64 bytes for partition table, 2 bytes for signatures), which is not very much code. Every disk, even a floppy, contains executable code in its MBR, even if the code is only enough to put out a message such as “Non-bootable disk in drive A:”. This code that is loaded by BIOS from this first sector is called the first stage boot loader or the stage 1 boot loader.

The standard hard drive MBR used by MS DOS, PC DOS, and Windows operating systems checks the partition table to find a primary partition on the boot drive that is marked as active, loads the first sector from that partition, and passes control to the beginning of the loaded code. This new piece of code is also known as the partition boot record. The partition boot record is actually another stage 1 boot loader, but this one has just enough intelligence to load a set of blocks from the partition. The code in this new set of blocks is called the stage 2 boot loader. As used by MS-DOS and PC-DOS, the stage 2 loader proceeds directly to load the rest of operating system. This is how your operating system pulls itself up by its bootstraps until it is up and running.


## A smart boot loader

A program that can reside on an operating system partition and is invoked either by the partition boot record of an active partition or by the master boot record. Some common Linux boot loaders are:

- LILO, the LInux LOader
- GRUB, the GRand Unified Boot loader (now referred to as GRUB Legacy)
- GRUB2, a newer boot loader that is installed in many common distributions
- Syslinux, a group of lightweight boot loaders for MS-DOS FAT filesystems (SYSLINUX), network booting (PXELINUX), bootable “El Torito” CD-ROMs (ISOLINUX), and Linux ext2/ext3/ext4 or btrfs filesystems (EXTLINUX)

# Chain loading

When a boot manager gets control, one thing that it can load is another boot manager. This is called chain loading, and it most frequently occurs when the boot manager that is located in the master boot record (MBR) loads the boot loader that is in a partition boot record. 

For example, you might use GRUB in one partition to launch the GRUB boot loader in another partition’s boot record to start the Linux system in that partition. This is not common, but it illustrates the possibilities.

# Linux boot loaders

This tutorial focuses on GRUB, GRUB 2, and LILO because these are the boot loaders included with most Linux distributions.

For the rest of this tutorial, assume GRUB means GRUB Legacy, unless the context specifically implies GRUB 2.

A new version of LILO called ELILO (which is designed for booting systems that use Intel’s Extensible Firmware Interface, or EFI, rather than BIOS) is also available.

# GRUB (GRand Unified Boot loader)

You can install GRUB into the MBR of your bootable hard drive or into the partition boot record of a partition. You can also install it on removable devices such as floppy disks, CDs, or USB keys. 

Note: Most GRUB examples in this tutorial use CentOS 6.

During Linux installation, you often specify your choice of boot manager. If you choose LILO, then you might not have GRUB installed. If you do not have GRUB installed and it is available for your distribution, then you need to install the package for it. This tutorial assumes that you already have the GRUB package installed.

GRUB (Legacy) has a configuration file that is usually stored in /boot/grub/grub.conf. If your file system supports symbolic links, as most Linux file systems do, you probably have /boot/grub/menu.lst as a symbolic link to /boot/grub/grub.conf.

The grub command (/sbin/grub, or, on some systems, /usr/sbin/grub) is a small but reasonably powerful shell that supports several commands for installing GRUB, booting systems, locating and displaying configuration files, and similar tasks.

This shell shares much code with the second stage GRUB boot loader, so it is useful to learn about GRUB without having to boot to a second stage GRUB environment. The GRUB stage 2 runs either in menu mode, so that you can choose an operating system from a menu, or in command mode, where you specify individual commands to load a system. There are also several other commands, such as grub-install, that use the grub shell and help automate tasks such as installing GRUB.

## Full-size Grub Config File

Listing 1: /boot/grub/menu.lst GRUB configuration example

```

# grub.conf generated by anaconda
#
# You do not have to rerun grub after making changes to this file
# NOTICE:  You do not have a /boot partition.  This means that
#          all kernel and initrd paths are relative to /, eg.
#          root (hd0,5)
#          kernel /boot/vmlinuz-version ro root=/dev/hda6
#          initrd /boot/initrd-version.img
#boot=/dev/hda
default=0
timeout=60
splashimage=(hd0,0)/boot/grub/splash.xpm.gz
#password --md5 $1$y.uQRs1W$Sqs30hDB3GtE957PoiDWO.

title Fedora 22 64-bit (sda5)
   root (hd0,4)
      kernel /boot/grub2/i386-pc/core.img

title Fedora 18 64-bit (sda7)
   root (hd0,6)
       kernel /boot/grub2/i386-pc/core.img

title CentOS 6 64-bit (sda11)
       root (hd0,10)
       configfile /boot/grub/menu.lst

title CentOS (2.6.32-504.23.4.el6.x86_64)
    root (hd0,10)
    kernel /boot/vmlinuz-2.6.32-504.23.4.el6.x86_64 ro \
           root=UUID=2f60a3b4-ef6c-4d4c-9ef4-50d7f75124a2 rd_NO_LUKS rd_NO_LVM \
          LANG=en_US.UTF-8 rd_NO_MD SYSFONT=latarcyrheb-sun16 crashkernel=128M \
           KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM rhgb quiet
    initrd /boot/initramfs-2.6.32-504.23.4.el6.x86_64.img

title Fedora 20 64-bit (sda10)
    root (hd0,9)
        configfile /boot/grub/menu.lst

title Ubuntu 12.04-LTS 64-bit (sda9)
    root (hd0,8)
        kernel /boot/grub/core.img

title Ubuntu 14.04 32-bit (sda12)
    root (hd0,11)
        kernel /boot/grub/core.img

title Slackware 13.37 64-bit (sda6)
    root (hd0,5)
chainloader +1
        boot

title Open SUSE 11.4 64-bit (sda8)
   root (hd0,7)
        configfile /boot/grub/menu.lst

title Windows Example
    rootnoverify (hd0,0)
    chainloader +1
#####
```

The first set of options in Listing 1 control how GRUB operates. For GRUB, these are called menu commands, and they must appear before other commands. The remaining sections give per-image options for the operating systems that you want to allow GRUB to boot. “Title” is considered a menu command. Each instance of title is followed by one or more general or menu entry commands.

The menu commands that apply to all other sections in Listing 1 are:

**#**

Any line starting with a `#` is a comment and is ignored by GRUB. This particular configuration file was originally generated by anaconda, the Red Hat installer. The comments often serve as an aid to the system upgrade program so that you can keep your GRUB configuration current with upgraded kernels.

**default**

Specifies which system to load if the user does not make a choice within a timeout. In Listing 1, default=0 means to load the first entry. Remember that GRUB counts from 0 rather than 1. If not specified, then the default is to boot the first entry, entry number 0.

**timeout**

Specifies a timeout in seconds before booting the default entry. Note that LILO uses tenths of a second for timeouts, while GRUB uses whole seconds.

**splashimage**

Specifies the background, or splash, image to be displayed with the boot menu. GRUB Legacy refers to the first hard drive as (hd0) and the first partition on that drive as (hd0,0), so the specification of splashimage=(hd0,0)/boot/grub/splash.xpm.gz means to use the file /boot/grub/splash.xpm.gz located on partition 1 of the first hard drive. Remember to count from 0. The image is an XPM file compressed with gzip. Support for splashimage is a patch that might or might not be included in your distribution.

**password**

Specifies a password that you must enter before you can unlock the menu and either edit a configuration line or enter GRUB commands. The password can be in clear text. GRUB also permits passwords to be stored as an MD5 digest, as in the commented out example in Listing 1. This is somewhat more secure, and most administrators set a password. Without a password, you have complete access to the GRUB command line.

Listing 1 shows a CentOS kernel, /boot/vmlinuz-2.6.32-504.23.4.el6.x86_64, on /dev/sda11 (hd0,10), plus several systems that are configured to chain load. Listing 1 also has examples of loading GRUB 2 via /boot/grub2/i386-pc/core.img and an example of a typical Windows XP chain loading entry, although this system does not actually have Windows installed. The commands used in these sections are:

**title**

Is a descriptive title that is shown as the menu item when Grub boots. You use the arrow keys to move up and down through the title list and then press Enter to select a particular entry.

**root**

Specifies the partition that will be booted. As with splashimage, remember that counting starts at 0, so the first Red Hat system that is specified as root (hd0,6) is actually on partition 7 of the first hard drive (/dev/hda7 in this case), while the first Ubuntu system, which is specified as root (hd1,10), is on the second hard drive (/dev/hdb11). GRUB attempts to mount this partition to check it and provide values to the booted operating system in some cases.

**kernel**

Specifies the kernel image to be loaded and any required kernel parameters. A kernel value like /boot/grub2/i386-pc/core.img usually means loading a GRUB 2 boot loader from the named root partition.

**initrd**

Is the name of the initial RAM disk, which contains modules needed by the kernel before your file systems are mounted.

**savedefault**

Is not used in this example. If the menu command default=saved is specified and the savedefault command is specified for an operating system, then booting that operating system causes it to become the default until another operating system with savedefault specified is booted. In Listing 1, the specification of default=0 overrides any saved default.

**boot**

Is an optional parameter that instructs GRUB to boot the selected operating system. This is the default action when all commands for a selection have been processed.

**lock**

Is not used in Listing 1. This does not boot the specified entry until a password is entered. If you use this, then you should also specify a password in the initial options; otherwise, a user can edit out your lock option and boot the system or add “single” to one of the other entries. It is possible to specify a different password for individual entries if you want.

**rootnoverify**

Is similar to root, except that GRUB does not attempt to mount the file system or verify its parameters. This is usually used for file systems such as NTFS that are not supported by GRUB. You might also use this if you want GRUB to load the master boot record on a hard drive (for example, to access a different configuration file or to reload your previous boot loader).

**chainloader**

Specifies that another file will be loaded as a stage 1 file. The value “+1” is equivalent to 0+1, which means to load one sector starting at sector 0; that is, load the first sector from the device specified by root or rootnoverify.

**configfile**

Specifies that the running copy of GRUB replaces its configuration file with one loaded from the target location. For this to work, it is advisable that the version of GRUB that is loading the new configfile is as current as the version that built it.

## Basic Grub Config File

Before you learn how to deal with such a large GRUB configuration file, let’s drop back to a smaller and simpler example. I use the file that CentOS 6 built for me when I installed it on /dev/sda11. This is shown in Listing 2. Again, we have used a backslash () to show where we broke long kernel lines for publication.

Listing 2: Basic GRUB configuration built by CentOS 6

```

# grub.conf generated by anaconda
#
# You do not have to rerun grub after making changes to this file
# NOTICE:  You do not have a /boot partition.  This means that
#          all kernel and initrd paths are relative to /, eg.
#          root (hd0,10)
#          kernel /boot/vmlinuz-version ro root=/dev/sdd11
#          initrd /boot/initrd-[generic-]version.img
#boot=/dev/sdd11
default=0
timeout=5
splashimage=(hd0,10)/boot/grub/splash.xpm.gz
hiddenmenu
title CentOS (2.6.32-504.23.4.el6.x86_64)
  root (hd0,10)
    kernel /boot/vmlinuz-2.6.32-504.23.4.el6.x86_64 ro \
           root=UUID=2f60a3b4-ef6c-4d4c-9ef4-50d7f75124a2 rd_NO_LUKS rd_NO_LVM \
           LANG=en_US.UTF-8 rd_NO_MD SYSFONT=latarcyrheb-sun16 crashkernel=128M \
           KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM rhgb quiet
    initrd /boot/initramfs-2.6.32-504.23.4.el6.x86_64.img
title CentOS 6 (2.6.32-504.el6.x86_64)
    root (hd0,10)
    kernel /boot/vmlinuz-2.6.32-504.el6.x86_64 ro \
           root=UUID=2f60a3b4-ef6c-4d4c-9ef4-50d7f75124a2 rd_NO_LUKS rd_NO_LVM \
           LANG=en_US.UTF-8 rd_NO_MD SYSFONT=latarcyrheb-sun16 crashkernel=128M \
          KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM rhgb quiet
    initrd /boot/initramfs-2.6.32-504.el6.x86_64.img
title Other
   rootnoverify (hd0,0)
   chainloader +1
```

Notice the command **hiddenmenu** that you did not see earlier. This causes GRUB to not display a menu, but rather boot the default entry as soon as the timeout expires. In our case this means the first entry (default=0) will be booted in 5 seconds (timeout=5). If you press **Enter** during this time, the menu will be displayed.

## Install Grub Config File

Once you have a GRUB configuration file, you need to install it, or preferably test it.

I’ll install GRUB in the partition boot record of the partition containing my CentOS distribution. I use the `grub-install` command and specify the device where the **512-byte stage1 boot loader** should go. In my example, that’s /dev/sda11 or (hd0,10) using GRUB notation. 

See Listing 3. You need to have root authority to write the partition boot record. If you have added or deleted devices you might have to remove your /boot/grub/device.map file and **allow grub-install to rebuild** is as shown in our example. This won’t happen often, but if `grub-install` throws some odd error that you don’t understand, you might find deleting the `device.map` file helpful.

Listing 3. Install GRUB Legacy in a partition boot record

```

[root@attic4-cent ~]# rm /boot/grub/device.map 
rm: remove regular file `/boot/grub/device.map'? y
[root@attic4-cent ~]# grub-install /dev/sda11
Probing devices to guess BIOS drives. This might take a long time.
Installation finished. No error reported.
This is the contents of the device map /boot/grub/device.map.
Check if this is correct or not. If any of the lines is incorrect,
fix it and re-run the script `grub-install'.

(fd0)   /dev/fd0
(hd0)   /dev/sda
(hd1)   /dev/sdb
(hd2)   /dev/sdc
(hd3)   /dev/sdd
```
As you already learned the standard DOS MBR can’t boot a logical partition, so you’ll need something else to get this system booted. One option would be to install GRUB in the MBR by doing `grub-install /dev/sda` which would also install GRUB in the MBR of our disk (/dev/sda). I’ll also show you how to do it with GRUB 2 in a moment, but before you commit to either approach step, you might want to test out your setup using a GRUB boot CD.


# GRUB 2

GRUB 2 is the successor to GRUB. It was rewritten from scratch to make it significantly more modular and portable. It targets different architectures and boot methods and has many new features, including the ability to handle UEFI firmware and GPT formatted drives. 

Note: Most GRUB 2 examples in this tutorial use Fedora 22 or Ubuntu 15.

The first thing you might notice about GRUB 2 is that **it does not install as a partition boot loader**. If you tell a Linux installer to install GRUB in a partition, that partition is not bootable by chain loading. GRUB 2 must be rebuilt when you update your system. Most system update processes handle this for you, but if you have multiple operating systems on a system, you probably have to do some work yourself. Now, I show you how to use GRUB 2 either alone or in conjunction with GRUB Legacy.

The GRUB 2 packages contain several programs, normally in /usr/bin or /usr/sbin. The actual package name has changed over time and is not the same for all distributions. The binaries also have names that usually start with grub- or grub2-. For example, on Ubuntu 14, you will find grub-image provided by package grub-common, while on Fedora 22, you will find grub2-mkimage provided by package grub2-tools.

The heart of GRUB 2 is a multiboot kernel (/boot/grub/core.img) along with a configuration file (/boot/grub/grub.cfg). These will be generated for you if you run grub-install and set the target as your MBR (for example: grub-install /dev/sdagrub-install/dev/sda). 

If you run grub-install /dev/sdagrub-install/dev/sda, the process builds a core image file for you, builds a configuration file, and installs GRUB 2 in your MBR. 

## Building the GRUB 2 configuration file

The GRUB 2 configuration file is normally `/boot/grub/grub.cfg`. Unlike GRUB Legacy, you should normally not edit this file yourself because it will be overwritten the next time your GRUB 2 installation is updated. You should build it using `grub-mkconfig`. 

On some systems, such as Ubuntu, the `update-grub` command is a front-end to grub-mkconfig that saves its output in `/boot/grub/grub.cfg`. These commands look for general settings (such as background or timeouts) in `/etc/default/grub` and then run executables from `/etc/grub.d/` to build various parts of the configuration file, such as the header, a section for the current Linux distribution, sections for other operating systems, and your own custom additions.

If you need to customize the GRUB 2 menu, you add your changes to a file in `/etc/grub.d/` such as `40_custom`, or add your own file. Remember that it needs to be executable.

Run `grub-mkconfig` (or `update-grub` if available) to generate a new `/boot/grub/grub.cfg` file as shown in Listing 8.

Listing 8. Building a GRUB 2 configuration file with grub-mkconfig

```

ian@attic-u14:~$ sudo grub-mkconfig -o /boot/grub/grub.cfg
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-3.16.0-43-generic
Found initrd image: /boot/initrd.img-3.16.0-43-generic
Found linux image: /boot/vmlinuz-3.16.0-30-generic
Found initrd image: /boot/initrd.img-3.16.0-30-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
Found Fedora release 20 (Heisenbug) on /dev/sda10
Found CentOS release 6.6 (Final) on /dev/sda11
Found Fedora release 22 (Twenty Two) on /dev/sda5
Found Slackware Linux (Slackware 13.37.0) on /dev/sda6
Found Fedora release 18 (Spherical Cow) on /dev/sda7
Found openSUSE 11.4 (x86_64) on /dev/sda8
Found Ubuntu 12.04 LTS (12.04) on /dev/sda9
done
```

## Booting with GRUB 2

You’ll boot the USB flash drive to see how it works.

```
grub> ls
(hd0) (hd0,msdos1) (hd1) (hd1,msdos12) (hd1,msdos11) (hd1,msdos10) ...
grub> set root=(hd1,12)
grub> ls /boot/grub/grub.cfg
grub.cfg
grub> configfile /boot/grub/grub.cfg

```


The commands entered were:

**ls**

With no arguments, lists the devices that were found. This can take some time to run. Flash drives are not normally BIOS drives, but if you boot from one, it likely shows up as `hd0` and displaces other drives, causing them not to be numbered as you expect. Using a bootable CD or DVD avoids this problem.

**set**

Sets variable values. In this case, you set the root variable. Compare with the GRUB legacy root command. You use `hd1` instead of `hd0`, because the previous command told you that `hd0` is now the USB flash drive from which you booted.

**ls**

With a path, displays files or directories. Use Bash-like tab completion to either complete the path component you are typing or to get a list of possible completions as you see here (I pressed tab after entering /boot/grub/gru).

configfile

As with GRUB legacy, you can load a configuration file using the `configfile` command. You load the one you built earlier.

After loading config file, as with GRUB legacy, you can edit configuration entries or enter commands before booting a system.










