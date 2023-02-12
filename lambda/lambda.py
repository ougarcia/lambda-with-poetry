import requests

def main():
    response = requests.get("https://httpbin.org/get")
    print(response.status_code)
    print(response.text)
    return response.text

def lambda_handler(event, context):
    main()

if __name__ == "__main__":
    main()
