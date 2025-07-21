
==Auto Scaling Groups

Auto scaling groups can increase or decrease EC2 instances automatically based on specific parameters
Ensure minimum and maximum number of EC2 instances which must keep running.

ASG has following attributes:
1) Launch Configuration
	1) AMI + instance type
	2) EC2 user data
	3) EBS volumes
	4) Security Groups
	5) SSH key pair
2) Min Size/ Max Size/Initial Capacity
3) Network and Subnets information
4) Load Balancer Information
5) Scaling Policies


Auto Scaling Alarms:
ASGs will scale based on the alarms

Scaling policies can be based on cpu, memory etc. parameters

Avg. Cpu utilization
Avg Users in 
Avg Users out


If you have instances under ASG and  if the instances are terminated for any reason the ASG will restart them.

