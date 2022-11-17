# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 19:05:03 2022

@author: DEKELCO
"""

import boto3
import os 


from botocore import UNSIGNED
from botocore.config import Config


def downloadDirectoryFroms3(bucketName, remoteDirectoryName):
    # s3_resource = boto3.resource('s3')
    s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    obj_key = '2017-02-21/papers-2017-02-21.zip'
    
    # s3.download_file(bucketName, obj_key, r'c:\tmp')
    with open(r'D:\NLP\Entity-Matching\hub\S2AND\data\huge\papers-2017-02-21.zip', 'wb') as fl:
        s3.download_fileobj(bucketName, obj_key, fl)
        
    objs = s3.list_objects(Bucket=bucketName)
     bucket = s3.Bucket(bucketName) 
    for obj in bucket.objects.filter(Prefix = remoteDirectoryName):
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
        bucket.download_file(obj.key, obj.key) # save to same path
        
        
        
downloadDirectoryFroms3(bucketName="ai2-s2-research-public",remoteDirectoryName="s2and-release")


import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('my_bucket_name')