## Additional questions
How do you intend to store the images?. Will the images be kept for a short time or long time. How frequently will already processed images be retrieved?
Is there a need to set up a data pipeline in the future?

## Assembling these components in the cloud will require a couple of tools.
A cloud provider in this case, I will be using AWS. 
Since there are a couple of applications, it will be convenient to set up the applications on pods running in a Kubernetes cluster. Kubernetes provides service discovery and provides load balancing solutions.
The Nodes for the cluster could be  accelerated computing instances which are the best options for running machine learning and high performance computing applications. 

An S3 bucket will be used to upload the images. Since the files are large, it will be a multipart upload.
In order to make the applications more scalable, a load balancer ingress can be used to balance incoming traffic and handle multiple requests coming in at the same time.  

AWS DataSync can be used to send images and it will be done through Direct connect or a Virtual Private Network utilizing private IP addresses accessible only from within your VPC.  This ensures that your VPC is not reachable over the internet, and prevent any packets from entering or exiting the network. This means that you can eliminate all internet access from your on-premises, but still use DataSync for data transfers to and from AWS using Private IP addresses.

For latency, AWS Global Accelerator helps you to achieve lower latency by improving performance for internet traffic. It used the AWS Global network to direct TCP or UDP traffic to a healthy application endpoint in the closest AWS Region to the client. Global Accelerator routes traffic from the client to the closest AWS edge location via anycast and then routes it to the closest regional endpoint over the AWS global network. 