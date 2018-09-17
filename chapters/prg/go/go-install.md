# Installation

[Official binary distributions](https://golang.org/dl/) are available for the FreeBSD (release 10-STABLE and above), Linux, macOS (10.10 and above), and Windows operating systems and the 32-bit (386) and 64-bit (amd64) x86 processor architectures.

If a binary distribution is not available for your combination of operating system and architecture, try [installing from source](https://golang.org/doc/install/source) or [installing gccgo instead of gc](https://golang.org/doc/install/gccgo).

Go binary distributions are available for these supported operating systems and architectures. Please ensure your system meets these requirements before proceeding. If your OS or architecture is not on the list, you may be able to install from source or use gccgo instead.

## Linux, macOS, and FreeBSD tarballs
[Download the archive](https://golang.org/dl/) and extract it into /usr/local, creating a Go tree in /usr/local/go. For example:
```
tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz
```

Choose the archive file appropriate for your installation. For instance, if you are installing Go version 1.2.1 for 64-bit x86 on Linux, the archive you want is called go1.2.1.linux-amd64.tar.gz.

(Typically these commands must be run as root or through sudo.)

Add /usr/local/go/bin to the PATH environment variable. You can do this by adding this line to your /etc/profile (for a system-wide installation) or $HOME/.profile:

```
export PATH=$PATH:/usr/local/go/bin
```

**Note**: changes made to a profile file may not apply until the next time you log into your computer. To apply the changes immediately, just run the shell commands directly or execute them from the profile using a command such as source $HOME/.profile.

## macOS package installer
[Download the package file](https://golang.org/dl/), open it, and follow the prompts to install the Go tools. The package installs the Go distribution to /usr/local/go.

The package should put the /usr/local/go/bin directory in your PATH environment variable. You may need to restart any open Terminal sessions for the change to take effect.

## Windows
The Go project provides two installation options for Windows users (besides [installing from source](https://golang.org/doc/install/source)): a zip archive that requires you to set some environment variables and an MSI installer that configures your installation automatically.

- MSI installer  
  Open the [MSI file](https://golang.org/dl/) and follow the prompts to install the Go tools. By default, the installer puts the Go distribution in c:\Go.

  The installer should put the c:\Go\bin directory in your PATH environment variable. You may need to restart any open command prompts for the change to take effect.

- Zip archive  
[Download the zip file](https://golang.org/dl/) and extract it into the directory of your choice (we suggest c:\Go).
If you chose a directory other than c:\Go, you must set the GOROOT environment variable to your chosen path.
Add the bin subdirectory of your Go root (for example, c:\Go\bin) to your PATH environment variable.


### Setting environment variables under Windows
Under Windows, you may set environment variables through the "Environment Variables" button on the "Advanced" tab of the "System" control panel. Some versions of Windows provide this control panel through the "Advanced System Settings" option inside the "System" control panel.

# Test your installation

Check that Go is installed correctly by setting up a workspace and building a simple program, as follows.

Create your workspace directory, $HOME/go. (If you'd like to use a different directory, you will need to set the GOPATH environment variable.)

Next, make the directory src/hello inside your workspace, and in that directory create a file named hello.go that looks like:

```go
package main

import "fmt"

func main() {
	fmt.Printf("hello, world\n")
}
```

Then build it with the go tool:

```
$ cd $HOME/go/src/hello
$ go build
```

The command above will build an executable named hello in the directory alongside your source code. Execute it to see the greeting:

```
$ ./hello
hello, world
```

If you see the "hello, world" message then your Go installation is working.

You can run go install to install the binary into your workspace's bin directory or go clean -i to remove it.

# Uninstallation

To remove an existing Go installation from your system delete the go directory. This is usually /usr/local/go under Linux, macOS, and FreeBSD or c:\Go under Windows.

You should also remove the Go bin directory from your PATH environment variable. Under Linux and FreeBSD you should edit /etc/profile or $HOME/.profile. If you installed Go with the macOS package then you should remove the /etc/paths.d/go file. Windows users should read the section about setting environment variables under Windows.

