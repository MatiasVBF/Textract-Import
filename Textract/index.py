import boto3

# Criar um cliente do AWS Textract
textract = boto3.client('textract')

def extract_text_from_image(bucket_name, document_name):
    response = textract.analyze_document(
        Document={'S3Object': {'Bucket': bucket_name, 'Name': document_name}},
        FeatureTypes=['TABLES', 'FORMS']  # Opcional, dependendo do que você precisa extrair
    )

    # Extrair o texto detectado
    extracted_text = ""
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            extracted_text += block['Text'] + "\n"

    return extracted_text

# Exemplo de uso
bucket_name = "seu-bucket"
document_name = "sua-imagem.png"

texto_extraido = extract_text_from_image(bucket_name, document_name)
print("Texto extraído:\n", texto_extraido)
