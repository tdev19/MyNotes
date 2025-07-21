
![[Pasted image 20240724232925.png]][[Pasted image 20240724233247.png]]![[Pasted image 20240724233830.png]]


VPC - Virtual Private Cloud
NAT - Network Address Translation

![[Pasted image 20240724233951.png]]


![[Pasted image 20240724234133.png]]

![[Pasted image 20240724234424.png]]
![[Pasted image 20240724234616.png]]
![[Pasted image 20240724234806.png]]
NACL - Network Access Control Lists

![[Pasted image 20240724235648.png]]

Stateful systems keep track of interactions and carry over data from one session to the next, while stateless systems don't preserve data between sessions


Eg. NACLs are stateless -- so if we are sending a request from ec2 instance to google.com.. we have to open both inbound and outbound ports as it won't understand it is the response of the same request

However security groups are stateful -- it will recognize that it is the response of the same request that was sent so we would need to open only outbound port to send request and it will automatically allow the response of the request

![[Pasted image 20240725001723.png]]
![[Pasted image 20240725002501.png]]



