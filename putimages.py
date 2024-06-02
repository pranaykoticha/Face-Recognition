import boto3
import os

# Initialize S3 resource
s3 = boto3.resource('s3')

# Specify your local directory path
local_directory = r'C:\Users\Admin\OneDrive\Desktop'

# List of objects for indexing with their corresponding full names
images = [
    ('Dinesh.jpg', 'Stock Burner'),
    ('hardwell.jpg', 'hardwell'),
    ('mark.jpg', 'mark'),
    ('Pranay.jpg', 'pranayy'),
    
]

# Specify your S3 bucket name
s3_bucket_name = 'pranaypics2'

# Iterate through list to upload objects to S3   
for image in images:
    local_path = os.path.join(local_directory, image[0])
    
    # Open the file in binary read mode
    with open(local_path, 'rb') as file:
        # Define the S3 object
        s3_object = s3.Object(s3_bucket_name, 'index/' + image[0])
        
        # Upload the file to S3 with metadata
        ret = s3_object.put(Body=file, Metadata={'FullName': image[1]})

    print(f"Uploaded {image[0]} to S3 bucket {s3_bucket_name} with metadata {image[1]}")
