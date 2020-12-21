#!/bin/python3

import boto3
from time import sleep


def deploy_instance():
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
         ImageId=input("Enter ami ID:\n"),
         MinCount=1,
         MaxCount=int(input("How many instances?\n")),
         InstanceType=input("Which type of instance?\n"),
         KeyName='sahar'
 )

def describe_instance():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
            print("ID: " + i['InstanceId'] + "\nIP Address: " + i['PublicIpAddress'] + "\n----------------------------------\n")



def destroy_instance():
    instances=input("enter the ids of the instances that you want to destroy:")
    ids = [instances]
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).terminate()


def stop_instance():
    instances=input("enter the ids of the instances that you want to stop:")
    ids = [instances]
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).stop()


def start_instance():
    instances=input("enter the ids of the instances that you want to start:")
    ids = [instances]
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).start()



def menu():
    while(True):
        choice=input("Menu:\n1.Describe EC2 \n2.Deploy EC2 \n3.Destroy Instance\n4.Stop Instance \n5.Start Instance \n")
        if(choice=="1"):
            print("Now we will show your Instances:...\n")
            sleep(3)
            describe_instance()
        elif(choice=="2"):
            deploy_instance()
        elif(choice=="3"):
            destroy_instance()
        elif(choice=="4"):
            stop_instance()
        elif(choice=="5"):
            start_instance()
        else:
            print("Enter 1-5 only!!!...\n")
            continue
        exit=input("Do you want to exit? yes/no\n")
        if(exit=="yes"):
            print("Bye...\n")
            break


####Main Script####
menu()
