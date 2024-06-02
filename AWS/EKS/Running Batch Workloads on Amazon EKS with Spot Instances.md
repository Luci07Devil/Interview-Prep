## Demonstrate how to use Amazon Elastic Kubernetes Service (EKS) for running cost-effective batch processing and big data workloads. 
We'll focus on utilizing **Spot Instances** to achieve cost savings while processing large-scale data.

## Project Title: Running Batch Workloads on Amazon EKS with Spot Instances

### Overview
This project showcases how to set up an Amazon EKS cluster to efficiently process batch workloads using Spot Instances. We'll use Apache Hadoop and Spark as examples of big data processing tools.

### Prerequisites
1. **AWS Account**: Ensure you have an active AWS account.
2. **AWS CLI and kubectl**: Install the AWS Command Line Interface (CLI) and kubectl (Kubernetes command-line tool).
3. **eksctl**: Install eksctl, a command-line utility for creating and managing EKS clusters.
4. **Docker**: Install Docker to build and push container images.

### Steps

1. **Create an EKS Cluster**:
   - Use eksctl to create an EKS cluster. Specify the desired instance types for your worker nodes, including Spot Instances. These Spot Instances will utilize unused EC2 capacity at discounted prices.
   - Example command:
     ```bash
     eksctl create cluster --name my-eks-cluster --node-type m5.large --nodes-min 2 --nodes-max 5 --node-volume-size 50 --spot
     ```

2. **Deploy Your Batch Workloads**:
   - Create Kubernetes Deployment manifests for your batch processing applications (e.g., Hadoop, Spark).
   - Deploy these workloads to your EKS cluster.
   - Example Hadoop Deployment YAML:
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: hadoop-batch
     spec:
       replicas: 3
       selector:
         matchLabels:
           app: hadoop-batch
       template:
         metadata:
           labels:
             app: hadoop-batch
         spec:
           containers:
             - name: hadoop-worker
               image: your-hadoop-image:latest
               # Add necessary environment variables and volume mounts
     ```

3. **Configure Spot Instances**:
   - Define a **Spot Fleet** or use the default Spot Instance configuration.
   - Specify the maximum price you're willing to pay for Spot Instances.
   - Example Spot Fleet configuration:
     ```json
     {
       "TargetCapacity": 10,
       "SpotPrice": "0.05",
       "IamFleetRole": "arn:aws:iam::123456789012:role/spot-fleet-role",
       "LaunchSpecifications": [
         {
           "InstanceType": "m5.large",
           "SubnetId": "subnet-12345678",
           "WeightedCapacity": 1
         }
       ]
     }
     ```

4. **Monitor and Scale**:
   - Set up monitoring using Amazon CloudWatch and Kubernetes metrics.
   - Use Auto Scaling Groups to automatically adjust the number of Spot Instances based on workload demand.

5. **Update Your README.md**:
   - In your project repository, create a README.md file.
   - Document the steps above, including any specific configurations or environment variables.
   - Provide instructions for deploying your batch workloads to the EKS cluster.

### Conclusion
By leveraging Amazon EKS and Spot Instances, you can efficiently process batch workloads while minimizing costs. Remember to fine-tune your Spot Instance configuration based on your workload requirements and budget constraints.

---

**References**:
1. [Common use cases in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/common-use-cases.html)¹
2. [Building an Amazon EKS Cluster Preconfigured to Run Asynchronous Batch Tasks](https://community.aws/tutorials/navigating-amazon-eks/eks-cluster-batch-processing)²
3. [Running Cost-Effective Batch Workloads with AWS Batch and Amazon EC2 Spot Instances](https://pages.awscloud.com/Running-Cost-Effective-Batch-Workloads-with-AWS-Batch-and-Amazon-EC2-Spot-Instances_1022-CMP_OD.html)³
4. [Large scale Batch Processing using AWS EMR on EC2](https://medium.com/epsilon-engineering-blog/large-scale-batch-processing-using-aws-emr-on-ec2-8ff1e58c2816)⁴
5. [Getting started with AWS Batch on Amazon EKS](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-eks.html)⁵

Source: Conversation with Copilot, 6/3/2024
(1) Common use cases in Amazon EKS - Amazon EKS. https://docs.aws.amazon.com/eks/latest/userguide/common-use-cases.html.
(2) Building an Amazon EKS Cluster Preconfigured to Run Asynchronous Batch .... https://community.aws/tutorials/navigating-amazon-eks/eks-cluster-batch-processing.
(3) Running Cost Effective Batch Workloads with AWS Batch and Amazon EC2 .... https://pages.awscloud.com/Running-Cost-Effective-Batch-Workloads-with-AWS-Batch-and-Amazon-EC2-Spot-Instances_1022-CMP_OD.html.
(4) Large scale Batch Processing using AWS EMR on EC2. https://medium.com/epsilon-engineering-blog/large-scale-batch-processing-using-aws-emr-on-ec2-8ff1e58c2816.
(5) Getting started with AWS Batch on Amazon EKS - AWS Batch. https://docs.aws.amazon.com/batch/latest/userguide/getting-started-eks.html.
