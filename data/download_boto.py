# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 19:05:03 2022

@author: DEKELCO
"""

import boto3
import os 


from botocore import UNSIGNED
from botocore.config import Config

bucketName="ai2-s2-research-public"

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
objs = s3.list_objects(Bucket=bucketName)
obj_key = '2017-02-21/papers-2017-02-21.zip'

# s3.download_file(bucketName, obj_key, r'c:\tmp')
with open(r'D:\NLP\Entity-Matching\hub\S2AND\data\huge\papers-2017-02-21.zip', 'wb') as fl:
    s3.download_fileobj(bucketName, obj_key, fl)


