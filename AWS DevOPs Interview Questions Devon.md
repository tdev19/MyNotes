
1) Scenario based -- I have created an EC2 instance and attached a disk to it. But whenever I restart the instance. The disk does not show up on the EC2 instance? what might be causing this issue?

--> when the ec2 instance gets restarted . It stops and entities attached to it get detached. But when it starts the entities\disks do not get reattached hence are not visible in the filesystem of the machine.

2) Do you know about fstab?
--> fstab is a configuration table. which contains  rules about where a specific filesystem is detected and the order in which filesystems are mounted.

Table structure is as follows
- **Device**: usually the given name or UUID of the mounted device (sda1/sda2/etc).
- **Mount Point**: designates the directory where the device is/will be mounted. 
- **File System Type**: nothing trick here, shows the type of filesystem in use. 
- **Options**: lists any active mount options. If using multiple options they must be separated by commas. 
- **Backup Operation**: (the first digit) this is a binary system where `1` = dump utility backup of a partition. `0` = no backup. This is an outdated backup method and should NOT be used. 
- **File System Check Order**: (second digit) Here we can see three possible outcomes.  `0` means that fsck will not check the filesystem. Numbers higher than this represent the check order. The root filesystem should be set to `1` and other partitions set to `2`.
![[Pasted image 20240726235224.png]]

3) I want to run some services running whenever I log into my EC2 instance? How can I configure these services?

	--> There is a file where we can specify commands that we want to be run at the start up
		1) Create a service file and configure to run it at startup.  for this need to create a system.md file on path /etc/systemd/system/  with filename as myservice.service with file contents as below
			
			[Unit]
			Description=My Custom Startup Script
			
			[Service]
			ExecStart=/path/to/your/command
			Restart=always
			User=username
			
			[Install]
			WantedBy=multi-user.target
	   2) edit the .profile or .bashsrc file add your commands to the end of it.
	   3) using crontab 
	    add entry like @reboot /path/to/command
	  4)  add commands to the rc.local file present on this path:  /etc/rc.local


4) What is the difference between monitoring and observability?
