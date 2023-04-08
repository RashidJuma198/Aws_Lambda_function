import boto3

# Replace the value below with the ARN of your SNS topic
sns_topic_arn = 'arn:aws:sns:us-east-1:123456789012:my-sns-topic'

def lambda_handler(event, context):
    # Replace the value below with the name of your S3 bucket
    bucket_name = 'wordcounter-1'

    # Get the file name from the event
    file_name = event['Records'][0]['s3']['object']['key']

    # Initialize the S3 client
    s3 = boto3.client('s3')

    # Get the file content from S3
    file_obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    file_content = file_obj['Body'].read().decode('utf-8')

    # Count the number of words in the file
    word_count = len(file_content.split())

    # Publish a message to SNS
    sns = boto3.client('sns')
    message = f'The file {file_name} contains {word_count} words.'
    sns.publish(TopicArn='arn:aws:sns:us-west-2:145972262256:returnWordCount', Message=message)

    # Return the word count as the output of the Lambda function
    return {
        'word_count': word_count
    }